"""
:author: Thomas Delaet <thomas@delaet.org>

Port for Domintell
:author: Zilvinas Binisevicius <zilvinas@binis.me>

"""
import time
import threading
import logging
from queue import Queue
import domintell
import domintell.messages
import serial
import serial.threaded
import socket

class Protocol(serial.threaded.Protocol):
    """Serial protocol."""

    def data_received(self, data):
        # pylint: disable-msg=E1101
        self.parser(data)


class DomintellException(Exception):
    """Domintell Exception."""
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)


class RS232Connection(domintell.DomintellConnection):
    """
        Wrapper for SerialPort connection configuration
        !! NOT TESTED !!
    """

    BAUD_RATE = 38400

    BYTE_SIZE = serial.EIGHTBITS

    PARITY = serial.PARITY_NONE
 
    STOPBITS = serial.STOPBITS_ONE

    XONXOFF = 0

    RTSCTS = 1

    SLEEP_TIME = 60 / 1000

    def __init__(self, device, controller=None):
        domintell.DomintellConnection.__init__(self)
        self.logger = logging.getLogger('domintell')
        self._device = device
        self.controller = controller
        try:
            self.serial = serial.Serial(port=device,
                                        baudrate=self.BAUD_RATE,
                                        bytesize=self.BYTE_SIZE,
                                        parity=self.PARITY,
                                        stopbits=self.STOPBITS,
                                        xonxoff=self.XONXOFF,
                                        rtscts=self.RTSCTS)
        except serial.serialutil.SerialException:
            self.logger.error("Could not open serial port, \
                              no messages are read or written to the bus")
            raise DomintellException("Could not open serial port")
        self._reader = serial.threaded.ReaderThread(self.serial, Protocol)
        self._reader.start()
        self._reader.protocol.parser = self.feed_parser
        self._reader.connect()
        self._write_queue = Queue()
        self._write_process = threading.Thread(None, self.write_daemon,
                                               "write_packets_process", (), {})
        self._write_process.daemon = True
        self._write_process.start()

    def stop(self):
        """Close serial port."""
        self.logger.warning("Stop executed")
        try:
            self._reader.close()
        except serial.serialutil.SerialException:
            self.logger.error("Error while closing device")
            raise DomintellException("Error while closing device")
        time.sleep(1)

    def feed_parser(self, data):
        """Parse received message."""
        assert isinstance(data, bytes)
        self.controller.feed_parser(data)

    def send(self, message, callback=None):
        """Add message to write queue."""
        assert isinstance(message, domintell.Message)
        self._write_queue.put_nowait((message, callback))

    def write_daemon(self):
        """Write thread."""
        while True:
            (message, callback) = self._write_queue.get(block=True)
            self.logger.info("Sending message on RS232 bus: %s", str(message))
            self.logger.debug("Sending binary message:  %s", str(message.to_binary()))
            self._reader.write(message.to_binary())
            time.sleep(self.SLEEP_TIME)
            if callback:
                callback()


class UDPConnection(domintell.DomintellConnection):
    """
    Wrapper for UDP connection configuration
    :author: Maikel Punie <maikel.punie@gmail.com>
    """
    SLEEP_TIME = 60 / 1000

    def __init__(self, device, controller=None, ping_interval=0):
        domintell.DomintellConnection.__init__(self)
        self.logger = logging.getLogger('domintell')
        self._device = device
        self.controller = controller
        self.ping_interval = ping_interval

        # get the address from a <host>:<port> format
        addr = device.split(':')
        self._addr = (addr[0], int(addr[1]))
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            # self._socket.connect( addr )
        except:
            self.logger.error("Could not open socket, \
                              no messages are read or written to the bus")
            raise DomintellException("Could not open socket port")
        # build a read thread
        self._listen_process = threading.Thread(None, self.read_daemon,
                                         "domintell-process-reader", (), {})
        self._listen_process.daemon = True
        self._listen_process.start()

        # build a writer thread
        self._write_queue = Queue()
        self._write_process = threading.Thread(None, self.write_daemon,
                                               "domintell-connection-writer", (), {})
        self._write_process.daemon = True
        self._write_process.start()

        # build a ping thread
        self._ping_process = threading.Thread(None, self.ping_daemon,
                                            "domintell-ping-writer", (), {})
        self._ping_process.daemon = True


    def stop(self):
        """Close UDP."""
        self.logger.warning("Stop executed")
        try:
            self._socket.close()
        except:
            self.logger.error("Error while closing socket")
            raise DomintellException("Error while closing socket")
        time.sleep(1)

    def feed_parser(self, data):
        """Parse received message."""
        assert isinstance(data, bytes)
        self.controller.feed_parser(data)

    def send(self, message, callback=None):
        """Add message to write queue."""
        assert isinstance(message, domintell.Message)
        self._write_queue.put_nowait((message, callback))

    def read_daemon(self):
        """Read thread."""
        while True:
            data = self._socket.recv(1024)
            self.feed_parser(data)

    def write_daemon(self):
        """Write thread."""
        while True:
            (message, callback) = self._write_queue.get(block=True)
            self.logger.info("Sending message to UDP: %s", str(message))
            self.logger.debug("Sending controll message:  %s", message.to_string())
            if message.is_binary():
                self._socket.sendto(message.to_string(), self._addr)
            else:
                self._socket.sendto(bytes(message.to_string(),'ascii'), self._addr)
            time.sleep(self.SLEEP_TIME)
            if callback:
                callback()
    
    def ping_daemon(self):
        """Put ping message into write thread every 60 sec"""
        s = self.ping_interval
        while True:
            p = domintell.messages.Ping()
            self.send(p)
            time.sleep(s)

    def start_ping(self, interval=-1):
        """
        Start sending PING message to DETH02 every minute.
        DETH02 will end Login 'session' if no messages received 
        in predefined interval (10mins default)
        """
        if interval > -1:
            self.ping_interval = interval

        if self.ping_interval > 0:
            if not self._ping_process.is_alive():
                self._ping_process.start()

"""
:author: Thomas Delaet <thomas@delaet.org>

Port for Domintell
:author: Zilvinas Binisevicius <zilvinas@binis.me>

"""
import logging
import domintell

NORMAL_MODE = 0
APP_INFO_MODE = 1
MSG_SESSION_OPENED =  'INFO:Session opened:INFO'
MSG_SESSION_CLOSED =  'INFO:Session closed:INFO'
MSG_SESSION_TIMEOUT = 'INFO:Session timeout:INFO'

class ParserError(Exception):
    """
    Error when invalid message is received
    """
    pass

class DomintellParser(object):
    """
    Transform Domintell message to Message object
    """

    def __init__(self, controller):
        assert isinstance(controller, domintell.Controller)
        self._mode = NORMAL_MODE
        self.logger = logging.getLogger('domintell')
        self.controller = controller

    def feed(self, data):
        """
        We are on UDP, one datagram shall contain entire message, 
        normal message is not less that 10 ASCII characters long,
        we will ignore shorter messages for now
        """
        
        # data = data.decode('ascii').lstrip('\r\n ')
        # my domintell version uses ascii for communication
        # FIXME need to eoncoding in config
        data = data.decode('iso8859_13').lstrip('\r\n ')
        if len(data) < 10:
            return

        message = self.parse(data)
        if isinstance(message, domintell.Message):
            self.controller.new_message(message)

    def parse(self, data):
        """
        parse message and return Message object, or None        
        """
        data = data.lstrip('\r\n ')
        assert len(data) > 0
        assert len(data) >= domintell.MINIMUM_MESSAGE_SIZE

        self.logger.info("Processing message [%s]", data.strip('\r\n '))
        if len(data) > domintell.MAXIMUM_MESSAGE_SIZE:
            self.logger.warning("Domintell message are maximum %s chars, this one is %s", str(
                domintell.MAXIMUM_MESSAGE_SIZE), str(len(data)))
            return
        
        ## Real parsing here
        
        'APPINFO'
        module_type = data[0:3]
        serial_number = data[3:9].strip()
        data_type = data[9:10]
        data_string = data[10:].rstrip()

        i = ['INF', '!! ']

        if module_type == 'APP':
            # looks like we received APPINFO start message
            # check more data
            logging.info("Switching to APPINFO moder")
            if data[0:7] == "APPINFO":
                # switching to APPINFO mode
                self._mode = APP_INFO_MODE

                # TODO: Start timer, to reset mode if end packet is lost
                # ..
                return domintell.ControllMessage('APPINFO', data)
        if module_type == 'END':
            # looks like we received APPINFO END message
            # check more data
            if data[0:11] == "END APPINFO":
                self._mode = NORMAL_MODE
                return domintell.ControllMessage('END APPINFO', data)

        
        if self._mode == APP_INFO_MODE:
            # we are in app info mode, regular messages won't be processed
            if self.contains_all(data, '[|]'):
                # module info message
                return domintell.ModuleInfoMessage(module_type, data)
        else:
            # normal mode
            if module_type in i:
                # some info message
                if data[0:24] == MSG_SESSION_OPENED:
                    return domintell.SessionOpenedMessage(data=data)
                elif data[0:24] == MSG_SESSION_CLOSED:
                    return domintell.SessionClosedMessage(data=data)
                elif data[0:25] == MSG_SESSION_TIMEOUT:
                    return domintell.SessionTimeoutMessage(data=data)
                return domintell.InfoMessage(module_type, data)

            # normal message
            if module_type in domintell.CommandRegistry:
                message = domintell.CommandRegistry[module_type]()
                message.populate(serial_number, data_type, data_string)
                return message
            else:
                self.logger.debug("Unrecognized message [%s]", str(module_type))

    def contains_all(self, str, set):
        return 0 not in [c in str for c in set]
    
    def contains_any(self, str, set):
        return 1 in [c in str for c in set]

    


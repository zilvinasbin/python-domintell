"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class SetTemperatureMessage(domintell.Command):
    """
    Set temperature
    """
    def __init__(self, moduleType, serialNumber, value):
        domintell.Command.__init__(self, moduleType, serialNumber, "%T", value)

class SetTemperatureModeMessage(domintell.Command):
    """
    Set temperature mode
    1 - Absense
    2 - Automatic
    5 - COmfort
    6 - Frost
    """
    def __init__(self, moduleType, serialNumber, value):
        domintell.Command.__init__(self, moduleType, serialNumber, "%M", value)

class SetTemperatureAutomaticMessage(domintell.Command):
    """
    Set AUTOMATIC mode
    """
    def __init__(self, moduleType, serialNumber):
        domintell.Command.__init__(self, moduleType, serialNumber, "%M", 2)

class SetTemperatureAbsenceMessage(domintell.Command):
    """
    Set ABSEBSE mode
    """
    def __init__(self, moduleType, serialNumber):
        domintell.Command.__init__(self, moduleType, serialNumber, "%M", 1)

class SetTemperatureComfortMessage(domintell.Command):
    """
    Set COMFORT mode
    """
    def __init__(self, moduleType, serialNumber):
        domintell.Command.__init__(self, moduleType, serialNumber, "%M", 5)

class SetTemperatureFrostMessage(domintell.Command):
    """
    Set FROST mode
    """
    def __init__(self, moduleType, serialNumber):
        domintell.Command.__init__(self, moduleType, serialNumber, "%M", 6)

class SetTemperatureSetPointMessage(domintell.Command):
    """
    Set temperature
    """
    def __init__(self, moduleType, serialNumber, value):
        domintell.Command.__init__(self, moduleType, serialNumber, "%T", value)

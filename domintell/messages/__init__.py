"""
:author: Thomas Delaet <thomas@delaet.org>
"""
# pylint: disable-msg=C0301
# appifo scan messages and system messages
from domintell.messages.appinfo_request import AppInfoRequest
from domintell.messages.module_info import ModuleInfoMessage
from domintell.messages.ping import Ping
from domintell.messages.login_request import LoginRequest
from domintell.messages.info import InfoMessage
from domintell.messages.control import ControllMessage
from domintell.messages.session_closed import SessionClosedMessage
from domintell.messages.session_opened import SessionOpenedMessage
from domintell.messages.session_timeout import SessionTimeoutMessage
# status messages
from domintell.messages.ai_status import GenericAIStatusMessage
from domintell.messages.ao_status import GenericAOStatusMessage
from domintell.messages.do_status import GenericDOStatusMessage
from domintell.messages.di_status import GenericDIStatusMessage
from domintell.messages.dio_status import GenericDIOStatusMessage
from domintell.messages.dbir_status import DBIRStatusMessage
from domintell.messages.dmr_status import DDMRStatusMessage
from domintell.messages.ddim_status import DDIMStatusMessage
from domintell.messages.din10v_status import DIN10VStatusMessage
from domintell.messages.dism_status import DISM4StatusMessage
from domintell.messages.dism_status import DISM8StatusMessage
from domintell.messages.dmov_status import DMOVStatusMessage
from domintell.messages.dpbu_status import DPBU01StatusMessage
from domintell.messages.dpbu_status import DPBU02StatusMessage
from domintell.messages.dpbu_status import DPBU04StatusMessage
from domintell.messages.dpbu_status import DPBU06StatusMessage
from domintell.messages.dtrp_status import DTRPStatusMessage
from domintell.messages.dtrv_status import DTRVStatusMessage
from domintell.messages.dtrv_status import DTRVBTStatusMessage
from domintell.messages.dtsc_status import DTSCStatusMessage
from domintell.messages.module_status_request import ModuleStatusRequest
from domintell.messages.dled_status  import DLEDStatusMessage
# Command messages
from domintell.messages.set_ao import SetAnalogOutputMessage
from domintell.messages.set_di import DigitalShortPush
from domintell.messages.set_di import DigitalLongPush
from domintell.messages.set_di import DigitalShortPushEnd
from domintell.messages.set_di import DigitalLongPushEnd
from domintell.messages.set_dimmer import SetDimmer
from domintell.messages.set_dimmer import StartDimmer
from domintell.messages.set_dimmer import StopDimmer
from domintell.messages.set_dimmer import IncrementDimmer
from domintell.messages.set_dimmer import DecrementDimmer
from domintell.messages.set_do import SetDigitalOutputMessage
from domintell.messages.set_do import SetDigitalOutputOnMessage
from domintell.messages.set_do import SetDigitalOutputOffMessage
from domintell.messages.set_do import TogleDigitalOutputMessage
from domintell.messages.set_temperature import SetTemperatureMessage
from domintell.messages.set_temperature import SetTemperatureModeMessage
from domintell.messages.set_temperature import SetTemperatureSetPointMessage
from domintell.messages.set_temperature import SetTemperatureComfortMessage
from domintell.messages.set_temperature import SetTemperatureAutomaticMessage
from domintell.messages.set_temperature import SetTemperatureAbsenceMessage
from domintell.messages.set_temperature import SetTemperatureFrostMessage
from domintell.messages.temperature_status import TE1TemperaturetatusMessage
from domintell.messages.temperature_status import TE2TemperaturetatusMessage
from domintell.messages.var_status import VARStatusMessage
from domintell.messages.var_status import SYSStatusMessage

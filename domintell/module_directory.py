"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell

MODULE_DIRECTORY = {
    'IS4': { 'type': 'DISM4', 'name': 'Control of 4 inputs (buttons)'},
    'IS8': { 'type': 'DISM8', 'name': 'Control of 8 inputs (buttons)'},
    'BU1': { 'type': 'DPBU01', 'name': '1 button module'},
    'BU2': { 'type': 'DPBU02', 'name': '2 button module'},
    'BU4': { 'type': 'DPBU04', 'name': '4 button module'},
    'BU6': { 'type': 'DPBU06', 'name': '6 button module'},
    'BIR': { 'type': 'DBIR01', 'name': '8 relay output module'},
    'TRP': { 'type': 'DTRP01', 'name': 'Output card for the control of up to 4 trip switches'},
    'TPV': { 'type': 'DTRP02', 'name': 'Output card for the control of 2 x 2 inverted trip switches'},    
    'DIM': { 'type': 'DDIM01', 'name': 'Control module for up to 8 dimmers'},
    'TE1': { 'type': 'DTEM01', 'name': 'Temperature sensor module. Allows the connection of the temperature sensor'},
    'TE2': { 'type': 'DTEM02', 'name': 'Temperature sensor module. Allows the connection of the temperature sensor'},
    'DIR': { 'type': 'DDIR01', 'name': 'Infrared Sensor'},
    'TSB': { 'type': 'DTSC0x', 'name': 'TFT back-lit color touchscreen'},
    'DET': { 'type': 'DMOV01', 'name': 'Movement sensor'},
    'LCD': { 'type': 'DLCD01', 'name': 'LCD'},
    'TRV': { 'type': 'DTRV01', 'name': '4 outputs control module. For the control of shutters, valves, motors, etc'},
    'LED': { 'type': 'DLED01', 'name': '4 outputs led control module'},
    'V24': { 'type': 'DTRVBT01', 'name': 'Single output card controlling motors, valves, shutters or Velux with low tension between 12 to 24Vdc'},
    'AMP': { 'type': 'DAMPLI01', 'name': ' 4 zones stereo audio amplifi er '},
    'VAR': { 'type': 'VAR', 'name': 'Variable'},
    'SYS': { 'type': 'SYS', 'name': 'System variable'},
    'D10': { 'type': 'DOUT10V01', 'name': '0 - 10Vdc output module'},
    'LC3': { 'type': 'DLCD01', 'name': 'LCD panel'},
    'FAN': { 'type': 'DFAN01', 'name': 'Fan coil controller'},
    'DMR': { 'type': 'DMR01', 'name': 'Output card with 5 x 250 V/3 A monopolar relays.'},
    'I10': { 'type': 'DIN10V01', 'name': '0 - 10Vdc input module'},
    'SFE': { 'type': 'SFE', 'name': 'Atmosphere'},
    'ZON': { 'type': 'ZON', 'name': 'Zone'},
    'MEM': { 'type': 'MEM', 'name': 'Memo'},
    'TPR': { 'type': 'TPR', 'name': 'Heating Schedule'}
}

def get_point_id(module_code, serial_number, channel=0):
    # assert isinstance(module_code, str)
    assert isinstance(serial_number, str)
    # hw_id = module_code.strip()
    se_no = serial_number.strip()

    pid = se_no
    if channel > 0 and channel < 9:
        pid = se_no + '-' + channel
    return pid

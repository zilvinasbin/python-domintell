"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell

MODULE_DIRECTORY = {
    'IS4': { 'type': 'DISM4', 'name': 'Control of 4 inputs (buttons)', 'io': 'di'},
    'IS8': { 'type': 'DISM8', 'name': 'Control of 8 inputs (buttons)', 'io': 'di'},
    'BU1': { 'type': 'DPBU01', 'name': '1 button module', 'io': 'di'},
    'BU2': { 'type': 'DPBU02', 'name': '2 button module', 'io': 'di'},
    'BU4': { 'type': 'DPBU04', 'name': '4 button module', 'io': 'di'},
    'BU6': { 'type': 'DPBU06', 'name': '6 button module', 'io': 'di'},
    'BIR': { 'type': 'DBIR01', 'name': '8 relay output module', 'io': 'do'},
    'TRP': { 'type': 'DTRP01', 'name': 'Output card for the control of up to 4 trip switches', 'io': 'do'},
    'TPV': { 'type': 'DTRP02', 'name': 'Output card for the control of 2 x 2 inverted trip switches', 'io': 'do'},    
    'DIM': { 'type': 'DDIM01', 'name': 'Control module for up to 8 dimmers', 'io': 'ao'},
    'TE1': { 'type': 'DTEM01', 'name': 'Temperature sensor module. Allows the connection of the temperature sensor', 'io': 't'},
    'TE2': { 'type': 'DTEM02', 'name': 'Temperature sensor module. Allows the connection of the temperature sensor', 'io': 't'},
    'DIR': { 'type': 'DDIR01', 'name': 'Infrared Sensor', 'io': 'ai'},
    'TSB': { 'type': 'DTSC0x', 'name': 'TFT back-lit color touchscreen', 'io': 't'},
    'DET': { 'type': 'DMOV01', 'name': 'Movement sensor', 'io': 'di'},
    'LCD': { 'type': 'DLCD01', 'name': 'LCD', 'io': 'unk'},
    'TRV': { 'type': 'DTRV01', 'name': '4 outputs control module. For the control of shutters, valves, motors, etc', 'io': 'do'},
    'LED': { 'type': 'DLED01', 'name': '4 outputs led control module', 'io': 'do'},
    'V24': { 'type': 'DTRVBT01', 'name': 'Single output card controlling motors, valves, shutters or Velux with low tension between 12 to 24Vdc', 'io': 'do'},
    'AMP': { 'type': 'DAMPLI01', 'name': ' 4 zones stereo audio amplifi er ', 'io': 'unk'},
    'VAR': { 'type': 'VAR', 'name': 'Variable', 'io': 'var'},
    'SYS': { 'type': 'SYS', 'name': 'System variable', 'io': 'var'},
    'D10': { 'type': 'DOUT10V01', 'name': '0 - 10Vdc output module', 'io': 'ao'},
    'LC3': { 'type': 'DLCD01', 'name': 'LCD panel', 'io': 'di'},
    'FAN': { 'type': 'DFAN01', 'name': 'Fan coil controller', 'io': 'do'},
    'DMR': { 'type': 'DMR01', 'name': 'Output card with 5 x 250 V/3 A monopolar relays.', 'io': 'do'},
    'I10': { 'type': 'DIN10V01', 'name': '0 - 10Vdc input module', 'io': 'ai'},
    'SFE': { 'type': 'SFE', 'name': 'Atmosphere', 'io': 'unk'},
    'ZON': { 'type': 'ZON', 'name': 'Zone', 'io': 'unk'},
    'MEM': { 'type': 'MEM', 'name': 'Memo', 'io': 'unk'},
    'TPR': { 'type': 'TPR', 'name': 'Heating Schedule', 'io': 'unk'}
}

def get_point_id(module_code, serial_number, channel=-1):
    # assert isinstance(module_code, str)
    assert isinstance(serial_number, str)
    # hw_id = module_code.strip()
    se_no = serial_number.strip()

    pid = se_no

    if not isinstance(channel, int):
        channel = -1
        
    if channel > -1 and channel < 8:
        channel += 1  # we use 0 based index internally confert to 1 based for domintell
        pid = "{}-{}".format(se_no, channel)

    return pid

from fpdf import FPDF

from lib import g
from lib import layout
from lib import t

# TABLE OF CONTENTS:
# ......................................
# System Overview........................................................[OVR]
# Hardware Design........................................................[HRD]
# Bill of Materials......................................................[BOM]
# Manufacturing & Assembly...............................................[MNF]
# Testing & Quality Control..............................................[TST]
# Regulatory & Safety Considerations.....................................[RGL]
# Appendix...............................................................[APX]
# Document References....................................................[RFR]

a4_w_mm = 210
a4_h_mm = 297
a4_x_pd = 20
container_w = a4_w_mm - int(a4_x_pd * 2)

h1_index = 0
h2_index = 0
h3_index = 0

def text_format(text):
    text_formatted = text
    text_formatted = text_formatted.replace('—', '')
    text_formatted = text_formatted.replace('₃', '3')
    text_formatted = text_formatted.replace('’', "'")
    return text_formatted

def doc_title(pdf, text, border=0):
    pdf.add_page()
    gap = a4_w_mm - container_w
    pdf.x = gap // 2
    font_size = 16
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size)
    pdf.multi_cell(container_w, line_height, txt=f'''{text.strip().upper()}''', ln=True, border=border, align='L')
    pdf.ln()

def h1(pdf, text, border=0):
    global h1_index
    global h2_index
    global h3_index
    h1_index += 1
    h2_index = 0
    h3_index = 0
    pdf.add_page()
    gap = a4_w_mm - container_w
    font_size = 16
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size, style="B")
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{h1_index}. {text.strip().upper()}''', ln=True, border=border, align='L')
    pdf.ln()

def h2(pdf, text, border=0):
    global h2_index
    global h3_index
    h2_index += 1
    h3_index = 0
    pdf.ln()
    # pdf.add_page()
    gap = a4_w_mm - container_w
    font_size = 14
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size, style="B")
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{h1_index}.{h2_index} {text.strip()}''', ln=True, border=border, align='L')
    pdf.ln()

def h3(pdf, text, border=0):
    global h3_index
    h3_index += 1
    pdf.ln()
    gap = a4_w_mm - container_w
    font_size = 12
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size, style="B")
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{h1_index}.{h2_index}.{h3_index} {text.strip()}''', ln=True, border=border, align='L')
    pdf.ln()
    
def paragraph(pdf, text, border=0):
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=text.strip(), ln=True, border=border, align='L')
    pdf.ln()

def list_unordered(pdf, lst, border=0):
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    for item in lst:
        pdf.x = gap // 2
        pdf.multi_cell(container_w, line_height, txt=f'''* {item.strip()}''', ln=True, border=border, align='L')

def list_unordered_item(pdf, text, border=0):
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=text.strip(), ln=True, border=border, align='L')
    pdf.ln()

def doc_master():
    pdf = FPDF()

    title = 'Aurora - Hardware Documentation'
    version = '1.0'
    date = '2025-08-07'
    author = 'Martin Pellizzer'
    organization = 'Ozonogroup'
    status = 'draft'
    revision_history = [
        {
            'Version': '1.0', 
            'Date': '2025-08-07', 
            'Author': 'Martin Pellizzer', 
            'Description of Change': 'Initial release of documentation', 
            'Approved By': 'Martin Pellizzer',
        },
    ]

    pdf.set_font("Arial", size=16)
    # pdf.cell(200, 10, txt="My First PDF", ln=True, align='C')
    doc_title(pdf, title)
    paragraph(pdf, f'Version: {version}')
    paragraph(pdf, f'Date: {date}')
    paragraph(pdf, f'Author: {author}')
    paragraph(pdf, f'Organization: {organization}')
    paragraph(pdf, f'Status: {status}')

    cell_version_w = 20
    cell_data_w = 30
    cell_author_w = 35
    cell_description_of_change_w = 65
    cell_approved_by_w = 35
    pdf.set_font("Arial", size=12)
    pdf.cell(cell_version_w, 10, txt=f'''Version''', border=1)
    pdf.cell(cell_data_w, 10, txt=f'''Date''', border=1)
    pdf.cell(cell_author_w, 10, txt=f'''Author''', border=1)
    pdf.cell(cell_description_of_change_w, 10, txt=f'''Description of Change''', border=1)
    pdf.cell(cell_approved_by_w, 10, txt=f'''Approved By''', border=1)
    pdf.ln()

    pdf.cell(cell_version_w, 10, txt=f'''{revision_history[0]['Version']}''', border=1)
    pdf.cell(cell_data_w, 10, txt=f'''{revision_history[0]['Date']}''', border=1)
    pdf.cell(cell_author_w, 10, txt=f'''{revision_history[0]['Author']}''', border=1)
    pdf.cell(cell_description_of_change_w, 10, txt=f'''{revision_history[0]['Description of Change']}''', border=1)
    pdf.cell(cell_approved_by_w, 10, txt=f'''{revision_history[0]['Approved By']}''', border=1)
    pdf.ln()

    with open('Master_Document_Template.txt') as f: template = f.read()
    template = t.template_gen(template)
    template = text_format(template)
    template_blocks = template.split('\n\n')
    for template_block in template_blocks:
        template_block = template_block.strip()
        if template_block == '': continue
        if template_block.startswith('### '):
            template_block = template_block.replace('### ', '').strip()
            h3(
                pdf, 
                text = f'''
                    {template_block}
                '''
            )
        elif template_block.startswith('## '):
            template_block = template_block.replace('## ', '').strip()
            h2(
                pdf, 
                text = f'''
                    {template_block}
                '''
            )
        elif template_block.startswith('# '):
            template_block = template_block.replace('# ', '').strip()
            h1(
                pdf, 
                text = f'''
                    {template_block}
                '''
            )
        elif template_block.startswith('- '):
            template_block = template_block.replace('- ', '* ').strip()
            print('##################################################')
            print('##################################################')
            print(template_block)
            print('##################################################')
            print('##################################################')
            list_unordered_item(
                pdf, 
                text = f'''
                    {template_block}
                ''', 
            )
        else:
            paragraph(
                pdf, 
                text = template_block,
            )

    pdf.output('Master_Document.pdf')
    quit()
    ################################################################################
    # 1. SYSTEM OVERVIEW.....................................................[OVR]
    ################################################################################
    h1(
        pdf, 
        text = f'''
            System Overview
        '''
    )
    
    # Purpose.............................
    ########################################
    h2(
        pdf, 
        text = f'''
            Purpose
        '''
    )
    paragraph(
        pdf, 
        text = f'''
            The Ozone Sanitization System is an automated disinfection device designed for enclosed environments such as rooms, cabinets, vehicles, HVAC ducts, and medical storage areas. It utilizes ozone gas (O3) to neutralize bacteria, viruses, fungi, and volatile organic compounds (VOCs) on surfaces and in the air.

Ozone is a powerful oxidizer, but it must be precisely generated and controlled due to its potential health risks. This system manages the ozone generation, concentration monitoring, safety interlocks, and exposure time to ensure safe and effective sanitization cycles, suitable for both industrial and consumer applications.
        '''
    )
    
    # Key Features........................
    ########################################
    h2(
        pdf, 
        text = f'''
            Key Features
        '''
    )
    h3(
        pdf, 
        text = f'''
            Programmable Ozone Generation Cycles
        '''
    )
    paragraph(
        pdf, 
        text = f'''
            Users can schedule automated cycles (e.g., 5, 10, 30 minutes) depending on room size and sanitization requirements. Optional pre- and post-cycle ventilation logic can be enabled.
        '''
    )
    h3(
        pdf, 
        text = f'''
            Real-Time Ozone Concentration Monitoring
        '''
    )
    paragraph(
        pdf, 
        text = f'''
            An onboard ozone gas sensor measures real-time O3 levels (in ppm), enabling dynamic control of the generator and accurate cycle termination.
        '''
    )
    h3(
        pdf, 
        text = f'''
            Touch or Mobile App Control
        '''
    )
    paragraph(
        pdf, 
        text = f'''
            The system can be operated via an onboard touch interface or remotely using a companion mobile app (via Wi-Fi/Bluetooth), allowing for flexible, remote scheduling and safety alerts.
        '''
    )
    h3(
        pdf, 
        text = f'''
            Safety Lockouts and Timers
        '''
    )
    paragraph(
        pdf, 
        text = f'''
            Built-in safety features include:
        '''
    )
    list_unordered(
        pdf, 
        lst = [
            f''' 
                Delayed start (to allow exit from the room)
Automatic shutdown if ozone exceeds safety limits
Lockout until residual ozone falls below 0.1 ppm
Audible/visual alarms during and after operation
            ''',
        ]
    )
    h3(
        pdf, 
        text = f'''
            Wi-Fi/Bluetooth Connectivity (Optional)
        '''
    )
    paragraph(
        pdf, 
        text = f'''
            For cloud logging, OTA updates, and remote monitoring, wireless connectivity is optionally available through a dedicated module (e.g., ESP32 or external BLE module).
        '''
    )

    # Operating Conditions................
    ########################################
    title = f'''Operating Conditions'''
    paragraph_text = f'''
Parameter	Value
Input Voltage	12V DC
Power Consumption	Max 20W
Operating Temperature	0°C to 45°C
Humidity Range	20% - 90% RH (non-cond.)
Ozone Output Rate	0 - 200 mg/h
Safe Residual Limit	< 0.1 ppm at cycle end

Note: Ozone output may vary slightly based on ambient humidity, temperature, and ozone generation method (e.g., corona discharge or UV lamp).
'''
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # System Block Diagram................
    ########################################
    title = f'''System Block Diagram'''
    paragraph_text = f'''
The system is built around a microcontroller that coordinates all subsystems. Here's a simplified block-level view of the architecture:
       +-----------------------------+
       |      12V DC Power Input     |
       +-----------------------------+
                    |
                    v
          +------------------+
          |  Power Regulation |
          | (3.3V, 5V Rails)  |
          +------------------+
                    |
                    v
          +------------------+
          |  Microcontroller |
          |  (Main Control)  |
          +------------------+
            /    |     \     \\
           /     |      \     \\
          v      v       v     v
+------------+ +------------+ +--------------+
|  Ozone     | |  Sensors   | |  UI (Touch / |
| Generator  | | (O3, Temp, | |  LEDs, Buzzer|
| Driver     | |  Humidity) | |  Buttons)    |
+------------+ +------------+ +--------------+
                                   |
                                   v
                            +---------------+
                            | Communication |
                            | (Wi-Fi/BLE)   |
                            +---------------+
'''
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Operating Conditions................
    ########################################
    title = f'''System Summary'''
    paragraph_text = f'''
This ozone sanitization unit provides a complete, standalone disinfection solution that's both intelligent and safety-conscious. Its modular architecture allows future expansions (e.g., logging, multi-room control, cloud connectivity) and customization based on application or regulatory needs.
'''
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    ################################################################################
    # HARDWARE DESIGN........................................................[HRD]
    ################################################################################
    title = f'''Hardware Design'''
    h1(pdf, title)

    # Schematics..........................
    ########################################
    title = f'''Schematics'''.strip()
    paragraph_text = f'''
        The circuit design is organized across five functional pages, each serving a distinct purpose in the overall system. Below is a detailed explanation of each schematic section:
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Power Regulation....................
    ########################################
    
    title = f'''Power Regulation'''.strip()
    paragraph_text = f'''
        This section handles incoming DC power, voltage conversion, and distribution:

Input: 12V DC from an external adapter.

Protection: TVS diode for surge protection, reverse-polarity diode, and fuse on the input line.

Conversion:

A buck converter steps 12V down to 5V for the ozone driver and digital circuitry.

An LDO regulator further steps 5V down to 3.3V for low-noise operation of the microcontroller and sensors.

Filtering: LC and ceramic capacitor filters on each output rail to minimize ripple.

Test points: Provided on 12V, 5V, and 3.3V lines for QA checks.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Microcontroller and Interfaces......
    ########################################
    
    title = f'''Microcontroller and Interfaces'''.strip()
    paragraph_text = f'''
        This page details the system's control core:

MCU: STM32F030F4P6 (32-bit ARM Cortex-M0, 48 MHz, 16KB Flash).

Clock Source: Internal RC oscillator; external crystal pads included for future expansion.

I/O:

GPIOs for buttons, LEDs, and control signals.

UART for serial communication/debugging.

I2C for sensor communication.

Reset & Programming:

External reset button, pull-up resistors on reset line.

SWD header for in-circuit programming/debugging.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Ozone Generator Driver..............
    ########################################
    
    title = f'''Ozone Generator Driver'''.strip()
    paragraph_text = f'''
        Control Circuit:

PWM signal from MCU drives a high-speed MOSFET (IRF840).

MOSFET switches the primary side of a step-up HV transformer.

Driver Protection:

Flyback diode across transformer primary.

Snubber circuit to suppress voltage spikes.

Safety Features:

Opto-isolation on the PWM control line.

HV warning silkscreen and spacing compliant with IPC-2221B clearance rules.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Sensors.............................
    ########################################
    
    title = f'''Sensors'''.strip()
    paragraph_text = f'''
        
Monitors environmental and operational conditions:

Ozone Sensor: MQ-131 analog gas sensor.

Operates with preheat cycle; signal connected to ADC pin of MCU.

Temperature & Humidity Sensor:

I2C-based digital sensor (SHT31-D or DHT22 depending on version).

Pull-up resistors included for I2C lines.

Analog Front-End (AFE):

RC filters on ADC input to remove high-frequency noise.

Grounded shield plane beneath sensor section.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # User Interface......................
    ########################################
    
    title = f'''User Interface'''.strip()
    paragraph_text = f'''
Allows user interaction and status feedback:

Push Buttons:

One "Start" and one "Stop" button connected with pull-down resistors.

Debounced in software.

LED Indicators:

Green: System OK

Red: Error or unsafe ozone level

Yellow: Active cycle

Optional Expansion:

Pads provided for OLED display (I2C, 4-pin).
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Note................................
    ########################################
    
    title = f'''Note'''.strip()
    paragraph_text = f'''
Full schematic drawings, with component values, designators, and annotations, are provided in /Schematics/Ozone_Sanitizer_Schematics.pdf. Editable source files (KiCad/Altium) are included in /Schematics/Source_Files/.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # PCB Layout..........................
    ########################################
    
    title = f'''PCB Layout'''.strip()
    paragraph_text = f'''
The PCB layout was designed with clear segregation between high-voltage and low-voltage areas to ensure operational safety and signal integrity. The following is a breakdown of physical and electrical design considerations:

Board Specifications
Dimensions: 85 mm x 60 mm

Layer Count: 2-layer FR4 board

Copper Thickness: 1 oz

Surface Finish: HASL

Key Layout Features
High-Voltage Isolation

All HV traces from the ozone driver are grouped and physically separated by at least 6 mm clearance from logic circuits.

A solid silkscreen warning and keep-out zone mark this area on both layers.

Star-Ground Topology

Sensor ground returns to a single central ground point, minimizing analog signal noise.

Power and logic grounds are separated until the star junction.

EMI Management

Ground planes used on both layers where possible.

Decoupling capacitors placed near all IC power pins.

Snubber networks and ferrite beads mitigate switching noise from the ozone driver.

Mechanical Considerations

Four mounting holes at corners with clearance around them.

Height limits maintained to support enclosure compatibility.

Test & Debug Features

Test points labeled for 12V, 5V, 3.3V, PWM, and Ozone ADC input.

SWD header located at the board edge for easy access during development.

3D renders, layer images, and fabrication-ready files are provided in /PCB_Layout/. Assembly and pick-and-place data are in /Manufacturing_Files/.
'''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)


    ################################################################################
    # Bill of Materials......................................................[BOM]
    ################################################################################
    
    title = f'''Bill of Materials (BOM)'''
    paragraph_text = f'''
The Bill of Materials (BOM) lists every component required to assemble the ozone sanitization system. This section provides a summary of the most critical components in the system, along with key information such as part numbers, manufacturers, and the roles they play in the circuit.

The complete, detailed BOM-containing all passive and active components, alternative part options, package sizes, and supplier references-is available in:
/BOM/Ozone_Sanitizer_BOM.xlsx
    '''.strip()
    h1(pdf, title)
    paragraph(pdf, paragraph_text)

    # Critical Components.................
    ########################################
    
    title = f'''Critical Components'''.strip()
    paragraph_text = f'''
These parts are essential for the core functionality of the system. Substitutions or sourcing changes should be carefully evaluated.

Ref	Description	Part Number	Manufacturer	Role in System
U1	Microcontroller (ARM Cortex-M0)	STM32F030F4P6	STMicroelectronics	Central control unit for ozone timing, sensor reading, and user interface logic
U3	Ozone Sensor (Analog Output)	MQ-131	Winsen	Senses ambient ozone concentration (ppm) during and after sanitization cycles
Q1	High Voltage MOSFET	IRF840	Infineon	Switches power to the high-voltage ozone generator module in PWM mode
D1	Fast Recovery Flyback Diode	UF4007	ON Semiconductor	Protects the MOSFET from voltage spikes caused by inductive load switching
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Supporting Components...............
    ########################################
    
    title = f'''Supporting Components'''.strip()
    paragraph_text = f'''
Note: Not all components are listed here. See the full BOM for all passives (resistors, capacitors), connectors, headers, LEDs, etc.

Voltage Regulators: 3.3V and 5V LDOs or buck converters (e.g., AMS1117, MP1584) to supply MCU and sensors.

Level Shifters or Op-Amps: Used for interfacing analog sensors to MCU ADC inputs with proper scaling.

User Interface Parts:

Momentary push buttons for Start/Stop

Status LEDs (Green: OK, Red: Warning)

Buzzer for alert tones

Protection Components:

TVS diodes on DC input

Polyfuse (self-resetting) for overcurrent protection
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Design and Sourcing Notes...........
    ########################################
    
    title = f'''Design and Sourcing Notes'''.strip()
    paragraph_text = f'''
Footprints: All components are chosen with standard SMD or through-hole footprints (e.g., 0603 passives, TO-220, DIP/SOIC).

Availability: Parts selected based on stable supply from major distributors (Digi-Key, Mouser, LCSC).

RoHS Compliance: All critical components are RoHS compliant for environmental safety.

Cost Considerations: Cost-effective components chosen without compromising safety (especially in HV areas).
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Component Substitution Guidelines...
    ########################################
    
    title = f'''Component Substitution Guidelines'''.strip()
    paragraph_text = f'''
Ref	Substitute Criteria	Notes
U1	Any STM32F0/F1 MCU with same pinout	Ensure bootloader and clock settings match
U3	Compatible analog ozone sensor	Must match voltage range and warm-up time (e.g., SPEC Sensors)
Q1	Any N-channel MOSFET, 500V+, >5A rating	Gate threshold and Rds(on) should be similar
D1	Any fast recovery diode, >1000V, 1A+	UF4004, UF5408 can also work depending on size
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Component Substitution Guidelines...
    ########################################
    title = f'''Full BOM File Contents'''.strip()
    paragraph_text = f'''
The Excel file includes:

Reference designator (e.g., R1, C2, U5)

Quantity per board

Component value or rating

Manufacturer and part number

Package (e.g., SOT-23, 0805)

Preferred distributor and order code

Substitution notes (if applicable)

Estimated unit cost (optional)

Refer to /BOM/Ozone_Sanitizer_BOM.xlsx for ordering and sourcing.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    ################################################################################
    # Manufacturing & Assembly...............................................[MNF]
    ################################################################################
    title = f'''Manufacturing & Assembly'''
    paragraph_text = f'''
    '''.strip()
    h1(pdf, title)
    paragraph(pdf, paragraph_text)

    # PCB Specifications..................
    ########################################
    
    title = f'''PCB Specifications'''.strip()
    paragraph_text = f'''
The following parameters define the printed circuit board (PCB) for the Ozone Sanitization System:

Number of Layers: 2

Board Thickness: 1.6 mm

Material: FR-4 (standard Tg ~135°C)

Copper Weight: 1 oz/ft² on all layers

Surface Finish: HASL (Hot Air Solder Leveling) - lead-free

Minimum Trace Width / Clearance: 6 mil / 6 mil

Solder Mask Color: Green (default; optional customization allowed)

Silkscreen: Top and bottom, white

Impedance Control: Not required

Mechanical Dimensions: 85 mm x 60 mm rectangular outline

Drill Size Tolerances: ±0.05 mm for plated holes

Mounting Holes: 4x Ø3.2 mm, non-plated, spaced for standard M3 hardware

See /PCB_Layout/Fabrication_Drawing.pdf for mechanical tolerances, board outline, and hole placement diagram.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Component Assembly Instructions.....
    ########################################
    
    title = f'''Component Assembly Instructions'''.strip()
    paragraph_text = f'''
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # Surface-Mount Device (SMD) Assembly.
    ########################################
    
    title = f'''Surface-Mount Device (SMD) Assembly'''.strip()
    paragraph_text = f'''
Assembly Method: Automated pick-and-place with reflow soldering

Reflow Profile: Standard lead-free profile, peak temp ~245°C

Placement Side: Top layer only

Notable Components:

MCU (U1): STM32F030F4P6, TSSOP-20

Sensors (U3): MQ-131 via analog signal interface board

Passive components: 0402 and 0603 standard packages

SMD Status: All SMD components are populated by default

Special Notes:

No components exceed 3 mm in height-compatible with standard feeders
    '''.strip()
    h3(pdf, title)
    paragraph(pdf, paragraph_text)

    # 4.2.2 Through-Hole Assembly.........
    ########################################
    
    title = f'''Surface-Mount Device (SMD) Assembly'''.strip()
    paragraph_text = f'''
The following components are not suitable for automated assembly and must be hand-soldered:

Ref	Component	Description	Notes
M1	Ozone Generator Module	High-voltage unit	Solder last, isolate properly
F1	Fuse Holder + Fuse (2A, fast-blow)	5x20 mm, through-hole	Orientation not critical
SW1	Mechanical On/Off Switch (optional)	Panel-mount	Solder only if panel used

Use low-residue, no-clean flux for manual soldering.

Trim leads flush with PCB bottom.

Avoid excess heat during soldering to prevent damage to ozone module.
    '''.strip()
    h3(pdf, title)
    paragraph(pdf, paragraph_text)

    # 4.3 Handling and Safety Guidelines..
    ########################################
    
    title = f'''Handling and Safety Guidelines'''.strip()
    paragraph_text = f'''
    CAUTION: HIGH VOLTAGE OPERATION

The ozone generator module operates at voltages exceeding 2,000V (2 kV).

During operation or testing:

Use insulated tools and wear rubber gloves and eye protection.

Ensure all connections are insulated and labeled appropriately.

Keep a minimum 6 mm creepage and clearance between high-voltage traces and other nets.

Never touch the board while powered-ozone modules can retain charge briefly after shutdown.

Design Safeguards:

Optocouplers isolate low-voltage MCU control signals from the ozone driver circuitry.

A 4 mm PCB isolation slot is milled under the high-voltage transformer to enhance clearance.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # 4.4 Assembly QA Checklist...........
    ########################################
    
    title = f'''Assembly QA Checklist'''.strip()
    paragraph_text = f'''
    | Item | Checkpoint                                      | Pass/Fail |
| ---- | ----------------------------------------------- | --------- |
| 1    | No visible solder bridges or cold joints        |           |
| 2    | All polarized components oriented correctly     |           |
| 3    | HV section soldered cleanly and safely isolated |           |
| 4    | All mounting holes unobstructed and deburred    |           |
| 5    | Connectors and headers are aligned and secure   |           |
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # 4.5 References......................
    ########################################
    
    title = f'''References'''.strip()
    paragraph_text = f'''
Fabrication Drawing:
See /PCB_Layout/Fabrication_Drawing.pdf for:

Mounting hole positions

Mechanical outline

Silk and solder mask alignment

Full BOM:
All part numbers, sourcing info, and alternative components are available in:
/BOM/Ozone_Sanitizer_BOM.xlsx
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    ################################################################################
    # Testing & Quality Control..............................................[TST]
    ################################################################################
    title = f'''Testing & Quality Control'''
    paragraph_text = f'''
        This section outlines the standard test procedures for verifying the electrical performance, sensor accuracy, and functional behavior of the ozone sanitization system. All units must pass these tests before deployment or shipment.
    '''.strip()
    h1(pdf, title)
    paragraph(pdf, paragraph_text)

    # 5.1 Power-On Test...........................................................
    ################################################################################
    title = f'''Power-On Test'''
    paragraph_text = f'''
        Purpose:
Verify that all power rails are correctly regulated and stable before functional operation begins.

Procedure:

Connect the DC power input (12V regulated supply).

Power on the unit.

Using a multimeter or oscilloscope, measure:

3.3V rail at the MCU VDD pin.

5.0V rail at sensor and peripheral power pins.

Ensure voltage is within:

3.3V ± 2% (3.23V - 3.37V)

5.0V ± 5% (4.75V - 5.25V)

Check for startup transients and excessive ripple using an oscilloscope (target: <50mV ripple).

Visually inspect for overheating regulators or misbehaving components.

Pass Criteria:

All measured voltages fall within tolerance.

No overheating components.

System remains powered and stable for 5 minutes.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # 5.2 Sensor Calibration and Response Test....................................
    ################################################################################
    title = f'''Sensor Calibration and Response Test'''
    paragraph_text = f'''
        Purpose:
Verify the ozone sensor responds correctly to varying concentrations and outputs analog values as expected.

Equipment Required:

Calibrated ozone generator (for lab testing)

Data acquisition system or MCU analog input

Known ozone concentrations (e.g., 0.05 ppm, 0.1 ppm, 0.2 ppm)

Procedure:

Place the device in a sealed test chamber.

Inject known ozone concentrations and allow stabilization (typically ~2 min).

Record sensor analog voltage for each concentration.

Compare against expected sensor curve from datasheet (e.g., MQ-131).

Optional: Log temperature and humidity to correct ozone readings.

Pass Criteria:

Sensor output is within ±10% of expected voltage response for given ppm.

Sensor noise (if monitored) is <5% of signal.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # 5.3 Functional Operation Test...............................................
    ################################################################################
    title = f'''Functional Operation Test'''
    paragraph_text = f'''
Purpose:
Verify the full system operates as intended over a full sanitization cycle.

Procedure:
Configure the device for a standard 5-minute sanitization cycle using the control interface.

Start the cycle and monitor:

Ozone generation begins within first 30 seconds.

Sensor feedback shows rising ozone concentration.

Ozone output curve stabilizes and peaks below the configured max (e.g., 0.2 ppm).

Verify control system responds appropriately:

Ozone generation stops when cycle ends or concentration limit is reached.

Ventilation system (if present) activates to clear residual ozone.

Check safety features:

If ozone exceeds safety threshold (e.g., 0.1 ppm), audible/visual alarm is triggered.

System enters lockout state until manual reset or timeout.

Pass Criteria:
System completes cycle without errors or resets.

Ozone levels follow expected profile.

Safety alarm triggers under over-concentration conditions.

Ozone returns to <0.05 ppm within 10 minutes post-cycle (with ventilation).
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # 5.4 Final QA Checklist......................................................
    ################################################################################
    title = f'''Final QA Checklist'''
    paragraph_text = f'''
| Test                      | Result    | Notes                 |
| ------------------------- | --------- | --------------------- |
| 3.3V Rail Stable          | Pass/Fail |                       |
| 5V Rail Stable            | Pass/Fail |                       |
| Sensor Response OK        | Pass/Fail | Voltage range checked |
| 5-Min Cycle Completed     | Pass/Fail |                       |
| Safety Alarm Trigger Test | Pass/Fail | Forced over ppm       |
| Ozone Cleared Post-Cycle  | Pass/Fail | Ventilation observed  |
| Physical Inspection       | Pass/Fail | Enclosure, wiring     |

Inspector: _____________________
Date: _____________________
Serial Number: ________________
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    ################################################################################
    # 6. Regulatory & Safety Considerations..................................[RGL]
    ################################################################################
    title = f'''Regulatory & Safety Considerations'''
    paragraph_text = f'''
        The ozone sanitization system operates with high-voltage ozone generation components and releases ozone gas into enclosed spaces. To ensure the system is safe for both users and technicians, and to meet regulatory compliance for commercial distribution, the following considerations have been addressed in the design:
    '''.strip()
    h1(pdf, title)
    paragraph(pdf, paragraph_text)

    # 6.1 Electrical Safety.......................................................
    ################################################################################
    title = f'''Electrical Safety'''
    paragraph_text = f'''
High-Voltage Clearance
The ozone generation module operates at voltages exceeding 2,000 V, necessitating strict physical separation between high-voltage and low-voltage circuits.

Minimum PCB clearance between high-voltage conductors and any other signal or ground trace is 6.0 mm, based on guidelines from IEC 61010-1 and IPC-2221B for pollution degree 2 environments.

Creepage distances are maintained using board layout techniques and routed slots near HV components when necessary.

Isolation and Protection
High-voltage sections are isolated using:

Optocouplers for signal control.

Ground plane separation and unbroken keep-out zones.

High-dielectric insulation in the ozone module's enclosure.

A fast-acting fuse and varistor are included on the input to protect from surges or reverse polarity connections.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # 6.2 EMI and Signal Integrity................................................
    ################################################################################
    title = f'''EMI and Signal Integrity'''
    paragraph_text = f'''
Shielding Techniques
Analog and digital signals-especially from the ozone, temperature, and humidity sensors-are routed separately from high-voltage switching lines.

Continuous ground fills are used under sensitive signal traces to reduce susceptibility to EMI.

A star grounding topology is implemented to avoid ground loops.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # 6.3 Ozone Exposure Safety...................................................
    ################################################################################
    title = f'''Ozone Exposure Safety'''
    paragraph_text = f'''
Occupational Exposure Compliance
Ozone is classified as a toxic gas at high concentrations. The system design enforces automated control to avoid unsafe ozone accumulation:

A real-time ozone sensor monitors air levels.

A cycle lockout timer ensures no operation occurs before the area is safe.

A ventilation sequence is automatically triggered at the end of each disinfection cycle.

The system is designed to comply with:

OSHA PEL: 0.1 ppm time-weighted average (TWA) over 8 hours.

NIOSH STEL: 0.3 ppm over 15 minutes.

Alarms & Fail-safes
A visual (LED) and audible (buzzer) alert is triggered if ozone levels exceed safety thresholds.

In the event of sensor failure, the system automatically halts ozone generation and logs an error.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # 6.4 Environmental Compliance................................................
    ################################################################################
    title = f'''Environmental Compliance'''
    paragraph_text = f'''
RoHS Directive 2011/65/EU
All electrical components, soldering materials, and PCBs used in the design are selected to be RoHS compliant, restricting the use of hazardous substances such as:

Lead (Pb)

Mercury (Hg)

Cadmium (Cd)

Hexavalent chromium (Cr6+)

PBB and PBDE flame retardants

A full compliance statement and supporting documentation from component suppliers are maintained in the manufacturing file.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    # 6.5 Target Regulatory Standards.............................................
    ################################################################################
    title = f'''Target Regulatory Standards'''
    paragraph_text = f'''
| Standard                   | Description                                                                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **IEC 61010-1**            | Safety requirements for electrical equipment for measurement, control, and laboratory use. Includes clearance/creepage, insulation, and protection. |
| **RoHS Directive**         | Restriction of Hazardous Substances in Electrical and Electronic Equipment.                                                                         |
| **OSHA 1910.1000**         | Occupational safety limits for ozone exposure in workplace environments.                                                                            |
| **NIOSH RELs**             | Recommended exposure limits for short-term exposure to ozone.                                                                                       |
| **IEC 60335-1 (optional)** | Safety for household and similar electrical appliances (if targeting consumer market).                                                              |
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)
    
    # 6.6 Labeling & Documentation................................................
    ################################################################################
    title = f'''Labeling & Documentation'''
    paragraph_text = f'''
The product is labeled with:

Cautionary notices: "High Voltage - Do Not Touch Internals."

Ozone Safety Label: Indicating restricted area entry during sanitization cycles.

User manual includes:

Operating precautions.

Maintenance schedules.

First-aid response to ozone overexposure.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    ################################################################################
    # 7. Appendix............................................................[APX]
    ################################################################################
    title = f'''Regulatory & Safety Considerations'''
    paragraph_text = f'''
    '''.strip()
    h1(pdf, title)
    paragraph(pdf, paragraph_text)
    
    # 7.1 Glossary................................................................
    ################################################################################
    title = f'''Glossary'''
    paragraph_text = f'''
| Term       | Description                                                                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MCU**    | *Microcontroller Unit* - The central control unit that manages sensor data, user input, and drives system logic. In this design, an STM32 32-bit MCU is used.           |
| **HV**     | *High Voltage* - Any voltage considered dangerous to humans or requiring special design rules. In this system, the ozone generator operates at high voltages (>2,000V). |
| **ppm**    | *Parts Per Million* - A measurement unit used to express the concentration of ozone in air. 1 ppm = 1 ozone molecule per 1 million air molecules.                       |
| **MOSFET** | *Metal-Oxide-Semiconductor Field-Effect Transistor* - Used for fast and efficient switching of high currents/voltages.                                                  |
| **DNP**    | *Do Not Populate* - A label in the BOM for optional components not assembled on the board.                                                                              |
| **RoHS**   | *Restriction of Hazardous Substances* - A directive restricting the use of certain hazardous materials in electrical/electronic products.                               |
| **FMEA**   | *Failure Modes and Effects Analysis* - A structured method for analyzing failure risks and their effects on the system.                                                 |
| **TWA**    | *Time-Weighted Average* - An occupational exposure standard representing average exposure to a chemical over a workday (e.g., OSHA's 0.1 ppm TWA for ozone).            |
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)
    
    # 7.2 Supporting Calculations.................................................
    ################################################################################
    title = f'''Supporting Calculations'''
    paragraph_text = f'''
Power Budget Estimate
This budget is used to size the power supply and check thermal constraints.
| Component Group                      | Approx. Power Draw           | Notes                                 |
| ------------------------------------ | ---------------------------- | ------------------------------------- |
| MCU (STM32F0 Series)                 | 80 mW                        | At full clock with peripherals active |
| Sensors (Ozone + Env)                | 150 mW                       | Ozone sensor + temp/humidity module   |
| User Interface (LEDs, buttons)       | 20 mW                        | Minimal draw; mostly idle             |
| Communication Module (e.g., ESP8266) | 50 mW (avg) / 200 mW (burst) | If enabled                            |
| **Low-Voltage Subtotal**             | **\~300 mW**                 | 5V and 3.3V rails                     |
| Ozone Generator Driver               | **15 W (peak)**              | Assumes 12V input @ 1.25A             |
| Safety Circuitry, margin             | \~0.5 W                      | Pull-ups, optocouplers, losses        |
| **Total Estimated Max**              | **\~16 W**                   | System-wide under full load           |
Notes:

A 12V/2A power supply provides sufficient margin.

Consider heatsinking and airflow for ozone driver module.

Ozone Output Estimation
Ozone Generator Module Specs:

Rated output: 100 mg/h (nominal) to 200 mg/h (peak, dry air)

Efficiency varies by temperature and humidity

Cycle time for room sterilization: 10-30 min (based on volume)

Estimated Ozone Output Curve vs. Time
(Insert real or simulated graph, or describe the trend.)
Time (min)    | Ozone Concentration (ppm)
--------------|---------------------------
0             | 0.00
1             | 0.05
2             | 0.10
3             | 0.20
4             | 0.35
5             | 0.45 (peak)
6-10          | 0.40-0.50 (steady)
>10           | Saturation or decay based on ventilation

Graph Notes:

Actual values depend on enclosure volume, airflow, humidity.

Use an ozone sensor with real-time monitoring to adjust cycle times dynamically.

Ventilation Decay Curve (Optional)
Also consider plotting ozone decay vs. time post-sanitization to ensure levels fall below 0.1 ppm within acceptable re-entry time (typically 30-60 minutes depending on ventilation).

    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    ################################################################################
    # 8. Document References.................................................[RFR]
    ################################################################################
    title = f'''Document References'''
    paragraph_text = f'''
        The ozone sanitization system operates with high-voltage ozone generation components and releases ozone gas into enclosed spaces. To ensure the system is safe for both users and technicians, and to meet regulatory compliance for commercial distribution, the following considerations have been addressed in the design:
    '''.strip()
    h1(pdf, title)
    paragraph(pdf, paragraph_text)
    
    # 8.1 Schematics..............................................................
    ################################################################################
    title = f'''Schematics'''
    paragraph_text = f'''
File: /Schematics/Ozone_Sanitizer_Schematics.pdf
Description:
This file contains the full set of electrical schematics for the ozone sanitization system. Each page is labeled and organized by subsystem:

Power Supply

Microcontroller Unit (MCU)

Ozone Generator Driver Circuit

Sensor Interface

User Interface (buttons, indicators)

Purpose:
Used by hardware engineers for troubleshooting, modification, and understanding circuit functionality. Essential for PCB layout review and testing.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)
    
    # 8.2 PCB Layout..............................................................
    ################################################################################
    title = f'''PCB Layout'''
    paragraph_text = f'''
File: /PCB_Layout/Fabrication_Drawing.pdf
Description:
Mechanical drawing of the PCB design including:

Board dimensions

Hole sizes and positions

Component outlines

Layer stack-up information

Mounting hole placement and tolerances

Notes for PCB fabrication (e.g., copper weight, soldermask color)

Purpose:
Used by PCB manufacturers to fabricate the physical board. Provides necessary information to ensure mechanical compatibility and manufacturability.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)
    
    # 8.3 Bill of Materials (BOM).................................................
    ################################################################################
    title = f'''Bill of Materials (BOM)'''
    paragraph_text = f'''
File: /BOM/Ozone_Sanitizer_BOM.xlsx
Description:
Complete list of all electronic and electromechanical components used in the system. Columns include:

Reference Designator (e.g., R1, U3, C5)

Component Description and Value

Manufacturer Name

Manufacturer Part Number

Preferred Distributor & SKU

Package/Footprint

Quantity per board

Notes (e.g., "Do not populate," "Critical component," "Alt allowed")

Purpose:
Used for sourcing components, estimating costs, and preparing for production. Also used by assembly houses to order and place components.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)
    
    # 8.4 Testing & Quality Control...............................................
    ################################################################################
    title = f'''Testing & Quality Control'''
    paragraph_text = f'''
File: /Testing_and_QC/Test_Procedures.pdf
Description:
Step-by-step procedures for verifying correct functionality of assembled boards and the final system. Includes:

Visual inspection checklist

Power-up verification (voltage rails, current draw)

Ozone output testing procedure

Sensor accuracy test using controlled exposure

Pass/fail criteria

Safety checks (e.g., HV isolation, shutdown behavior)

Purpose:
Used by QA technicians and engineers during pre-deployment and batch production testing. Ensures that each unit meets functional and safety requirements.
    '''.strip()
    h2(pdf, title)
    paragraph(pdf, paragraph_text)

    ########################################
    # SAVE...........................[SAV]
    ########################################
    pdf.output('Master_Document.pdf')

doc_master()

from fpdf import FPDF


# TABLE OF CONTENTS:
# ......................................
# System Overview................[OVR]
# Hardware Design................[HRD]

def h1(pdf, text):
    pdf.set_font("Arial", size=36)
    pdf.cell(0, 5, txt=text, ln=True)
    pdf.ln()

def h2(pdf, text):
    pdf.set_font("Arial", size=24)
    pdf.cell(0, 5, txt=text, ln=True)
    pdf.ln()

def h3(pdf, text):
    pdf.set_font("Arial", size=16)
    pdf.ln()
    pdf.cell(0, 5, txt=text, ln=True)
    pdf.ln()
    
def paragraph(pdf, text):
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 6, txt=text, ln=True)

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

    pdf.add_page()

    pdf.set_font("Arial", size=16)
    # pdf.cell(200, 10, txt="My First PDF", ln=True, align='C')
    h1(pdf, title)
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

    ########################################
    # SYSTEM OVERVIEW................[OVR]
    ########################################
    pdf.add_page()
    h2_text = f'''1. System Overview'''
    h2(pdf, h2_text)
    
    # Purpose.............................
    ########################################
    h3_text = f'''1.1 Purpose'''
    paragraph_text = f'''The Ozone Sanitization System is an automated disinfection device designed for enclosed environments such as rooms, cabinets, vehicles, HVAC ducts, and medical storage areas. It utilizes ozone gas (O3) to neutralize bacteria, viruses, fungi, and volatile organic compounds (VOCs) on surfaces and in the air.

Ozone is a powerful oxidizer, but it must be precisely generated and controlled due to its potential health risks. This system manages the ozone generation, concentration monitoring, safety interlocks, and exposure time to ensure safe and effective sanitization cycles, suitable for both industrial and consumer applications.
    '''.strip()
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)
    
    # Key Features........................
    ########################################
    h3_text = f'''1.2 Key Features'''
    paragraph_text = f'''Programmable Ozone Generation Cycles
Users can schedule automated cycles (e.g., 5, 10, 30 minutes) depending on room size and sanitization requirements. Optional pre- and post-cycle ventilation logic can be enabled.

Real-Time Ozone Concentration Monitoring
An onboard ozone gas sensor measures real-time O3 levels (in ppm), enabling dynamic control of the generator and accurate cycle termination.

Touch or Mobile App Control
The system can be operated via an onboard touch interface or remotely using a companion mobile app (via Wi-Fi/Bluetooth), allowing for flexible, remote scheduling and safety alerts.

Safety Lockouts and Timers
Built-in safety features include:

Delayed start (to allow exit from the room)

Automatic shutdown if ozone exceeds safety limits

Lockout until residual ozone falls below 0.1 ppm

Audible/visual alarms during and after operation

Wi-Fi/Bluetooth Connectivity (Optional)
For cloud logging, OTA updates, and remote monitoring, wireless connectivity is optionally available through a dedicated module (e.g., ESP32 or external BLE module).
    '''.strip()
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Operating Conditions................
    ########################################
    h3_text = f'''1.3 Operating Conditions'''
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # System Block Diagram................
    ########################################
    h3_text = f'''1.4 System Block Diagram'''
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Operating Conditions................
    ########################################
    h3_text = f'''1.5 System Summary'''
    paragraph_text = f'''
This ozone sanitization unit provides a complete, standalone disinfection solution that's both intelligent and safety-conscious. Its modular architecture allows future expansions (e.g., logging, multi-room control, cloud connectivity) and customization based on application or regulatory needs.
'''
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    ########################################
    # HARDWARE DESIGN................[HRD]
    ########################################
    pdf.add_page()
    h2_text = f'''2. Hardware Design'''
    h2(pdf, h2_text)

    # Schematics..........................
    ########################################
    h3_text = f'''1.1 Schematics'''.strip()
    paragraph_text = f'''
        The circuit design is organized across five functional pages, each serving a distinct purpose in the overall system. Below is a detailed explanation of each schematic section:
    '''.strip()
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Power Regulation....................
    ########################################
    pdf.add_page()
    h3_text = f'''Power Regulation'''.strip()
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Microcontroller and Interfaces......
    ########################################
    pdf.add_page()
    h3_text = f'''Microcontroller and Interfaces'''.strip()
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Ozone Generator Driver..............
    ########################################
    pdf.add_page()
    h3_text = f'''Ozone Generator Driver'''.strip()
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Sensors.............................
    ########################################
    pdf.add_page()
    h3_text = f'''Sensors'''.strip()
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # User Interface......................
    ########################################
    pdf.add_page()
    h3_text = f'''User Interface'''.strip()
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Note................................
    ########################################
    pdf.add_page()
    h3_text = f'''Note'''.strip()
    paragraph_text = f'''
Full schematic drawings, with component values, designators, and annotations, are provided in /Schematics/Ozone_Sanitizer_Schematics.pdf. Editable source files (KiCad/Altium) are included in /Schematics/Source_Files/.
    '''.strip()
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # PCB Layout..........................
    ########################################
    pdf.add_page()
    h3_text = f'''PCB Layout'''.strip()
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)


    ########################################
    # Bill of Materials..............[BOM]
    ########################################
    pdf.add_page()
    h2_text = f'''3. Bill of Materials (BOM)'''
    paragraph_text = f'''
The Bill of Materials (BOM) lists every component required to assemble the ozone sanitization system. This section provides a summary of the most critical components in the system, along with key information such as part numbers, manufacturers, and the roles they play in the circuit.

The complete, detailed BOM-containing all passive and active components, alternative part options, package sizes, and supplier references-is available in:
/BOM/Ozone_Sanitizer_BOM.xlsx
    '''.strip()
    h2(pdf, h2_text)
    paragraph(pdf, paragraph_text)

    # Critical Components.................
    ########################################
    pdf.add_page()
    h3_text = f'''Critical Components'''.strip()
    paragraph_text = f'''
These parts are essential for the core functionality of the system. Substitutions or sourcing changes should be carefully evaluated.

Ref	Description	Part Number	Manufacturer	Role in System
U1	Microcontroller (ARM Cortex-M0)	STM32F030F4P6	STMicroelectronics	Central control unit for ozone timing, sensor reading, and user interface logic
U3	Ozone Sensor (Analog Output)	MQ-131	Winsen	Senses ambient ozone concentration (ppm) during and after sanitization cycles
Q1	High Voltage MOSFET	IRF840	Infineon	Switches power to the high-voltage ozone generator module in PWM mode
D1	Fast Recovery Flyback Diode	UF4007	ON Semiconductor	Protects the MOSFET from voltage spikes caused by inductive load switching
    '''.strip()
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Supporting Components...............
    ########################################
    pdf.add_page()
    h3_text = f'''Supporting Components'''.strip()
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Design and Sourcing Notes...........
    ########################################
    pdf.add_page()
    h3_text = f'''Design and Sourcing Notes'''.strip()
    paragraph_text = f'''
Footprints: All components are chosen with standard SMD or through-hole footprints (e.g., 0603 passives, TO-220, DIP/SOIC).

Availability: Parts selected based on stable supply from major distributors (Digi-Key, Mouser, LCSC).

RoHS Compliance: All critical components are RoHS compliant for environmental safety.

Cost Considerations: Cost-effective components chosen without compromising safety (especially in HV areas).
    '''.strip()
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Component Substitution Guidelines...
    ########################################
    pdf.add_page()
    h3_text = f'''Component Substitution Guidelines'''.strip()
    paragraph_text = f'''
Ref	Substitute Criteria	Notes
U1	Any STM32F0/F1 MCU with same pinout	Ensure bootloader and clock settings match
U3	Compatible analog ozone sensor	Must match voltage range and warm-up time (e.g., SPEC Sensors)
Q1	Any N-channel MOSFET, 500V+, >5A rating	Gate threshold and Rds(on) should be similar
D1	Any fast recovery diode, >1000V, 1A+	UF4004, UF5408 can also work depending on size
    '''.strip()
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    # Component Substitution Guidelines...
    ########################################
    pdf.add_page()
    h3_text = f'''Full BOM File Contents'''.strip()
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
    h3(pdf, h3_text)
    paragraph(pdf, paragraph_text)

    ########################################
    # SAVE...........................[SAV]
    ########################################
    pdf.output('Master_Document.pdf')

doc_master()
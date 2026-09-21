# Stakeholder Requirement Matrix

## Ozone Sensor Expansion Module — ZE27-O3 / RS485 / CORE

### 1. Purpose

This document defines the questions to be addressed with the stakeholders of the ozone sensor expansion module.

The objective is to identify stakeholder needs, constraints, expected behavior, failure handling, interfaces, and verification expectations before deriving the formal module requirements.

The module under consideration:

* acquires measurements from one ZE27-O3 ozone sensor;
* communicates with the sensor through RS485-1;
* validates the received sensor data;
* stores the latest valid measurement;
* communicates with the main CORE through RS485-2;
* acts as a Modbus slave on RS485-2;
* is installed inside an electrical control cabinet on DIN rail.

The answers collected through these interviews shall be subsequently transformed into formal stakeholder and system/module requirements.

---

# 2. Stakeholder Matrix

## STK-007 / STK-008 — System Architect / System Engineer

### Objective

Understand the role of the module within the complete ozone system and establish its functional boundaries.

| ID     | Question                                                                                                                          |
| ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| SYS-01 | What is the exact purpose of this module within the complete system?                                                              |
| SYS-02 | What functions are explicitly within the responsibility of this module?                                                           |
| SYS-03 | Which functions are explicitly outside the responsibility of this module?                                                         |
| SYS-04 | Is the module considered only a communication gateway, or does it have responsibility for measurement validation and diagnostics? |
| SYS-05 | Which system functions depend on the ozone measurement provided by this module?                                                   |
| SYS-06 | What is the maximum acceptable delay between acquisition by the sensor and availability of the measurement to the CORE?           |
| SYS-07 | What is the required measurement update frequency at system level?                                                                |
| SYS-08 | What should the system do if the module does not provide a valid measurement?                                                     |
| SYS-09 | What should happen if the module completely loses communication with the CORE?                                                    |
| SYS-10 | What should happen if the module loses communication with the sensor?                                                             |
| SYS-11 | What should happen if the sensor provides an invalid measurement?                                                                 |
| SYS-12 | How should an obsolete/stale measurement be treated by the system?                                                                |
| SYS-13 | Is the latest valid measurement allowed to remain available after communication with the sensor is lost?                          |
| SYS-14 | If yes, for how long may the last valid measurement be considered usable?                                                         |
| SYS-15 | What information about the sensor/module state must be visible to the rest of the system?                                         |
| SYS-16 | Are there system-level startup requirements for the module?                                                                       |
| SYS-17 | Are there system-level reset or recovery requirements?                                                                            |
| SYS-18 | What are the expected behaviors during power loss and power restoration?                                                          |
| SYS-19 | Are there existing system interfaces or conventions that the module must follow?                                                  |
| SYS-20 | Are there future versions or variants of the system that this module should be able to support?                                   |
| SYS-21 | Are there requirements for backward compatibility with existing CORE firmware?                                                    |
| SYS-22 | Are there requirements for forward compatibility with future CORE firmware?                                                       |
| SYS-23 | Are there system-level safety or hazard analyses that impose requirements on this module?                                         |
| SYS-24 | What environmental conditions must the module operate under as part of the complete system?                                       |
| SYS-25 | Which existing system requirements should be inherited by this module?                                                            |
| SYS-26 | Which system-level requirements are particularly critical and must not be violated?                                               |
| SYS-27 | What assumptions are currently made about the module that need to be explicitly verified?                                         |
| SYS-28 | Are there known limitations or known failure scenarios from previous versions of the system?                                      |
| SYS-29 | Are there existing modules with similar functionality whose behavior should be reused?                                            |
| SYS-30 | What is the expected lifecycle of the module and the overall system?                                                              |

---

# 3. STK-011 / STK-012 — CORE Firmware / Software Engineer

### Objective

Define the complete interface between the module and the CORE.

| ID      | Question                                                                         |
| ------- | -------------------------------------------------------------------------------- |
| CORE-01 | What exact communication protocol must be used between the CORE and the module?  |
| CORE-02 | Is Modbus RTU the required protocol?                                             |
| CORE-03 | What Modbus slave address should the module use?                                 |
| CORE-04 | How is the module address configured?                                            |
| CORE-05 | Must the address be fixed, configurable, or automatically assigned?              |
| CORE-06 | What baud rate, parity, data bits, and stop bits must be used?                   |
| CORE-07 | Which Modbus function codes must the module support?                             |
| CORE-08 | Which registers must the CORE be able to read?                                   |
| CORE-09 | Are any registers required for writing configuration or commands to the module?  |
| CORE-10 | What data format should be used for the ozone measurement?                       |
| CORE-11 | What unit should be used for the ozone measurement?                              |
| CORE-12 | What resolution is required for the ozone measurement?                           |
| CORE-13 | What numerical range must be supported?                                          |
| CORE-14 | How should invalid or unavailable measurements be represented?                   |
| CORE-15 | Does the CORE need a separate measurement-validity flag?                         |
| CORE-16 | Does the CORE need to know when the measurement becomes stale?                   |
| CORE-17 | Does the CORE need to know the age of the last valid measurement?                |
| CORE-18 | Which sensor and module diagnostic information must be exposed through Modbus?   |
| CORE-19 | Does the CORE need error counters?                                               |
| CORE-20 | How frequently will the CORE poll the module?                                    |
| CORE-21 | What is the maximum acceptable response time to a valid Modbus request?          |
| CORE-22 | What should happen if the CORE receives no response?                             |
| CORE-23 | How many retries will the CORE perform after a communication failure?            |
| CORE-24 | How should Modbus exception responses be handled?                                |
| CORE-25 | What should happen if the CORE receives an invalid measurement status?           |
| CORE-26 | What should happen if the module returns a stale measurement?                    |
| CORE-27 | What should happen if the module resets while the CORE is operating?             |
| CORE-28 | What behavior is expected immediately after module startup?                      |
| CORE-29 | Are there restrictions on consecutive Modbus requests?                           |
| CORE-30 | Are there timing constraints imposed by the existing CORE Modbus implementation? |

---

# 4. STK-017 / STK-018 / STK-019 — Sensor / Instrumentation Engineer

### Objective

Fully characterize the ZE27-O3 interface and behavior.

| ID     | Question                                                                                                                 |
| ------ | ------------------------------------------------------------------------------------------------------------------------ |
| SNS-01 | What exact ZE27-O3 variant/model is being used?                                                                          |
| SNS-02 | What communication protocol does the sensor use?                                                                         |
| SNS-03 | Is communication with the sensor one-way or request/response?                                                            |
| SNS-04 | Which device is the RS485 master on the sensor interface?                                                                |
| SNS-05 | What are the RS485 baud rate, parity, data bits, and stop bits?                                                          |
| SNS-06 | What sensor address is used?                                                                                             |
| SNS-07 | Is the sensor address configurable?                                                                                      |
| SNS-08 | How is the beginning of a sensor frame identified?                                                                       |
| SNS-09 | How is the end of a sensor frame identified?                                                                             |
| SNS-10 | Is the frame length fixed or variable?                                                                                   |
| SNS-11 | How is the expected frame length determined?                                                                             |
| SNS-12 | What is the exact frame format?                                                                                          |
| SNS-13 | Which bytes contain the ozone measurement?                                                                               |
| SNS-14 | What unit is used by the sensor?                                                                                         |
| SNS-15 | What is the measurement range?                                                                                           |
| SNS-16 | What is the measurement resolution?                                                                                      |
| SNS-17 | What accuracy is guaranteed by the sensor?                                                                               |
| SNS-18 | What CRC/checksum algorithm is used?                                                                                     |
| SNS-19 | Which bytes are included in the CRC calculation?                                                                         |
| SNS-20 | What is the CRC byte order?                                                                                              |
| SNS-21 | How frequently does the sensor transmit measurements?                                                                    |
| SNS-22 | Does the sensor require an initialization or warm-up period?                                                             |
| SNS-23 | How long after power-on can the first valid measurement be expected?                                                     |
| SNS-24 | What happens when the sensor cannot produce a valid measurement?                                                         |
| SNS-25 | Does the sensor transmit explicit error/status codes?                                                                    |
| SNS-26 | Are there special values indicating invalid measurements?                                                                |
| SNS-27 | What happens when the measured concentration is outside the specified range?                                             |
| SNS-28 | What happens when the sensor loses power and subsequently restarts?                                                      |
| SNS-29 | What happens if communication is interrupted and then restored?                                                          |
| SNS-30 | Are there known communication anomalies, timing constraints, or undocumented behaviors that the module must accommodate? |

---

# 5. STK-070 — Ozone Process Engineer

### Objective

Understand what the ozone measurement actually means to the process and how its quality affects system behavior.

| ID      | Question                                                                             |
| ------- | ------------------------------------------------------------------------------------ |
| PROC-01 | What process variable is the ozone sensor measuring?                                 |
| PROC-02 | What unit is used at process level?                                                  |
| PROC-03 | What measurement range is required by the process?                                   |
| PROC-04 | What measurement resolution is required by the process?                              |
| PROC-05 | What measurement accuracy is required by the process?                                |
| PROC-06 | How frequently does the process need a new measurement?                              |
| PROC-07 | What is the maximum acceptable measurement latency?                                  |
| PROC-08 | How should a missing measurement be treated by the process?                          |
| PROC-09 | How should an invalid measurement be treated?                                        |
| PROC-10 | How should an obsolete measurement be treated?                                       |
| PROC-11 | Is the latest valid measurement useful after sensor communication is lost?           |
| PROC-12 | If so, for how long?                                                                 |
| PROC-13 | What measurement values should be considered physically impossible?                  |
| PROC-14 | Are there expected transient values during startup or shutdown?                      |
| PROC-15 | Are there process states in which the sensor measurement should be ignored?          |
| PROC-16 | Are there conditions under which the sensor measurement is known to be unreliable?   |
| PROC-17 | Does the process require detection of rapid changes in ozone concentration?          |
| PROC-18 | Is filtering or averaging of the sensor measurement required?                        |
| PROC-19 | If filtering is required, where should it be performed: sensor, module, or CORE?     |
| PROC-20 | Is calibration information required by the process?                                  |
| PROC-21 | Does the process require detection of sensor drift?                                  |
| PROC-22 | Are there process alarms based on the ozone measurement?                             |
| PROC-23 | Which measurement faults must be distinguished at process level?                     |
| PROC-24 | What is the consequence of receiving an incorrect but numerically valid measurement? |
| PROC-25 | Are there process-specific requirements for measurement availability or continuity?  |

---

# 6. STK-013 — Module Firmware Engineer

### Objective

Define implementable firmware behavior while avoiding premature architectural decisions.

| ID    | Question                                                                                        |
| ----- | ----------------------------------------------------------------------------------------------- |
| FW-01 | What operating states must the module support?                                                  |
| FW-02 | What must happen immediately after power-on?                                                    |
| FW-03 | What must happen if initialization of RS485-1 fails?                                            |
| FW-04 | What must happen if initialization of RS485-2 fails?                                            |
| FW-05 | How should incoming sensor frames be detected?                                                  |
| FW-06 | What determines that a complete sensor frame has been received?                                 |
| FW-07 | What timeout shall be used during frame reception?                                              |
| FW-08 | What should happen when a frame is incomplete?                                                  |
| FW-09 | What should happen when a frame exceeds the maximum expected size?                              |
| FW-10 | What should happen when a frame contains an invalid header or structure?                        |
| FW-11 | What should happen when CRC validation fails?                                                   |
| FW-12 | Should invalid frames affect the last valid measurement?                                        |
| FW-13 | How should the module detect loss of communication with the sensor?                             |
| FW-14 | How should measurement age be tracked?                                                          |
| FW-15 | How should measurement validity be represented internally?                                      |
| FW-16 | How should the module behave if a valid sensor frame arrives while processing a Modbus request? |
| FW-17 | How should the module behave if a Modbus request arrives while receiving sensor data?           |
| FW-18 | What happens if multiple Modbus requests arrive consecutively?                                  |
| FW-19 | What should happen after a Modbus CRC error?                                                    |
| FW-20 | What should happen after an unsupported Modbus function code?                                   |
| FW-21 | What should happen after a Modbus request timeout?                                              |
| FW-22 | How should RS485 direction control be handled?                                                  |
| FW-23 | What conditions determine that RS485 transmission is complete?                                  |
| FW-24 | What should happen if the interface cannot return to receive mode?                              |
| FW-25 | What watchdog/recovery behavior is required?                                                    |
| FW-26 | Which internal errors should be latched and which should automatically clear?                   |
| FW-27 | Which diagnostic counters should be maintained?                                                 |
| FW-28 | What behavior is required after firmware reset?                                                 |
| FW-29 | What behavior is required after watchdog reset?                                                 |
| FW-30 | What behavior must be deterministic and time-bounded?                                           |

---

# 7. STK-014 — Module Hardware Engineer

### Objective

Identify electrical and electronic requirements.

| ID    | Question                                                                      |
| ----- | ----------------------------------------------------------------------------- |
| HW-01 | What supply voltage is available to the module?                               |
| HW-02 | What are the minimum and maximum allowed supply voltages?                     |
| HW-03 | What maximum current consumption is permitted?                                |
| HW-04 | Are there startup current constraints?                                        |
| HW-05 | Is galvanic isolation required between the module and the RS485 interfaces?   |
| HW-06 | Is galvanic isolation required between the module and the power supply?       |
| HW-07 | What RS485 transceiver characteristics are required?                          |
| HW-08 | Are termination resistors required?                                           |
| HW-09 | How should RS485 biasing/failsafe resistors be implemented?                   |
| HW-10 | Who is responsible for RS485 termination in the complete system?              |
| HW-11 | What protection is required against ESD?                                      |
| HW-12 | What protection is required against surge/transient events?                   |
| HW-13 | What reverse-polarity protection is required?                                 |
| HW-14 | What overvoltage/overcurrent protection is required?                          |
| HW-15 | What watchdog and reset mechanisms are required?                              |
| HW-16 | Is non-volatile storage required for configuration or diagnostics?            |
| HW-17 | What information must remain available after power cycling?                   |
| HW-18 | Are status LEDs required?                                                     |
| HW-19 | Which physical conditions must be indicated by LEDs?                          |
| HW-20 | Is a hardware reset required?                                                 |
| HW-21 | Is a service/programming interface required?                                  |
| HW-22 | Is firmware update possible after the module is installed in the cabinet?     |
| HW-23 | What PCB environmental requirements apply?                                    |
| HW-24 | What maximum operating temperature must be supported?                         |
| HW-25 | What maximum power dissipation is permitted?                                  |
| HW-26 | Are creepage/clearance requirements applicable?                               |
| HW-27 | What grounding architecture is required?                                      |
| HW-28 | How should cable shields be connected?                                        |
| HW-29 | Are there constraints on component selection, approved vendors, or lifecycle? |
| HW-30 | Are there hardware reuse requirements from existing modules?                  |

---

# 8. STK-020 / STK-021 — Electrical / Control Cabinet Engineer

### Objective

Define how the module must be installed and wired in the actual control cabinet.

| ID     | Question                                                              |
| ------ | --------------------------------------------------------------------- |
| CAB-01 | What DIN rail standard and dimensions must the module support?        |
| CAB-02 | What maximum module width is available?                               |
| CAB-03 | Where will the module be positioned relative to the CORE?             |
| CAB-04 | What other devices will be installed next to the module?              |
| CAB-05 | Are there thermal constraints due to neighboring devices?             |
| CAB-06 | What supply voltage and wiring system will be used?                   |
| CAB-07 | Which terminals must be accessible from the front?                    |
| CAB-08 | What connector/m terminal type is preferred or mandatory?             |
| CAB-09 | What wire cross-sections must be supported?                           |
| CAB-10 | Are ferrules or specific terminal technologies required?              |
| CAB-11 | How should RS485 wiring be routed?                                    |
| CAB-12 | Are separate cable routes required for power and communication?       |
| CAB-13 | What type of RS485 cable will be used?                                |
| CAB-14 | Is shielded cable mandatory?                                          |
| CAB-15 | Where should the cable shield be connected?                           |
| CAB-16 | Are there cabinet grounding requirements that affect the module?      |
| CAB-17 | Are there cabinet-level EMC requirements?                             |
| CAB-18 | Must the module remain accessible after cabinet installation?         |
| CAB-19 | Must LEDs remain visible when the cabinet is closed?                  |
| CAB-20 | Are labels or terminal markings required?                             |
| CAB-21 | What information must be printed on the module?                       |
| CAB-22 | Is module removal possible without disconnecting neighboring modules? |
| CAB-23 | Is hot-plugging allowed or prohibited?                                |
| CAB-24 | What installation procedure should be followed during commissioning?  |
| CAB-25 | Are there restrictions on cable length for either RS485 interface?    |

---

# 9. STK-025 — Functional Safety Engineer

### Objective

Define the consequences and required behavior of incorrect, missing, delayed, or stale measurements.

| ID      | Question                                                                                      |
| ------- | --------------------------------------------------------------------------------------------- |
| SAFE-01 | Is the ozone measurement used by a safety-related function?                                   |
| SAFE-02 | Can failure of this module contribute to a hazardous situation?                               |
| SAFE-03 | What hazardous conditions can result from an incorrect ozone measurement?                     |
| SAFE-04 | What hazardous conditions can result from a missing measurement?                              |
| SAFE-05 | What hazardous conditions can result from an obsolete measurement?                            |
| SAFE-06 | What is the required safe behavior after loss of the sensor signal?                           |
| SAFE-07 | What is the required safe behavior after loss of communication with the CORE?                 |
| SAFE-08 | What is the required safe behavior after a module internal failure?                           |
| SAFE-09 | Must invalid measurements be explicitly identified?                                           |
| SAFE-10 | What maximum time may elapse before a sensor communication failure is detected?               |
| SAFE-11 | What maximum time may elapse before a stale measurement is declared invalid?                  |
| SAFE-12 | Is the last valid measurement allowed to remain available after sensor failure?               |
| SAFE-13 | If yes, for how long?                                                                         |
| SAFE-14 | Must different fault types be distinguishable?                                                |
| SAFE-15 | Which faults must be latched?                                                                 |
| SAFE-16 | Which faults may automatically clear after recovery?                                          |
| SAFE-17 | What is the expected behavior after power-on before a valid sensor measurement is available?  |
| SAFE-18 | What is the expected behavior after a watchdog reset?                                         |
| SAFE-19 | Are diagnostic mechanisms required to detect latent failures?                                 |
| SAFE-20 | Are redundant measurements or plausibility checks required?                                   |
| SAFE-21 | Are there limits on the probability of dangerous failure?                                     |
| SAFE-22 | Is a specific safety integrity level or performance level applicable?                         |
| SAFE-23 | Which safety standards apply to this function?                                                |
| SAFE-24 | Which failure modes must be considered in the system hazard analysis?                         |
| SAFE-25 | Which safety requirements must be inherited by the module?                                    |
| SAFE-26 | What evidence must the module provide to demonstrate compliance with the safety requirements? |

---

# 10. STK-031 / STK-033 — Verification / Test Engineer

### Objective

Ensure that every requirement can be objectively verified.

| ID      | Question                                                                       |
| ------- | ------------------------------------------------------------------------------ |
| TEST-01 | How should successful sensor communication be verified?                        |
| TEST-02 | How should frame reception be tested?                                          |
| TEST-03 | How should incomplete frames be tested?                                        |
| TEST-04 | How should oversized frames be tested?                                         |
| TEST-05 | How should CRC errors be injected and detected?                                |
| TEST-06 | How should corrupted sensor data be tested?                                    |
| TEST-07 | How should sensor communication timeout be tested?                             |
| TEST-08 | How should sensor disconnection be tested?                                     |
| TEST-09 | How should sensor reconnection be tested?                                      |
| TEST-10 | How should startup/warm-up behavior be verified?                               |
| TEST-11 | How should the last valid measurement behavior be verified?                    |
| TEST-12 | How should stale measurement detection be verified?                            |
| TEST-13 | How should Modbus request reception be verified?                               |
| TEST-14 | How should Modbus CRC errors be tested?                                        |
| TEST-15 | How should unsupported function codes be tested?                               |
| TEST-16 | How should invalid register requests be tested?                                |
| TEST-17 | How should Modbus response timing be measured?                                 |
| TEST-18 | How should RS485 direction switching be verified?                              |
| TEST-19 | How should simultaneous or closely spaced sensor/Core communication be tested? |
| TEST-20 | How should watchdog recovery be tested?                                        |
| TEST-21 | How should power cycling be tested?                                            |
| TEST-22 | How should brown-out or supply interruption be tested?                         |
| TEST-23 | Which diagnostic counters/statuses must be externally verifiable?              |
| TEST-24 | What test interfaces are required?                                             |
| TEST-25 | Are automated tests required?                                                  |
| TEST-26 | What test equipment is available?                                              |
| TEST-27 | What environmental tests are required?                                         |
| TEST-28 | What EMC tests are required?                                                   |
| TEST-29 | What boundary conditions must be tested?                                       |
| TEST-30 | What constitutes pass/fail for each critical behavior?                         |

---

# 11. STK-043 / STK-045 — Service / Maintenance Engineer

### Objective

Define requirements that make the module diagnosable, replaceable, and maintainable in the field.

| ID      | Question                                                                                        |
| ------- | ----------------------------------------------------------------------------------------------- |
| SERV-01 | How will a technician determine that the module is malfunctioning?                              |
| SERV-02 | How will a technician distinguish a sensor fault from a module fault?                           |
| SERV-03 | How will a technician distinguish a sensor communication fault from a CORE communication fault? |
| SERV-04 | Are status LEDs required?                                                                       |
| SERV-05 | What information should each LED communicate?                                                   |
| SERV-06 | Are diagnostic registers required?                                                              |
| SERV-07 | Which errors should be visible to a service technician?                                         |
| SERV-08 | Should error counters be retained after reset?                                                  |
| SERV-09 | Should error history be retained after power loss?                                              |
| SERV-10 | How should the module be reset during service?                                                  |
| SERV-11 | Is a physical reset button required?                                                            |
| SERV-12 | Is remote reset required?                                                                       |
| SERV-13 | Can the module be replaced without modifying the CORE configuration?                            |
| SERV-14 | Can a replacement module automatically obtain its configuration?                                |
| SERV-15 | How is the Modbus address configured on a replacement module?                                   |
| SERV-16 | How is firmware version identified?                                                             |
| SERV-17 | How is hardware revision identified?                                                            |
| SERV-18 | Is a serial number or unique module ID required?                                                |
| SERV-19 | How should firmware be updated in the field?                                                    |
| SERV-20 | What should happen if firmware update fails?                                                    |
| SERV-21 | What service tools are available?                                                               |
| SERV-22 | Is a laptop/service interface required?                                                         |
| SERV-23 | What information should be available without connecting a service tool?                         |
| SERV-24 | What information should be available through the CORE?                                          |
| SERV-25 | What are the expected replacement time and service constraints?                                 |
| SERV-26 | Are there environmental or safety precautions for servicing the module?                         |
| SERV-27 | Are there existing troubleshooting procedures that the module must support?                     |
| SERV-28 | What are the most common failures observed on similar systems?                                  |
| SERV-29 | Which diagnostic information would significantly reduce troubleshooting time?                   |
| SERV-30 | What field failure information should be recorded and returned to engineering?                  |

---

# 12. Cross-Stakeholder Questions

These questions should be asked across multiple stakeholders because they often reveal contradictions.

| ID       | Question                                                       | Primary stakeholders                 |
| -------- | -------------------------------------------------------------- | ------------------------------------ |
| CROSS-01 | What exactly constitutes a valid ozone measurement?            | System, Sensor, Process, Safety      |
| CROSS-02 | What exactly constitutes an invalid measurement?               | Sensor, Process, Safety, CORE        |
| CROSS-03 | How long can the last valid measurement be used?               | System, Process, Safety, CORE        |
| CROSS-04 | Who is responsible for declaring the measurement stale?        | System, Firmware, CORE, Safety       |
| CROSS-05 | Who is responsible for filtering or averaging the measurement? | Sensor, Process, Firmware, CORE      |
| CROSS-06 | Who owns the definition of the Modbus register map?            | System, CORE, Firmware               |
| CROSS-07 | Who owns the definition of sensor protocol parameters?         | Sensor, Firmware                     |
| CROSS-08 | Who defines communication timeout values?                      | System, CORE, Firmware               |
| CROSS-09 | Who defines the safe behavior after sensor failure?            | Safety, System, Process              |
| CROSS-10 | Who defines the required diagnostic information?               | Service, CORE, System, Safety        |
| CROSS-11 | Who defines the acceptance criteria for the module?            | System, Quality, Test                |
| CROSS-12 | Who approves changes to the module interface?                  | System, CORE, Configuration          |
| CROSS-13 | Which parameters must be configurable versus fixed?            | System, CORE, Manufacturing, Service |
| CROSS-14 | Which failures must be recoverable without power cycling?      | System, Firmware, Service            |
| CROSS-15 | Which failures require a manual intervention?                  | Safety, Service, System              |
| CROSS-16 | What information must survive a module restart?                | System, Service, Firmware            |
| CROSS-17 | What information must survive complete power loss?             | System, Service, Quality             |
| CROSS-18 | Which requirements are safety-critical?                        | Safety, System                       |
| CROSS-19 | Which requirements are performance-critical?                   | System, Process, CORE                |
| CROSS-20 | Which requirements are mandatory for regulatory compliance?    | Compliance, Safety, Quality          |

---

# 13. Interview Output

The answer to each question should **not immediately become a module requirement**.

Each interview should produce an entry such as:

| Field                      | Example                                                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Stakeholder                | CORE Firmware Engineer                                                                                              |
| Question                   | CORE-17                                                                                                             |
| Stakeholder need           | CORE must know whether the measurement is still current                                                             |
| Stakeholder requirement ID | STK-REQ-CORE-004                                                                                                    |
| Requirement statement      | The system shall provide information allowing the CORE to determine whether the latest ozone measurement is current |
| Derived module requirement | REQ-MOD-IF-012                                                                                                      |
| Rationale                  | Prevent use of obsolete sensor data                                                                                 |
| Priority                   | TBD                                                                                                                 |
| Verification method        | Test                                                                                                                |
| Status                     | Proposed                                                                                                            |

This distinction is important because the stakeholder might say:

> "I need to know whether the measurement is current."

That does **not** yet dictate whether the module should implement:

```text
DATA_AGE
```

or:

```text
DATA_VALID
```

or:

```text
TIMESTAMP
```

or some combination of these.

Those are design decisions that come later.

---

# 14. Suggested Priority During Interviews

I would also add a **Priority** field to every answer:

| Priority         | Meaning                              |
| ---------------- | ------------------------------------ |
| **MUST**         | Requirement is mandatory             |
| **SHOULD**       | Requirement is strongly desired      |
| **COULD**        | Desirable if cost/complexity permits |
| **TBD**          | Priority has not yet been agreed     |
| **OUT OF SCOPE** | Explicitly excluded                  |

Don't use this priority to decide the technical implementation yet. It is simply a way of distinguishing **mandatory stakeholder needs from preferences**.

---

# 15. Important interview rule

For each stakeholder, I would explicitly ask one final question:

> **"What have we not asked you that you believe this module must do, must not do, or must guarantee?"**

This question is surprisingly valuable because your predefined questionnaire inevitably contains assumptions.

I'd also ask the inverse:

> **"What functionality might someone reasonably expect from this module that you explicitly do NOT want it to provide?"**

That helps establish the **scope boundary**, which is particularly important for a small module like this. Otherwise requirements tend to creep in later—for example, filtering, calibration, sensor control, safety logic, configuration management, or process control logic that was never intended to belong inside the expansion module.

The completed answers from this matrix are then the input to **Artifact #2 → Stakeholder Requirements**, where each meaningful answer gets a unique `STK-REQ-xxx` ID and is written as a stakeholder-level need before we derive the technical `MOD-REQ-xxx` requirements.










Yes. If the interview is meant to be **project-agnostic**, then we should not ask questions like “What should the ozone module do?” or “What Modbus registers do you need?”. Those belong to a later, project-specific interview.

For a **System Architect / System Engineer**, the objective is to discover the system-level context and constraints that will eventually drive requirements for *whatever subsystem/module is being developed*.

I would structure the interview around **system context → responsibilities → interfaces → behavior → performance → failure handling → safety → lifecycle → verification → constraints**.

## System Architect / System Engineer — Generalized Stakeholder Question Set

### A. System Context and Purpose

**SA-01.** What is the overall purpose of the system?

**SA-02.** What problem is the system intended to solve?

**SA-03.** What are the main functions the overall system must perform?

**SA-04.** What are the main subsystems, modules, or components that make up the system?

**SA-05.** How are the responsibilities divided among those subsystems?

**SA-06.** What is the role of the subsystem/module being developed within the overall system?

**SA-07.** What functions are explicitly within the scope of this subsystem?

**SA-08.** What functions are explicitly outside the scope of this subsystem?

**SA-09.** Are there existing systems, products, architectures, or platforms that this project must integrate with or replace?

**SA-10.** Are there different system variants, configurations, or product versions that the subsystem must support?

---

### B. System-Level Requirements

**SA-11.** What are the most important capabilities that the system must provide?

**SA-12.** Which system-level requirements are mandatory, and which are desirable?

**SA-13.** Are there requirements imposed by customers, users, higher-level systems, or other external stakeholders?

**SA-14.** Are there requirements inherited from an existing product or system?

**SA-15.** Are there requirements that cannot be changed because they are already defined by another system or interface?

**SA-16.** Are there requirements that are particularly critical to the system's operation?

**SA-17.** Are there any system behaviors that are explicitly prohibited?

**SA-18.** Are there assumptions about how the system will be used that the subsystem must rely upon?

**SA-19.** Are there operating conditions under which the system must continue functioning, degrade gracefully, or shut down?

**SA-20.** Which requirements are currently known, and which are still expected to be defined during the project?

---

### C. Functional Allocation

**SA-21.** Which system functions are allocated to this subsystem?

**SA-22.** Why were those functions allocated to this subsystem?

**SA-23.** Which functions are performed by other subsystems?

**SA-24.** Are there functions that are shared between multiple subsystems?

**SA-25.** Are there functions for which responsibility is currently unclear?

**SA-26.** What information does this subsystem need from other parts of the system?

**SA-27.** What information does this subsystem need to provide to other parts of the system?

**SA-28.** Which subsystem is responsible for making decisions based on the information produced by this subsystem?

**SA-29.** Which subsystem is responsible for detecting and handling failures originating from this subsystem?

**SA-30.** Are there any functions that must remain independent from the operation of other subsystems?

---

### D. Interfaces and System Integration

**SA-31.** What other systems, subsystems, devices, or external entities must this subsystem interact with?

**SA-32.** What information must be exchanged across each interface?

**SA-33.** Who is responsible for generating each piece of information?

**SA-34.** Who is responsible for consuming each piece of information?

**SA-35.** Which subsystem controls the communication or interaction?

**SA-36.** Are interfaces already defined, or are they part of this project's scope?

**SA-37.** Are there existing communication protocols, data formats, or interface standards that must be used?

**SA-38.** Are there timing requirements associated with any interface?

**SA-39.** Are there bandwidth, throughput, latency, synchronization, or update-rate constraints?

**SA-40.** What should happen if an interface becomes unavailable?

**SA-41.** What should happen if received information is incomplete, invalid, corrupted, inconsistent, or unexpected?

**SA-42.** Are interfaces expected to remain compatible across different versions of the system?

---

### E. System Behavior and Operating Modes

**SA-43.** What operating modes does the overall system have?

**SA-44.** Which operating modes are relevant to this subsystem?

**SA-45.** What should the subsystem do during system startup?

**SA-46.** What should the subsystem do during normal operation?

**SA-47.** What should the subsystem do during shutdown?

**SA-48.** What should happen when the system transitions between operating modes?

**SA-49.** Are there special modes such as maintenance, commissioning, calibration, diagnostics, service, or firmware update?

**SA-50.** Which functions are available in each operating mode?

**SA-51.** Are there conditions that prevent the system from entering a particular operating mode?

**SA-52.** What events should cause a transition from one operating mode to another?

---

### F. Timing and Performance

**SA-53.** Are there system-level response-time requirements?

**SA-54.** Are there maximum acceptable delays between an event occurring and the system responding to it?

**SA-55.** Are there minimum or maximum update rates for information exchanged within the system?

**SA-56.** Are there synchronization requirements between subsystems?

**SA-57.** Are there startup-time requirements?

**SA-58.** Are there recovery-time requirements following a fault or communication loss?

**SA-59.** Are there throughput, processing, memory, or resource limitations that affect the subsystem?

**SA-60.** Which timing requirements are safety-critical or otherwise particularly important?

---

### G. Faults, Failures, and Abnormal Conditions

**SA-61.** What failures of this subsystem could affect the overall system?

**SA-62.** What failures of other subsystems could affect this subsystem?

**SA-63.** How should the system behave when this subsystem is unavailable?

**SA-64.** Which failures must be detected?

**SA-65.** Which failures must be reported to other parts of the system?

**SA-66.** Which failures require the system to enter a degraded mode?

**SA-67.** Which failures require the system to stop or enter a safe state?

**SA-68.** What information must remain available when a failure occurs?

**SA-69.** How should the system distinguish between valid information, invalid information, missing information, and outdated information?

**SA-70.** What should happen when a previously detected fault disappears?

**SA-71.** Should faults automatically recover, require acknowledgement, or require intervention?

**SA-72.** Are there known single points of failure that the subsystem must avoid introducing?

---

### H. Safety and Risk

**SA-73.** What safety-related functions does the overall system perform?

**SA-74.** Can failure of this subsystem create a hazardous condition?

**SA-75.** Can incorrect information from this subsystem lead another subsystem to perform an unsafe action?

**SA-76.** What happens if this subsystem provides an incorrect but plausible value?

**SA-77.** What happens if this subsystem stops providing information entirely?

**SA-78.** What information must be considered trustworthy before it can be used for safety-related decisions?

**SA-79.** Are there defined safe states or safe reactions associated with subsystem failures?

**SA-80.** Are there safety requirements, safety integrity requirements, or risk controls that apply to this subsystem?

**SA-81.** Are there diagnostic or monitoring functions required to detect dangerous failures?

---

### I. Data and Information

**SA-82.** What information does the subsystem need to acquire?

**SA-83.** What information does the subsystem need to generate?

**SA-84.** What information must be stored or retained?

**SA-85.** How long must information remain available?

**SA-86.** Are data accuracy, resolution, range, or precision requirements defined at system level?

**SA-87.** Are timestamps, sequence numbers, quality indicators, validity indicators, or status information required?

**SA-88.** How should the system distinguish between a value that is valid, unavailable, stale, estimated, substituted, or erroneous?

**SA-89.** Are there requirements regarding the integrity or authenticity of exchanged information?

**SA-90.** Are historical data or event records required?

---

### J. Configuration and Variants

**SA-91.** Which aspects of the subsystem are expected to be configurable?

**SA-92.** Which parameters are fixed by design?

**SA-93.** Who is responsible for configuring the subsystem?

**SA-94.** When is configuration performed?

**SA-95.** Can configuration change during normal operation?

**SA-96.** What should happen if configuration data are missing, invalid, or incompatible?

**SA-97.** Must the subsystem support different hardware, software, sensor, or system variants?

**SA-98.** How should compatibility between subsystem versions and system versions be managed?

---

### K. Startup, Shutdown, Recovery, and Reset

**SA-99.** What should happen when the subsystem is powered on?

**SA-100.** What conditions must be satisfied before the subsystem is considered operational?

**SA-101.** What should the subsystem report before valid information is available?

**SA-102.** What should happen after a reset?

**SA-103.** What should happen after an unexpected power interruption?

**SA-104.** What should happen when communication with another subsystem is lost and later restored?

**SA-105.** What should happen when the subsystem itself temporarily becomes unavailable?

**SA-106.** Are automatic recovery mechanisms required?

**SA-107.** Are there conditions under which automatic recovery must not occur?

---

### L. Diagnostics and Maintenance

**SA-108.** What diagnostic information must the subsystem provide?

**SA-109.** Who will consume the diagnostic information?

**SA-110.** What faults, warnings, states, or events must be distinguishable?

**SA-111.** Are error counters, event counters, operating statistics, or historical fault information required?

**SA-112.** What information is required to determine whether a problem originates in this subsystem or elsewhere?

**SA-113.** What information is required by service personnel during troubleshooting?

**SA-114.** Are diagnostic functions required during commissioning or installation?

**SA-115.** Are diagnostic functions required during normal operation?

**SA-116.** Are there restrictions on what diagnostic functions may do to the system during operation?

---

### M. Physical and Environmental Constraints

**SA-117.** Where will the subsystem be installed?

**SA-118.** What physical constraints are imposed by the system architecture?

**SA-119.** What power sources are available?

**SA-120.** What environmental conditions must the subsystem tolerate?

**SA-121.** Are there restrictions related to temperature, humidity, vibration, contamination, altitude, or other environmental conditions?

**SA-122.** Are there restrictions related to electromagnetic compatibility or electrical noise?

**SA-123.** Are there space, mounting, connector, wiring, or accessibility constraints?

**SA-124.** Are there requirements concerning installation, replacement, or maintenance?

---

### N. Regulatory, Standards, and Compliance

**SA-125.** Which standards apply to the overall system?

**SA-126.** Which standards apply specifically to this subsystem?

**SA-127.** Are there customer-specific standards or specifications that must be followed?

**SA-128.** Are there regulatory or certification requirements?

**SA-129.** Are there requirements concerning cybersecurity, data security, or access control?

**SA-130.** Are there requirements inherited from another certified or previously approved system?

**SA-131.** Are there restrictions on changing existing interfaces because of certification or compliance?

---

### O. Lifecycle and Maintainability

**SA-132.** What is the expected operational lifetime of the system?

**SA-133.** What is the expected lifetime of the subsystem?

**SA-134.** Is the subsystem expected to be replaceable in the field?

**SA-135.** What should happen after replacing the subsystem?

**SA-136.** Is reconfiguration, calibration, commissioning, or verification required after replacement?

**SA-137.** Are firmware or software updates expected during the product lifetime?

**SA-138.** How should compatibility between updated subsystem firmware and the rest of the system be maintained?

**SA-139.** Are spare parts or multiple hardware revisions expected?

**SA-140.** Are there end-of-life or obsolescence constraints?

---

### P. Verification and Acceptance

**SA-141.** How will the system determine that this subsystem satisfies its intended purpose?

**SA-142.** Which subsystem behaviors must be demonstrable during system-level testing?

**SA-143.** Which requirements must be verified under normal operating conditions?

**SA-144.** Which requirements must be verified under abnormal or fault conditions?

**SA-145.** Are there specific acceptance criteria already defined?

**SA-146.** Are there system-level test environments, simulators, or test equipment that the subsystem must support?

**SA-147.** What evidence is required before the subsystem can be accepted?

**SA-148.** Are there requirements that cannot be adequately verified by testing and therefore require analysis, inspection, or demonstration?

---

### Q. Architecture and Design Constraints

**SA-149.** Are there architectural decisions that have already been made and cannot be changed?

**SA-150.** Are there technologies, protocols, components, or implementation approaches that are mandated?

**SA-151.** Are there technologies or implementation approaches that are explicitly prohibited?

**SA-152.** Which design decisions are considered open and may be chosen by the development team?

**SA-153.** Are there interfaces or architectural boundaries that must not be changed?

**SA-154.** Are there dependencies on existing hardware or software?

**SA-155.** Are there resource constraints inherited from the overall architecture?

**SA-156.** Are there requirements concerning modularity, scalability, reuse, or future expansion?

---

### R. Project and Change Management

**SA-157.** What are the major project constraints?

**SA-158.** Are there schedule, cost, resource, technology, or manufacturing constraints that affect the subsystem?

**SA-159.** Which requirements are fixed, and which may be negotiated or changed?

**SA-160.** Who has authority to approve changes to system requirements?

**SA-161.** How are changes to system architecture controlled?

**SA-162.** How should the subsystem handle future changes that are already anticipated?

**SA-163.** Are there planned future versions or extensions that should influence the architecture now?

---

## The most important closing questions

I would **always finish the System Architect interview with these**, because they often reveal requirements that a structured questionnaire misses:

**SA-164.** What are the three most important things this subsystem must do correctly?

**SA-165.** What are the three most dangerous or unacceptable things this subsystem could do incorrectly?

**SA-166.** What failures of this subsystem would be most concerning to you?

**SA-167.** What assumptions are we currently making that you believe we need to verify?

**SA-168.** What requirements do you expect other stakeholders to impose on this subsystem?

**SA-169.** What existing interfaces or constraints could we easily overlook?

**SA-170.** What aspects of the architecture are intentionally left open for the development team to decide?

**SA-171.** What future changes should we design for, even if they are not required today?

**SA-172.** What have we not asked that you believe is important for defining this subsystem?

**SA-173.** What functionality might someone reasonably expect from this subsystem that you explicitly do **not** want it to provide?

---

## One important distinction

For this particular stakeholder, I would **not try to get all the detailed answers in one interview**.

The System Architect should primarily give you the **system-level picture**:

> **Why does the subsystem exist? What is its responsibility? What does it interact with? What constraints does the system impose on it? What happens when things go wrong?**

Then the other stakeholders fill in the details.

For example:

**System Architect**

> “The subsystem shall provide measurement information to the main controller.”

**Sensor Engineer**

> “The sensor communicates using this protocol, at this baud rate, with this frame structure.”

**CORE Engineer**

> “The controller expects the information through this interface, in this format, with these timing requirements.”

**Safety Engineer**

> “The measurement cannot be considered trustworthy under these conditions.”

**Service Engineer**

> “When the sensor is disconnected, the technician needs to be able to distinguish that condition from a module failure.”

Those answers then converge into your **Stakeholder Requirements Specification**, and eventually into the detailed **Module Requirements Specification**.

So, for a reusable company process, I would actually make this questionnaire your **generic System Architect / System Engineer interview template**, with the project-specific questions added later only where necessary.










ok i have a rough idea on how these document will look like. now lets get serious and practical. i want to compile a list of questions for each stakeholder, but i want to do it one stakeholder at a time. i want to start with System Architect / System Engineer. so give me a list of questions for this stakeholder. give about 20-30 in the style of the stakeholder requirement matrix as you suggested before.

---


Absolutely. For the **System Architect / System Engineer**, I would keep the questions focused on the **system-level role of the module**, its boundaries, interfaces, expected behavior, constraints, and interactions with CORE and the ozone sensor.

The goal is **not yet to design the module**. We want to understand what the overall system requires from it.

Below is a practical **Stakeholder Requirement Matrix** section you can use directly.

# Stakeholder Requirement Matrix

## STK-007 / STK-008 — System Architect / System Engineer

**Stakeholder role:** Defines the overall system architecture, functional allocation, interfaces, system-level behavior, and constraints that the ozone sensor expansion module must satisfy.

**Objective of interview:** Determine what the overall system expects from the module, what responsibilities belong to the module versus CORE or other system elements, and what system-level constraints must be respected.

---

| ID         | Question                                                                                                                                                                     | Purpose / Information Needed                                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **SYS-01** | What is the overall purpose of this ozone sensor expansion module within the system?                                                                                         | Understand the module's intended system-level role.                            |
| **SYS-02** | What system function or problem is this module intended to solve?                                                                                                            | Identify the actual system need behind the module.                             |
| **SYS-03** | Which functions are expected to be performed by the module, and which functions must remain the responsibility of CORE?                                                      | Establish functional boundaries between the module and CORE.                   |
| **SYS-04** | Are there any functions that the module must explicitly **not** perform?                                                                                                     | Define scope exclusions and prevent unintended functionality.                  |
| **SYS-05** | How does the module fit into the overall system architecture?                                                                                                                | Identify dependencies and architectural relationships.                         |
| **SYS-06** | Which system components communicate directly with this module?                                                                                                               | Identify all external interfaces and communication partners.                   |
| **SYS-07** | Is the module expected to communicate only with CORE and one ozone sensor, or are other communication partners expected now or in the future?                                | Confirm communication scope and possible extensibility requirements.           |
| **SYS-08** | What information does the system need from the ozone sensor?                                                                                                                 | Identify the required data provided by the sensor.                             |
| **SYS-09** | What does CORE need to know about the ozone measurement in addition to the numerical value itself?                                                                           | Identify required status, validity, freshness, diagnostics, units, etc.        |
| **SYS-10** | How should the system behave when the sensor is disconnected, unavailable, or stops transmitting data?                                                                       | Define system-level behavior during sensor communication failure.              |
| **SYS-11** | How should the system behave when a sensor message is received but the data is invalid or fails integrity checking?                                                          | Define handling of invalid sensor data.                                        |
| **SYS-12** | If communication with the sensor is temporarily lost, should the last valid measurement remain available to CORE? If so, under what conditions?                              | Determine stale-data behavior.                                                 |
| **SYS-13** | How should CORE distinguish between a current valid measurement, a stale measurement, and the absence of a valid measurement?                                                | Define system-level data validity semantics.                                   |
| **SYS-14** | What is the maximum acceptable age of an ozone measurement before the system considers it stale or unusable?                                                                 | Establish the system freshness requirement.                                    |
| **SYS-15** | What measurement update rate does the system require from the ozone sensor/module?                                                                                           | Establish required measurement frequency.                                      |
| **SYS-16** | What is the maximum acceptable delay between a valid sensor measurement becoming available and CORE being able to obtain it?                                                 | Establish end-to-end data latency.                                             |
| **SYS-17** | What should happen during module startup before the first valid ozone measurement has been received?                                                                         | Define startup data validity and system behavior.                              |
| **SYS-18** | What should happen if the module is operating correctly but CORE temporarily stops communicating with it?                                                                    | Define independence of sensor acquisition and CORE communication.              |
| **SYS-19** | What should happen after communication with CORE is restored?                                                                                                                | Define recovery behavior and whether data acquisition continues transparently. |
| **SYS-20** | What should happen after the module loses power and restarts?                                                                                                                | Define power-cycle recovery expectations.                                      |
| **SYS-21** | Are there system-level requirements for automatic recovery from sensor communication failures, or is manual intervention acceptable?                                         | Establish recovery philosophy.                                                 |
| **SYS-22** | What information must be available to the system for diagnosing sensor, module, or communication failures?                                                                   | Identify system diagnostic requirements.                                       |
| **SYS-23** | Does CORE need to distinguish between different failure causes, such as sensor disconnected, invalid sensor data, communication timeout, module fault, or stale measurement? | Determine required fault/status granularity.                                   |
| **SYS-24** | What Modbus functions, addresses, data types, status information, or other interface behavior does CORE expect from the module?                                              | Identify the required CORE-module interface at system level.                   |
| **SYS-25** | Are there existing Modbus conventions or register-mapping rules in the product/system that this module must follow?                                                          | Ensure consistency with the existing system architecture.                      |
| **SYS-26** | Are there existing system requirements for units, resolution, measurement range, scaling, byte order, or representation of ozone concentration?                              | Define measurement representation requirements.                                |
| **SYS-27** | Are there system-level timing requirements for communication with CORE, such as maximum response time or communication timeout?                                              | Identify interface timing constraints.                                         |
| **SYS-28** | Are there system-level safety functions or decisions that depend on the ozone measurement?                                                                                   | Identify safety-related dependencies and consequences of bad data.             |
| **SYS-29** | What should the system do if no valid ozone measurement is available for an extended period?                                                                                 | Define system-level degraded/fault behavior.                                   |
| **SYS-30** | What assumptions are currently being made about the sensor, module, CORE, or communication interfaces that must be confirmed before the design is finalized?                 | Identify hidden assumptions and unresolved architectural issues.               |

---

## Recommended Follow-up Questions

If the discussion is going well, I would add these questions because they often expose requirements that otherwise remain implicit:

| ID         | Question                                                                                                                                                | Purpose / Information Needed                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **SYS-31** | Is this module intended to be a reusable platform component for other sensor types, or is it specifically dedicated to the ZE27-O3 sensor?              | Determine whether reuse/generality is a system requirement.                          |
| **SYS-32** | Is support for more than one ozone sensor expected in a future version of the system?                                                                   | Identify potential architectural constraints without prematurely designing for them. |
| **SYS-33** | Does the system require the module to remain operational if the ozone sensor is unavailable?                                                            | Clarify module/system availability expectations.                                     |
| **SYS-34** | Is the ozone measurement used directly by a control algorithm, displayed to an operator, logged, used for diagnostics, or some combination of these?    | Understand downstream use and consequences of measurement errors/delay.              |
| **SYS-35** | Which system-level requirements or specifications already define the behavior of this module?                                                           | Identify existing sources that should take precedence over assumptions.              |
| **SYS-36** | Are there existing modules in the product family whose architecture, communication behavior, diagnostics, or service concept this module should follow? | Identify architectural/product-family constraints.                                   |
| **SYS-37** | Are there requirements concerning firmware updates, configuration, device identification, or compatibility with different CORE firmware versions?       | Identify lifecycle and compatibility requirements.                                   |
| **SYS-38** | What are the consequences to the overall system if the module provides an incorrect ozone value?                                                        | Understand criticality and required integrity/diagnostic behavior.                   |
| **SYS-39** | What are the consequences if the module reports "valid" data that is actually stale or corrupted?                                                       | Identify the importance of validity/freshness mechanisms.                            |
| **SYS-40** | What requirements have we not discussed that you believe this module must satisfy, must not violate, or must guarantee?                                 | Capture requirements that were not anticipated by the questionnaire.                 |

---

## Important Interview Rule

For each answer, **do not immediately convert the answer into a module requirement**.

For example:

> **SYS-14:** What is the maximum acceptable age of an ozone measurement before it becomes stale?

Stakeholder answer:

> "The system can use the last valid value for up to 5 seconds."

At this stage, record:

* **Raw stakeholder answer:** System can use last valid value for up to 5 s.
* **Interpretation:** Ozone data older than 5 s may no longer be considered current.
* **Requirement candidate:** System shall provide sufficient information to determine whether the ozone measurement is within the permitted age.
* **Open question:** What exactly must happen after 5 s?
* **Affected stakeholders:** CORE Firmware, Ozone Process, Functional Safety.
* **Potential StRS requirement:** To be derived after the stakeholder interview.

The final **Module Requirement** might eventually become something completely different, for example:

> `REQ-MOD-XXX — The module shall set the OZONE_DATA_VALID status to FALSE when no valid sensor measurement has been received for 5 s.`

But that implementation-level requirement belongs **later**, in the Module Requirements Specification.

---

## What You Should Capture During the Interview

For every `SYS-XX` question, I recommend recording at least:

| Field                 | Example                                                        |
| --------------------- | -------------------------------------------------------------- |
| Question ID           | SYS-14                                                         |
| Stakeholder           | System Architect                                               |
| Question              | What is the maximum acceptable age...?                         |
| Stakeholder Answer    | 5 s                                                            |
| Clarification         | Applies during normal operation                                |
| Interpretation        | Data older than 5 s is stale                                   |
| Requirement Candidate | System shall provide freshness indication                      |
| Priority              | MUST                                                           |
| Source Type           | Requirement / Constraint / Interface / Assumption / Open Issue |
| Open Issue            | Exact behavior after 5 s TBD                                   |
| Follow-up Stakeholder | CORE Firmware + Ozone Process                                  |
| Final Disposition     | STK-REQ-009 / TBD                                              |
| Notes                 | Confirm during system-level review                             |

This separation is important because **the interview record preserves what the stakeholder actually said**, while the StRS contains the **clean, reviewed stakeholder requirements** derived from those answers.

I would use **SYS-01 to SYS-30 as the core interview** and keep **SYS-31 to SYS-40 as optional deeper questions**. That gives you a manageable first interview while still covering the architectural issues that are most likely to create problems later.












ok i have a rough idea on how these document will look like. now lets get serious and practical. i want to compile a list of questions for each stakeholder, but i want to do it one stakeholder at a time. i want to start with System Architect / System Engineer. so give me a list of questions for this stakeholder. in specific i what the question to be generalized, in the sense that these questions must fit any type of project, since i don't know the project beforehand and these interviews are meant to discover just that.

---


Absolutely. At this stage, I would **not** ask questions about ozone, RS485, Modbus, sensors, or even the specific module. Those belong later.

For the **System Architect / System Engineer**, the interview should discover the system itself: its purpose, boundaries, actors, interfaces, constraints, behaviors, risks, and the role of the product being developed.

The questions should therefore be reusable across projects — industrial equipment, embedded products, automation systems, medical devices, consumer products, etc.

## System Architect / System Engineer — Stakeholder Interview Questions

I would structure the interview into **12 areas**. The order is intentional: start broad, then progressively go deeper.

### 1. System Purpose and Objectives

| ID     | Question                                                                        |
| ------ | ------------------------------------------------------------------------------- |
| SYS-01 | What is the overall purpose of the system?                                      |
| SYS-02 | What problem is the system intended to solve?                                   |
| SYS-03 | What are the main objectives the system must achieve?                           |
| SYS-04 | What are the most important functions the system must provide?                  |
| SYS-05 | What outcomes are expected from the system?                                     |
| SYS-06 | How will we know that the system is successful?                                 |
| SYS-07 | Are there any system objectives that are considered mandatory versus desirable? |
| SYS-08 | What would constitute an unacceptable system outcome or failure?                |

**Why ask this:** Before defining what a component must do, you need to understand **why the system exists**.

---

### 2. System Context

| ID     | Question                                                                                           |
| ------ | -------------------------------------------------------------------------------------------------- |
| SYS-09 | Where and in what context will the system operate?                                                 |
| SYS-10 | What other systems, products, machines, or infrastructure interact with this system?               |
| SYS-11 | Who or what interacts with the system during normal operation?                                     |
| SYS-12 | Who or what interacts with the system during installation, commissioning, maintenance, or service? |
| SYS-13 | What external systems does the system depend on?                                                   |
| SYS-14 | What external systems depend on this system?                                                       |
| SYS-15 | Are there system boundaries that must be clearly defined?                                          |
| SYS-16 | What is explicitly outside the responsibility of this system?                                      |

This section is particularly important because many requirements problems are actually **boundary problems**.

For example:

> "The system shall detect an unsafe condition."

Immediately you need to know:

* Does this system detect it?
* Does another system detect it?
* Does this system only report it?
* Does another system act on it?
* Is the system responsible for the final safety response?

---

### 3. System Functions and Behavior

| ID     | Question                                                                |
| ------ | ----------------------------------------------------------------------- |
| SYS-17 | What are the major functions the system must perform?                   |
| SYS-18 | What are the major operating modes of the system?                       |
| SYS-19 | How does the system transition between operating modes?                 |
| SYS-20 | What events can cause a change of system state or mode?                 |
| SYS-21 | What should the system do during normal operation?                      |
| SYS-22 | What should the system do during abnormal operation?                    |
| SYS-23 | What should the system do when required inputs are unavailable?         |
| SYS-24 | What should the system do when an internal function fails?              |
| SYS-25 | What should happen when the system starts up?                           |
| SYS-26 | What should happen when the system shuts down?                          |
| SYS-27 | What should happen after a restart or power interruption?               |
| SYS-28 | Are there any functions that must operate continuously or periodically? |

Here you're trying to discover the **behavioral model of the system**, not yet how it will be implemented.

---

### 4. System Interfaces

| ID     | Question                                                                                      |
| ------ | --------------------------------------------------------------------------------------------- |
| SYS-29 | What are the system's external interfaces?                                                    |
| SYS-30 | What information enters the system through each interface?                                    |
| SYS-31 | What information does the system provide through each interface?                              |
| SYS-32 | Which interfaces are mandatory for system operation?                                          |
| SYS-33 | Which interfaces are optional?                                                                |
| SYS-34 | Are there timing requirements associated with any interfaces?                                 |
| SYS-35 | Are there data format, protocol, or communication requirements?                               |
| SYS-36 | Are there physical, electrical, mechanical, or environmental interface constraints?           |
| SYS-37 | What happens if an external interface becomes unavailable?                                    |
| SYS-38 | What happens if an external system provides invalid or unexpected information?                |
| SYS-39 | Who owns the definition of each external interface?                                           |
| SYS-40 | Are any interfaces governed by existing standards, specifications, or legacy implementations? |

Notice that these questions don't assume **what type of interface** exists.

The answer could be:

* Ethernet
* CAN
* RS485
* analog
* digital I/O
* mechanical
* hydraulic
* pneumatic
* wireless
* software API
* human interface
* etc.

---

### 5. Data and Information

| ID     | Question                                                                                  |
| ------ | ----------------------------------------------------------------------------------------- |
| SYS-41 | What information does the system need in order to perform its functions?                  |
| SYS-42 | What information does the system need to produce for other systems or users?              |
| SYS-43 | Which information is considered critical?                                                 |
| SYS-44 | What are the required accuracy, resolution, or quality characteristics of important data? |
| SYS-45 | How current must important information be?                                                |
| SYS-46 | How should missing, invalid, inconsistent, or outdated information be handled?            |
| SYS-47 | Does the system need to retain information over time?                                     |
| SYS-48 | If information is retained, how long must it be retained?                                 |
| SYS-49 | Is historical information required for diagnostics, traceability, or operation?           |
| SYS-50 | Are there rules regarding ownership, access, or modification of system data?              |

This section is very useful later when defining requirements for individual modules.

---

### 6. Performance and Timing

| ID     | Question                                                                                |
| ------ | --------------------------------------------------------------------------------------- |
| SYS-51 | What are the most important system performance requirements?                            |
| SYS-52 | Are there response-time requirements?                                                   |
| SYS-53 | Are there throughput or capacity requirements?                                          |
| SYS-54 | Are there sampling, update, or execution-rate requirements?                             |
| SYS-55 | Are there latency requirements between an event and the corresponding system response?  |
| SYS-56 | Are there startup-time requirements?                                                    |
| SYS-57 | Are there shutdown-time requirements?                                                   |
| SYS-58 | Are there synchronization requirements between different parts of the system?           |
| SYS-59 | Are there performance requirements that apply only under specific operating conditions? |
| SYS-60 | What are the consequences if a performance requirement is not achieved?                 |

---

### 7. Operating Environment and Constraints

| ID     | Question                                                                                                        |
| ------ | --------------------------------------------------------------------------------------------------------------- |
| SYS-61 | In what environmental conditions must the system operate?                                                       |
| SYS-62 | What are the expected operating temperature, humidity, pressure, vibration, shock, or contamination conditions? |
| SYS-63 | Are there restrictions on installation location or orientation?                                                 |
| SYS-64 | Are there space or weight constraints?                                                                          |
| SYS-65 | Are there power-supply constraints?                                                                             |
| SYS-66 | Are there electromagnetic or electrical environment constraints?                                                |
| SYS-67 | Are there restrictions related to hazardous or classified environments?                                         |
| SYS-68 | Are there installation or infrastructure constraints?                                                           |
| SYS-69 | Are there constraints imposed by existing equipment or legacy systems?                                          |
| SYS-70 | Which constraints are fixed and which are still negotiable?                                                     |

The last question is especially valuable.

A requirement like:

> "The product shall operate from 24 VDC."

could actually be:

* a genuine system requirement,
* a customer constraint,
* a legacy constraint,
* or simply an engineer's current design assumption.

You want to discover which one it is.

---

### 8. Safety, Risk and Failure Behavior

| ID     | Question                                                                                           |
| ------ | -------------------------------------------------------------------------------------------------- |
| SYS-71 | What could go wrong at system level?                                                               |
| SYS-72 | What are the most significant hazards or risks associated with the system?                         |
| SYS-73 | Which failures could create unsafe conditions?                                                     |
| SYS-74 | What must the system do when a critical fault occurs?                                              |
| SYS-75 | Are there defined safe states or degraded states?                                                  |
| SYS-76 | Which functions are safety-critical?                                                               |
| SYS-77 | What must happen if a required subsystem or external dependency fails?                             |
| SYS-78 | Should the system continue operating after certain failures?                                       |
| SYS-79 | Which failures must cause the system to stop or enter a safe state?                                |
| SYS-80 | Are there existing safety analyses, risk assessments, FMEA, hazard analyses, or similar documents? |
| SYS-81 | Are there regulatory or functional-safety requirements that constrain the architecture?            |

Don't try to solve the safety architecture in this interview. The goal is to discover **where safety requirements exist and who owns them**.

---

### 9. Reliability, Availability and Recovery

| ID     | Question                                                               |
| ------ | ---------------------------------------------------------------------- |
| SYS-82 | What level of system availability is expected?                         |
| SYS-83 | Are there requirements concerning reliability or expected lifetime?    |
| SYS-84 | Which failures must the system recover from automatically?             |
| SYS-85 | Which failures require operator intervention?                          |
| SYS-86 | Which failures require maintenance intervention?                       |
| SYS-87 | How quickly should the system recover from recoverable failures?       |
| SYS-88 | What should happen after an unexpected power loss?                     |
| SYS-89 | What should happen after a software or subsystem restart?              |
| SYS-90 | Is degraded operation required when part of the system is unavailable? |
| SYS-91 | Are redundancy, fallback, backup, or failover mechanisms required?     |

---

### 10. Installation, Maintenance and Lifecycle

| ID      | Question                                                                        |
| ------- | ------------------------------------------------------------------------------- |
| SYS-92  | How is the system expected to be installed?                                     |
| SYS-93  | What configuration is required during installation?                             |
| SYS-94  | What commissioning activities are required?                                     |
| SYS-95  | What maintenance activities are expected during the system lifetime?            |
| SYS-96  | Which components or subsystems are expected to be replaceable?                  |
| SYS-97  | Should replacement require recalibration, reconfiguration, or reprogramming?    |
| SYS-98  | What diagnostic information must be available to maintenance personnel?         |
| SYS-99  | What is the expected service life of the system?                                |
| SYS-100 | Are firmware/software updates required during the system lifetime?              |
| SYS-101 | Are there requirements concerning backward compatibility or field upgrades?     |
| SYS-102 | What happens to the system when a replaceable component is removed or replaced? |

---

### 11. Standards, Regulations and External Constraints

| ID      | Question                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------- |
| SYS-103 | Which standards, regulations, directives, or customer specifications apply to the system?         |
| SYS-104 | Are there mandatory certification or compliance requirements?                                     |
| SYS-105 | Are there industry-specific requirements that must be considered?                                 |
| SYS-106 | Are there internal company standards that the system must follow?                                 |
| SYS-107 | Are there existing architectural or interface standards that must be followed?                    |
| SYS-108 | Are there customer-specific requirements that override or supplement general requirements?        |
| SYS-109 | Who is responsible for determining and maintaining the applicable compliance requirements?        |
| SYS-110 | Are there existing compliance, certification, or qualification documents we should use as inputs? |

---

### 12. Architecture, Allocation and Project Boundaries

This is perhaps the most important section specifically for the **System Architect**.

| ID      | Question                                                                                              |
| ------- | ----------------------------------------------------------------------------------------------------- |
| SYS-111 | What are the major subsystems or building blocks of the system?                                       |
| SYS-112 | What responsibilities are assigned to each subsystem?                                                 |
| SYS-113 | Which functions are intentionally allocated outside the product being developed?                      |
| SYS-114 | How are responsibilities divided between hardware, firmware, software, and external systems?          |
| SYS-115 | Which interfaces between subsystems are already defined?                                              |
| SYS-116 | Which architectural decisions have already been made?                                                 |
| SYS-117 | Which architectural decisions are still open?                                                         |
| SYS-118 | Which parts of the architecture are fixed constraints and which are alternatives under consideration? |
| SYS-119 | Are there existing products, modules, platforms, or architectures that this project must reuse?       |
| SYS-120 | Are there legacy interfaces or behaviors that must be preserved?                                      |
| SYS-121 | Are there known architectural weaknesses or technical debt that this project is expected to address?  |
| SYS-122 | What assumptions is the current architecture based on?                                                |
| SYS-123 | Which assumptions have been verified, and which remain unverified?                                    |
| SYS-124 | What architectural decisions could have the greatest impact on the project if they change?            |
| SYS-125 | What system-level trade-offs are currently being considered?                                          |

---

# 13. Requirements, Verification and Acceptance

I would definitely include this section. System engineers sometimes define what the system should do but don't explicitly define **how we will know that it does it**.

| ID      | Question                                                                                        |
| ------- | ----------------------------------------------------------------------------------------------- |
| SYS-126 | How will the system requirements ultimately be verified?                                        |
| SYS-127 | Which requirements must be demonstrated on the complete system?                                 |
| SYS-128 | Which requirements can be verified at subsystem or component level?                             |
| SYS-129 | Are there requirements that require testing under real operating conditions?                    |
| SYS-130 | Are there requirements that require analysis, inspection, or demonstration rather than testing? |
| SYS-131 | What are the system-level acceptance criteria?                                                  |
| SYS-132 | Who determines whether the system meets its requirements?                                       |
| SYS-133 | What evidence is required to demonstrate compliance?                                            |
| SYS-134 | Are there existing system-level test procedures or acceptance procedures?                       |
| SYS-135 | What happens when a requirement cannot be objectively verified?                                 |

---

# 14. Assumptions, Open Issues and Unknowns

This section is extremely useful at the **beginning of an unknown project**.

| ID      | Question                                                                           |
| ------- | ---------------------------------------------------------------------------------- |
| SYS-136 | What assumptions are currently being made about the system?                        |
| SYS-137 | Which assumptions have not yet been validated?                                     |
| SYS-138 | What information do we still need before the system requirements can be finalized? |
| SYS-139 | Which requirements are currently uncertain or likely to change?                    |
| SYS-140 | Are there conflicting requirements from different stakeholders?                    |
| SYS-141 | Are there any known technical uncertainties?                                       |
| SYS-142 | Are there any known customer or business uncertainties?                            |
| SYS-143 | Are there any dependencies on decisions outside this project?                      |
| SYS-144 | What decisions must be made before detailed subsystem requirements can be defined? |
| SYS-145 | What are the biggest unknowns or risks from a system-engineering perspective?      |

---

# 15. Final "Discovery" Questions

I would always finish the interview with these. They often uncover things that a structured questionnaire misses.

| ID      | Question                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------- |
| SYS-146 | What important requirement have we not discussed?                                                       |
| SYS-147 | What important system behavior have we not discussed?                                                   |
| SYS-148 | What could someone misunderstand about the system if they only read the current requirements?           |
| SYS-149 | What requirement is most likely to be overlooked during development?                                    |
| SYS-150 | What requirement is most likely to cause problems later if it is not defined now?                       |
| SYS-151 | Are there any requirements that you consider obvious but that are not currently documented?             |
| SYS-152 | Are there any things the system must explicitly **not** do?                                             |
| SYS-153 | Are there any behaviors that would be technically possible but unacceptable?                            |
| SYS-154 | Are there any existing documents, designs, specifications, test reports, or standards we should review? |
| SYS-155 | Who else should we interview to understand the system completely?                                       |

---

# The important part: don't turn this into a 155-question interview

I would **keep the full question bank**, but I would not sit down with the System Architect and mechanically ask all 155 questions.

Instead, treat it as a **question library**.

For an actual project, you could use three levels:

### Core questions — always ask

I'd mark approximately **25–35 questions** as `CORE`.

These establish the minimum system understanding:

* SYS-01 — purpose
* SYS-02 — problem
* SYS-03 — objectives
* SYS-09 — operating context
* SYS-10 — interacting systems
* SYS-13 — dependencies
* SYS-15 — system boundaries
* SYS-16 — out of scope
* SYS-17 — major functions
* SYS-18 — operating modes
* SYS-20 — state transitions
* SYS-21 — normal behavior
* SYS-22 — abnormal behavior
* SYS-25 — startup
* SYS-27 — restart/recovery
* SYS-29 — external interfaces
* SYS-37 — interface failure behavior
* SYS-41 — required information
* SYS-46 — invalid/missing data
* SYS-51 — performance
* SYS-61 — environment
* SYS-71 — system risks
* SYS-74 — critical fault behavior
* SYS-75 — safe/degraded states
* SYS-84 — automatic recovery
* SYS-92 — installation
* SYS-95 — maintenance
* SYS-103 — applicable standards
* SYS-111 — architecture/subsystems
* SYS-112 — responsibility allocation
* SYS-116 — existing decisions
* SYS-117 — open architectural decisions
* SYS-126 — verification
* SYS-136 — assumptions
* SYS-138 — missing information
* SYS-146 — missing requirements

Then the remaining questions become **conditional questions**.

For example:

> "Does the system retain information?"

If **yes**, ask SYS-47 → SYS-50.

If **no**, skip that branch.

This makes the questionnaire reusable across very different projects.

---

# I would also add metadata to every question

Since you're building a formal stakeholder requirements process, I would not store the questions as just a numbered list.

Your **Stakeholder Requirement Matrix** could have:

| Field                 | Example                                    |
| --------------------- | ------------------------------------------ |
| Question ID           | SYS-029                                    |
| Stakeholder           | System Architect / System Engineer         |
| Category              | Interface                                  |
| Question              | What are the system's external interfaces? |
| Mandatory             | Yes                                        |
| Applicability         | All projects                               |
| Answer                | —                                          |
| Clarification         | —                                          |
| Follow-up Required    | —                                          |
| Answer Type           | Open                                       |
| Resulting Artifact    | Elicitation Record                         |
| Requirement Candidate | —                                          |
| Requirement ID        | —                                          |
| Status                | Open                                       |

And I'd add one particularly useful field:

### `Question Intent`

For example:

> **SYS-029 — Question Intent:** Identify all external interfaces so that interface-related stakeholder requirements can be derived.

This prevents the questionnaire itself from becoming just a checklist. Every question has a **reason for existing**.

---

## One more important distinction

For this stakeholder, I would deliberately avoid questions such as:

> "Should the module use RS485?"

or:

> "Should the firmware use a state machine?"

or:

> "Should we use Modbus RTU?"

Those are already **solution/design questions**.

Instead:

> "What communication interfaces must the product provide?"

and:

> "What information must be exchanged with each external system?"

The System Architect may answer:

> "The module must communicate with the main controller using the existing industrial communication bus."

That is useful information.

**Only later** should the relevant technical stakeholder/documentation tell you that the bus is, for example, Modbus RTU over RS485.

That separation is what will keep your requirements process reusable across projects.

### Recommended next step

For your master questionnaire, I'd make this a **System Architect / System Engineer Question Bank v1.0** with roughly **150 questions**, but classify every question as:

* **CORE** — ask on virtually every project
* **CONDITIONAL** — ask when applicable
* **DEEP-DIVE** — ask only when the discussion indicates it is needed

Then we can do the **same exercise for the next stakeholder**, without contaminating the questions with assumptions from the ozone project.











ok, now let's move on to the next stakeholder that is: CORE Firmware Engineer. so give me a list of questions for this stakeholder. give me a complete and comprehensive list of questions. also, mark the 20-30 questions that are the most important, and then give me the 5 that i must absolutely not miss as they are mission-critical.




Yes. For the **CORE Firmware Engineer**, the objective is slightly different from the System Architect interview.

The System Architect tells you **what the system needs to accomplish**.
The CORE Firmware Engineer tells you **what the module must provide to the existing CORE firmware, how CORE expects to interact with it, and what assumptions/constraints exist on the CORE side**.

I would therefore make this question bank broad enough to work for essentially any embedded/industrial project, while keeping the questions independent of any specific protocol, sensor, MCU, or architecture.

---

# CORE Firmware Engineer — Stakeholder Question Bank

**Legend**

* 🔴 **CRITICAL** — must absolutely not be missed
* ⭐ **CORE** — among the 20–30 most important questions
* ○ **DEEP-DIVE** — ask when applicable

I recommend keeping the full question bank in your master questionnaire. During an actual interview, use the ⭐ questions as the minimum structured interview and use the others to investigate the relevant branches.

---

# 1. CORE Firmware Context

The first objective is to understand **what the CORE actually is** and what role this module plays in relation to it.

| ID       | Priority | Question                                                                                |
| -------- | -------- | --------------------------------------------------------------------------------------- |
| CORE-001 | ⭐        | What is the role and responsibility of the CORE firmware within the overall system?     |
| CORE-002 | ⭐        | What functionality does the CORE currently provide that is relevant to this new module? |
| CORE-003 | ⭐        | What functionality is expected to be provided by the new module rather than by CORE?    |
| CORE-004 | ⭐        | Where is the boundary of responsibility between CORE and the new module?                |
| CORE-005 | ⭐        | What information does CORE need from the module?                                        |
| CORE-006 | ⭐        | What information does the module need to receive from CORE?                             |
| CORE-007 | ○        | Is CORE an existing product/firmware or is it being developed in parallel?              |
| CORE-008 | ○        | Which version or configuration of CORE is relevant to this project?                     |
| CORE-009 | ○        | Are there legacy behaviors that the new module must support?                            |
| CORE-010 | ○        | Are there existing modules that CORE already communicates with in a similar way?        |

### Why this matters

A surprisingly common failure is defining a perfectly reasonable module interface that doesn't actually fit the existing CORE architecture.

The first thing you need to establish is:

> **"What does CORE expect this module to be?"**

---

# 2. CORE–Module Functional Interaction

Now establish what the actual interaction is supposed to accomplish.

| ID       | Priority | Question                                                                     |
| -------- | -------- | ---------------------------------------------------------------------------- |
| CORE-011 | ⭐        | What functions does CORE expect the module to provide?                       |
| CORE-012 | ⭐        | How does CORE know that the module is present and available?                 |
| CORE-013 | ⭐        | How does CORE obtain data from the module?                                   |
| CORE-014 | ⭐        | Does CORE actively request information, or is information pushed to CORE?    |
| CORE-015 | ⭐        | What events cause CORE to communicate with the module?                       |
| CORE-016 | ○        | Does CORE communicate with the module periodically, asynchronously, or both? |
| CORE-017 | ○        | Does CORE need to configure the module?                                      |
| CORE-018 | ○        | Does CORE need to command the module?                                        |
| CORE-019 | ○        | Does CORE need to acknowledge information received from the module?          |
| CORE-020 | ○        | Does CORE need to send commands to change the module's operating mode?       |
| CORE-021 | ○        | What should happen if CORE does not communicate with the module?             |
| CORE-022 | ○        | What should happen if the module does not respond to CORE?                   |
| CORE-023 | ○        | What should happen if communication is interrupted temporarily?              |
| CORE-024 | ○        | What should happen when communication is restored?                           |

---

# 3. Interface Definition

This is one of the most important sections.

Don't assume the interface is serial, Ethernet, CAN, Modbus, etc.

| ID       | Priority | Question                                                              |
| -------- | -------- | --------------------------------------------------------------------- |
| CORE-025 | 🔴       | What communication interface does CORE expect to use with the module? |
| CORE-026 | ⭐        | Who is responsible for initiating communication?                      |
| CORE-027 | ⭐        | What communication protocol or interface standard must be used?       |
| CORE-028 | ⭐        | What addressing mechanism is used?                                    |
| CORE-029 | ⭐        | How is the module uniquely identified?                                |
| CORE-030 | ⭐        | What messages/requests can CORE send to the module?                   |
| CORE-031 | ⭐        | What messages/responses can the module send to CORE?                  |
| CORE-032 | ⭐        | What data must be exchanged for each message/request?                 |
| CORE-033 | ⭐        | What data format must be used?                                        |
| CORE-034 | ○        | What byte ordering/endianness is expected?                            |
| CORE-035 | ○        | What encoding is used for numerical values?                           |
| CORE-036 | ○        | Are signed and unsigned values used?                                  |
| CORE-037 | ○        | How are floating-point values represented, if applicable?             |
| CORE-038 | ○        | Are scaling factors used?                                             |
| CORE-039 | ○        | Are offsets used?                                                     |
| CORE-040 | ○        | What units are expected for each value?                               |
| CORE-041 | ○        | What resolution is required?                                          |
| CORE-042 | ○        | What ranges are valid?                                                |
| CORE-043 | ○        | Are reserved values or special codes defined?                         |

---

# 4. Data Semantics

This is particularly important because **a numeric value by itself often isn't enough**.

For example:

> `123`

Could mean:

* valid measurement = 123
* stale measurement = 123
* invalid measurement = 123
* sensor disconnected
* last known value
* default value
* error code

The CORE engineer needs to define what those situations mean.

| ID       | Priority | Question                                                                      |
| -------- | -------- | ----------------------------------------------------------------------------- |
| CORE-044 | ⭐        | How does CORE determine whether received data is valid?                       |
| CORE-045 | 🔴       | How does CORE distinguish a valid value from an invalid or unavailable value? |
| CORE-046 | ⭐        | Does CORE need status information in addition to the numerical value?         |
| CORE-047 | ⭐        | Does CORE need to know how old the received data is?                          |
| CORE-048 | ⭐        | How should stale data be represented?                                         |
| CORE-049 | ⭐        | How should unavailable data be represented?                                   |
| CORE-050 | ⭐        | How should invalid data be represented?                                       |
| CORE-051 | ○        | Are there defined error codes or status codes already used by CORE?           |
| CORE-052 | ○        | Does CORE expect quality flags or validity flags?                             |
| CORE-053 | ○        | Does CORE need timestamps?                                                    |
| CORE-054 | ○        | Does CORE need sequence numbers or counters?                                  |
| CORE-055 | ○        | Does CORE need diagnostic counters?                                           |
| CORE-056 | ○        | Are there values that must never be interpreted as valid measurements?        |

---

# 5. Timing and Performance

The module may technically provide the correct data but still fail the system because it provides it too slowly.

| ID       | Priority | Question                                                                                                            |
| -------- | -------- | ------------------------------------------------------------------------------------------------------------------- |
| CORE-057 | ⭐        | How frequently does CORE need the module data?                                                                      |
| CORE-058 | ⭐        | What is the maximum acceptable latency for obtaining new data?                                                      |
| CORE-059 | ⭐        | What is the maximum acceptable communication response time?                                                         |
| CORE-060 | ⭐        | Are there timing constraints between a physical event and the corresponding information becoming available to CORE? |
| CORE-061 | ○        | What communication timeout does CORE use?                                                                           |
| CORE-062 | ○        | How many communication retries does CORE perform?                                                                   |
| CORE-063 | ○        | What retry interval does CORE use?                                                                                  |
| CORE-064 | ○        | How long can CORE tolerate missing responses?                                                                       |
| CORE-065 | ○        | Are there periodic communication deadlines?                                                                         |
| CORE-066 | ○        | Are there synchronization requirements?                                                                             |
| CORE-067 | ○        | Is deterministic timing required?                                                                                   |
| CORE-068 | ○        | What happens if the module responds later than expected?                                                            |

---

# 6. Communication Failure Behavior

This is another area where hidden assumptions frequently exist.

| ID       | Priority | Question                                                                      |
| -------- | -------- | ----------------------------------------------------------------------------- |
| CORE-069 | ⭐        | How does CORE detect that communication with the module has failed?           |
| CORE-070 | ⭐        | What should CORE do when communication fails?                                 |
| CORE-071 | ⭐        | What should CORE do after a single communication error?                       |
| CORE-072 | ○        | What should CORE do after repeated communication errors?                      |
| CORE-073 | ⭐        | How many consecutive failures cause CORE to consider the module unavailable?  |
| CORE-074 | ○        | Does CORE automatically retry communication?                                  |
| CORE-075 | ○        | How should temporary communication loss differ from permanent module failure? |
| CORE-076 | ⭐        | How does CORE detect that communication has recovered?                        |
| CORE-077 | ○        | What should happen to previously received data after communication is lost?   |
| CORE-078 | ○        | Should CORE continue using the last known value?                              |
| CORE-079 | ○        | If CORE continues using the last known value, for how long?                   |
| CORE-080 | ○        | When should CORE declare the data invalid or unavailable?                     |

---

# 7. Module Availability and Health

The module itself may need to communicate more than just process data.

| ID       | Priority | Question                                                                                 |
| -------- | -------- | ---------------------------------------------------------------------------------------- |
| CORE-081 | ⭐        | Does CORE need to know whether the module is operational?                                |
| CORE-082 | ⭐        | Does CORE need to distinguish module communication failure from module internal failure? |
| CORE-083 | ⭐        | Does CORE need a module health/status indication?                                        |
| CORE-084 | ○        | Does CORE need the module firmware version?                                              |
| CORE-085 | ○        | Does CORE need the module hardware revision?                                             |
| CORE-086 | ○        | Does CORE need the module serial number or unique identifier?                            |
| CORE-087 | ○        | Does CORE need to know whether the module has completed initialization?                  |
| CORE-088 | ○        | Does CORE need to know whether the module is operating in a degraded mode?               |
| CORE-089 | ○        | Does CORE need module diagnostic information?                                            |
| CORE-090 | ○        | Does CORE need access to module fault codes?                                             |

---

# 8. Startup and Initialization

Startup behavior is often overlooked until integration testing.

| ID       | Priority | Question                                                                         |
| -------- | -------- | -------------------------------------------------------------------------------- |
| CORE-091 | ⭐        | What does CORE expect the module to do immediately after power-up?               |
| CORE-092 | ⭐        | When should CORE consider the module ready for communication?                    |
| CORE-093 | ⭐        | What should CORE receive if the module has not yet completed initialization?     |
| CORE-094 | ⭐        | What should happen if the module has not yet acquired valid data?                |
| CORE-095 | ○        | Does CORE perform an initialization or discovery sequence?                       |
| CORE-096 | ○        | Is there a defined startup handshake?                                            |
| CORE-097 | ○        | Does CORE expect the module to report its configuration during startup?          |
| CORE-098 | ○        | Are there startup timing limits?                                                 |
| CORE-099 | ○        | What should happen if the module does not become ready within the expected time? |
| CORE-100 | ○        | Does CORE need to distinguish startup state from fault state?                    |

---

# 9. Reset, Restart and Recovery

| ID       | Priority | Question                                                                     |
| -------- | -------- | ---------------------------------------------------------------------------- |
| CORE-101 | ⭐        | What should CORE expect after the module is reset?                           |
| CORE-102 | ⭐        | How should CORE detect that the module has restarted?                        |
| CORE-103 | ⭐        | Does CORE need to reinitialize or reconfigure the module after restart?      |
| CORE-104 | ⭐        | What should happen to previously received data after a module restart?       |
| CORE-105 | ○        | Should CORE automatically recover communication after a module restart?      |
| CORE-106 | ○        | How should CORE behave after a power interruption?                           |
| CORE-107 | ○        | Does CORE need to distinguish a module restart from a communication failure? |
| CORE-108 | ○        | Are there watchdog-related behaviors that CORE must understand?              |

---

# 10. Configuration

Determine whether CORE is simply a consumer or also a configuration authority.

| ID       | Priority | Question                                                                               |
| -------- | -------- | -------------------------------------------------------------------------------------- |
| CORE-109 | ⭐        | Which module parameters must CORE be able to configure?                                |
| CORE-110 | ⭐        | Which parameters are fixed during manufacturing and which can be changed in the field? |
| CORE-111 | ○        | Does CORE need to read the module configuration?                                       |
| CORE-112 | ○        | Does CORE need to write the module configuration?                                      |
| CORE-113 | ○        | Who is the authoritative owner of each configuration parameter?                        |
| CORE-114 | ○        | When does a configuration change take effect?                                          |
| CORE-115 | ○        | Must configuration survive a module restart?                                           |
| CORE-116 | ○        | Must configuration survive a firmware update?                                          |
| CORE-117 | ○        | How should invalid configuration values be handled?                                    |
| CORE-118 | ○        | Does CORE need confirmation that a configuration change was successfully applied?      |

---

# 11. Faults, Alarms and Diagnostics

| ID       | Priority | Question                                                                          |
| -------- | -------- | --------------------------------------------------------------------------------- |
| CORE-119 | ⭐        | Which module faults must be visible to CORE?                                      |
| CORE-120 | ⭐        | Which module faults should generate a system-level alarm?                         |
| CORE-121 | ⭐        | How should CORE distinguish warnings from faults?                                 |
| CORE-122 | ⭐        | Does CORE need individual fault types or only a general fault indication?         |
| CORE-123 | ○        | Does CORE need access to fault history?                                           |
| CORE-124 | ○        | Does CORE need access to communication error counters?                            |
| CORE-125 | ○        | Does CORE need sensor or subsystem diagnostic information?                        |
| CORE-126 | ○        | Which faults should automatically clear when the underlying condition disappears? |
| CORE-127 | ○        | Which faults require explicit acknowledgement?                                    |
| CORE-128 | ○        | Which faults require a reset?                                                     |
| CORE-129 | ○        | Should diagnostic information be available during normal operation?               |
| CORE-130 | ○        | Are there existing CORE diagnostic conventions that the module must follow?       |

---

# 12. Error Handling and Invalid Requests

Especially important if CORE communicates with the module using a defined protocol.

| ID       | Priority | Question                                                            |
| -------- | -------- | ------------------------------------------------------------------- |
| CORE-131 | ⭐        | How should CORE handle an invalid response from the module?         |
| CORE-132 | ⭐        | How should CORE handle malformed or incomplete data?                |
| CORE-133 | ⭐        | How should CORE handle unexpected values?                           |
| CORE-134 | ○        | How should CORE handle an unsupported command or function?          |
| CORE-135 | ○        | How should CORE handle an invalid parameter?                        |
| CORE-136 | ○        | How should CORE handle a communication integrity error?             |
| CORE-137 | ○        | Are protocol error responses standardized across the system?        |
| CORE-138 | ○        | Should CORE retry after receiving an error response?                |
| CORE-139 | ○        | Should different error types result in different recovery behavior? |

---

# 13. Firmware Architecture and Integration

These questions are specifically useful when CORE already exists.

| ID       | Priority | Question                                                                                    |
| -------- | -------- | ------------------------------------------------------------------------------------------- |
| CORE-140 | ⭐        | Where in the CORE firmware architecture should support for the new module be implemented?   |
| CORE-141 | ⭐        | Is there an existing software abstraction for this type of module/interface?                |
| CORE-142 | ⭐        | Should the module be represented through an existing software interface or a new one?       |
| CORE-143 | ○        | What existing drivers, communication stacks, or middleware are relevant?                    |
| CORE-144 | ○        | Are there existing reusable communication libraries?                                        |
| CORE-145 | ○        | Are there coding or architectural constraints that the module interface must respect?       |
| CORE-146 | ○        | Are there limitations in CPU time, RAM, flash, communication bandwidth, or task scheduling? |
| CORE-147 | ○        | Does the new functionality require changes to existing CORE tasks or state machines?        |
| CORE-148 | ○        | Does the new functionality affect existing real-time behavior?                              |
| CORE-149 | ○        | Are there existing APIs that the new module must integrate with?                            |
| CORE-150 | ○        | What existing functionality could be affected by introducing this module?                   |

---

# 14. Firmware Scheduling and Concurrency

Useful whenever CORE is a real-time or multitasking system.

| ID       | Priority | Question                                                                                   |
| -------- | -------- | ------------------------------------------------------------------------------------------ |
| CORE-151 | ○        | In which CORE task, thread, or execution context will communication with the module occur? |
| CORE-152 | ○        | What execution frequency is available for communication with the module?                   |
| CORE-153 | ○        | Are there higher-priority activities that can delay communication?                         |
| CORE-154 | ○        | Are there concurrency constraints when accessing the received module data?                 |
| CORE-155 | ○        | Can multiple software components access the module data?                                   |
| CORE-156 | ○        | Are synchronization mechanisms required?                                                   |
| CORE-157 | ○        | Are there real-time deadlines associated with processing the module data?                  |
| CORE-158 | ○        | What happens if module communication takes longer than expected?                           |

---

# 15. Data Ownership and Consistency

This section becomes important when the same information is used in multiple places.

| ID       | Priority | Question                                                                   |
| -------- | -------- | -------------------------------------------------------------------------- |
| CORE-159 | ⭐        | Which system component is the authoritative source for each piece of data? |
| CORE-160 | ⭐        | When does CORE consider received data to be current?                       |
| CORE-161 | ⭐        | Can CORE cache module data?                                                |
| CORE-162 | ○        | How long may cached data be used?                                          |
| CORE-163 | ○        | How does CORE detect that cached data is no longer valid?                  |
| CORE-164 | ○        | Can multiple modules provide the same type of data?                        |
| CORE-165 | ○        | If multiple sources exist, how does CORE select the applicable source?     |
| CORE-166 | ○        | How are conflicting values handled?                                        |
| CORE-167 | ○        | Is data consistency required across multiple interfaces or tasks?          |

---

# 16. Versioning and Compatibility

Very important for industrial products with long lifetimes.

| ID       | Priority | Question                                                             |
| -------- | -------- | -------------------------------------------------------------------- |
| CORE-168 | ⭐        | Which versions of CORE must be compatible with the module?           |
| CORE-169 | ⭐        | Which versions of the module must be compatible with CORE?           |
| CORE-170 | ⭐        | How will incompatible firmware/interface versions be detected?       |
| CORE-171 | ○        | Is backward compatibility required?                                  |
| CORE-172 | ○        | Is forward compatibility required?                                   |
| CORE-173 | ○        | How are interface changes managed between firmware versions?         |
| CORE-174 | ○        | Does CORE need to identify the module interface version?             |
| CORE-175 | ○        | What should happen if CORE detects an unsupported module version?    |
| CORE-176 | ○        | Are firmware updates expected to change the communication interface? |

---

# 17. Firmware Update and Field Service

| ID       | Priority | Question                                                                |
| -------- | -------- | ----------------------------------------------------------------------- |
| CORE-177 | ○        | Does CORE participate in updating the module firmware?                  |
| CORE-178 | ○        | Can the module firmware be updated independently of CORE?               |
| CORE-179 | ○        | What happens if the module is running an older firmware version?        |
| CORE-180 | ○        | What happens if a firmware update fails?                                |
| CORE-181 | ○        | Must CORE prevent operation with incompatible module firmware?          |
| CORE-182 | ○        | Does CORE need to report module firmware versions to service personnel? |
| CORE-183 | ○        | Are field diagnostics required through CORE?                            |
| CORE-184 | ○        | Can service personnel force communication tests through CORE?           |

---

# 18. Safety-Related Interaction

Don't assume the CORE engineer owns the safety requirements. The purpose here is to understand the **firmware-side behavior** resulting from them.

| ID       | Priority | Question                                                                                         |
| -------- | -------- | ------------------------------------------------------------------------------------------------ |
| CORE-185 | ⭐        | Does CORE use any information from the module for safety-related decisions?                      |
| CORE-186 | 🔴       | What must CORE do if safety-relevant information from the module becomes invalid or unavailable? |
| CORE-187 | ⭐        | Are there defined safe or degraded behaviors associated with loss of module data?                |
| CORE-188 | ○        | Are there timing limits for safety-relevant information?                                         |
| CORE-189 | ○        | Does CORE need to detect stale safety-relevant information?                                      |
| CORE-190 | ○        | Are there independent mechanisms for detecting failure of the module?                            |
| CORE-191 | ○        | Are there requirements concerning diagnostic coverage or fault detection?                        |
| CORE-192 | ○        | Are there safety standards or safety architectures that constrain the interface?                 |

---

# 19. Testing and Verification

The CORE engineer should help define not only what the interface does, but how CORE will verify it.

| ID       | Priority | Question                                                             |
| -------- | -------- | -------------------------------------------------------------------- |
| CORE-193 | ⭐        | How will CORE's interaction with the module be tested?               |
| CORE-194 | ⭐        | What communication scenarios must be tested?                         |
| CORE-195 | ⭐        | What failure scenarios must be tested?                               |
| CORE-196 | ○        | Are automated tests available for the CORE-module interface?         |
| CORE-197 | ○        | Can the module be simulated or mocked during CORE testing?           |
| CORE-198 | ○        | Is a hardware-in-the-loop test environment available?                |
| CORE-199 | ○        | What test tools are normally used?                                   |
| CORE-200 | ○        | What boundary conditions must be tested?                             |
| CORE-201 | ○        | What timing behavior must be verified?                               |
| CORE-202 | ○        | How should communication faults be injected during testing?          |
| CORE-203 | ○        | What constitutes successful integration between CORE and the module? |

---

# 20. Existing Documentation and References

| ID       | Priority | Question                                                                                   |
| -------- | -------- | ------------------------------------------------------------------------------------------ |
| CORE-204 | ⭐        | What existing documents define the CORE-module interface?                                  |
| CORE-205 | ⭐        | Are there existing interface specifications we should reuse?                               |
| CORE-206 | ○        | Are there existing firmware design documents relevant to this integration?                 |
| CORE-207 | ○        | Are there existing source-code implementations that should be considered authoritative?    |
| CORE-208 | ○        | Are there existing test procedures or test reports?                                        |
| CORE-209 | ○        | Are there known limitations or defects in the existing implementation?                     |
| CORE-210 | ○        | Which documentation should be treated as the authoritative source when documents disagree? |

---

# 21. Assumptions and Unknowns

| ID       | Priority | Question                                                                                                |
| -------- | -------- | ------------------------------------------------------------------------------------------------------- |
| CORE-211 | ⭐        | What assumptions does the CORE firmware currently make about the module?                                |
| CORE-212 | ⭐        | Which of those assumptions have not yet been verified?                                                  |
| CORE-213 | ⭐        | Are there any undocumented behaviors that the module must support because CORE already depends on them? |
| CORE-214 | ○        | Are there known limitations in CORE that constrain the module design?                                   |
| CORE-215 | ○        | Are there requirements that CORE cannot currently satisfy without firmware changes?                     |
| CORE-216 | ○        | Are there unresolved interface decisions?                                                               |
| CORE-217 | ○        | Are there conflicting expectations between CORE and the system architecture?                            |
| CORE-218 | ○        | What information is still missing before the module interface can be finalized?                         |

---

# 22. Final Discovery Questions

Never skip these.

| ID       | Priority | Question                                                                             |
| -------- | -------- | ------------------------------------------------------------------------------------ |
| CORE-219 | ⭐        | What is the most important thing the module must provide to CORE?                    |
| CORE-220 | ⭐        | What is the most likely integration problem between CORE and the module?             |
| CORE-221 | ⭐        | What behavior would cause CORE to interpret the module incorrectly?                  |
| CORE-222 | ○        | What requirement is most likely to be overlooked when defining the interface?        |
| CORE-223 | ○        | What existing CORE behavior must not be broken by this module?                       |
| CORE-224 | ○        | What should the module explicitly **not** do from CORE's perspective?                |
| CORE-225 | ⭐        | What requirement or behavior have we not discussed that you believe is important?    |
| CORE-226 | ⭐        | Who else should we speak to before the CORE-module interface is considered complete? |

---

# The 30 CORE Questions I Would Mark as "Most Important"

If you want a **30-question practical interview**, I would use these:

|  # | ID          | Question                                                                            |
| -: | ----------- | ----------------------------------------------------------------------------------- |
|  1 | 🔴 CORE-001 | What is the role and responsibility of the CORE firmware within the overall system? |
|  2 | 🔴 CORE-004 | Where is the boundary of responsibility between CORE and the new module?            |
|  3 | 🔴 CORE-005 | What information does CORE need from the module?                                    |
|  4 | 🔴 CORE-006 | What information does the module need to receive from CORE?                         |
|  5 | ⭐ CORE-011  | What functions does CORE expect the module to provide?                              |
|  6 | ⭐ CORE-013  | How does CORE obtain data from the module?                                          |
|  7 | ⭐ CORE-014  | Does CORE actively request information, or is information pushed to CORE?           |
|  8 | 🔴 CORE-025 | What communication interface does CORE expect to use with the module?               |
|  9 | 🔴 CORE-026 | Who is responsible for initiating communication?                                    |
| 10 | 🔴 CORE-027 | What communication protocol or interface standard must be used?                     |
| 11 | ⭐ CORE-030  | What messages/requests can CORE send to the module?                                 |
| 12 | ⭐ CORE-031  | What messages/responses can the module send to CORE?                                |
| 13 | ⭐ CORE-032  | What data must be exchanged for each message/request?                               |
| 14 | ⭐ CORE-033  | What data format must be used?                                                      |
| 15 | 🔴 CORE-045 | How does CORE distinguish a valid value from an invalid or unavailable value?       |
| 16 | ⭐ CORE-047  | Does CORE need to know how old the received data is?                                |
| 17 | ⭐ CORE-050  | How should invalid data be represented?                                             |
| 18 | ⭐ CORE-057  | How frequently does CORE need the module data?                                      |
| 19 | ⭐ CORE-058  | What is the maximum acceptable latency for obtaining new data?                      |
| 20 | ⭐ CORE-059  | What is the maximum acceptable communication response time?                         |
| 21 | ⭐ CORE-069  | How does CORE detect that communication with the module has failed?                 |
| 22 | ⭐ CORE-070  | What should CORE do when communication fails?                                       |
| 23 | ⭐ CORE-076  | How does CORE detect that communication has recovered?                              |
| 24 | ⭐ CORE-081  | Does CORE need to know whether the module is operational?                           |
| 25 | ⭐ CORE-091  | What does CORE expect the module to do immediately after power-up?                  |
| 26 | ⭐ CORE-094  | What should happen if the module has not yet acquired valid data?                   |
| 27 | ⭐ CORE-103  | Does CORE need to reinitialize or reconfigure the module after restart?             |
| 28 | ⭐ CORE-109  | Which module parameters must CORE be able to configure?                             |
| 29 | ⭐ CORE-168  | Which versions of CORE must be compatible with the module?                          |
| 30 | ⭐ CORE-193  | How will CORE's interaction with the module be tested?                              |

---

# The 5 Questions You Absolutely Must Not Miss

If the interview went badly and you could only ask **five questions**, I would make them these.

### 🔴 1. What is the boundary of responsibility between CORE and the new module?

**CORE-004**

This is fundamental.

You need to know exactly where one system stops and the other begins.

Without this, you can easily create:

* duplicated functionality,
* missing functionality,
* contradictory behavior,
* incorrect fault handling,
* unclear ownership.

---

### 🔴 2. What communication interface does CORE expect to use with the module, and what is the required interaction model?

**CORE-025 + CORE-026 + CORE-027**

In practice, I'd ask these together:

> **"How is CORE expected to communicate with the module, which side initiates communication, and what protocol/interface rules already exist?"**

This establishes the fundamental interface contract.

---

### 🔴 3. How does CORE distinguish valid, invalid, unavailable, and stale data?

**CORE-045**

This is arguably the most important **data-semantics** question.

Don't accept an answer such as:

> "CORE just reads the value."

Push further:

> "How does CORE know whether that value is actually usable?"

That one question can expose requirements for:

* validity,
* freshness,
* status,
* error states,
* communication loss,
* initialization,
* sensor failure,
* fallback behavior.

---

### 🔴 4. What must CORE do when communication with the module or the module data itself becomes unavailable?

**CORE-070 + CORE-186**

This exposes the **failure behavior**.

You want to understand:

> Normal → degraded → fault → recovery

rather than only:

> Normal → data received.

This is particularly important if the data is used by control or safety-related functions.

---

### 🔴 5. What existing CORE behavior, interface, assumption, or limitation must the new module accommodate?

**CORE-211 + CORE-213 + CORE-214**

I'd actually ask this as one deliberately broad question:

> **"What existing behavior, assumption, limitation, or undocumented dependency in CORE could constrain the design of the new module?"**

This is the question most likely to uncover the things that aren't written in any specification.

---

# A Useful Interview Strategy

I would **not** run the interview in numerical order.

For a real project, I'd conduct it roughly like this:

**1. Understand CORE**

> What is CORE responsible for?

↓

**2. Define the boundary**

> What does CORE do vs. what does the new module do?

↓

**3. Define information**

> What does CORE need from the module?

> What does the module need from CORE?

↓

**4. Define interaction**

> Who initiates communication?

> How often?

> What happens during normal operation?

↓

**5. Define data semantics**

> What constitutes valid data?

> What constitutes stale data?

> What happens when data isn't available?

↓

**6. Define failure behavior**

> What happens when communication fails?

> What happens when the module fails?

> How does recovery work?

↓

**7. Define startup/restart**

> What happens after power-up?

> What happens after a module reset?

↓

**8. Define compatibility**

> Which CORE/module versions must work together?

↓

**9. Define verification**

> How are we going to prove that this interface works?

↓

**10. Ask what you didn't know to ask**

> "What have we not discussed that could cause an integration problem?"

That last question is surprisingly valuable.

---

## One important addition to your overall methodology

For the **CORE Firmware Engineer**, I would add one column to your Stakeholder Requirement Matrix that we didn't need to emphasize as much for the System Architect:

### `Existing vs. New`

Because the CORE engineer may tell you:

> "CORE already assumes that every connected module provides a heartbeat."

That's very different from:

> "The new module shall provide a heartbeat."

The first is an **existing CORE constraint/interface assumption**.

The second is a **new module requirement** derived from that constraint.

Your elicitation record should therefore distinguish:

| Answer                                         | Classification                    |
| ---------------------------------------------- | --------------------------------- |
| "CORE already expects this."                   | Existing constraint               |
| "CORE needs the module to provide this."       | Stakeholder requirement candidate |
| "We normally do this, but it isn't mandatory." | Engineering convention/preference |
| "We haven't decided yet."                      | Open issue                        |
| "CORE currently cannot support this."          | Existing limitation               |
| "We could change CORE if necessary."           | Design option / project decision  |

That distinction will make the transition from **Stakeholder Elicitation → StRS → Module Requirements** much cleaner.

# Stakeholder Requirements Specification

## Ozone Sensor Expansion Module

### ZE27-O3 Sensor Interface / CORE Interface

**Document ID:** SRS-O3-001
**Revision:** A
**Status:** Example / Training
**Prepared by:** Requirements Engineering
**Purpose:** Example of conversion from stakeholder elicitation results into formal stakeholder requirements.

---

# 1. Purpose

This document defines the stakeholder requirements for the Ozone Sensor Expansion Module.

The requirements contained in this document are derived from stakeholder needs, stakeholder interviews, system context, existing system constraints, and applicable interface expectations.

This document defines **what the system/module is required to provide from the stakeholder perspective**.

It intentionally avoids unnecessary implementation details.

Detailed technical behavior and implementation requirements shall be defined in the subsequent **Module Requirements Specification (MRS)**.

---

# 2. Scope

The subject of this specification is a DIN-rail expansion module installed inside the system control cabinet.

The module shall:

* acquire ozone measurement data from one ZE27-O3 sensor;
* communicate with the sensor through RS485-1;
* validate received sensor data;
* make the latest valid ozone measurement available to CORE;
* communicate with CORE through RS485-2;
* use Modbus RTU for the CORE interface;
* provide measurement validity and diagnostic information as required by the system.

The module is not responsible for overall ozone process control.

---

# 3. System Context

The relevant system context is:

```text
             ZE27-O3
               Sensor
                 |
                 | RS485-1
                 |
                 v
       +----------------------+
       | Ozone Sensor         |
       | Expansion Module     |
       |                      |
       | Measurement          |
       | Validation           |
       | Diagnostics          |
       | CORE Interface       |
       +----------------------+
                 |
                 | RS485-2
                 | Modbus RTU
                 |
                 v
                CORE
```

The module acts as an intermediary between the ozone sensor and the CORE controller.

---

# 4. Requirement Sources

Stakeholder requirements are derived from the following sources.

| Source ID | Source                            |
| --------- | --------------------------------- |
| STK-007   | System Architect                  |
| STK-008   | System Engineer                   |
| STK-011   | CORE Firmware Engineer            |
| STK-017   | Sensor / Instrumentation Engineer |
| STK-070   | Ozone Process Engineer            |
| STK-013   | Module Firmware Engineer          |
| STK-014   | Module Hardware Engineer          |
| STK-020   | Electrical Engineer               |
| STK-025   | Functional Safety Engineer        |
| STK-031   | Verification Engineer             |
| STK-043   | Service Engineer                  |

Detailed evidence for each requirement is maintained in the Stakeholder Elicitation & Interview Record.

---

# 5. Requirement Conventions

Each stakeholder requirement receives a unique identifier:

```text
STK-REQ-XXX
```

Requirements shall:

* describe an externally observable need or constraint;
* be necessary;
* be unambiguous;
* be atomic where practical;
* be verifiable;
* be traceable to a source;
* avoid unnecessary implementation decisions.

Priority values:

| Priority | Meaning                                      |
| -------- | -------------------------------------------- |
| MUST     | Mandatory requirement                        |
| SHOULD   | Required unless formally justified otherwise |
| COULD    | Desirable requirement                        |
| TBD      | Requirement not yet sufficiently defined     |
| OUT      | Explicitly outside scope                     |

---

# 6. Functional Stakeholder Requirements

## STK-REQ-001 — Ozone Measurement Acquisition

The system shall acquire ozone concentration measurements from one connected ZE27-O3 sensor.

**Source:** STK-007, STK-017
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-002 — Single Sensor

The system shall support one ozone sensor for the target module configuration.

**Source:** STK-007, STK-017
**Priority:** MUST
**Verification:** Inspection / Test

---

## STK-REQ-003 — Measurement Availability

The system shall make the latest successfully validated ozone measurement available to CORE.

**Source:** STK-007, STK-011
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-004 — Measurement Integrity

The system shall ensure that only successfully validated sensor measurements are accepted as valid measurements.

**Source:** STK-013, STK-017, STK-025
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-005 — Invalid Measurement Rejection

The system shall prevent an invalid sensor message from being accepted as a valid ozone measurement.

**Source:** STK-013
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-006 — Preservation of Last Valid Measurement

When a newly received sensor message is invalid, the system shall retain the most recently accepted valid ozone measurement.

**Source:** STK-013, STK-070
**Priority:** MUST
**Verification:** Test

---

# 7. Measurement Validity and Freshness

## STK-REQ-007 — Measurement Validity Information

The system shall provide information that allows CORE to determine whether the available ozone measurement is valid.

**Source:** STK-011, STK-025
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-008 — Measurement Freshness

The system shall provide information that allows CORE to determine whether the available ozone measurement is within the defined freshness limit.

**Source:** STK-007, STK-011, STK-070
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-009 — Stale Measurement

The system shall identify an ozone measurement as stale when no valid measurement has been received within the defined freshness interval.

**Source:** STK-070, STK-025
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-010 — Freshness Interval

The maximum acceptable age of a valid ozone measurement during normal system operation shall be 5 seconds.

**Source:** STK-070
**Priority:** TBD
**Verification:** Analysis / Test

**Note:** This value is hypothetical and requires confirmation from System Architecture and Functional Safety.

---

# 8. Sensor Communication Requirements

## STK-REQ-011 — Sensor Interface

The system shall communicate with the selected ZE27-O3 sensor using the applicable sensor communication interface.

**Source:** STK-017, STK-018
**Priority:** MUST
**Verification:** Test / Inspection

---

## STK-REQ-012 — Sensor Communication Monitoring

The system shall detect loss of valid communication with the ozone sensor.

**Source:** STK-013, STK-043
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-013 — Sensor Communication Recovery

The system shall automatically resume normal measurement acquisition after sensor communication is restored.

**Source:** STK-013, STK-043
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-014 — Sensor Communication Independence

Loss of sensor communication shall not prevent the system from providing diagnostic information to CORE.

**Source:** STK-013, STK-043
**Priority:** MUST
**Verification:** Test

---

# 9. CORE Interface Requirements

## STK-REQ-015 — CORE Communication

The system shall provide the ozone measurement to CORE through the defined digital communication interface.

**Source:** STK-011, STK-007
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-016 — Modbus RTU

The CORE interface shall use Modbus RTU.

**Source:** STK-011
**Priority:** MUST
**Verification:** Test / Inspection

---

## STK-REQ-017 — Module Role

The expansion module shall operate as a Modbus slave and CORE shall operate as the Modbus master.

**Source:** STK-011
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-018 — Measurement Read Request

The system shall allow CORE to request the current ozone measurement from the module.

**Source:** STK-011
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-019 — Measurement Status

The CORE interface shall provide measurement status information in addition to the numerical ozone value.

**Source:** STK-011, STK-025
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-020 — Invalid Modbus Request

The module shall provide the applicable response when CORE sends an unsupported or invalid Modbus request.

**Source:** STK-011
**Priority:** MUST
**Verification:** Test

---

# 10. Measurement Representation

## STK-REQ-021 — Measurement Unit

The ozone concentration shall be represented using the unit defined by the system.

**Source:** STK-070, STK-011
**Priority:** MUST
**Verification:** Inspection / Test

**Example value:** ppm

---

## STK-REQ-022 — Measurement Resolution

The ozone measurement shall provide the resolution required by the system.

**Source:** STK-070
**Priority:** MUST
**Verification:** Test

**Example value:** 0.1 ppm

---

## STK-REQ-023 — Measurement Range

The system shall support the ozone concentration range required for the intended application and selected sensor.

**Source:** STK-017, STK-070
**Priority:** MUST
**Verification:** Analysis / Test

---

# 11. Startup Requirements

## STK-REQ-024 — Startup Initialization

Following power-up, the system shall initialize the functions necessary to acquire and provide ozone measurement data.

**Source:** STK-013, STK-014
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-025 — No Measurement Available

Before the first valid ozone measurement is received, the system shall indicate that no valid ozone measurement is available.

**Source:** STK-025, STK-070
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-026 — First Valid Measurement

Following acquisition of the first valid sensor measurement, the system shall make the measurement available to CORE.

**Source:** STK-007, STK-011
**Priority:** MUST
**Verification:** Test

---

# 12. Diagnostic Requirements

## STK-REQ-027 — Sensor Communication Diagnostic

The system shall provide an indication of the current sensor communication state.

**Source:** STK-043, STK-045
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-028 — Invalid Data Diagnostic

The system shall provide diagnostic information when invalid sensor data is detected.

**Source:** STK-013, STK-043
**Priority:** SHOULD
**Verification:** Test

---

## STK-REQ-029 — Firmware Identification

The module shall provide its firmware version through an available service or system interface.

**Source:** STK-043
**Priority:** SHOULD
**Verification:** Inspection / Test

---

## STK-REQ-030 — Communication Error Diagnostics

The system shall provide sufficient diagnostic information to allow service personnel to identify loss of sensor communication.

**Source:** STK-043, STK-045
**Priority:** MUST
**Verification:** Test

---

# 13. Service Requirements

## STK-REQ-031 — Fault Identification

The diagnostic information shall allow service personnel to distinguish, where technically possible, between sensor communication faults, CORE communication faults, and module faults.

**Source:** STK-043, STK-045
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-032 — Module Replacement

The module shall be replaceable without requiring modification of the connected sensor installation.

**Source:** STK-043, STK-020
**Priority:** SHOULD
**Verification:** Demonstration

---

## STK-REQ-033 — Replacement Configuration

The system shall define the required configuration procedure for a replacement module.

**Source:** STK-043, STK-011
**Priority:** MUST
**Verification:** Inspection / Demonstration

---

# 14. Hardware and Installation Requirements

## STK-REQ-034 — DIN-Rail Installation

The module shall be suitable for installation on the DIN rail used by the target control cabinet.

**Source:** STK-020, STK-021
**Priority:** MUST
**Verification:** Inspection

---

## STK-REQ-035 — Cabinet Supply

The module shall operate from the electrical supply available within the target control cabinet.

**Source:** STK-014, STK-020
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-036 — RS485 Interfaces

The module shall provide separate communication interfaces for the sensor and CORE connections.

**Source:** STK-014, STK-020
**Priority:** MUST
**Verification:** Inspection / Test

---

## STK-REQ-037 — Service Accessibility

Required service indicators and connections shall remain accessible when the module is installed in the target cabinet.

**Source:** STK-020, STK-043
**Priority:** SHOULD
**Verification:** Inspection

---

# 15. Performance Requirements

## STK-REQ-038 — Measurement Update Rate

The system shall support a minimum valid ozone measurement update rate of one measurement per second.

**Source:** STK-070, STK-007
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-039 — Measurement Latency

The maximum time between successful acquisition of a valid sensor measurement and availability of that measurement to CORE shall be 500 ms.

**Source:** STK-007, STK-011
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-040 — CORE Response Time

The module shall respond to a valid CORE data request within 100 ms.

**Source:** STK-011
**Priority:** MUST
**Verification:** Test

---

# 16. Recovery Requirements

## STK-REQ-041 — Automatic Sensor Recovery

The system shall automatically recover measurement acquisition following temporary sensor communication interruption.

**Source:** STK-013, STK-043
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-042 — CORE Communication Independence

Loss of CORE communication shall not prevent continued sensor measurement acquisition.

**Source:** STK-007, STK-013
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-043 — Power Recovery

Following restoration of module power, the system shall return to normal operation without requiring manual intervention, provided that the sensor and CORE interfaces are operational.

**Source:** STK-014, STK-043
**Priority:** MUST
**Verification:** Test

---

# 17. Safety-Related Requirements

## STK-REQ-044 — Explicit Invalid State

The system shall explicitly identify when a valid ozone measurement is unavailable.

**Source:** STK-025
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-045 — Explicit Stale State

The system shall explicitly identify when the ozone measurement exceeds the defined freshness limit.

**Source:** STK-025, STK-070
**Priority:** MUST
**Verification:** Test

---

## STK-REQ-046 — No Implicit Validity

The existence of a previously received numeric ozone value shall not by itself indicate that the measurement is currently valid.

**Source:** STK-025
**Priority:** MUST
**Verification:** Test

---

# 18. Environmental Requirements

## STK-REQ-047 — Operating Temperature

The module shall operate within the ambient temperature range specified for the target cabinet installation.

**Source:** STK-014, STK-020
**Priority:** MUST
**Verification:** Test

---

# 19. Scope Exclusions

The stakeholder analysis identified the following functions as outside the scope of the module.

### OUT-001 — Ozone Process Control

The module shall not perform closed-loop ozone process control.

### OUT-002 — Process Alarm Management

The module shall not be responsible for generating process-level alarms unless explicitly assigned by a higher-level system requirement.

### OUT-003 — Sensor Calibration

The module shall not perform ozone sensor calibration.

### OUT-004 — Multi-Sensor Operation

The current module configuration shall support one ozone sensor only.

### OUT-005 — Historical Data Logging

The module shall not provide long-term historical ozone data storage.

---

# 20. Open / TBD Requirements

Some stakeholder answers are insufficient to establish final requirements.

| ID      | Topic                  | Current Information        | Required Action              |
| ------- | ---------------------- | -------------------------- | ---------------------------- |
| TBD-001 | Stale threshold        | 5 s proposed               | Confirm with System + Safety |
| TBD-002 | Modbus address         | Fixed address proposed     | Confirm with CORE team       |
| TBD-003 | Baud rate              | 19200 proposed             | Confirm CORE interface       |
| TBD-004 | Ozone unit             | ppm proposed               | Confirm system standard      |
| TBD-005 | Measurement range      | Sensor-dependent           | Confirm selected sensor      |
| TBD-006 | Diagnostic persistence | Not decided                | Decide with service team     |
| TBD-007 | Firmware update        | Service connector proposed | Confirm service concept      |

---

# 21. Stakeholder Requirement Summary

| Category                   | Number |
| -------------------------- | -----: |
| Functional                 |      6 |
| Measurement / Validity     |      4 |
| Sensor Communication       |      4 |
| CORE Interface             |      6 |
| Measurement Representation |      3 |
| Startup                    |      3 |
| Diagnostics                |      4 |
| Service                    |      3 |
| Hardware / Installation    |      4 |
| Performance                |      3 |
| Recovery                   |      3 |
| Safety                     |      3 |
| Environmental              |      1 |
| **Total**                  | **47** |

---

# 22. Traceability to Stakeholder Elicitation

Every stakeholder requirement shall trace back to evidence in the Stakeholder Elicitation & Interview Record.

Example:

| Stakeholder Requirement | Source Answer |
| ----------------------- | ------------- |
| STK-REQ-006             | ANS-FW-012    |
| STK-REQ-009             | ANS-PROC-010  |
| STK-REQ-015             | ANS-CORE-003  |
| STK-REQ-019             | ANS-CORE-015  |
| STK-REQ-030             | ANS-SERV-007  |
| STK-REQ-034             | ANS-CAB-001   |

This provides the first half of the traceability chain.

The RTM will later extend it:

```text
Answer
  ↓
Stakeholder Requirement
  ↓
Module Requirement
  ↓
Design
  ↓
Verification
```

---

# 23. Requirement Approval

Each requirement shall be reviewed and approved by the appropriate stakeholder/system owner before being baselined.

Approval shall confirm:

* requirement correctly represents stakeholder intent;
* requirement is necessary;
* requirement is unambiguous;
* requirement is feasible;
* requirement is verifiable;
* priority is correct;
* open assumptions have been identified;
* conflicting stakeholder requirements have been resolved or documented.

---

# 24. Transition to Module Requirements

The Stakeholder Requirements Specification is the input to the Module Requirements Specification.

The transition shall preserve traceability.

For example:

### Stakeholder requirement

**STK-REQ-006**

> When a newly received sensor message is invalid, the system shall retain the most recently accepted valid ozone measurement.

↓

### Derived module requirements

**REQ-MOD-006**

> The module shall validate the received sensor frame before updating the stored measurement.

**REQ-MOD-007**

> The module shall update the stored measurement only after successful validation of the sensor frame.

**REQ-MOD-008**

> The module shall retain the previously stored valid measurement when validation of a newly received sensor frame fails.

The stakeholder requirement describes the **required system behavior**.

The module requirements break that behavior into precise technical obligations for the module.

---

# 25. Document Boundary

The following distinction shall be maintained:

| Question                                  | Document                                   |
| ----------------------------------------- | ------------------------------------------ |
| Who is interested?                        | Stakeholder Register                       |
| What should we ask?                       | Stakeholder Requirement Matrix             |
| What did they say?                        | Stakeholder Elicitation Record             |
| What does the system/stakeholder require? | **Stakeholder Requirements Specification** |
| What exactly must our module do?          | Module Requirements Specification          |
| Can we trace and verify it?               | RTM                                        |

The Stakeholder Requirements Specification therefore represents the **approved bridge between stakeholder input and engineering requirements**.

# Stakeholder Requirements Specification

## Ozone Sensor Expansion Module

### ZE27-O3 Sensor Interface / CORE Modbus Interface

**Document status:** Example / Training Document
**Revision:** A
**Purpose:** Demonstration of how stakeholder interview answers are transformed into formal stakeholder requirements.

---

## 1. Purpose

This document defines the stakeholder requirements for the Ozone Sensor Expansion Module.

The module is intended to acquire ozone concentration measurements from one ZE27-O3 sensor through RS485-1 and make the latest valid measurement available to the CORE controller through RS485-2 using Modbus RTU.

This document represents the **stakeholder-level requirements** and is intentionally independent of the detailed implementation.

The requirements in this document are derived from hypothetical stakeholder answers and are provided only as an example of the requirements-engineering process.

---

# 2. System Context

The expansion module is installed inside the system control cabinet on a DIN rail.

The module has two independent communication interfaces:

* **RS485-1:** communication with one ZE27-O3 ozone sensor
* **RS485-2:** Modbus RTU communication with the CORE controller

The expected functional relationship is:

```text
       ZE27-O3 Sensor
              |
           RS485-1
              |
              v
    +-----------------------+
    | Ozone Sensor          |
    | Expansion Module      |
    |                       |
    | Acquisition           |
    | Validation            |
    | Measurement storage   |
    | Diagnostics           |
    | Modbus slave          |
    +-----------------------+
              |
           RS485-2
              |
              v
             CORE
        Modbus master
```

The module shall not perform ozone process control. Process control remains the responsibility of the CORE/system controller.

---

# 3. Stakeholder Sources

The stakeholder requirements in this document originate from the following hypothetical stakeholder inputs:

| Source ID | Stakeholder                | Example input                                                   |
| --------- | -------------------------- | --------------------------------------------------------------- |
| STK-007   | System Architect           | Module shall provide reliable ozone data to CORE                |
| STK-011   | CORE Firmware Engineer     | CORE requires a defined Modbus interface                        |
| STK-017   | Instrumentation Engineer   | Sensor communication must follow the defined sensor protocol    |
| STK-070   | Ozone Process Engineer     | Stale measurements shall not be treated as current measurements |
| STK-013   | Module Firmware Engineer   | Invalid frames shall not overwrite valid data                   |
| STK-014   | Module Hardware Engineer   | Module shall operate from the defined cabinet supply            |
| STK-020   | Electrical Engineer        | Module shall be suitable for DIN-rail cabinet installation      |
| STK-025   | Functional Safety Engineer | Measurement validity shall be explicitly identifiable           |
| STK-031   | Verification Engineer      | Communication failures shall be detectable and testable         |
| STK-043   | Service Engineer           | Faults shall be diagnosable without removing the module         |

---

# 4. Stakeholder Needs

Before writing formal requirements, the interview answers have been consolidated into the following stakeholder needs.

### SN-001 — Reliable measurement acquisition

The system needs the module to acquire ozone measurements from the connected sensor reliably.

### SN-002 — Measurement integrity

The system needs to distinguish valid sensor measurements from corrupted or invalid communication frames.

### SN-003 — No propagation of invalid data

The system needs to prevent invalid sensor data from replacing the most recently validated measurement.

### SN-004 — Measurement freshness

The CORE needs to determine whether the available ozone measurement is still current.

### SN-005 — Defined CORE interface

The CORE needs a stable and documented method for reading the ozone measurement and its status.

### SN-006 — Communication fault detection

The system needs communication failures between the sensor and module to be detectable.

### SN-007 — Diagnostic capability

Service personnel need sufficient information to distinguish sensor-side, module-side, and CORE-side communication problems.

### SN-008 — Predictable startup behavior

The module needs a defined behavior after power-up before a valid sensor measurement has been acquired.

### SN-009 — Cabinet compatibility

The module needs to be suitable for installation inside the existing electrical control cabinet.

### SN-010 — Recoverability

The module needs to recover from temporary communication interruptions without requiring unnecessary manual intervention.

---

# 5. Stakeholder Requirements

## 5.1 General Functional Requirements

### STK-REQ-001 — Sensor measurement acquisition

The module shall acquire ozone concentration measurements from one connected ZE27-O3 sensor through RS485-1.

**Source:** STK-007, STK-017
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-002 — Single sensor support

The module shall support one ozone sensor connected to RS485-1.

**Source:** STK-007, STK-017
**Priority:** MUST
**Verification:** Test / Inspection

---

### STK-REQ-003 — Continuous measurement availability

The module shall maintain the latest successfully validated ozone measurement received from the sensor.

**Source:** STK-007, STK-013, STK-070
**Priority:** MUST
**Verification:** Test

---

## 5.2 Measurement Validity

### STK-REQ-004 — Frame validation

The module shall validate each received sensor message before accepting the associated ozone measurement.

**Source:** STK-017, STK-013
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-005 — CRC validation

The module shall detect sensor messages containing an invalid CRC according to the applicable sensor communication protocol.

**Source:** STK-017
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-006 — Invalid measurement rejection

The module shall not update the stored ozone measurement when the received sensor message is invalid.

**Source:** STK-013, STK-025
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-007 — Last valid measurement preservation

When an invalid sensor message is received, the module shall retain the most recently accepted valid ozone measurement.

**Source:** STK-013, STK-070
**Priority:** MUST
**Verification:** Test

---

## 5.3 Measurement Freshness

### STK-REQ-008 — Measurement validity status

The module shall provide an indication that distinguishes a valid/current ozone measurement from an unavailable or invalid measurement.

**Source:** STK-025, STK-011
**Priority:** MUST
**Verification:** Test / Inspection

---

### STK-REQ-009 — Measurement age

The system interface shall provide sufficient information for the CORE to determine whether the available ozone measurement exceeds the defined freshness limit.

**Source:** STK-007, STK-011, STK-070
**Priority:** MUST
**Verification:** Test

**Note:** This requirement does not yet specify whether the implementation shall use a data-age register, timestamp, status bit, counter, or another mechanism.

---

### STK-REQ-010 — Stale measurement

A measurement shall be considered stale when no valid sensor measurement has been received within the system-defined freshness interval.

**Source:** STK-007, STK-070, STK-025
**Priority:** MUST
**Verification:** Test

**Example stakeholder answer:**
"The measurement shall be considered stale after 5 seconds without a valid sensor update."

**Example derived value:**
Freshness interval = 5 s.

This value should be confirmed before becoming a final product requirement.

---

## 5.4 Sensor Communication

### STK-REQ-011 — Sensor communication protocol

The module shall communicate with the ZE27-O3 sensor using the communication protocol defined for the selected sensor variant.

**Source:** STK-017, STK-018
**Priority:** MUST
**Verification:** Test / Inspection

---

### STK-REQ-012 — Sensor communication interruption

The module shall detect the absence of valid sensor communication within the defined sensor communication timeout.

**Source:** STK-013, STK-017
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-013 — Sensor reconnection

The module shall automatically resume acquisition of ozone measurements after communication with a previously unavailable sensor is restored.

**Source:** STK-013, STK-043
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-014 — Sensor communication recovery

Temporary loss of sensor communication shall not require a power cycle of the module to restore normal measurement acquisition.

**Source:** STK-043, STK-013
**Priority:** MUST
**Verification:** Test

---

# 6. CORE Interface Requirements

## 6.1 Modbus Communication

### STK-REQ-015 — Modbus interface

The module shall provide the ozone measurement to the CORE using Modbus RTU over RS485-2.

**Source:** STK-011, STK-007
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-016 — Module role

The module shall operate as a Modbus slave and the CORE shall operate as the Modbus master for communication over RS485-2.

**Source:** STK-011
**Priority:** MUST
**Verification:** Test / Inspection

---

### STK-REQ-017 — CORE polling

The module shall provide the requested ozone data in response to valid Modbus requests from the CORE.

**Source:** STK-011
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-018 — Invalid Modbus request

The module shall reject unsupported or invalid Modbus requests using the applicable Modbus exception mechanism.

**Source:** STK-011, STK-013
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-019 — Modbus communication recovery

A temporary interruption of Modbus communication shall not prevent the module from continuing to acquire sensor measurements.

**Source:** STK-007, STK-013
**Priority:** MUST
**Verification:** Test

---

## 6.2 Measurement Representation

### STK-REQ-020 — Ozone measurement unit

The ozone measurement provided to CORE shall use the system-defined ozone concentration unit.

**Source:** STK-070, STK-011
**Priority:** MUST
**Verification:** Test / Inspection

**Example stakeholder answer:**
"The system uses ppm."

---

### STK-REQ-021 — Measurement resolution

The ozone measurement provided to CORE shall preserve the resolution required by the system.

**Source:** STK-070, STK-011
**Priority:** MUST
**Verification:** Test

**Example stakeholder answer:**
"0.1 ppm resolution is sufficient."

---

### STK-REQ-022 — Measurement range

The module shall support the ozone measurement range required by the system and the selected sensor.

**Source:** STK-017, STK-070
**Priority:** MUST
**Verification:** Test / Analysis

---

# 7. Startup Requirements

### STK-REQ-023 — Power-up initialization

After power-up, the module shall initialize its communication interfaces and internal functions before accepting normal operation.

**Source:** STK-013, STK-014
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-024 — No valid measurement at startup

Before the first valid ozone measurement has been received, the module shall indicate that a valid ozone measurement is not available.

**Source:** STK-025, STK-070
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-025 — Startup measurement

The module shall make the first valid ozone measurement available to CORE after successful acquisition and validation of the sensor data.

**Source:** STK-007, STK-011
**Priority:** MUST
**Verification:** Test

---

# 8. Diagnostic Requirements

### STK-REQ-026 — Sensor communication status

The module shall provide diagnostic information indicating whether valid communication with the ozone sensor is currently established.

**Source:** STK-043, STK-013
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-027 — CRC error indication

The module shall provide a diagnostic indication when invalid sensor CRCs are detected.

**Source:** STK-013, STK-043
**Priority:** SHOULD
**Verification:** Test

---

### STK-REQ-028 — Communication error indication

The module shall provide diagnostic information that allows service personnel to identify a loss of sensor communication.

**Source:** STK-043, STK-045
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-029 — Firmware identification

The module shall provide its firmware version through the service or system interface.

**Source:** STK-043, STK-013
**Priority:** SHOULD
**Verification:** Test / Inspection

---

### STK-REQ-030 — Diagnostic counters

The module shall provide counters for selected communication errors to support troubleshooting.

**Source:** STK-043, STK-031
**Priority:** SHOULD
**Verification:** Test

**Note:** The exact counters are intentionally not defined at stakeholder level.

---

# 9. Service and Maintenance Requirements

### STK-REQ-031 — Fault discrimination

The diagnostic interface shall provide sufficient information to distinguish, where technically possible, between:

* sensor communication failure;
* invalid sensor data;
* CORE communication failure;
* internal module fault.

**Source:** STK-043, STK-045
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-032 — Module replacement

A failed module shall be replaceable without modification of the connected ozone sensor.

**Source:** STK-043, STK-021
**Priority:** SHOULD
**Verification:** Demonstration

---

### STK-REQ-033 — Replacement configuration

The system shall define how the configuration of a replacement module is established.

**Source:** STK-043, STK-011
**Priority:** MUST
**Verification:** Inspection / Demonstration

**Example stakeholder answer:**
"The replacement module should use the standard Modbus address defined for this position."

This answer still needs to be transformed into a more precise system requirement later.

---

# 10. Electrical and Mechanical Requirements

### STK-REQ-034 — DIN-rail installation

The module shall be suitable for installation on the DIN rail used by the target control cabinet.

**Source:** STK-020, STK-021
**Priority:** MUST
**Verification:** Inspection

---

### STK-REQ-035 — Cabinet supply

The module shall operate from the electrical supply available in the target control cabinet.

**Source:** STK-020, STK-014
**Priority:** MUST
**Verification:** Test

**Example stakeholder answer:**
"24 VDC nominal supply is available."

---

### STK-REQ-036 — RS485 connections

The module shall provide dedicated electrical connections for RS485-1 and RS485-2.

**Source:** STK-020, STK-014
**Priority:** MUST
**Verification:** Inspection

---

### STK-REQ-037 — Service accessibility

Required status indicators and service-accessible connections shall remain accessible after installation in the target cabinet.

**Source:** STK-020, STK-043
**Priority:** SHOULD
**Verification:** Inspection

---

# 11. Performance Requirements

### STK-REQ-038 — Measurement update rate

The module shall support the sensor measurement update rate required by the system.

**Source:** STK-007, STK-070
**Priority:** MUST
**Verification:** Test

**Example stakeholder answer:**
"At least one valid measurement every 1 second is required."

---

### STK-REQ-039 — Measurement availability latency

The time between successful receipt of a valid sensor measurement and availability of that measurement to CORE shall not exceed the system-defined maximum latency.

**Source:** STK-007, STK-011
**Priority:** MUST
**Verification:** Test

**Example stakeholder answer:**
"Maximum acceptable latency is 500 ms."

---

### STK-REQ-040 — Modbus response time

The module shall respond to a valid Modbus request from CORE within the maximum response time defined by the system.

**Source:** STK-011, STK-013
**Priority:** MUST
**Verification:** Test

**Example stakeholder answer:**
"CORE expects a response within 100 ms."

---

# 12. Recovery Requirements

### STK-REQ-041 — Automatic recovery

The module shall automatically recover normal sensor acquisition following a temporary sensor communication interruption.

**Source:** STK-013, STK-043
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-042 — Independent communication recovery

Loss of communication with CORE shall not require restarting sensor acquisition.

**Source:** STK-007, STK-013
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-043 — Recovery after power restoration

Following restoration of the module power supply, the module shall return to normal operation without requiring manual intervention, provided that the sensor and CORE interfaces are operational.

**Source:** STK-014, STK-043
**Priority:** MUST
**Verification:** Test

---

# 13. Safety-Related Stakeholder Requirements

### STK-REQ-044 — Invalid measurement indication

The module shall provide an explicit indication when the ozone measurement is unavailable or does not satisfy the defined validity criteria.

**Source:** STK-025, STK-070
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-045 — Stale measurement indication

The module shall provide an explicit indication when the available measurement has exceeded the defined freshness interval.

**Source:** STK-025, STK-070
**Priority:** MUST
**Verification:** Test

---

### STK-REQ-046 — No implicit validity

The module shall not indicate an ozone measurement as valid solely because a previous numeric measurement exists.

**Source:** STK-025
**Priority:** MUST
**Verification:** Test

---

# 14. Environmental Requirements

### STK-REQ-047 — Operating temperature

The module shall operate within the temperature range specified for the target control cabinet installation.

**Source:** STK-020, STK-014
**Priority:** MUST
**Verification:** Test

**Example stakeholder answer:**
"Cabinet ambient temperature is expected to remain between 0 °C and 50 °C."

---

### STK-REQ-048 — Cabinet environment

The module shall be suitable for operation in the environmental conditions of the target electrical control cabinet.

**Source:** STK-020, STK-023
**Priority:** MUST
**Verification:** Analysis / Test

---

# 15. Scope Boundaries

The following functions were explicitly identified as **outside the module's responsibility**.

### OUT-001 — Ozone process control

The module shall not perform closed-loop ozone process control.

### OUT-002 — Process alarm generation

The module shall not be responsible for determining process-level ozone alarms unless explicitly assigned by a future system requirement.

### OUT-003 — Sensor calibration

The module shall not perform sensor calibration.

### OUT-004 — Multi-sensor management

The module shall not support multiple ozone sensors in the current product variant.

### OUT-005 — Historical process logging

The module shall not provide long-term historical ozone data logging.

These exclusions are important because they prevent stakeholder expectations from silently expanding the module's scope.

---

# 16. Open Issues / TBD Items

The stakeholder interviews have identified several requirements that cannot yet be finalized.

| ID      | Topic                     | Current assumption        | Status          |
| ------- | ------------------------- | ------------------------- | --------------- |
| TBD-001 | Sensor timeout            | 2 s                       | To be confirmed |
| TBD-002 | Stale threshold           | 5 s                       | To be confirmed |
| TBD-003 | Modbus slave address      | Fixed by cabinet position | To be confirmed |
| TBD-004 | Modbus baud rate          | 19200 bit/s               | To be confirmed |
| TBD-005 | Ozone unit                | ppm                       | To be confirmed |
| TBD-006 | Measurement resolution    | 0.1 ppm                   | To be confirmed |
| TBD-007 | Measurement range         | Sensor-dependent          | To be confirmed |
| TBD-008 | CRC error counter         | Required                  | To be confirmed |
| TBD-009 | Error counter persistence | Across power cycle        | To be confirmed |
| TBD-010 | Firmware update mechanism | Service connector         | To be confirmed |

---

# 17. Requirement Quality Review

Each stakeholder requirement shall be reviewed for:

* necessity;
* unambiguous wording;
* singularity;
* consistency;
* feasibility;
* verifiability;
* traceability;
* correct stakeholder ownership;
* correct priority;
* absence of unnecessary implementation constraints.

For example:

**Poor stakeholder requirement:**

> The module shall configure RS485-2, wait for CORE, read the request, configure RS485-2 for writing, send the buffer and then configure RS485-2 for reading.

This is primarily an **implementation/design description**.

A better stakeholder requirement is:

> The module shall provide the latest valid ozone measurement to CORE in response to a valid Modbus request.

The detailed RS485 direction control, buffering, state machine, interrupt handling, DMA, etc. belong later in the technical/design requirements.

---

# 18. Requirement Derivation Example

One of the most important purposes of this document is to show the transition from stakeholder need to technical requirement.

### Stakeholder answer

> "CORE needs to know whether the ozone value is still current."

↓

### Stakeholder need

**SN-004:**
The CORE needs to determine whether the available ozone measurement is still current.

↓

### Stakeholder requirement

**STK-REQ-009:**
The system interface shall provide sufficient information for the CORE to determine whether the available ozone measurement exceeds the defined freshness limit.

↓

### Later: module technical requirements

Possible derived requirements might be:

**REQ-MOD-XXX:**
The module shall maintain the timestamp or age of the most recently accepted valid sensor measurement.

**REQ-MOD-XXX:**
The module shall expose measurement validity through Modbus register X.

**REQ-MOD-XXX:**
The module shall expose measurement age through Modbus register Y.

Notice that the stakeholder requirement did **not** dictate the implementation.

The design team is free to determine whether timestamp, age counter, status bits, or another mechanism is technically appropriate.

---

# 19. Example Requirement Traceability

The requirements can now be traced in both directions.

| Stakeholder Need | Stakeholder Requirement | Future Module Requirement | Verification |
| ---------------- | ----------------------- | ------------------------- | ------------ |
| SN-001           | STK-REQ-001             | REQ-MOD-001               | TEST-001     |
| SN-002           | STK-REQ-004             | REQ-MOD-002               | TEST-002     |
| SN-003           | STK-REQ-006             | REQ-MOD-003               | TEST-003     |
| SN-004           | STK-REQ-009             | REQ-MOD-004               | TEST-004     |
| SN-005           | STK-REQ-015             | REQ-MOD-010               | TEST-010     |
| SN-006           | STK-REQ-012             | REQ-MOD-020               | TEST-020     |
| SN-007           | STK-REQ-031             | REQ-MOD-030               | TEST-030     |
| SN-008           | STK-REQ-024             | REQ-MOD-040               | TEST-040     |
| SN-009           | STK-REQ-034             | REQ-HW-001                | TEST-HW-001  |
| SN-010           | STK-REQ-041             | REQ-MOD-050               | TEST-050     |

This table becomes the foundation for the later **Requirements Traceability Matrix (RTM)**.

---

# 20. What Happens Next?

At this point the requirements-engineering chain is:

```text
Stakeholder Register
        |
        v
Stakeholder Questions
        |
        v
Stakeholder Answers
        |
        v
Stakeholder Needs
        |
        v
STAKEHOLDER REQUIREMENTS
        |
        v
MODULE / SYSTEM REQUIREMENTS
        |
        v
DESIGN REQUIREMENTS
        |
        v
IMPLEMENTATION
        |
        v
VERIFICATION
        |
        v
VALIDATION
```

The document you are looking at is therefore **not yet your final module specification**.

The next major document should be:

## Module Requirements Specification

That document will take requirements such as:

> "The module shall not update the stored ozone measurement when the received sensor message is invalid."

and turn them into precise engineering requirements covering:

* RS485-1 configuration;
* frame detection;
* receive timeout;
* frame length;
* buffer behavior;
* CRC algorithm;
* byte order;
* measurement extraction;
* measurement validity;
* stale detection;
* internal data model;
* RS485-2 configuration;
* Modbus slave address;
* register map;
* supported function codes;
* Modbus exception behavior;
* response timing;
* RS485 direction control;
* startup;
* watchdog;
* diagnostics;
* error recovery;
* hardware requirements;
* electrical requirements;
* environmental requirements.

That is where your original sequence — **receive → buffer → validate → store → respond to CORE** — should be transformed into formal, testable technical requirements.

| ID | Stakeholder Need | Stakeholder Req. | Module Req. | Source | Priority | Design Element | Verification ID | Verification Method | Status | Evidence | Notes |
| -- | ---------------- | ---------------- | ----------- | ------ | -------- | -------------- | --------------- | ------------------- | ------ | -------- | ----- |







# Requirements Traceability Matrix

## Ozone Sensor Expansion Module

### ZE27-O3 Sensor Interface / CORE Modbus Interface

**Document status:** Example / Training Document
**Revision:** A
**Purpose:** Demonstration of requirements traceability from stakeholder needs through module requirements to verification.

---

# 1. Purpose

This Requirements Traceability Matrix (RTM) establishes bidirectional traceability between:

1. Stakeholder needs
2. Stakeholder requirements
3. Module/system requirements
4. Design or implementation elements
5. Verification activities
6. Verification results

The purpose of the RTM is to demonstrate that:

* every relevant stakeholder need has been converted into one or more requirements;
* every module requirement has a valid source;
* every module requirement can be verified;
* every requirement is covered by at least one verification activity;
* no verification test exists without a corresponding requirement;
* changes to requirements can be assessed for their impact on design and testing.

---

# 2. Requirement Identification Scheme

The following identifiers are used.

| Prefix       | Meaning                       |
| ------------ | ----------------------------- |
| SN-xxx       | Stakeholder Need              |
| STK-REQ-xxx  | Stakeholder Requirement       |
| REQ-MOD-xxx  | Module Functional Requirement |
| REQ-HW-xxx   | Hardware Requirement          |
| REQ-IF-xxx   | Interface Requirement         |
| REQ-DIAG-xxx | Diagnostic Requirement        |
| REQ-PERF-xxx | Performance Requirement       |
| REQ-ENV-xxx  | Environmental Requirement     |
| TEST-xxx     | Verification Test             |
| INS-xxx      | Inspection                    |
| ANA-xxx      | Analysis                      |
| DEM-xxx      | Demonstration                 |

---

# 3. Traceability Chain

The intended traceability chain is:

```text
Stakeholder
    |
    v
Stakeholder Need
    |
    v
Stakeholder Requirement
    |
    v
Module Requirement
    |
    v
Design / Implementation
    |
    v
Verification Method
    |
    v
Verification Result
```

For example:

```text
SN-003
  |
  v
STK-REQ-006
  |
  v
REQ-MOD-003
  |
  v
FW: Measurement Validation Manager
  |
  v
TEST-003
  |
  v
PASS
```

---

# 4. Master Traceability Matrix

## 4.1 Measurement Acquisition

| Stakeholder Need                        | Stakeholder Requirement | Module Requirement | Design Element               | Verification | Status |
| --------------------------------------- | ----------------------- | ------------------ | ---------------------------- | ------------ | ------ |
| SN-001 Reliable measurement acquisition | STK-REQ-001             | REQ-MOD-001        | Sensor Communication Manager | TEST-001     | PASS   |
| SN-001                                  | STK-REQ-002             | REQ-MOD-002        | Sensor Interface             | TEST-002     | PASS   |
| SN-001                                  | STK-REQ-003             | REQ-MOD-003        | Measurement Data Manager     | TEST-003     | PASS   |
| SN-002 Measurement integrity            | STK-REQ-004             | REQ-MOD-004        | Frame Validation Manager     | TEST-004     | PASS   |
| SN-002                                  | STK-REQ-005             | REQ-MOD-005        | CRC Validation               | TEST-005     | PASS   |
| SN-003 No propagation of invalid data   | STK-REQ-006             | REQ-MOD-006        | Measurement Data Manager     | TEST-006     | PASS   |
| SN-003                                  | STK-REQ-007             | REQ-MOD-007        | Measurement Data Manager     | TEST-007     | PASS   |

---

# 5. Detailed Module Requirement Traceability

## 5.1 Sensor Communication

### REQ-MOD-001

**Requirement:**

> The module shall acquire ozone measurement frames from the connected ZE27-O3 sensor through RS485-1.

**Source:** STK-REQ-001

**Design element:** Sensor Communication Manager

**Verification:** TEST-001

**Verification method:** Functional test

**Test description:**

1. Connect a simulated ZE27-O3 sensor to RS485-1.
2. Transmit a valid sensor frame.
3. Observe the module's received data.
4. Verify that the frame is received and processed.

**Expected result:**
The module receives and processes the valid sensor frame.

**Result:** PASS

---

### REQ-MOD-002

**Requirement:**

> The module shall support communication with one ozone sensor connected to RS485-1.

**Source:** STK-REQ-002

**Design element:** Sensor Interface

**Verification:** TEST-002

**Verification method:** Inspection + Functional Test

**Result:** PASS

---

# 6. Frame Validation Traceability

### REQ-MOD-004

**Requirement:**

> The module shall validate the structure and integrity of every received sensor frame before extracting the ozone measurement.

**Source:** STK-REQ-004

**Design element:** Frame Validation Manager

**Verification:** TEST-004

**Test cases:**

| Test Case | Description                 | Expected Result |
| --------- | --------------------------- | --------------- |
| TC-004-01 | Valid frame                 | Accepted        |
| TC-004-02 | Invalid header              | Rejected        |
| TC-004-03 | Incorrect frame length      | Rejected        |
| TC-004-04 | Invalid CRC                 | Rejected        |
| TC-004-05 | Corrupted measurement field | Rejected        |
| TC-004-06 | Incomplete frame            | Rejected        |

**Result:** PASS

---

### REQ-MOD-005

**Requirement:**

> The module shall calculate and validate the sensor frame CRC according to the applicable sensor communication protocol.

**Source:** STK-REQ-005

**Design element:** CRC Validation Function

**Verification:** TEST-005

**Test method:**

A known set of valid and intentionally corrupted frames shall be transmitted to the module.

**Expected result:**

* valid CRC → frame accepted;
* invalid CRC → frame rejected.

**Result:** PASS

---

# 7. Invalid Measurement Traceability

### REQ-MOD-006

**Requirement:**

> The module shall not update the stored ozone measurement when the received sensor frame fails validation.

**Source:** STK-REQ-006

**Design element:** Measurement Data Manager

**Verification:** TEST-006

**Test sequence:**

```text
1. Send valid measurement = 10.0 ppm
2. Verify stored value = 10.0 ppm
3. Send invalid frame containing 20.0 ppm
4. Verify frame rejected
5. Read stored measurement
```

**Expected result:**

```text
Stored measurement remains = 10.0 ppm
```

**Result:** PASS

---

### REQ-MOD-007

**Requirement:**

> When a sensor communication error occurs, the module shall retain the last valid measurement until the measurement becomes unavailable according to the defined freshness rules.

**Source:** STK-REQ-007, STK-REQ-010

**Design element:** Measurement Data Manager / Freshness Monitor

**Verification:** TEST-007

**Test sequence:**

```text
Valid frame
      |
      v
10.0 ppm
      |
Sensor communication lost
      |
      v
Last valid value retained
      |
Freshness timeout exceeded
      |
      v
Measurement marked stale
```

**Result:** PASS

---

# 8. Measurement Freshness Traceability

### REQ-MOD-010

**Requirement:**

> The module shall determine the age of the most recently accepted valid ozone measurement.

**Source:** STK-REQ-009

**Design element:** Freshness Monitor

**Verification:** TEST-010

**Verification method:** Functional test

**Test cases:**

| Test      | Condition                   | Expected                       |
| --------- | --------------------------- | ------------------------------ |
| TC-010-01 | New valid frame             | Age resets                     |
| TC-010-02 | 1 s after valid frame       | Age ≈ 1 s                      |
| TC-010-03 | 5 s without valid frame     | Stale threshold reached        |
| TC-010-04 | New valid frame after stale | Age resets / measurement valid |

**Result:** PASS

---

### REQ-MOD-011

**Requirement:**

> The module shall indicate the ozone measurement as stale when no valid sensor measurement has been received for 5 seconds.

**Source:** STK-REQ-010

**Design element:** Freshness Monitor

**Verification:** TEST-011

**Result:** PASS

**Note:**
The 5-second value is fictional in this example and must be replaced by the approved system value.

---

# 9. CORE / Modbus Traceability

### REQ-IF-001

**Requirement:**

> The module shall operate as a Modbus RTU slave on RS485-2.

**Source:** STK-REQ-015, STK-REQ-016

**Design element:** Modbus Slave Stack

**Verification:** TEST-020

**Result:** PASS

---

### REQ-IF-002

**Requirement:**

> The module shall return the latest valid ozone measurement in response to a valid Modbus read request from CORE.

**Source:** STK-REQ-017

**Design element:** Modbus Register Manager

**Verification:** TEST-021

**Test sequence:**

```text
Sensor
  |
  | 12.5 ppm
  v
Module
  |
  | valid measurement stored
  |
CORE -- Modbus Read --> Module
CORE <-- 12.5 ppm ---- Module
```

**Result:** PASS

---

### REQ-IF-003

**Requirement:**

> The module shall provide an explicit measurement validity status to CORE.

**Source:** STK-REQ-008, STK-REQ-044

**Design element:** Modbus Register Manager

**Verification:** TEST-022

**Test cases:**

| Condition                        | Expected status                               |
| -------------------------------- | --------------------------------------------- |
| Valid fresh measurement          | VALID                                         |
| No measurement after startup     | INVALID                                       |
| Sensor communication lost        | STALE/INVALID                                 |
| CRC errors only, before timeout  | Previous value + valid/stale according to age |
| Fresh measurement after recovery | VALID                                         |

**Result:** PASS

---

### REQ-IF-004

**Requirement:**

> The module shall provide measurement freshness information to CORE.

**Source:** STK-REQ-009

**Design element:** Modbus Register Manager

**Verification:** TEST-023

**Result:** PASS

---

# 10. Modbus Error Handling

### REQ-IF-005

**Requirement:**

> The module shall return the applicable Modbus exception response for unsupported function codes.

**Source:** STK-REQ-018

**Design element:** Modbus Slave Stack

**Verification:** TEST-024

**Test:**

Send unsupported function code.

**Expected result:**

Module returns the applicable Modbus exception response.

**Result:** PASS

---

### REQ-IF-006

**Requirement:**

> The module shall reject requests for undefined registers using the applicable Modbus exception response.

**Source:** STK-REQ-018

**Design element:** Modbus Register Manager

**Verification:** TEST-025

**Result:** PASS

---

# 11. Communication Independence

### REQ-MOD-020

**Requirement:**

> Loss of RS485-2 communication with CORE shall not prevent continued acquisition and validation of sensor data on RS485-1.

**Source:** STK-REQ-019, STK-REQ-042

**Design element:** Communication Task Architecture

**Verification:** TEST-030

**Test:**

1. Establish normal sensor communication.
2. Confirm valid measurements.
3. Disconnect RS485-2.
4. Continue transmitting sensor measurements.
5. Reconnect RS485-2.
6. Read measurement from CORE.

**Expected result:**

Sensor acquisition continues during CORE communication loss.

**Result:** PASS

---

# 12. Recovery Traceability

### REQ-MOD-030

**Requirement:**

> Following restoration of sensor communication, the module shall automatically resume acquisition and validation of sensor measurements.

**Source:** STK-REQ-013, STK-REQ-041

**Design element:** Sensor Communication Manager

**Verification:** TEST-031

**Test:**

```text
Normal operation
      |
Sensor disconnected
      |
Communication timeout
      |
Sensor unavailable
      |
Sensor reconnected
      |
Automatic recovery
      |
Valid measurement acquired
```

**Result:** PASS

---

# 13. Startup Traceability

### REQ-MOD-040

**Requirement:**

> After power-up, the module shall indicate that no valid measurement is available until a valid sensor measurement has been received.

**Source:** STK-REQ-024

**Design element:** Startup State Manager

**Verification:** TEST-040

**Test sequence:**

1. Power module.
2. Do not provide sensor data.
3. Read measurement status.
4. Verify invalid/unavailable status.
5. Provide valid sensor frame.
6. Read measurement status.
7. Verify valid status.

**Result:** PASS

---

# 14. Diagnostic Traceability

### REQ-DIAG-001

**Requirement:**

> The module shall provide a diagnostic indication when sensor communication is lost.

**Source:** STK-REQ-026, STK-REQ-028

**Design element:** Diagnostic Manager

**Verification:** TEST-050

**Result:** PASS

---

### REQ-DIAG-002

**Requirement:**

> The module shall maintain a counter of detected invalid sensor CRCs.

**Source:** STK-REQ-027, STK-REQ-030

**Design element:** Diagnostic Manager

**Verification:** TEST-051

**Test:**

1. Start CRC counter at zero.
2. Send valid frame.
3. Send invalid CRC frame.
4. Read counter.
5. Repeat three times.

**Expected result:**

Counter increments once for each detected CRC error.

**Result:** PASS

---

### REQ-DIAG-003

**Requirement:**

> The module shall provide its firmware version through the defined diagnostic interface.

**Source:** STK-REQ-029

**Design element:** Firmware Information Manager

**Verification:** TEST-052

**Result:** PASS

---

# 15. Hardware Traceability

### REQ-HW-001

**Requirement:**

> The module shall be mechanically compatible with the target DIN-rail installation.

**Source:** STK-REQ-034

**Design element:** Mechanical enclosure

**Verification:** INS-001

**Verification:** Dimensional inspection.

**Result:** PASS

---

### REQ-HW-002

**Requirement:**

> The module shall operate from a 24 VDC nominal supply within the specified operating voltage range.

**Source:** STK-REQ-035

**Design element:** Power Supply Circuit

**Verification:** TEST-HW-001

**Test range:**

| Supply condition          | Expected         |
| ------------------------- | ---------------- |
| Minimum specified voltage | Normal operation |
| Nominal voltage           | Normal operation |
| Maximum specified voltage | Normal operation |

**Result:** PASS

---

### REQ-HW-003

**Requirement:**

> The module shall provide electrically independent RS485-1 and RS485-2 communication interfaces.

**Source:** STK-REQ-036

**Design element:** RS485 Transceivers

**Verification:** TEST-HW-002

**Result:** PASS

---

# 16. Environmental Traceability

### REQ-ENV-001

**Requirement:**

> The module shall operate within an ambient temperature range of 0 °C to 50 °C.

**Source:** STK-REQ-047

**Design element:** Complete module

**Verification:** TEST-ENV-001

**Verification method:** Environmental test.

**Result:** PASS

**Note:**
The temperature range is fictional for this example.

---

# 17. Performance Traceability

### REQ-PERF-001

**Requirement:**

> The module shall support a minimum valid measurement update rate of one measurement per second.

**Source:** STK-REQ-038

**Design element:** Sensor Communication Manager

**Verification:** TEST-PERF-001

**Result:** PASS

---

### REQ-PERF-002

**Requirement:**

> A successfully received valid sensor measurement shall become available through the CORE interface within 500 ms.

**Source:** STK-REQ-039

**Design element:** Measurement Data Manager / Modbus Register Manager

**Verification:** TEST-PERF-002

**Result:** PASS

---

### REQ-PERF-003

**Requirement:**

> The module shall respond to a valid Modbus request within 100 ms.

**Source:** STK-REQ-040

**Design element:** Modbus Slave Stack

**Verification:** TEST-PERF-003

**Result:** PASS

---

# 18. Bidirectional Traceability

The RTM shall be reviewed in both directions.

## 18.1 Forward Traceability

Starting from stakeholder needs:

```text
SN-001
  ↓
STK-REQ-001
  ↓
REQ-MOD-001
  ↓
TEST-001
  ↓
PASS
```

This answers:

> "Did we implement and verify what the stakeholder asked for?"

---

## 18.2 Backward Traceability

Starting from a module requirement:

```text
REQ-MOD-006
  ↓
STK-REQ-006
  ↓
SN-003
```

This answers:

> "Why does this requirement exist?"

If a module requirement cannot be traced to a legitimate source, it should be reviewed.

---

# 19. Verification Coverage

The following summary provides an example of requirement verification coverage.

| Requirement category |  Total | Verified |  Open | Coverage |
| -------------------- | -----: | -------: | ----: | -------: |
| Functional           |     15 |       15 |     0 |     100% |
| Interface            |      8 |        8 |     0 |     100% |
| Diagnostics          |      6 |        6 |     0 |     100% |
| Hardware             |      5 |        5 |     0 |     100% |
| Performance          |      3 |        3 |     0 |     100% |
| Environmental        |      3 |        3 |     0 |     100% |
| **Total**            | **40** |   **40** | **0** | **100%** |

This table is illustrative only.

In a real project, "100% coverage" should be based on the actual approved requirements and completed verification evidence.

---

# 20. Orphan Analysis

An important RTM activity is identifying "orphans."

## 20.1 Orphan Requirements

A requirement is an orphan if it has no identifiable source.

Example:

```text
REQ-MOD-099
"The module shall store 100 measurements."
```

If nobody requested historical storage and no higher-level requirement requires it, the requirement may be unnecessary.

It should either:

* be traced to a valid source;
* be justified as a derived engineering requirement;
* or be removed.

---

## 20.2 Uncovered Requirements

A requirement is uncovered if it has no verification method.

Example:

```text
REQ-MOD-015
"The module shall recover from sensor communication loss."
```

If there is no:

```text
TEST-xxx
```

linked to it, the RTM identifies a verification gap.

---

## 20.3 Uncovered Stakeholder Needs

Example:

```text
SN-007
Service personnel need sufficient information
to distinguish sensor and module faults.
```

If no stakeholder requirement traces back to SN-007, then the stakeholder need has been lost during requirements derivation.

This is exactly the kind of problem the RTM is designed to reveal.

---

# 21. Change Impact Example

Suppose the system architect changes:

> "The maximum acceptable measurement latency is 500 ms."

to:

> "The maximum acceptable measurement latency is 200 ms."

The RTM allows the impact to be followed:

```text
STK-REQ-039
      ↓
REQ-PERF-002
      ↓
Measurement Data Manager
      ↓
Modbus Register Manager
      ↓
TEST-PERF-002
      ↓
Performance test configuration
```

Therefore, changing one stakeholder requirement potentially affects:

* firmware timing;
* task scheduling;
* buffering;
* Modbus response handling;
* performance tests;
* acceptance criteria.

This is much more useful than simply changing "500 ms" in one document.

---

# 22. Requirement Change Control

Any change to an approved requirement shall be evaluated for impact on:

* parent stakeholder requirements;
* derived module requirements;
* hardware;
* firmware;
* software;
* interfaces;
* mechanical design;
* safety;
* diagnostics;
* verification tests;
* validation tests;
* documentation;
* production;
* service procedures.

Example:

| Change                  | Affected requirements     | Affected design      | Affected tests |
| ----------------------- | ------------------------- | -------------------- | -------------- |
| Stale timeout 5 s → 2 s | STK-REQ-010, REQ-MOD-011  | Freshness Monitor    | TEST-011       |
| Modbus address changed  | STK-REQ-016, REQ-IF-001   | Modbus configuration | TEST-020       |
| New diagnostic counter  | STK-REQ-030, REQ-DIAG-002 | Diagnostic Manager   | TEST-051       |
| Supply range changed    | STK-REQ-035, REQ-HW-002   | Power Supply         | TEST-HW-001    |

---

# 23. Final RTM Acceptance Criteria

The RTM shall be considered complete when:

1. Every stakeholder need has at least one stakeholder requirement.
2. Every stakeholder requirement is traced to one or more module requirements.
3. Every module requirement has a legitimate source.
4. Every module requirement has a defined verification method.
5. Every verification test traces to one or more requirements.
6. No requirement remains without verification coverage.
7. No test exists without a requirement or justified verification objective.
8. Safety-related requirements have dedicated verification evidence.
9. Interface requirements have dedicated interface verification.
10. Performance requirements have quantitative acceptance criteria.
11. Open/TBD requirements are explicitly identified.
12. Requirement changes can be traced to affected design and verification artifacts.

---

# 24. Example Final Traceability Chain

For the most important function of this module, the complete chain could look like this:

```text
STAKEHOLDER
System needs reliable ozone measurement
        │
        ▼
SN-003
Invalid sensor data shall not replace valid data
        │
        ▼
STK-REQ-006
Module shall not update stored measurement
when received sensor message is invalid
        │
        ▼
REQ-MOD-006
Module shall reject invalid frames and retain
the previously accepted measurement
        │
        ▼
DESIGN
Frame Validation Manager
+
Measurement Data Manager
        │
        ▼
TEST-006
Valid measurement → corrupt frame
        │
        ▼
EXPECTED
Previous valid value remains unchanged
        │
        ▼
RESULT
PASS
```

That is the essence of requirements traceability.

---

# 25. Four-Document Workflow

The complete documentation structure is therefore:

### Document 1 — Stakeholder Register

**Who cares about the product?**

```text
System Architect
CORE Engineer
Sensor Engineer
Service Engineer
...
```

↓

### Document 2 — Stakeholder Requirement Matrix

**What do we need to ask them?**

```text
What happens if the sensor disconnects?
How fresh must the measurement be?
What does CORE need to know?
How should faults be indicated?
...
```

↓

### Document 3 — Module Requirements Specification

**What exactly must the module do?**

```text
REQ-MOD-001
REQ-MOD-002
REQ-IF-001
REQ-HW-001
REQ-PERF-001
...
```

↓

### Document 4 — Requirements Traceability Matrix

**Can we prove that everything requested was implemented and verified?**

```text
Stakeholder Need
      ↓
Stakeholder Requirement
      ↓
Module Requirement
      ↓
Design
      ↓
Verification
      ↓
Result
```

---

# 26. Key Principle

The RTM should not become a second copy of the requirements specification.

Its purpose is **traceability**, not specification.

A good RTM should allow someone to take any important statement and answer four questions quickly:

> **Why do we need this?**

→ Stakeholder need / requirement

> **What does the module do about it?**

→ Module requirement

> **Where is it implemented?**

→ Design / implementation element

> **How do we know it works?**

→ Verification activity and result

If those four questions can be answered for every requirement, your requirements chain is under control.

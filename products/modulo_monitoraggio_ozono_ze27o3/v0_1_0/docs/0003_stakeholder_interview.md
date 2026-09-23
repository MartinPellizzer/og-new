## STK-007/008 — System Architect / System Engineer

| Field                 | Purpose                                                          |
| --------------------- | ---------------------------------------------------------------- |
| Answer ID             | Unique identifier                                                |
| Question ID           | Link to original question                                        |
| Stakeholder           | Who answered                                                     |
| Date                  | When answer was obtained                                         |
| Interviewer           | Who collected it                                                 |
| Question              | Exact question asked                                             |
| Stakeholder Answer    | What they actually said                                          |
| Clarification         | Additional discussion                                            |
| Interpretation        | Your engineering interpretation                                  |
| Requirement Candidate | Possible requirement derived from answer                         |
| Priority              | MUST / SHOULD / COULD / TBD                                      |
| Source Type           | Requirement / constraint / assumption / preference / information |
| Open Issue            | Anything unresolved                                              |
| Follow-up             | What must be clarified                                           |
| Final Disposition     | Accepted / rejected / TBD / converted to requirement             |
| Requirement ID        | Link to eventual STK-REQ                                         |
| Notes                 | Anything else                                                    |


| Field              | Example                                                                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Answer ID          | ANS-PROC-010-001                                                                                                                                            |
| Question ID        | PROC-10                                                                                                                                                     |
| Stakeholder        | STK-070 Ozone Process Engineer                                                                                                                              |
| Date               | 2026-09-21                                                                                                                                                  |
| Question           | How long can the system continue using the last valid ozone measurement if no new measurement is received?                                                  |
| Stakeholder Answer | "We don't want the controller to keep using it indefinitely. Five seconds is acceptable because the process doesn't change significantly faster than that." |
| Clarification      | Stakeholder confirmed that 5 s is the maximum acceptable age for normal operation.                                                                          |
| Interpretation     | Measurement older than 5 s should not be considered current.                                                                                                |
| Type               | System requirement candidate                                                                                                                                |
| Priority           | MUST                                                                                                                                                        |
| Open Issue         | Confirm with Functional Safety and System Architect.                                                                                                        |
| Follow-up          | Verify whether 5 s is also acceptable for safety-related behavior.                                                                                          |
| Disposition        | Candidate for stakeholder requirement                                                                                                                       |
| Requirement ID     | STK-REQ-010                                                                                                                                                 |
| Notes              | Value is provisional until cross-stakeholder agreement.                                                                                                     |


### SYS-01 — What is the overall purpose of the system?

| Field              | Example                                                                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Answer ID          | ANS-SYS-001-001                                                                                                                                             |
| Question ID        | SYS-01                                                                                                                                                      |
| Stakeholder        | STK-007/008 - System Architect / System Engineer                                                                                                            |
| Date               | 2026-09-21                                                                                                                                                  |
| Question           | What is the overall purpose of the system?                                                                                                                  |
| Stakeholder Answer | "We don't want the controller to keep using it indefinitely. Five seconds is acceptable because the process doesn't change significantly faster than that." |
| Clarification      | Stakeholder confirmed that 5 s is the maximum acceptable age for normal operation.                                                                          |
| Interpretation     | Measurement older than 5 s should not be considered current.                                                                                                |
| Type               | System requirement candidate                                                                                                                                |
| Priority           | MUST                                                                                                                                                        |
| Open Issue         | Confirm with Functional Safety and System Architect.                                                                                                        |
| Follow-up          | Verify whether 5 s is also acceptable for safety-related behavior.                                                                                          |
| Disposition        | Candidate for stakeholder requirement                                                                                                                       |
| Requirement ID     | STK-REQ-010                                                                                                                                                 |
| Notes              | Value is provisional until cross-stakeholder agreement.                                                                                                     |

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


Yes — that is an important missing layer.

You currently have:

**1. Stakeholder Register** → who do we need?
**2. Stakeholder Requirement Matrix** → what do we ask them?
**3. ???** → what did they actually answer?
**4. Stakeholder Requirements Specification** → what requirements did we derive?
**5. Module Requirements Specification** → what must the module technically do?
**6. RTM** → can we trace and verify everything?

I would **not put the raw answers directly into the Stakeholder Requirements Specification**. Keep the interview evidence separate.

The clean structure is:

```text
STAKEHOLDER REGISTER
        │
        ▼
STAKEHOLDER QUESTIONNAIRE / MATRIX
        │
        ▼
STAKEHOLDER INTERVIEW RECORDS        ← missing layer
        │
        ▼
STAKEHOLDER REQUIREMENTS SPECIFICATION
        │
        ▼
MODULE REQUIREMENTS SPECIFICATION
        │
        ▼
RTM
```

## The missing document: Stakeholder Interview / Elicitation Record

I recommend creating **one document called:**

> **Stakeholder Elicitation & Interview Record**

rather than creating a completely separate document for every stakeholder.

However, inside it, have **one section per stakeholder interview**.

For your project, it could look like:

```text
Stakeholder Elicitation & Interview Record
│
├── 1. Document information
├── 2. Interview methodology
├── 3. STK-007/008 System Architect / System Engineer
├── 4. STK-011/012 CORE Firmware / Software
├── 5. STK-017/018/019 Sensor / Instrumentation
├── 6. STK-070 Ozone Process Engineer
├── 7. STK-013 Module Firmware
├── 8. STK-014 Module Hardware
├── 9. STK-020/021 Electrical / Cabinet
├── 10. STK-025 Functional Safety
├── 11. STK-031/033 Verification / Test
├── 12. STK-043/045 Service / Maintenance
└── 13. Cross-stakeholder findings
```

The critical thing is that this document should preserve **what the stakeholder actually said**, rather than immediately interpreting it as a requirement.

---

# 1. What should you record for every answer?

I would use a table like this:

| Field                 | Purpose                                                          |
| --------------------- | ---------------------------------------------------------------- |
| Answer ID             | Unique identifier                                                |
| Question ID           | Link to original question                                        |
| Stakeholder           | Who answered                                                     |
| Date                  | When answer was obtained                                         |
| Interviewer           | Who collected it                                                 |
| Question              | Exact question asked                                             |
| Stakeholder Answer    | What they actually said                                          |
| Clarification         | Additional discussion                                            |
| Interpretation        | Your engineering interpretation                                  |
| Requirement Candidate | Possible requirement derived from answer                         |
| Priority              | MUST / SHOULD / COULD / TBD                                      |
| Source Type           | Requirement / constraint / assumption / preference / information |
| Open Issue            | Anything unresolved                                              |
| Follow-up             | What must be clarified                                           |
| Final Disposition     | Accepted / rejected / TBD / converted to requirement             |
| Requirement ID        | Link to eventual STK-REQ                                         |
| Notes                 | Anything else                                                    |

The most important separation is:

**Answer ≠ Requirement**

For example:

> "We don't want the machine to use an old ozone value if the sensor has stopped communicating."

That is an **answer / stakeholder statement**.

It isn't yet necessarily the final wording of the requirement.

You might interpret it as:

> The system must distinguish a current measurement from an obsolete measurement.

Then derive:

> **STK-REQ-010:** The system shall indicate the ozone measurement as stale when no valid sensor measurement has been received within the defined freshness interval.

And only later derive the technical module requirements.

---

# 2. Example using your ozone module

Let's take one of the questions from the matrix.

### Question

**PROC-10**

> How long can the system continue using the last valid ozone measurement if no new measurement is received?

Suppose the Ozone Process Engineer answers:

> "We don't want the controller to keep using it indefinitely. Five seconds is acceptable because the process doesn't change significantly faster than that."

Don't immediately write:

> `STK-REQ-010: stale after 5 seconds`

Instead, record the actual interview information first.

### Interview record

| Field              | Example                                                                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Answer ID          | ANS-PROC-010-001                                                                                                                                            |
| Question ID        | PROC-10                                                                                                                                                     |
| Stakeholder        | STK-070 Ozone Process Engineer                                                                                                                              |
| Date               | 2026-09-21                                                                                                                                                  |
| Question           | How long can the system continue using the last valid ozone measurement if no new measurement is received?                                                  |
| Stakeholder Answer | "We don't want the controller to keep using it indefinitely. Five seconds is acceptable because the process doesn't change significantly faster than that." |
| Clarification      | Stakeholder confirmed that 5 s is the maximum acceptable age for normal operation.                                                                          |
| Interpretation     | Measurement older than 5 s should not be considered current.                                                                                                |
| Type               | System requirement candidate                                                                                                                                |
| Priority           | MUST                                                                                                                                                        |
| Open Issue         | Confirm with Functional Safety and System Architect.                                                                                                        |
| Follow-up          | Verify whether 5 s is also acceptable for safety-related behavior.                                                                                          |
| Disposition        | Candidate for stakeholder requirement                                                                                                                       |
| Requirement ID     | STK-REQ-010                                                                                                                                                 |
| Notes              | Value is provisional until cross-stakeholder agreement.                                                                                                     |

Now you have an **auditable record** of how the requirement came about.

---

# 3. You should distinguish different types of answers

This is extremely useful.

Not every answer produces a requirement.

I'd classify every answer into one of these categories:

### A. Requirement

The stakeholder is defining something the system/module must do.

Example:

> "CORE must know whether the measurement is stale."

→ **Requirement candidate**

---

### B. Constraint

Something the design must work within.

Example:

> "The module has to fit into a 22.5 mm DIN-rail position."

→ **Constraint**

---

### C. Interface definition

Something defining interaction with another system.

Example:

> "CORE communicates using Modbus RTU."

→ **Interface requirement/input**

---

### D. Preference

Something the stakeholder would like but which isn't necessarily mandatory.

Example:

> "It would be nice if the LED showed the sensor state."

→ **Preference / SHOULD candidate**

---

### E. Assumption

Something believed to be true but not yet verified.

Example:

> "The cabinet already provides 24 VDC."

→ **Assumption**

This is particularly important because assumptions can become nasty project risks later.

---

### F. Information

Useful information that does not directly become a requirement.

Example:

> "We've had problems with RS485 communication on another product."

→ **Engineering information / lesson learned**

This might influence design, but it isn't itself a requirement.

---

### G. Open issue

The stakeholder doesn't know or stakeholders disagree.

Example:

> "We're not sure whether the Modbus address should be fixed or configurable."

→ **Open issue / TBD**

---

### H. Out of scope

The stakeholder explicitly says something is not required.

Example:

> "The module doesn't need to store historical measurements."

→ **Scope exclusion**

These classifications will make your requirements process much cleaner.

---

# 4. I would add an "Answer Disposition" table

At the end of each stakeholder interview, summarize what happened to their answers.

For example:

| Answer ID        | Topic                 | Classification | Action                        | Result      |
| ---------------- | --------------------- | -------------- | ----------------------------- | ----------- |
| ANS-PROC-010-001 | Measurement freshness | Requirement    | Derive requirement            | STK-REQ-010 |
| ANS-PROC-011-001 | Filtering             | Open issue     | Discuss with System Architect | TBD         |
| ANS-PROC-012-001 | Historical data       | Out of scope   | Record exclusion              | OUT-005     |
| ANS-PROC-013-001 | Process dynamics      | Information    | Engineering input             | Note        |
| ANS-PROC-014-001 | Alarm behavior        | Requirement    | Cross-check with safety       | STK-REQ-XXX |

This gives you a very nice bridge between the **interviews** and the **Stakeholder Requirements Specification**.

---

# 5. Don't lose disagreements

This is one of the most important reasons to have this document.

Imagine:

### Ozone Process Engineer

> "Five seconds stale is acceptable."

But:

### Functional Safety Engineer

> "Five seconds is too long for the safety function."

You **should not silently resolve this** by choosing one.

Record both:

| Stakeholder              | Answer                                 |
| ------------------------ | -------------------------------------- |
| STK-070 Process Engineer | 5 s acceptable                         |
| STK-025 Safety Engineer  | 5 s not acceptable for safety function |

Then create:

> **OPEN-023: Define freshness requirement for normal process control and safety-related functions.**

This may eventually lead to two different requirements.

For example:

```text
Normal process data:
Maximum age = 5 s

Safety-related validity:
Maximum detection time = 1 s
```

That is much better than accidentally mixing two different concepts into one "stale timeout."

---

# 6. Keep the original answer

I strongly recommend having **both**:

> **Stakeholder Answer**

and

> **Engineering Interpretation**

as separate fields.

For example:

**Stakeholder Answer**

> "If the sensor stops talking, the operator needs to know."

**Engineering Interpretation**

> The system needs a diagnostic indication for loss of sensor communication.

Why?

Because six months later somebody might challenge:

> "Why did we create this requirement?"

You can go:

```text
REQ-MOD-023
     ↓
STK-REQ-031
     ↓
ANS-SERV-007
     ↓
SERV-07
     ↓
Service Engineer
```

and see exactly where it came from.

---

# 7. I would actually use three layers for the answers

For a serious engineering project, I would structure the missing layer like this:

## 3A — Interview Record

Contains the **raw information**.

```text
Question
Answer
Clarification
Who said it
When
Context
```

This is your evidence.

---

## 3B — Answer Analysis / Disposition

Contains your engineering processing.

```text
Answer
↓
Requirement?
Constraint?
Assumption?
Preference?
Information?
Open issue?
Out of scope?
↓
Action
```

This is your analysis.

---

## 3C — Stakeholder Requirements

Contains only the **approved, cleaned-up requirements**.

```text
STK-REQ-001
STK-REQ-002
STK-REQ-003
...
```

This is your controlled requirements baseline.

That separation is excellent for avoiding "requirement contamination."

---

# 8. The complete document set I'd use

So I'd slightly modify our original four-document architecture.

### Document 01 — Stakeholder Register

**Purpose:** Who are the stakeholders?

```text
STK-001 Customer
STK-007 System Architect
STK-011 CORE Engineer
...
```

---

### Document 02 — Stakeholder Requirement Matrix

**Purpose:** What do we ask them?

```text
SYS-01
SYS-02
...
CORE-01
CORE-02
...
```

---

### Document 03 — Stakeholder Elicitation & Interview Record

**Purpose:** What did they actually tell us?

```text
Question
↓
Answer
↓
Clarification
↓
Classification
↓
Interpretation
↓
Open issues
↓
Requirement candidate
```

This is the document you were missing.

---

### Document 04 — Stakeholder Requirements Specification

**Purpose:** What does the organization formally require?

```text
STK-REQ-001
STK-REQ-002
...
```

These should be clean, atomic, unambiguous, and testable.

---

### Document 05 — Module Requirements Specification

**Purpose:** What exactly must our module do?

```text
REQ-MOD-001
REQ-MOD-002
REQ-IF-001
REQ-HW-001
...
```

---

### Document 06 — Requirements Traceability Matrix

**Purpose:** Can we trace everything from origin to verification?

```text
Stakeholder
   ↓
Need
   ↓
Stakeholder Requirement
   ↓
Module Requirement
   ↓
Design
   ↓
Test
   ↓
Result
```

So although we originally called it the **"four-document workflow,"** I would actually use **six artifacts** for a disciplined engineering project.

The two additional ones that make the process much stronger are:

**03 — Stakeholder Elicitation & Interview Record**

and, if the project is large enough,

**an explicit Stakeholder Requirements Specification** rather than jumping straight from interview answers to module requirements.

---

## One practical recommendation

For your particular project, I would make **Document 03 an Excel workbook rather than a Word document**.

Something like:

```text
Stakeholder_Elicitation.xlsx

[01_Interview_Index]
[02_System_Architect]
[03_CORE]
[04_Sensor]
[05_Ozone_Process]
[06_Module_Firmware]
[07_Module_Hardware]
[08_Electrical_Cabinet]
[09_Safety]
[10_Verification]
[11_Service]
[12_Open_Issues]
[13_Answer_Disposition]
```

Then your actual requirements documents remain controlled Word/PDF documents, while the interview workbook acts as the **requirements evidence database**.

That gives you a very clean chain:

**"What did we ask?" → "What did they say?" → "What did we decide it means?" → "What requirement did we create?" → "How did we implement and verify it?"**

That's the structure I'd recommend for your ozone module project.

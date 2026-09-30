| ID          | Stakeholder / Role                           | Category            | Relationship with module                                 | Potential requirement areas                                     |
| ----------- | -------------------------------------------- | ------------------- | -------------------------------------------------------- | --------------------------------------------------------------- |
| **STK-001** | Customer / End Customer                      | Business            | Uses the overall ozone system                            | Functional expectations, availability, diagnostics, maintenance |
| **STK-002** | System Owner / Plant Owner                   | Business            | Owns/operates the installation                           | Availability, lifecycle, maintenance, safety                    |
| **STK-003** | System Operator                              | Operations          | Operates the ozone system                                | Status information, alarms, usability                           |
| **STK-004** | System Integrator                            | System              | Integrates the ozone system into a larger installation   | Interfaces, communication, configuration                        |
| **STK-005** | Project Manager                              | Project             | Responsible for project delivery                         | Scope, schedule, cost, milestones                               |
| **STK-006** | Product Manager                              | Product             | Defines product-level expectations                       | Features, variants, lifecycle, cost                             |
| **STK-007** | System Architect                             | Engineering         | Defines overall system architecture                      | Module responsibilities, interfaces, dependencies               |
| **STK-008** | System Engineer                              | Engineering         | Derives module requirements from system requirements     | Functional and system requirements                              |
| **STK-009** | Application Engineer                         | Engineering         | Defines how the module is used in the application        | Operating modes, data, system behavior                          |
| **STK-010** | Controls / Automation Engineer               | Engineering         | Defines control-system interaction                       | CORE interface, timing, states, alarms                          |
| **STK-011** | CORE Firmware Engineer                       | Software            | Develops the master communicating with the module        | Modbus, registers, timing, errors                               |
| **STK-012** | CORE Software Engineer                       | Software            | Uses module data in application logic                    | Data semantics, validity, diagnostics                           |
| **STK-013** | Module Firmware Engineer                     | Software            | Implements the module firmware                           | Functional behavior, state machine, error handling              |
| **STK-014** | Module Hardware Engineer                     | Hardware            | Designs the module electronics                           | MCU, RS485, power, protection, EMC                              |
| **STK-015** | Electronics Architect                        | Hardware            | Defines electronic architecture                          | Interfaces, isolation, component strategy                       |
| **STK-016** | PCB Designer                                 | Hardware            | Designs PCB implementation                               | Layout, connectors, EMC, manufacturability                      |
| **STK-017** | Sensor / Instrumentation Engineer            | Sensor              | Defines ZE27-O3 integration                              | Sensor protocol, measurement, errors, timing                    |
| **STK-018** | Sensor Supplier / Manufacturer               | External            | Provides sensor specifications                           | Protocol, electrical, environmental limits                      |
| **STK-019** | Sensor Application Specialist                | External/Technical  | Provides practical sensor integration knowledge          | Startup, calibration, failure modes                             |
| **STK-020** | Electrical Engineer                          | Electrical          | Defines electrical integration                           | Power, wiring, grounding, protection                            |
| **STK-021** | Control Cabinet Designer                     | Electrical          | Integrates module into cabinet                           | DIN rail, terminals, wiring, accessibility                      |
| **STK-022** | Mechanical Engineer                          | Mechanical          | Defines mechanical integration                           | Dimensions, mounting, thermal constraints                       |
| **STK-023** | Thermal Engineer                             | Engineering         | Assesses heat dissipation                                | Temperature, power dissipation                                  |
| **STK-024** | EMC Engineer                                 | Compliance          | Defines EMC requirements                                 | Emissions, immunity, RS485 behavior                             |
| **STK-025** | Functional Safety Engineer                   | Safety              | Defines safety-related behavior                          | Safe state, fault behavior, diagnostics                         |
| **STK-026** | HSE / EHS Engineer                           | Safety              | Considers operator/environmental safety                  | Hazard-related behavior                                         |
| **STK-027** | Cybersecurity Engineer                       | Security            | Assesses communication/security risks                    | Interfaces, access, firmware/configuration                      |
| **STK-028** | Regulatory / Compliance Engineer             | Compliance          | Defines applicable regulations                           | Standards, certification, compliance                            |
| **STK-029** | Certification Engineer / Laboratory          | Compliance          | Performs external/internal certification                 | EMC, safety, environmental tests                                |
| **STK-030** | Quality Engineer                             | Quality             | Ensures requirements and processes are controlled        | Traceability, acceptance criteria                               |
| **STK-031** | Verification Engineer                        | V&V                 | Defines requirement verification                         | Testability, acceptance criteria                                |
| **STK-032** | Validation Engineer                          | V&V                 | Validates module/system behavior                         | System-level behavior                                           |
| **STK-033** | Test Engineer                                | V&V                 | Implements module tests                                  | Functional, communication, fault tests                          |
| **STK-034** | Test Automation Engineer                     | V&V                 | Automates testing                                        | Interfaces, diagnostics, test hooks                             |
| **STK-035** | Manufacturing Engineer                       | Manufacturing       | Defines production process                               | Programming, configuration, EOL testing                         |
| **STK-036** | Production Technician                        | Manufacturing       | Builds and tests physical modules                        | Assembly, connectors, configuration                             |
| **STK-037** | Production Test Engineer                     | Manufacturing       | Defines production test                                  | EOL test, programming, diagnostics                              |
| **STK-038** | Supply Chain / Procurement                   | Supply Chain        | Sources components                                       | Availability, lifecycle, approved components                    |
| **STK-039** | Component Engineer                           | Hardware/Supply     | Controls component selection                             | Obsolescence, qualification, alternatives                       |
| **STK-040** | PCB / Electronics Manufacturer               | Supplier            | Manufactures electronics                                 | DFM, testability, production constraints                        |
| **STK-041** | Mechanical Manufacturer                      | Supplier            | Manufactures enclosure/mechanical parts                  | Mechanical tolerances, materials                                |
| **STK-042** | Assembly Supplier                            | Supplier            | May assemble the module                                  | Assembly and test requirements                                  |
| **STK-043** | Service Engineer                             | Service             | Maintains systems in field                               | Diagnostics, replacement, troubleshooting                       |
| **STK-044** | Field Service Technician                     | Service             | Physically interacts with module                         | Accessibility, LEDs, connectors, replacement                    |
| **STK-045** | Maintenance Engineer                         | Maintenance         | Defines maintenance strategy                             | Failure detection, replacement, serviceability                  |
| **STK-046** | Technical Support Engineer                   | Support             | Supports customers remotely                              | Diagnostics, logs, error information                            |
| **STK-047** | Reliability Engineer                         | Reliability         | Assesses reliability                                     | MTBF, failure modes, lifetime                                   |
| **STK-048** | RAMS Engineer                                | Reliability/Safety  | Assesses reliability/availability/maintainability/safety | Failure behavior, availability, maintenance                     |
| **STK-049** | Configuration Manager                        | Configuration       | Controls product configurations                          | Firmware versions, parameters, Modbus address                   |
| **STK-050** | Release Manager                              | Product/Software    | Controls releases                                        | Version compatibility, update process                           |
| **STK-051** | Firmware Update / Bootloader Engineer        | Software            | Defines firmware update mechanism                        | Update, recovery, rollback                                      |
| **STK-052** | Documentation Engineer                       | Documentation       | Documents module/system                                  | Manuals, specifications, troubleshooting                        |
| **STK-053** | Technical Writer                             | Documentation       | Produces user/service documentation                      | Installation and maintenance information                        |
| **STK-054** | Training / Service Training Engineer         | Support             | Trains service personnel                                 | Diagnostics, replacement, configuration                         |
| **STK-055** | Spare Parts / Logistics Manager              | Logistics           | Manages replacement modules                              | Part numbers, interchangeability, packaging                     |
| **STK-056** | Product Lifecycle Manager                    | Product             | Manages long-term product support                        | Obsolescence, revisions, compatibility                          |
| **STK-057** | Change Control Board                         | Governance          | Approves technical changes                               | Change impact, compatibility                                    |
| **STK-058** | Project Quality Manager                      | Quality             | Oversees project quality                                 | Reviews, traceability, deviations                               |
| **STK-059** | Legal / Regulatory Affairs                   | Business/Compliance | Assesses legal/regulatory obligations                    | Product compliance, documentation                               |
| **STK-060** | Certification / Notified Body Representative | External            | May assess compliance                                    | Certification requirements                                      |
| **STK-061** | Customer Service / After-Sales               | Business            | Handles customer issues                                  | Diagnostics, replacement, compatibility                         |
| **STK-062** | Sales / Technical Sales                      | Business            | Communicates product capabilities                        | Supported configurations, limitations                           |
| **STK-063** | IT / Infrastructure Engineer                 | IT                  | May support production/service infrastructure            | Programming, diagnostics, connectivity                          |
| **STK-064** | Manufacturing IT / MES Engineer              | Manufacturing IT    | Integrates production testing                            | Traceability, test data, serial numbers                         |
| **STK-065** | Supplier Quality Engineer                    | Supplier Quality    | Controls external suppliers                              | Component/module quality                                        |
| **STK-066** | Environmental / Sustainability Engineer      | Compliance          | Assesses environmental requirements                      | RoHS, REACH, materials, lifecycle                               |
| **STK-067** | Installation Engineer                        | Installation        | Installs system in customer environment                  | Wiring, commissioning, configuration                            |
| **STK-068** | Commissioning Engineer                       | Installation        | Starts and verifies system                               | Startup, diagnostics, calibration                               |
| **STK-069** | Calibration / Metrology Engineer             | Instrumentation     | Defines measurement quality                              | Accuracy, calibration, traceability                             |
| **STK-070** | Ozone Process Engineer                       | Domain Expert       | Defines meaning/use of ozone measurement                 | Measurement range, process requirements                         |
| **STK-071** | Process Control Engineer                     | Domain Expert       | Uses ozone measurement for process control               | Sampling rate, validity, response time                          |
| **STK-072** | Risk / Hazard Analysis Engineer              | Safety              | Performs system risk analysis                            | Failure modes, hazardous states                                 |
| **STK-073** | FMEA / DFMEA Owner                           | Quality/Safety      | Analyzes module failure modes                            | Detection, severity, occurrence, recovery                       |
| **STK-074** | Internal Auditor                             | Quality             | May audit development process                            | Traceability, documentation, compliance                         |
| **STK-075** | External Auditor / Customer Auditor          | External            | May audit product/process                                | Evidence, records, compliance                                   |


| ID          | Stakeholder                             | Why it matters                                             |
| ----------- | --------------------------------------- | ---------------------------------------------------------- |
| **STK-076** | ZE27-O3 datasheet/specification         | Defines sensor interface and behavior                      |
| **STK-077** | Modbus specification                    | Defines CORE/module communication behavior                 |
| **STK-078** | Applicable product standards            | May impose electrical/EMC/safety requirements              |
| **STK-079** | Customer specifications                 | May impose additional interface or diagnostic requirements |
| **STK-080** | Existing system architecture            | Constrains module interfaces and behavior                  |
| **STK-081** | Existing CORE implementation            | May impose practical communication constraints             |
| **STK-082** | Existing cabinet architecture           | Constrains mechanical/electrical integration               |
| **STK-083** | Existing service procedures             | May impose diagnostic/replacement requirements             |
| **STK-084** | Existing production test infrastructure | May constrain testability and interfaces                   |
| **STK-085** | Existing module/product family          | May impose reuse/compatibility requirements                |

## INTERVIEW

Tier 1 — Must consult
- System Architect / System Engineer
- CORE Firmware Engineer
- Sensor / Instrumentation Engineer
- Ozone Process Engineer
- Module Firmware Engineer
- Module Hardware Engineer
- Electrical / Control Cabinet Engineer
- Functional Safety Engineer
- Verification / Test Engineer
- Service / Maintenance Engineer

Tier 2 — Consult during definition
- Mechanical Engineer
- EMC Engineer
- Quality Engineer
- Manufacturing Engineer
- Reliability Engineer
- Calibration / Metrology Engineer
- Cybersecurity Engineer
- Product Manager
- Configuration / Release Manager
- Installation / Commissioning Engineer

Tier 3 — Consult if applicable
- Customer / System Integrator
- Regulatory / Compliance Engineer
- Certification laboratory
- Supply Chain / Component Engineer
- Production Test Engineer
- Technical Support
- Documentation
- Product Lifecycle
- Customer Service
- Procurement

## STAKEHOLDER

| Field                            | Purpose                                  |
| -------------------------------- | ---------------------------------------- |
| **Stakeholder ID**               | Unique identifier                        |
| **Role**                         | E.g. CORE Firmware Engineer              |
| **Name**                         | Actual person, once identified           |
| **Organization**                 | Internal / customer / supplier           |
| **Category**                     | System, HW, SW, Safety, etc.             |
| **Influence**                    | High / Medium / Low                      |
| **Interest**                     | High / Medium / Low                      |
| **Direct / Indirect**            | Relationship to module                   |
| **Requirement Source?**          | Yes / No                                 |
| **Interview Required?**          | Yes / No                                 |
| **Representative**               | If another person represents this role   |
| **Relevant Lifecycle Phase**     | Design / Production / Service / EOL      |
| **Requirement Areas**            | Communication, safety, diagnostics, etc. |
| **Interview Status**             | Not started / Scheduled / Complete       |
| **Related Stakeholder Req. IDs** | Links to your next artifact              |
| **Notes**                        | Free text                                |

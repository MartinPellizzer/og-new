System Architect

- The Relay Module shall execute relay-output commands received from Core
- The Relay Module shall provide Core output status
- The Relay Module shall provide Core diagnostics
- The Relay Module shall transition its outputs to defined safe states when system-level fault conditions


# Answer ID 2

- The Relay Module shall provide eight independently controlled relay-driver channels
- The Relay Module shall manage the activation of the drivers
- The Relay Module shall manage the deactivation of the drivers
- The Relay Module shall monitor module faults
- The Relay Module shall monitor output faults
- The Relay Module shall communicate the status of the outputs to Core
- The Relay Module shall communicate the diagnostics of the outputs to Core
- The Relay Module shall communicate to Core via Modbus RTU over RS-485
- The Relay Module shall enforce local fault-handling behavior

- The Relay Module shall initialize all driver outputs to their defined startup states before accepting normal output commands
- The Relay Module shall detect loss of communication with the CORE within a specified timeout and apply the predefined response for each output
- The Relay Module shall validate each received command before changing an output state
- The Relay Module shall distinguish commanded driver states from independently measured output states and physical relay states wherever the required monitoring hardware is provided
- The Relay Module shall implement defined fault-latching, fault-clearing and recovery behavior for each fault category
- The Relay Module shall detect defined firmware execution failures and ensure that a reset or stalled processor cannot cause unintended driver activation
- The Relay Module shall meet specified response-time limits for output commands, fault detection and fault response
- The Relay Module shall provide its identity, hardware revision, firmware version and required configuration information to the CORE
- The Relay Module shall operate within its specified electrical and environmental limits and provide defined protection against relevant electrical faults
- The Relay Module shall be verified against defined functional, communication, fault-handling and electrical acceptance criteria


# Answer ID 3

What behavior does the system require from each of the eight relay outputs?

Each output shall independently assume the ON or OFF state commanded by the
CORE within the specified response time, while preventing an individual channel fault
from affecting the other channels and maintaining the output's defined safe behavior
under fault conditions.

- The Relay Module shall set the independent outputs in ON or OFF state commanded by CORE
- The Relay Module shall set the outputs within the specified response time
- The Relay Module shall prevent an individual channel fault from affecting the other channels 
- The Relay Module shall maintain the output's defined safe behavior under fault conditions

- The Relay Module shall validate received output commands and execute them only when they are valid and permitted by the defined operating and fault-handling rules
- Changing the commanded state of one output shall not unintentionally change the state of any other output
- The Relay Module shall provide the output-state feedback required to verify command execution, using a clearly defined distinction between commanded state, driver state and physical relay state



# Answer ID 4

What must happen to every relay output when communication with the CORE is lost?

Upon detecting a communication timeout with the CORE, every relay output shall
transition to its predefined safe state, which shall be OFF unless a system-level
hazard analysis explicitly requires another state.

- The Relay Module shall detect a communication timeout with the CORE
- The Relay Module shall set every relay output to its predefined safe state when communication timeout
- The Relay Module shall set every relay output to OFF when communication timeout unless a system-level hazard analysis explicitly requires another state



# Answer ID 5

What is the required system behavior if the Relay Module itself fails?

Any Relay Module failure that could compromise safe operation shall cause the affected outputs to transition to their defined safe states, prevent unintended activation, and provide sufficient fault information to the CORE to initiate the appropriate Aurora system fault response.

- The Relay Module shall set the output to defined safe states when module failure state
- The Relay Module shall prevent unintended activation of the output
- The Relay Module shall provide fault information to the CORE to initiate fault response



# Answer ID 6

Question ID 6
Answer ID 6
Stakeholder Role CORE Firmware Engineer

Which responsibilities belong to the CORE and which responsibilities belong to the Relay Module?

The CORE shall own all system-level decisions, sequencing, interlocks, operating
modes and desired relay states, while the Relay Module shall execute those
commands deterministically, manage its eight physical driver outputs, perform local
hardware diagnostics, and report its status and faults to the CORE.

- The CORE shall own all system-level decisions
- The CORE shall own all system-level sequencing
- The CORE shall own all system-level interlocks
- The CORE shall own all system-level operating modes 
- The CORE shall own all system-level desired relay states
- The Relay Module shall execute execute commands deterministically
- The Relay Module shall manage its eight physical driver outputs
- The Relay Module shall perform local hardware diagnostics
- The Relay Module shall report its status to the CORE
- The Relay Module shall report its faults to the CORE


# Answer ID 7

Question ID 7
Answer ID 7
Stakeholder Role CORE Firmware Engineer

What commands must the CORE be able to send to the Relay Module?

The CORE shall be able to command each of the eight outputs independently,
initialize and reset the module, request status and diagnostics, and synchronize or
restore the required output states after startup or communication recovery.

- The CORE shall command each of the eight outputs independently
- The CORE shall initialize the module
- The CORE shall reset the module
- The CORE shall request status to the module 
- The CORE shall request diagnostics to the module 
- The CORE shall synchronize the required output states after startup/communication recovery
- The CORE shall restore the required output states after startup/ communication recovery


# Answer ID 8

Question ID 8
Answer ID 8
Stakeholder Role CORE Firmware Engineer

What information must the Relay Module provide back to the CORE?

The Relay Module shall report the state of all eight outputs, module health, individual channel faults, communication status, relevant electrical/thermal diagnostics, firmware/hardware identification, and any condition preventing reliable output control.

- The Relay Module shall report the state of all eight outputs
- The Relay Module shall report the module health
- The Relay Module shall report the individual channel faults
- The Relay Module shall report the communication status
- The Relay Module shall report the relevant electrical diagnostics
- The Relay Module shall report the relevant thermal diagnostics
- The Relay Module shall report the firmware identification
- The Relay Module shall report the hardware identification
- The Relay Module shall report any condition preventing reliable output control


# Answer ID 9

Question ID 9
Answer ID 9
Stakeholder Role CORE Firmware Engineer

How should the CORE detect that communication with the Relay Module has been
lost?

The CORE shall use a supervised communication mechanism with a defined
response timeout and consecutive failed transactions, declaring the Relay Module
unavailable when the configured communication-loss threshold is exceeded.

- The CORE shall use a supervised communication mechanism 
- The CORE shall define response timeout
- The CORE shall define response timeout
- The CORE shall define consecutive failed transactions
- The CORE shall declare Relay Module unavailable when the configured communication-loss threshold is exceeded


# Answer ID 10

Question ID 10
Answer ID 10
Stakeholder Role CORE Firmware Engineer

What should the CORE do when communication with the Relay Module is lost?

The CORE shall immediately declare a Relay Module communication fault, prevent further normal relay commands, transition Aurora to the appropriate safe system state, notify the HMI, and automatically re-synchronize the required relay states only after reliable communication has been restored.

- The CORE shall immediately declare a Relay Module communication fault
- The CORE shall prevent further normal relay commands
- The CORE shall transition Aurora to the appropriate safe system state
- The CORE shall notify Aurora the HMI
- The CORE shall automatically re-synchronize the required relay states only after reliable communication has been restored

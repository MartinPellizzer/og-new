<head>
<title>
Aurora: Module Relay x8
</title>
<subtitle>
Stakeholders Requirements
</subtitle>
</head>
<rev>
Version, Date, Author, Description
0.1.0, 2026-07-02, Martin Pellizzer, Starting version
</rev>
<body>
# requirements

## Requirement 1
### Requirement
The Relay Module shall execute relay-output commands received from CORE



## Requirement 2
### Requirement
The Relay Module shall provide CORE with output status



## Requirement 3
### Requirement
The Relay Module shall provide CORE with module diagnostics



## Requirement 4
### Requirement
The Relay Module shall transition its outputs to safe states when system-level fault



## Requirement 5
### Requirement
The Relay Module shall provide eight indipendently controlled relay-driven channels



## Requirement 6
### Requirement
The Relay Module shall manage activation of each channel



## Requirement 7
### Requirement
The Relay Module shall manage deactivation of each channel



## Requirement 8
### Requirement
The Relay Module shall monitor output faults



## Requirement 9
### Requirement
The Relay Module shall communicate channels status to CORE



## Requirement 10
### Requirement
The Relay Module shall communicate channels diagnostics to CORE



## Requirement 11
### Requirement
The Relay Module shall communicate to CORE via Modbus RTU protocol



## Requirement 12
### Requirement
The Relay Module shall communicate to CORE via RS-485 hardware standard



## Requirement 13
### Requirement
The Relay Module shall enforce local fault-handling



## Requirement 14
### Requirement
The Relay Module shall turn ON/OFF outputs within specified time



## Requirement 15
### Requirement
The Relay Module shall prevent one faulty channel to affect other channels



## Requirement 16
### Requirement
The Relay Module shall maintain the output defined safe behavior under fault conditions



## Requirement 17
### Requirement
The Relay Module shall detect communication timeout with CORE



## Requirement 18
### Requirement
The Relay Module shall transition to its outputs to predefined safe state when timeout with CORE



## Requirement 19
### Requirement
The Relay Module shall transition to defined safe state when in failure state



## Requirement 20
### Requirement
The Relay Module shall prevent unintended activation when in failure state



## Requirement 21
### Requirement
The Relay Module shall provide sufficient fault information to CORE when in failure state



## Requirement 22
### Requirement
The Relay Module shall execute commands deterministically



## Requirement 23
### Requirement
The Relay Module shall manage its eight physical driver outputs



## Requirement 24
### Requirement
The Relay Module shall perform local hardware diagnostics



## Requirement 25
### Requirement
The Relay Module shall report its status to CORE



## Requirement 26
### Requirement
The Relay Module shall report its faults to CORE



## Requirement 27
### Requirement
The Relay Module shall report the state of all eight outputs



## Requirement 28
### Requirement
The Relay Module shall report the module health



## Requirement 29
### Requirement
The Relay Module shall report individual channel faults



## Requirement 30
### Requirement
The Relay Module shall report communication status



## Requirement 31
### Requirement
The Relay Module shall report electrical identification



## Requirement 32
### Requirement
The Relay Module shall report thermal identification



## Requirement 33
### Requirement
The Relay Module shall report diagnostics identification



## Requirement 34
### Requirement
The Relay Module shall report firmware identification



## Requirement 35
### Requirement
The Relay Module shall report hardware identification



## Requirement 36
### Requirement
The Relay Module shall report any condition preventing reliable output control



## Requirement 37
### Requirement
The Relay Module shall reliably energize its assigned relay coil across the full specified supply



## Requirement 38
### Requirement
The Relay Module shall independently energize its assigned relay coil across the full specified supply



## Requirement 39
### Requirement
The Relay Module shall energize its assigned relay coil across the full specified temperature



## Requirement 40
### Requirement
The Relay Module shall energize its assigned relay coil across the full specified tolerance range



## Requirement 41
### Requirement
The Relay Module shall energize its assigned relay coil with adequate voltage



## Requirement 42
### Requirement
The Relay Module shall energize its assigned relay coil with adequate voltage margin



## Requirement 43
### Requirement
The Relay Module shall energize its assigned relay coil with adequate current margin



## Requirement 44
### Requirement
The Relay Module shall energize its assigned relay coil with continuous-duty



## Requirement 45
### Requirement
The Relay Module shall energize its assigned relay coil with continuous-duty capability



## Requirement 46
### Requirement
The Relay Module shall energize its assigned relay coil with short-circuit protection



## Requirement 47
### Requirement
The Relay Module shall energize its assigned relay coil with overload protection



## Requirement 48
### Requirement
The Relay Module shall energize its assigned relay coil with no unintended activation during reset conditions



## Requirement 49
### Requirement
The Relay Module shall energize its assigned relay coil with no unintended activation during fault conditions



## Requirement 50
### Requirement
The Relay Module shall operate with coils that have a defined nominal voltage



## Requirement 51
### Requirement
The Relay Module shall operate with coils that have allowable voltage range



## Requirement 52
### Requirement
The Relay Module shall operate with coils that have nominal current



## Requirement 53
### Requirement
The Relay Module shall operate with coils that have maximum current



## Requirement 54
### Requirement
The Relay Module shall operate with coils that have defined resistance



## Requirement 55
### Requirement
The Relay Module shall operate with coils that have defined inductance



## Requirement 56
### Requirement
The Relay Module shall operate with coils that have defined inrush behavior



## Requirement 57
### Requirement
The Relay Module shall operate with coils that have defined continuous-duty rating



## Requirement 58
### Requirement
The Relay Module shall operate with coils that have operate characteristics that are fully compatible with its corresponding driver



## Requirement 59
### Requirement
The Relay Module shall operate with coils that have release characteristics that are fully compatible with its corresponding driver



## Requirement 60
### Requirement
The Relay Module shall operate correctly over the complete specified nominal supply range



## Requirement 61
### Requirement
The Relay Module shall operate correctly over the complete specified nominal supply range, including component tolerances



## Requirement 62
### Requirement
The Relay Module shall operate correctly over the complete specified nominal supply range, including steady-state variation



## Requirement 63
### Requirement
The Relay Module shall operate correctly over the complete specified nominal supply range, including startup conditions



## Requirement 64
### Requirement
The Relay Module shall operate correctly over the complete specified nominal supply range, including brownouts



## Requirement 65
### Requirement
The Relay Module shall operate correctly over the complete specified nominal supply range, including overvoltage



## Requirement 66
### Requirement
The Relay Module shall operate correctly over the complete specified nominal supply range, including ripple



## Requirement 67
### Requirement
The Relay Module shall operate correctly over the complete specified nominal supply range, including transient disturbances from cabinet



## Requirement 68
### Requirement
The Relay Module shall have drivers with appropriately sized suppressions



## Requirement 69
### Requirement
The Relay Module shall have drivers with appropriately sized suppressions, such as a flyback diode



## Requirement 70
### Requirement
The Relay Module shall have drivers with appropriately sized suppressions, such as a TVS/clamp network



## Requirement 71
### Requirement
The Relay Module shall limit the coil-generated transient to a safe level without exceeding driver ratings



## Requirement 72
### Requirement
The Relay Module shall limit the coil-generated transient to a safe level without causing unacceptable relay release-time delays



## Requirement 73
### Requirement
The Relay Module shall transition all relay outputs to defined safe state during out-of-range brownout



## Requirement 74
### Requirement
The Relay Module shall transition all relay outputs to defined safe state during power loss



## Requirement 75
### Requirement
The Relay Module shall initialize deterministically with outputs disabled until valid control from the CORE is established after power restoration


</body>

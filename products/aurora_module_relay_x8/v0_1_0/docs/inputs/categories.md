<head>
<title>
Aurora: Module Relay x8
</title>
<subtitle>
Categories
</subtitle>
</head>
<rev>
Version, Date, Author, Description
0.1.0, 2026-07-02, Martin Pellizzer, Starting version
</rev>
<body>

# 1. CORE

---

## 1.1 CORE Communicate

- The Relay Module shall communicate to CORE

---

### 1.1.1 The Relay Module shall communicate to CORE

#### Statements

- The Relay Module shall communicate to CORE via Modbus RTU protocol

- The Relay Module shall communicate to CORE via RS-485 hardware standard

---

## 1.2 CORE Execute

- The Relay Module shall execute relay-output commands (ON/OFF) received from CORE

- The Relay Module shall execute relay-output commands (ON/OFF) deterministically

- The Relay Module shall execute relay-output commands (ON/OFF) within specified time

- The Relay Module shall execute normal operation only when explicit reauthorization from CORE is given

---

### 1.2.1 The Relay Module shall execute relay-output commands (ON/OFF) received from CORE

#### Statements

- The Relay Module shall execute relay-output commands received from CORE

- The Relay Module shall manage the eight relay outputs to control or influence the ozone-generation process by operating the required process equipment and auxiliaries

---

### 1.2.2 The Relay Module shall execute relay-output commands (ON/OFF) deterministically

#### Statements

- The Relay Module shall execute commands deterministically

---

### 1.2.3 The Relay Module shall execute relay-output commands (ON/OFF) within specified time

#### Statements

- The Relay Module shall turn ON/OFF outputs within specified time

---

### 1.2.4 The Relay Module shall execute normal operation only when explicit reauthorization from CORE is given

#### Statements

- The Relay Module shall require explicit reauthorization from CORE before returning to normal operation

---

## 1.3 CORE Report

- The Relay Module shall report to CORE its status

- The Relay Module shall report to CORE outputs status

- The Relay Module shall report to CORE communication status

- The Relay Module shall report to CORE diagnostics

- The Relay Module shall report to CORE diagnostics identification

- The Relay Module shall report to CORE fault information

- The Relay Module shall report to CORE individual channel faults

- The Relay Module shall report to CORE any condition preventing reliable output control

- The Relay Module shall report to CORE module health

- The Relay Module shall report to CORE electrical identification

- The Relay Module shall report to CORE thermal identification

- The Relay Module shall report to CORE firmware identification

- The Relay Module shall report to CORE hardware identification

---

### 1.3.1 The Relay Module shall report to CORE its status

#### Statements

- The Relay Module shall report its status to CORE

---

### 1.3.2 The Relay Module shall report to CORE outputs status

#### Statements

- The Relay Module shall provide CORE with output status

- The Relay Module shall communicate channels status to CORE

- The Relay Module shall report the state of all eight outputs

---

### 1.3.3 The Relay Module shall report to CORE communication status

#### Statements

- The Relay Module shall report communication status

- The Relay Module shall report the communication fault when communication with CORE is restored

---

### 1.3.4 The Relay Module shall report to CORE diagnostics

#### Statements

- The Relay Module shall provide CORE with module diagnostics

- The Relay Module shall communicate channels diagnostics to CORE

---

### 1.3.5 The Relay Module shall report to CORE diagnostics identification

#### Statements

- The Relay Module shall report diagnostics identification

---

### 1.3.6 The Relay Module shall report to CORE fault information

#### Statements

- The Relay Module shall provide sufficient fault information to CORE when in failure state

- The Relay Module shall report its faults to CORE

- The Relay Module shall report the fault as required when it detects an internal fault capable of compromising safe operation

---

### 1.3.7 The Relay Module shall report to CORE individual channel faults

#### Statements

- The Relay Module shall report individual channel faults

---

### 1.3.8 The Relay Module shall report to CORE any condition preventing reliable output control

#### Statements

- The Relay Module shall report any condition preventing reliable output control

---

### 1.3.9 The Relay Module shall report to CORE module health

#### Statements

- The Relay Module shall report the module health

---

### 1.3.10 The Relay Module shall report to CORE electrical identification

#### Statements

- The Relay Module shall report electrical identification

---

### 1.3.11 The Relay Module shall report to CORE thermal identification

#### Statements

- The Relay Module shall report thermal identification

---

### 1.3.12 The Relay Module shall report to CORE firmware identification

#### Statements

- The Relay Module shall report firmware identification

---

### 1.3.13 The Relay Module shall report to CORE hardware identification

#### Statements

- The Relay Module shall report hardware identification

---

## 1.4 CORE Monitor

- The Relay Module shall monitor communication timeout with CORE

- The Relay Module shall monitor timeout with CORE to transition to its outputs to predefined safe state

---

### 1.4.1 The Relay Module shall monitor communication timeout with CORE

#### Statements

- The Relay Module shall detect communication timeout with CORE

---

### 1.4.2 The Relay Module shall monitor timeout with CORE to transition to its outputs to predefined safe state

#### Statements

- The Relay Module shall transition to its outputs to predefined safe state when timeout with CORE

- The Relay Module shall autonomously transition every output to its predefined safe state when communication with the CORE is lost beyond the defined safety timeout

- The Relay Module shall maintain a predefined safe state when communication with the CORE is lost beyond the defined safety timeout

---

# 2. Relay Module

- The Relay Module shall operate correctly over the complete specified nominal supply range

- The Relay Module shall operate correctly over the complete specified nominal supply range, including component tolerances

- The Relay Module shall operate correctly over the complete specified nominal supply range, including steady-state variation

- The Relay Module shall operate correctly over the complete specified nominal supply range, including startup conditions

- The Relay Module shall operate correctly over the complete specified nominal supply range, including brownouts

- The Relay Module shall operate correctly over the complete specified nominal supply range, including overvoltage

- The Relay Module shall operate correctly over the complete specified nominal supply range, including ripple

- The Relay Module shall operate correctly over the complete specified nominal supply range, including transient disturbances from cabinet

- The Relay Module shall locally enforce fault-handling

- The Relay Module shall locally perform hardware diagnostics

- The Relay Module shall locally enforce the safety-related output constraints for its eight relay channels

- The Relay Module shall locally enforce the fail-safe behavior for its eight relay channels

- The Relay Module shall locally enforce output-level safety constraints

- The Relay Module shall locally enforce watchdog/communication-loss responses

- The Relay Module shall detect relevant hardware faults

- The Relay Module shall define safe-states for all its outputs (based on its associated hazard analysis)

- The Relay Module shall define OFF/de-energized as the default safe-state unless a documented safety analysis requires a specific output to remain energized

- The Relay Module shall include a startup sequence that verifies all required permissives

- The Relay Module shall include a startup sequence that establishes the required gas flow

- The Relay Module shall include a startup sequence that establishes the supporting utilities

- The Relay Module shall include a startup sequence that enables cooling

- The Relay Module shall include a startup sequence that enables other auxiliaries

- The Relay Module shall include a startup sequence that confirms healthy operating feedback of auxiliaries

- The Relay Module shall include a startup sequence that energizes the ozone-generation system

- The Relay Module shall include a startup sequence that transitions Aurora to the normal ozone-production state  when the startup sequence is complete

- The Relay Module shall include a shutdown sequence that disables ozone generation

- The Relay Module shall include a shutdown sequence that maintains the required cooling

- The Relay Module shall include a shutdown sequence that maintains the required gas-flow/purge functions for the specified post-run period

- The Relay Module shall include a shutdown sequence that maintains the safely de-energizes the remaining auxiliaries in the defined order

- The Relay Module shall include a shutdown sequence that maintains the confirms that the process has reached the stopped state

- The Relay Module shall permit ozone generation only when all required utilities are available

- The Relay Module shall permit ozone generation only when gas flow is within their specified limits

- The Relay Module shall permit ozone generation only when cooling is within their specified limits

- The Relay Module shall permit ozone generation only when required valves are in their correct states

- The Relay Module shall permit ozone generation only when required auxiliaries are in their correct states

- The Relay Module shall permit ozone generation only when no active safety interlock is violated

- The Relay Module shall permit ozone generation only when no active process interlock is violated

- The Relay Module shall permit ozone generation only when all required feedback signals are valid

- The Relay Module shall permit ozone generation only when the system is in an authorized operating mode

- The Relay Module shall immediately stop  ozone generation whenever a condition capable of creating an unsafe or uncontrolled process state is detected

- The Relay Module shall immediately stop  ozone generation when detected a loss of required gas flow

- The Relay Module shall immediately stop  ozone generation when detected a loss of required cooling

- The Relay Module shall immediately stop  ozone generation when detected a critical equipment failure

- The Relay Module shall immediately stop  ozone generation when detected hazardous process-variable limits

- The Relay Module shall immediately stop  ozone generation when detected loss of required safety permissives

- The Relay Module shall immediately stop  ozone generation when detected emergency shutdown

- The Relay Module shall immediately stop  ozone generation when detected defined critical interlock

- The Relay Module shall operate correctly over the complete specified nominal supply range, including ripple

- The Relay Module shall prevent reactivation until the reauthorization conditions are satisfied when it detects an internal fault capable of compromising safe operation

- The Relay Module shall transition all relay outputs to defined safe state during out-of-range brownout

- The Relay Module shall transition all relay outputs to defined safe state during power loss

- The Relay Module shall initialize deterministically with outputs disabled until valid control from the CORE is established after power restoration

- The Relay Module shall transition its outputs to safe states when system-level fault

- The Relay Module shall monitor output faults

- The Relay Module shall maintain the output defined safe behavior under fault conditions

- The Relay Module shall prevent one faulty channel to affect other channels

- The Relay Module shall provide eight indipendently controlled relay-driven channels

- The Relay Module shall manage activation of each channel

- The Relay Module shall manage deactivation of each channel

---

# 3. Relay Driver

---

## 3.5 Relay Driver Energize

- The Relay Module shall energize each relay coil independently across the full specified supply

- The Relay Module shall energize its assigned relay coil across the full specified temperature tolerance range

- The Relay Module shall energize its assigned relay coil with adequate voltage margin

- The Relay Module shall energize its assigned relay coil with adequate current margin

- The Relay Module shall energize its assigned relay coil with continuous-duty capability

- The Relay Module shall energize its assigned relay coil with short-circuit protection

- The Relay Module shall energize its assigned relay coil with overload protection

- The Relay Module shall energize its assigned relay coil with no unintended activation during reset conditions

- The Relay Module shall energize its assigned relay coil with no unintended activation during fault conditions

---

### 3.5.1 The Relay Module shall energize each relay coil independently across the full specified supply

#### Statements

- The Relay Module shall reliably energize its assigned relay coil across the full specified supply

- The Relay Module shall independently energize its assigned relay coil across the full specified supply

---

### 3.5.2 The Relay Module shall energize its assigned relay coil across the full specified temperature tolerance range

#### Statements

- The Relay Module shall energize its assigned relay coil across the full specified temperature

- The Relay Module shall energize its assigned relay coil across the full specified tolerance range

---

### 3.5.3 The Relay Module shall energize its assigned relay coil with adequate voltage margin

#### Statements

- The Relay Module shall energize its assigned relay coil with adequate voltage

- The Relay Module shall energize its assigned relay coil with adequate voltage margin

---

### 3.5.4 The Relay Module shall energize its assigned relay coil with adequate current margin

#### Statements

- The Relay Module shall energize its assigned relay coil with adequate current margin

---

### 3.5.5 The Relay Module shall energize its assigned relay coil with continuous-duty capability

#### Statements

- The Relay Module shall energize its assigned relay coil with continuous-duty

- The Relay Module shall energize its assigned relay coil with continuous-duty capability

---

### 3.5.6 The Relay Module shall energize its assigned relay coil with short-circuit protection

#### Statements

- The Relay Module shall energize its assigned relay coil with short-circuit protection

---

### 3.5.7 The Relay Module shall energize its assigned relay coil with overload protection

#### Statements

- The Relay Module shall energize its assigned relay coil with overload protection

---

### 3.5.8 The Relay Module shall energize its assigned relay coil with no unintended activation during reset conditions

#### Statements

- The Relay Module shall energize its assigned relay coil with no unintended activation during reset conditions

---

### 3.5.9 The Relay Module shall energize its assigned relay coil with no unintended activation during fault conditions

#### Statements

- The Relay Module shall energize its assigned relay coil with no unintended activation during fault conditions

---

## 3.6 Relay Driver Limit

- The Relay Module shall limit the coil-generated transient to a safe level without exceeding driver ratings

- The Relay Module shall limit the coil-generated transient to a safe level without causing unacceptable relay release-time delays

---

### 3.6.1 The Relay Module shall limit the coil-generated transient to a safe level without exceeding driver ratings

#### Statements

- The Relay Module shall limit the coil-generated transient to a safe level without exceeding driver ratings

---

### 3.6.2 The Relay Module shall limit the coil-generated transient to a safe level without causing unacceptable relay release-time delays

#### Statements

- The Relay Module shall limit the coil-generated transient to a safe level without causing unacceptable relay release-time delays

---

## 3.7 Relay Driver Include

- The Relay Module shall have drivers with appropriately sized suppressions

- The Relay Module shall have drivers with appropriately sized suppressions, such as a flyback diode

- The Relay Module shall have drivers with appropriately sized suppressions, such as a TVS/clamp network

---

### 3.7.1 The Relay Module shall have drivers with appropriately sized suppressions

#### Statements

- The Relay Module shall have drivers with appropriately sized suppressions

---

### 3.7.2 The Relay Module shall have drivers with appropriately sized suppressions, such as a flyback diode

#### Statements

- The Relay Module shall have drivers with appropriately sized suppressions, such as a flyback diode

---

### 3.7.3 The Relay Module shall have drivers with appropriately sized suppressions, such as a TVS/clamp network

#### Statements

- The Relay Module shall have drivers with appropriately sized suppressions, such as a TVS/clamp network

---

# 4. Relay

---

## 4.8 Relay Operate

- The Relay Module shall operate with coils that have a defined nominal voltage range

- The Relay Module shall operate with coils that have defined nominal current

- The Relay Module shall operate with coils that have defined maximum current

- The Relay Module shall operate with coils that have defined resistance

- The Relay Module shall operate with coils that have defined inductance

- The Relay Module shall operate with coils that have defined inrush behavior

- The Relay Module shall operate with coils that have defined continuous-duty rating

- The Relay Module shall operate with coils that have operate characteristics that are fully compatible with its corresponding driver

- The Relay Module shall operate with coils that have release characteristics that are fully compatible with its corresponding driver

---

### 4.8.1 The Relay Module shall operate with coils that have a defined nominal voltage range

#### Statements

- The Relay Module shall operate with coils that have a defined nominal voltage

- The Relay Module shall operate with coils that have allowable voltage range

---

### 4.8.2 The Relay Module shall operate with coils that have defined nominal current

#### Statements

- The Relay Module shall operate with coils that have nominal current

---

### 4.8.3 The Relay Module shall operate with coils that have defined maximum current

#### Statements

- The Relay Module shall operate with coils that have maximum current

---

### 4.8.4 The Relay Module shall operate with coils that have defined resistance

#### Statements

- The Relay Module shall operate with coils that have defined resistance

---

### 4.8.5 The Relay Module shall operate with coils that have defined inductance

#### Statements

- The Relay Module shall operate with coils that have defined inductance

---

### 4.8.6 The Relay Module shall operate with coils that have defined inrush behavior

#### Statements

- The Relay Module shall operate with coils that have defined inrush behavior

---

### 4.8.7 The Relay Module shall operate with coils that have defined continuous-duty rating

#### Statements

- The Relay Module shall operate with coils that have defined continuous-duty rating

---

### 4.8.8 The Relay Module shall operate with coils that have operate characteristics that are fully compatible with its corresponding driver

#### Statements

- The Relay Module shall operate with coils that have operate characteristics that are fully compatible with its corresponding driver

---

### 4.8.9 The Relay Module shall operate with coils that have release characteristics that are fully compatible with its corresponding driver

#### Statements

- The Relay Module shall operate with coils that have release characteristics that are fully compatible with its corresponding driver

---


</body>

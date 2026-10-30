<head>
<title>
Aurora: Module Relay x8
</title>
<subtitle>
Specifications
</subtitle>
</head>
<rev>
Version, Date, Author, Description
0.1.0, xxxx-xx-xx, Martin Pellizzer, Starting version
</rev>
<body>

# 1. Specifications

---


## 1.1 CORE Communication

### 1.1.2 Hardware

The Relay Module shall communicate with CORE via RS-485 physical interface.

| Setting            | Value                                |
| ------------------ | ------------------------------------ |
| Physical interface | RS-485                               |
| Number of wires    | 2-wire (A, B)                        |

---

### 1.1.1 Software

The Relay Module shall communicate with CORE via Modbus RTU protocol.

| Setting            | Value                                |
| ------------------ | ------------------------------------ |
| Protocollo         | Modbus RTU                           |
| Module role        | Slave                                |
| Module ID          | 0x01                                 |
| Baud rate          | 9600 bps                             |
| Data format        | 8 bits, no parity, 1 stop bit (8N1)  |

---

## 1.2 CORE Commands

The Relay Module shall execute commands received from CORE to turn ON/OFF each relay driver independently.

---

### 1.2.1 CORE Command: Turn ON a realy driver

The Relay Module shall turn ON a relay driver when receiving one of the following Modbus commands.

---

#### 1.2.1.1 CORE Command: Turn ON a realy driver number 1

The Relay Module shall turn ON the relay driver number 1 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x00                            |
| Turn ON            | 0xFF 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 00 FF 00 XX XX

---

#### 1.2.1.2 CORE Command: Turn ON a realy driver number 2

The Relay Module shall turn ON the relay driver number 2 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x01                            |
| Turn ON            | 0xFF 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 01 FF 00 XX XX

---

#### 1.2.1.3 CORE Command: Turn ON a realy driver number 3

The Relay Module shall turn ON the relay driver number 3 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x02                            |
| Turn ON            | 0xFF 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 02 FF 00 XX XX

---

#### 1.2.1.4 CORE Command: Turn ON a realy driver number 4

The Relay Module shall turn ON the relay driver number 4 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x03                            |
| Turn ON            | 0xFF 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 03 FF 00 XX XX

---

#### 1.2.1.5 CORE Command: Turn ON a realy driver number 5

The Relay Module shall turn ON the relay driver number 5 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x04                            |
| Turn ON            | 0xFF 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 04 FF 00 XX XX

---

#### 1.2.1.6 CORE Command: Turn ON a realy driver number 6

The Relay Module shall turn ON the relay driver number 6 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x05                            |
| Turn ON            | 0xFF 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 05 FF 00 XX XX

---

#### 1.2.1.7 CORE Command: Turn ON a realy driver number 7

The Relay Module shall turn ON the relay driver number 7 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x06                            |
| Turn ON            | 0xFF 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 06 FF 00 XX XX

---

#### 1.2.1.8 CORE Command: Turn ON a realy driver number 8

The Relay Module shall turn ON the relay driver number 8 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x07                            |
| Turn ON            | 0xFF 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 07 FF 00 XX XX

---

### 1.2.2 CORE Command: Turn OFF a realy driver

The Relay Module shall turn OFF a relay driver when receiving one of the following Modbus commands.

---

#### 1.2.2.1 CORE Command: Turn OFF a realy driver number 1

The Relay Module shall turn OFF the relay driver number 1 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x00                            |
| Turn OFF           | 0x00 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 00 FF 00 XX XX

---

#### 1.2.2.2 CORE Command: Turn OFF a realy driver number 2

The Relay Module shall turn OFF the relay driver number 2 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x01                            |
| Turn OFF           | 0x00 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 01 FF 00 XX XX

---

#### 1.2.2.3 CORE Command: Turn OFF a realy driver number 3

The Relay Module shall turn OFF the relay driver number 3 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x02                            |
| Turn OFF           | 0x00 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 02 FF 00 XX XX

---

#### 1.2.2.4 CORE Command: Turn OFF a realy driver number 4

The Relay Module shall turn OFF the relay driver number 4 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x03                            |
| Turn OFF           | 0x00 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 03 FF 00 XX XX

---

#### 1.2.2.5 CORE Command: Turn OFF a realy driver number 5

The Relay Module shall turn OFF the relay driver number 5 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x04                            |
| Turn OFF           | 0x00 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 04 FF 00 XX XX

---

#### 1.2.2.6 CORE Command: Turn OFF a realy driver number 6

The Relay Module shall turn OFF the relay driver number 6 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x05                            |
| Turn OFF           | 0x00 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 05 FF 00 XX XX

---

#### 1.2.2.7 CORE Command: Turn OFF a realy driver number 7

The Relay Module shall turn OFF the relay driver number 7 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x06                            |
| Turn OFF           | 0x00 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 06 FF 00 XX XX

---

#### 1.2.2.8 CORE Command: Turn OFF a realy driver number 8

The Relay Module shall turn OFF the relay driver number 8 when receiving the following Modbus commands.

| Description        | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x05                                 |
| Coil address       | 0x00 0x07                            |
| Turn OFF           | 0x00 0x00                            |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 05 00 07 FF 00 XX XX

---

## 1.3 CORE Report

---

### 1.3.1 CORE Report: Health

The Relay Module shall report to CORE its health.

Example:

| Value    | Description                                                           |
| -------- | --------------------------------------------------------------------- |
| UNKNOWN  | Health condition has not yet been evaluated                           |
| HEALTHY  | Module is operating normally                                          |
| DEGRADED | Module is operational but a non-critical issue has been detected      |
| CRITICAL | A serious issue has been detected that compromises reliable operation |
| FAILED   | Module is unable to perform its intended function                     |

TODO: Not implemented in this version

### 1.3.2 CORE Report: Status Module

The Relay Module shall report to CORE its status. 

Possible status:

| Value | Description |
| ------------------ | ------------------------------------ |
| INITIALIZING | Module is powering up and performing initialization | 
| READY | Module is initialized and ready to operate |
| OPERATING | Module is operating and controlling its outputs |
| WARNING | Module is operational but has an active warning |
| FAULT | A fault has been detected that affects normal operation |
| MAINTENANCE | Module is in maintenance or service mode |
| OFFLINE | Module is not operational or has been intentionally disabled |

Modbus register definition: 

| Parameter          | Value                                |
| ------------------ | ------------------------------------ |
| Register name      | Module_Status                        |
| Register address   | [TODO] 30001 (0x0000 zero-based)     |
| Function code      | FC04                                 |
| Register type      | Input Register                       |
| Data type          | UINT16                               |
| Access             | Read-only                            |
| Default value      | 0 (INITIALIZING)                     |
| Update             | Whenever operational state changes   |

Modbus master command:  

| Parameter          | Value                                |
| ------------------ | ------------------------------------ |
| Module ID          | 0x01                                 |
| Function code      | 0x04                                 |
| Starting address   | [TODO] 0x00 0x00                     |
| Quantity           | [TODO] 0x00 0x01                     |
| CRC16              | 0xXX 0xXX                            |

The complete data frame is: 01 04 00 00 00 01 XX XX

Modbus slave response:  

| Parameter              | Value                                |
| ---------------------- | ------------------------------------ |
| Module ID              | 0x01                                 |
| Function code          | 0x04                                 |
| Number of data bytes   | 0x00 0x02                            |
| Register value         | 0xXX 0xXX                            |
| CRC16                  | 0xXX 0xXX                            |

The complete data frame is: 01 04 02 XX XX XX XX

---

#### 1.3.2.1 CORE Report: Status Module INITIALIZING

The Relay Module shall report the status INITIALIZING (if it's in such state) when Modbus asks for it.

| Parameter              | Value                                |
| ---------------------- | ------------------------------------ |
| Module ID              | 0x01                                 |
| Function code          | 0x04                                 |
| Number of data bytes   | 0x00 0x02                            |
| Register value         | 0x00 0x00                            |
| CRC16                  | 0xXX 0xXX                            |

The complete data frame is: 01 04 02 00 00 XX XX

---

#### 1.3.2.2 CORE Report: Status Module READY

The Relay Module shall report the status READY (if it's in such state) when Modbus asks for it.

| Parameter              | Value                                |
| ---------------------- | ------------------------------------ |
| Module ID              | 0x01                                 |
| Function code          | 0x04                                 |
| Number of data bytes   | 0x00 0x02                            |
| Register value         | 0x00 0x01                            |
| CRC16                  | 0xXX 0xXX                            |

The complete data frame is: 01 04 02 00 01 XX XX

---

#### 1.3.2.3 CORE Report: Status Module OPERATING

The Relay Module shall report the status OPERATING (if it's in such state) when Modbus asks for it.

| Parameter              | Value                                |
| ---------------------- | ------------------------------------ |
| Module ID              | 0x01                                 |
| Function code          | 0x04                                 |
| Number of data bytes   | 0x00 0x02                            |
| Register value         | 0x00 0x02                            |
| CRC16                  | 0xXX 0xXX                            |

The complete data frame is: 01 04 02 00 02 XX XX

---

#### 1.3.2.4 CORE Report: Status Module WARNING

The Relay Module shall report the status WARNING (if it's in such state) when Modbus asks for it.

| Parameter              | Value                                |
| ---------------------- | ------------------------------------ |
| Module ID              | 0x01                                 |
| Function code          | 0x04                                 |
| Number of data bytes   | 0x00 0x02                            |
| Register value         | 0x00 0x03                            |
| CRC16                  | 0xXX 0xXX                            |

The complete data frame is: 01 04 02 00 03 XX XX

---

#### 1.3.2.5 CORE Report: Status Module FAULT

The Relay Module shall report the status FAULT (if it's in such state) when Modbus asks for it.

| Parameter              | Value                                |
| ---------------------- | ------------------------------------ |
| Module ID              | 0x01                                 |
| Function code          | 0x04                                 |
| Number of data bytes   | 0x00 0x02                            |
| Register value         | 0x00 0x04                            |
| CRC16                  | 0xXX 0xXX                            |

The complete data frame is: 01 04 02 00 04 XX XX

---

#### 1.3.2.6 CORE Report: Status Module MAINTENANCE

The Relay Module shall report the status MAINTENANCE (if it's in such state) when Modbus asks for it.

| Parameter              | Value                                |
| ---------------------- | ------------------------------------ |
| Module ID              | 0x01                                 |
| Function code          | 0x04                                 |
| Number of data bytes   | 0x00 0x02                            |
| Register value         | 0x00 0x05                            |
| CRC16                  | 0xXX 0xXX                            |

The complete data frame is: 01 04 02 00 05 XX XX

---

#### 1.3.2.7 CORE Report: Status Module OFFLINE

The Relay Module shall report the status OFFLINE (if it's in such state) when Modbus asks for it.

| Parameter              | Value                                |
| ---------------------- | ------------------------------------ |
| Module ID              | 0x01                                 |
| Function code          | 0x04                                 |
| Number of data bytes   | 0x00 0x02                            |
| Register value         | 0x00 0x06                            |
| CRC16                  | 0xXX 0xXX                            |

The complete data frame is: 01 04 02 00 06 XX XX

---

### 1.3.2 CORE Report: Status Outputs

[TODO] The Relay Module shall report the output status of the relay drivers. It should report ONLY the status of the outputs (GPIO) communicated by the microcontroller, not the output status of the actual relay coils, since there no feedback system for that.




## 1.2 CORE Execute

- The Relay Module shall execute relay-output commands (ON/OFF) deterministically

- The Relay Module shall execute relay-output commands (ON/OFF) within specified time

- The Relay Module shall execute normal operation only when explicit reauthorization from CORE is given


---

## 1.3 CORE Report

- The Relay Module shall report to CORE outputs status

- The Relay Module shall report to CORE communication status

- The Relay Module shall report to CORE diagnostics

- The Relay Module shall report to CORE diagnostics identification

- The Relay Module shall report to CORE fault information

- The Relay Module shall report to CORE individual channel faults

- The Relay Module shall report to CORE any condition preventing reliable output control

- The Relay Module shall report to CORE electrical identification

- The Relay Module shall report to CORE thermal identification

- The Relay Module shall report to CORE firmware identification

- The Relay Module shall report to CORE hardware identification

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

# 2. Module

---

## 2.1 Module Relay Driver

- The Relay Module shall provide eight indipendently controlled relay-driven channels

- The Relay Module shall manage activation of each driver channel

- The Relay Module shall manage deactivation of each driver channel

- The Relay Module shall energize each relay coil independently across the full specified supply

- The Relay Module shall energize its assigned relay coil across the full specified temperature tolerance range

- The Relay Module shall energize its assigned relay coil with adequate voltage margin

- The Relay Module shall energize its assigned relay coil with adequate current margin

- The Relay Module shall energize its assigned relay coil with continuous-duty capability

- The Relay Module shall energize its assigned relay coil with short-circuit protection

- The Relay Module shall energize its assigned relay coil with overload protection

- The Relay Module shall energize its assigned relay coil with no unintended activation during reset conditions

- The Relay Module shall energize its assigned relay coil with no unintended activation during fault conditions

- The Relay Module shall limit the coil-generated transient to a safe level without exceeding driver ratings

- The Relay Module shall limit the coil-generated transient to a safe level without causing unacceptable relay release-time delays

- The Relay Module shall have drivers with appropriately sized suppressions

- The Relay Module shall have drivers with appropriately sized suppressions, such as a flyback diode

- The Relay Module shall have drivers with appropriately sized suppressions, such as a TVS/clamp network

---

### 2.1.1 The Relay Module shall provide eight indipendently controlled relay-driven channels

#### Statements

- The Relay Module shall provide eight indipendently controlled relay-driven channels

- The Relay Module shall manage its eight physical driver outputs

---

### 2.1.2 The Relay Module shall manage activation of each driver channel

#### Statements

- The Relay Module shall manage activation of each channel

---

### 2.1.3 The Relay Module shall manage deactivation of each driver channel

#### Statements

- The Relay Module shall manage deactivation of each channel

---

### 2.1.4 The Relay Module shall energize each relay coil independently across the full specified supply

#### Statements

- The Relay Module shall reliably energize its assigned relay coil across the full specified supply

- The Relay Module shall independently energize its assigned relay coil across the full specified supply

---

### 2.1.5 The Relay Module shall energize its assigned relay coil across the full specified temperature tolerance range

#### Statements

- The Relay Module shall energize its assigned relay coil across the full specified temperature

- The Relay Module shall energize its assigned relay coil across the full specified tolerance range

---

### 2.1.6 The Relay Module shall energize its assigned relay coil with adequate voltage margin

#### Statements

- The Relay Module shall energize its assigned relay coil with adequate voltage

- The Relay Module shall energize its assigned relay coil with adequate voltage margin

---

### 2.1.7 The Relay Module shall energize its assigned relay coil with adequate current margin

#### Statements

- The Relay Module shall energize its assigned relay coil with adequate current margin

---

### 2.1.8 The Relay Module shall energize its assigned relay coil with continuous-duty capability

#### Statements

- The Relay Module shall energize its assigned relay coil with continuous-duty

- The Relay Module shall energize its assigned relay coil with continuous-duty capability

---

### 2.1.9 The Relay Module shall energize its assigned relay coil with short-circuit protection

#### Statements

- The Relay Module shall energize its assigned relay coil with short-circuit protection

---

### 2.1.10 The Relay Module shall energize its assigned relay coil with overload protection

#### Statements

- The Relay Module shall energize its assigned relay coil with overload protection

---

### 2.1.11 The Relay Module shall energize its assigned relay coil with no unintended activation during reset conditions

#### Statements

- The Relay Module shall energize its assigned relay coil with no unintended activation during reset conditions

---

### 2.1.12 The Relay Module shall energize its assigned relay coil with no unintended activation during fault conditions

#### Statements

- The Relay Module shall energize its assigned relay coil with no unintended activation during fault conditions

---

### 2.1.13 The Relay Module shall limit the coil-generated transient to a safe level without exceeding driver ratings

#### Statements

- The Relay Module shall limit the coil-generated transient to a safe level without exceeding driver ratings

---

### 2.1.14 The Relay Module shall limit the coil-generated transient to a safe level without causing unacceptable relay release-time delays

#### Statements

- The Relay Module shall limit the coil-generated transient to a safe level without causing unacceptable relay release-time delays

---

### 2.1.15 The Relay Module shall have drivers with appropriately sized suppressions

#### Statements

- The Relay Module shall have drivers with appropriately sized suppressions

---

### 2.1.16 The Relay Module shall have drivers with appropriately sized suppressions, such as a flyback diode

#### Statements

- The Relay Module shall have drivers with appropriately sized suppressions, such as a flyback diode

---

### 2.1.17 The Relay Module shall have drivers with appropriately sized suppressions, such as a TVS/clamp network

#### Statements

- The Relay Module shall have drivers with appropriately sized suppressions, such as a TVS/clamp network

---

## 2.2 Module Power Supply

- The Relay Module shall operate correctly over the complete specified nominal supply range

- The Relay Module shall operate correctly over the complete specified nominal supply range, including component tolerances

- The Relay Module shall operate correctly over the complete specified nominal supply range, including steady-state variation

- The Relay Module shall operate correctly over the complete specified nominal supply range, including startup conditions

- The Relay Module shall operate correctly over the complete specified nominal supply range, including brownouts

- The Relay Module shall operate correctly over the complete specified nominal supply range, including overvoltage

- The Relay Module shall operate correctly over the complete specified nominal supply range, including ripple

- The Relay Module shall operate correctly over the complete specified nominal supply range, including transient disturbances from cabinet

- The Relay Module shall operate correctly over the complete specified nominal supply range, including ripple

---

### 2.2.1 The Relay Module shall operate correctly over the complete specified nominal supply range

#### Statements

- The Relay Module shall operate correctly over the complete specified nominal supply range

---

### 2.2.2 The Relay Module shall operate correctly over the complete specified nominal supply range, including component tolerances

#### Statements

- The Relay Module shall operate correctly over the complete specified nominal supply range, including component tolerances

---

### 2.2.3 The Relay Module shall operate correctly over the complete specified nominal supply range, including steady-state variation

#### Statements

- The Relay Module shall operate correctly over the complete specified nominal supply range, including steady-state variation

---

### 2.2.4 The Relay Module shall operate correctly over the complete specified nominal supply range, including startup conditions

#### Statements

- The Relay Module shall operate correctly over the complete specified nominal supply range, including startup conditions

---

### 2.2.5 The Relay Module shall operate correctly over the complete specified nominal supply range, including brownouts

#### Statements

- The Relay Module shall operate correctly over the complete specified nominal supply range, including brownouts

---

### 2.2.6 The Relay Module shall operate correctly over the complete specified nominal supply range, including overvoltage

#### Statements

- The Relay Module shall operate correctly over the complete specified nominal supply range, including overvoltage

---

### 2.2.7 The Relay Module shall operate correctly over the complete specified nominal supply range, including ripple

#### Statements

- The Relay Module shall operate correctly over the complete specified nominal supply range, including ripple

---

### 2.2.8 The Relay Module shall operate correctly over the complete specified nominal supply range, including transient disturbances from cabinet

#### Statements

- The Relay Module shall operate correctly over the complete specified nominal supply range, including transient disturbances from cabinet

---

### 2.2.9 The Relay Module shall operate correctly over the complete specified nominal supply range, including ripple

#### Statements

- The Relay Module shall operate correctly over the complete specified nominal supply range, including ripple

---

## 2.3 Module Startup

- The Relay Module shall include a startup sequence that verifies all required permissives

- The Relay Module shall include a startup sequence that establishes the required gas flow

- The Relay Module shall include a startup sequence that establishes the supporting utilities

- The Relay Module shall include a startup sequence that enables cooling

- The Relay Module shall include a startup sequence that enables other auxiliaries

- The Relay Module shall include a startup sequence that confirms healthy operating feedback of auxiliaries

- The Relay Module shall include a startup sequence that energizes the ozone-generation system

- The Relay Module shall include a startup sequence that transitions Aurora to the normal ozone-production state  when the startup sequence is complete

- The Relay Module shall initialize deterministically with outputs disabled until valid control from the CORE is established after power restoration

---

### 2.3.1 The Relay Module shall include a startup sequence that verifies all required permissives

#### Statements

- The Relay Module shall include a startup sequence that verifies all required permissives

---

### 2.3.2 The Relay Module shall include a startup sequence that establishes the required gas flow

#### Statements

- The Relay Module shall include a startup sequence that establishes the required gas flow

---

### 2.3.3 The Relay Module shall include a startup sequence that establishes the supporting utilities

#### Statements

- The Relay Module shall include a startup sequence that establishes the supporting utilities

---

### 2.3.4 The Relay Module shall include a startup sequence that enables cooling

#### Statements

- The Relay Module shall include a startup sequence that enables cooling

---

### 2.3.5 The Relay Module shall include a startup sequence that enables other auxiliaries

#### Statements

- The Relay Module shall include a startup sequence that enables other auxiliaries

---

### 2.3.6 The Relay Module shall include a startup sequence that confirms healthy operating feedback of auxiliaries

#### Statements

- The Relay Module shall include a startup sequence that confirms healthy operating feedback of auxiliaries

---

### 2.3.7 The Relay Module shall include a startup sequence that energizes the ozone-generation system

#### Statements

- The Relay Module shall include a startup sequence that energizes the ozone-generation system

---

### 2.3.8 The Relay Module shall include a startup sequence that transitions Aurora to the normal ozone-production state  when the startup sequence is complete

#### Statements

- The Relay Module shall include a startup sequence that transitions Aurora to the normal ozone-production state  when the startup sequence is complete

---

### 2.3.9 The Relay Module shall initialize deterministically with outputs disabled until valid control from the CORE is established after power restoration

#### Statements

- The Relay Module shall initialize deterministically with outputs disabled until valid control from the CORE is established after power restoration

---

## 2.4 Module Shutdown

- The Relay Module shall include a shutdown sequence that disables ozone generation

- The Relay Module shall include a shutdown sequence that maintains the required cooling

- The Relay Module shall include a shutdown sequence that maintains the required gas-flow/purge functions for the specified post-run period

- The Relay Module shall include a shutdown sequence that maintains the safely de-energizes the remaining auxiliaries in the defined order

- The Relay Module shall include a shutdown sequence that maintains the confirms that the process has reached the stopped state

---

### 2.4.1 The Relay Module shall include a shutdown sequence that disables ozone generation

#### Statements

- The Relay Module shall include a shutdown sequence that disables ozone generation

---

### 2.4.2 The Relay Module shall include a shutdown sequence that maintains the required cooling

#### Statements

- The Relay Module shall include a shutdown sequence that maintains the required cooling

---

### 2.4.3 The Relay Module shall include a shutdown sequence that maintains the required gas-flow/purge functions for the specified post-run period

#### Statements

- The Relay Module shall include a shutdown sequence that maintains the required gas-flow/purge functions for the specified post-run period

---

### 2.4.4 The Relay Module shall include a shutdown sequence that maintains the safely de-energizes the remaining auxiliaries in the defined order

#### Statements

- The Relay Module shall include a shutdown sequence that maintains the safely de-energizes the remaining auxiliaries in the defined order

---

### 2.4.5 The Relay Module shall include a shutdown sequence that maintains the confirms that the process has reached the stopped state

#### Statements

- The Relay Module shall include a shutdown sequence that maintains the confirms that the process has reached the stopped state

---

## 2.5 Module Permit

- The Relay Module shall permit ozone generation only when all required utilities are available

- The Relay Module shall permit ozone generation only when gas flow is within their specified limits

- The Relay Module shall permit ozone generation only when cooling is within their specified limits

- The Relay Module shall permit ozone generation only when required valves are in their correct states

- The Relay Module shall permit ozone generation only when required auxiliaries are in their correct states

- The Relay Module shall permit ozone generation only when no active safety interlock is violated

- The Relay Module shall permit ozone generation only when no active process interlock is violated

- The Relay Module shall permit ozone generation only when all required feedback signals are valid

- The Relay Module shall permit ozone generation only when the system is in an authorized operating mode

---

### 2.5.1 The Relay Module shall permit ozone generation only when all required utilities are available

#### Statements

- The Relay Module shall permit ozone generation only when all required utilities are available

---

### 2.5.2 The Relay Module shall permit ozone generation only when gas flow is within their specified limits

#### Statements

- The Relay Module shall permit ozone generation only when gas flow is within their specified limits

---

### 2.5.3 The Relay Module shall permit ozone generation only when cooling is within their specified limits

#### Statements

- The Relay Module shall permit ozone generation only when cooling is within their specified limits

---

### 2.5.4 The Relay Module shall permit ozone generation only when required valves are in their correct states

#### Statements

- The Relay Module shall permit ozone generation only when required valves are in their correct states

---

### 2.5.5 The Relay Module shall permit ozone generation only when required auxiliaries are in their correct states

#### Statements

- The Relay Module shall permit ozone generation only when required auxiliaries are in their correct states

---

### 2.5.6 The Relay Module shall permit ozone generation only when no active safety interlock is violated

#### Statements

- The Relay Module shall permit ozone generation only when no active safety interlock is violated

---

### 2.5.7 The Relay Module shall permit ozone generation only when no active process interlock is violated

#### Statements

- The Relay Module shall permit ozone generation only when no active process interlock is violated

---

### 2.5.8 The Relay Module shall permit ozone generation only when all required feedback signals are valid

#### Statements

- The Relay Module shall permit ozone generation only when all required feedback signals are valid

---

### 2.5.9 The Relay Module shall permit ozone generation only when the system is in an authorized operating mode

#### Statements

- The Relay Module shall permit ozone generation only when the system is in an authorized operating mode

---

## 2.6 Module Stop

- The Relay Module shall immediately stop  ozone generation whenever a condition capable of creating an unsafe or uncontrolled process state is detected

- The Relay Module shall immediately stop  ozone generation when detected a loss of required gas flow

- The Relay Module shall immediately stop  ozone generation when detected a loss of required cooling

- The Relay Module shall immediately stop  ozone generation when detected a critical equipment failure

- The Relay Module shall immediately stop  ozone generation when detected hazardous process-variable limits

- The Relay Module shall immediately stop  ozone generation when detected loss of required safety permissives

- The Relay Module shall immediately stop  ozone generation when detected emergency shutdown

- The Relay Module shall immediately stop  ozone generation when detected defined critical interlock

---

### 2.6.1 The Relay Module shall immediately stop  ozone generation whenever a condition capable of creating an unsafe or uncontrolled process state is detected

#### Statements

- The Relay Module shall immediately stop  ozone generation whenever a condition capable of creating an unsafe or uncontrolled process state is detected

---

### 2.6.2 The Relay Module shall immediately stop  ozone generation when detected a loss of required gas flow

#### Statements

- The Relay Module shall immediately stop  ozone generation when detected a loss of required gas flow

---

### 2.6.3 The Relay Module shall immediately stop  ozone generation when detected a loss of required cooling

#### Statements

- The Relay Module shall immediately stop  ozone generation when detected a loss of required cooling

---

### 2.6.4 The Relay Module shall immediately stop  ozone generation when detected a critical equipment failure

#### Statements

- The Relay Module shall immediately stop  ozone generation when detected a critical equipment failure

---

### 2.6.5 The Relay Module shall immediately stop  ozone generation when detected hazardous process-variable limits

#### Statements

- The Relay Module shall immediately stop  ozone generation when detected hazardous process-variable limits

---

### 2.6.6 The Relay Module shall immediately stop  ozone generation when detected loss of required safety permissives

#### Statements

- The Relay Module shall immediately stop  ozone generation when detected loss of required safety permissives

---

### 2.6.7 The Relay Module shall immediately stop  ozone generation when detected emergency shutdown

#### Statements

- The Relay Module shall immediately stop  ozone generation when detected emergency shutdown

---

### 2.6.8 The Relay Module shall immediately stop  ozone generation when detected defined critical interlock

#### Statements

- The Relay Module shall immediately stop  ozone generation when detected defined critical interlock

---

## 2.7 Module Enforce

- The Relay Module shall locally enforce fault-handling

- The Relay Module shall locally enforce the safety-related output constraints for its eight relay channels

- The Relay Module shall locally enforce the fail-safe behavior for its eight relay channels

- The Relay Module shall locally enforce output-level safety constraints

- The Relay Module shall locally enforce watchdog/communication-loss responses

---

### 2.7.1 The Relay Module shall locally enforce fault-handling

#### Statements

- The Relay Module shall enforce local fault-handling

- The Relay Module shall locally enforce internal fault handling

---

### 2.7.2 The Relay Module shall locally enforce the safety-related output constraints for its eight relay channels

#### Statements

- The Relay Module shall locally enforce the safety-related output constraints for its eight relay channels

---

### 2.7.3 The Relay Module shall locally enforce the fail-safe behavior for its eight relay channels

#### Statements

- The Relay Module shall locally enforce the fail-safe behavior for its eight relay channels

---

### 2.7.4 The Relay Module shall locally enforce output-level safety constraints

#### Statements

- The Relay Module shall locally enforce output-level safety constraints

---

### 2.7.5 The Relay Module shall locally enforce watchdog/communication-loss responses

#### Statements

- The Relay Module shall locally enforce watchdog/communication-loss responses

---

## 2.8 Module Diagnostic

- The Relay Module shall locally perform hardware diagnostics

---

### 2.8.1 The Relay Module shall locally perform hardware diagnostics

#### Statements

- The Relay Module shall perform local hardware diagnostics

---

## 2.9 Module Safety

- The Relay Module shall transition all relay outputs to defined safe state during out-of-range brownout

- The Relay Module shall transition all relay outputs to defined safe state during power loss

- The Relay Module shall define safe-states for all its outputs (based on its associated hazard analysis)

- The Relay Module shall define OFF/de-energized as the default safe-state unless a documented safety analysis requires a specific output to remain energized

- The Relay Module shall transition its outputs to safe states when system-level fault

---

### 2.9.1 The Relay Module shall transition all relay outputs to defined safe state during out-of-range brownout

#### Statements

- The Relay Module shall transition all relay outputs to defined safe state during out-of-range brownout

---

### 2.9.2 The Relay Module shall transition all relay outputs to defined safe state during power loss

#### Statements

- The Relay Module shall transition all relay outputs to defined safe state during power loss

---

### 2.9.3 The Relay Module shall define safe-states for all its outputs (based on its associated hazard analysis)

#### Statements

- The Relay Module shall have a formally defined safe state for all its outputs based on its associated hazard analysis

---

### 2.9.4 The Relay Module shall define OFF/de-energized as the default safe-state unless a documented safety analysis requires a specific output to remain energized

#### Statements

- The Relay Module shall have OFF/de-energized as the default safe state unless a documented safety analysis requires a specific output to remain energized

---

### 2.9.5 The Relay Module shall transition its outputs to safe states when system-level fault

#### Statements

- The Relay Module shall transition its outputs to safe states when system-level fault

- The Relay Module shall transition to defined safe state when in failure state

---

## 2.10 Module Fault

- The Relay Module shall monitor output faults

- The Relay Module shall maintain the output defined safe behavior under fault conditions

- The Relay Module shall prevent one faulty channel to affect other channels

- The Relay Module shall detect relevant hardware faults

- The Relay Module shall prevent reactivation until the reauthorization conditions are satisfied when it detects an internal fault capable of compromising safe operation

---

### 2.10.1 The Relay Module shall monitor output faults

#### Statements

- The Relay Module shall monitor output faults

- The Relay Module shall detect relevant output faults

---

### 2.10.2 The Relay Module shall maintain the output defined safe behavior under fault conditions

#### Statements

- The Relay Module shall maintain the output defined safe behavior under fault conditions

- The Relay Module shall prevent unintended activation when in failure state

- The Relay Module shall transition affected outputs to their predefined safe states independently of higher-level system decisions

- The Relay Module shall immediately prevent unsafe output activation when it detects an internal fault capable of compromising safe operation

- The Relay Module shall force all affected outputs to their defined safe states when it detects an internal fault capable of compromising safe operation

- The Relay Module shall latch the fault as required when it detects an internal fault capable of compromising safe operation

- The Relay Module shall prevent reactivation until the fault-clear conditions are satisfied when it detects an internal fault capable of compromising safe operation

- The Relay Module shall locally enforce defined safe-state behavior without relying solely on the CORE

---

### 2.10.3 The Relay Module shall prevent one faulty channel to affect other channels

#### Statements

- The Relay Module shall prevent one faulty channel to affect other channels

---

### 2.10.4 The Relay Module shall detect relevant hardware faults

#### Statements

- The Relay Module shall detect relevant hardware faults

---

### 2.10.5 The Relay Module shall prevent reactivation until the reauthorization conditions are satisfied when it detects an internal fault capable of compromising safe operation

#### Statements

- The Relay Module shall prevent reactivation until the reauthorization conditions are satisfied when it detects an internal fault capable of compromising safe operation

---

# 3. Relay

---

## 3.1 Relay Coil

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

### 3.1.1 The Relay Module shall operate with coils that have a defined nominal voltage range

#### Statements

- The Relay Module shall operate with coils that have a defined nominal voltage

- The Relay Module shall operate with coils that have allowable voltage range

---

### 3.1.2 The Relay Module shall operate with coils that have defined nominal current

#### Statements

- The Relay Module shall operate with coils that have nominal current

---

### 3.1.3 The Relay Module shall operate with coils that have defined maximum current

#### Statements

- The Relay Module shall operate with coils that have maximum current

---

### 3.1.4 The Relay Module shall operate with coils that have defined resistance

#### Statements

- The Relay Module shall operate with coils that have defined resistance

---

### 3.1.5 The Relay Module shall operate with coils that have defined inductance

#### Statements

- The Relay Module shall operate with coils that have defined inductance

---

### 3.1.6 The Relay Module shall operate with coils that have defined inrush behavior

#### Statements

- The Relay Module shall operate with coils that have defined inrush behavior

---

### 3.1.7 The Relay Module shall operate with coils that have defined continuous-duty rating

#### Statements

- The Relay Module shall operate with coils that have defined continuous-duty rating

---

### 3.1.8 The Relay Module shall operate with coils that have operate characteristics that are fully compatible with its corresponding driver

#### Statements

- The Relay Module shall operate with coils that have operate characteristics that are fully compatible with its corresponding driver

---

### 3.1.9 The Relay Module shall operate with coils that have release characteristics that are fully compatible with its corresponding driver

#### Statements

- The Relay Module shall operate with coils that have release characteristics that are fully compatible with its corresponding driver

---


</body>

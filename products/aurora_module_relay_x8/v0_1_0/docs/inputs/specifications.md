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
0.1.0, 2026-07-02, Martin Pellizzer, Starting version
</rev>
<body>

# 1. CORE

---

## 1.1 CORE Communication

---

### 1.1.1 CORE Communication Hardware

| Setting            | Value                                |
| ------------------ | ------------------------------------ |
| Physical interface | RS485 |
| Wires              | 2 wires (A, B) |

---

### 1.1.2 CORE Communication Software

| Setting            | Value                                |
| ------------------ | ------------------------------------ |
| Protocol           | Modbus |
| Mode               | RTU |
| Role               | Slave |
| Device ID          | 1                                 |
| Baud rate          | 9600 bps |
| Data bits          | 8 |
| Parity             | None  |
| Stop bits          | 1  |

---

#### 1.1.2.1 CORE Communication Software Modbus Register Map

The following table lists the address ranges for different modbus operations.

                | Address Range                     | Category                          |
                | --------------------------------- | ------------------------------------ |
                | 40001-40099 | Identification |
| 40101-40199 | Status |
| 40201-40299 | Diagnostic |
| 40301-40399 | Fault |
| 00001-00099 | Relay Driver |

---

The following table lists the specific addresses for each modbus operation.

                | Address                           | Parameter                          |
                | --------------------------------- | ------------------------------------ |
                | 40001 | Identification Electrical |
| 40002 | Identification Thermal |
| 40003 | Identification Hardware |
| 40004 | Identification Software |
| 00001 | Command Relay Driver 1 |
| 00002 | Command Relay Driver 2 |
| 00003 | Command Relay Driver 3 |
| 00004 | Command Relay Driver 4 |
| 00005 | Command Relay Driver 5 |
| 00006 | Command Relay Driver 6 |
| 00007 | Command Relay Driver 7 |
| 00008 | Command Relay Driver 8 |
| 40101 | Status Module |
| 40102 | Status Relay Driver 1 |
| 40103 | Status Relay Driver 2 |
| 40104 | Status Relay Driver 3 |
| 40105 | Status Relay Driver 4 |
| 40106 | Status Relay Driver 5 |
| 40107 | Status Relay Driver 6 |
| 40108 | Status Relay Driver 7 |
| 40109 | Status Relay Driver 8 |

---

### 1.1.3 CORE Read Identification

---

#### 1.1.3.1 CORE Read Identification Electrical

---

#### 1.1.3.2 CORE Read Identification Thermal

---

#### 1.1.3.3 CORE Read Identification Hardware

---

#### 1.1.3.4 CORE Read Identification Firmware

---

## 1.2 CORE Write

---

### 1.2.1 CORE Write Turn ON Relay Driver

---

#### 1.2.1.1 CORE Write Turn ON Relay Driver 1

The Relay Module (Slave) shall turn ON the relay driver 1 when CORE (Master) sends the following message.





| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 00 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 3A |
| CRC-16 - Low Byte        | 8C  |

The complete request data frame is: 01 05 00 00 FF 00 8C 3A

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 00 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 3A |
| CRC-16 - Low Byte        | 8C  |

The complete response data frame is: 01 05 00 00 FF 00 8C 3A

---

#### 1.2.1.2 CORE Write Turn ON Relay Driver 2

The Relay Module (Slave) shall turn ON the relay driver 2 when CORE (Master) sends the following message.




| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 01 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | FA |
| CRC-16 - Low Byte        | DD  |

The complete request data frame is: 01 05 00 01 FF 00 DD FA

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 01 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | FA |
| CRC-16 - Low Byte        | DD  |

The complete response data frame is: 01 05 00 01 FF 00 DD FA

---

#### 1.2.1.3 CORE Write Turn ON Relay Driver 3

The Relay Module (Slave) shall turn ON the relay driver 3 when CORE (Master) sends the following message.







| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 02 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | FA |
| CRC-16 - Low Byte        | 2D  |

The complete request data frame is: 01 05 00 02 FF 00 2D FA

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 02 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | FA |
| CRC-16 - Low Byte        | 2D  |

The complete response data frame is: 01 05 00 02 FF 00 2D FA

---

#### 1.2.1.4 CORE Write Turn ON Relay Driver 4

The Relay Module (Slave) shall turn ON the relay driver 4 when CORE (Master) sends the following message.







| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 03 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 3A |
| CRC-16 - Low Byte        | 7C  |

The complete request data frame is: 01 05 00 03 FF 00 7C 3A

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 03 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 3A |
| CRC-16 - Low Byte        | 7C  |

The complete response data frame is: 01 05 00 03 FF 00 7C 3A

---

#### 1.2.1.5 CORE Write Turn ON Relay Driver 5

The Relay Module (Slave) shall turn ON the relay driver 5 when CORE (Master) sends the following message.







| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 04 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | FB |
| CRC-16 - Low Byte        | CD  |

The complete request data frame is: 01 05 00 04 FF 00 CD FB

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 04 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | FB |
| CRC-16 - Low Byte        | CD  |

The complete response data frame is: 01 05 00 04 FF 00 CD FB

---

#### 1.2.1.6 CORE Write Turn ON Relay Driver 6

The Relay Module (Slave) shall turn ON the relay driver 6 when CORE (Master) sends the following message.







| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 05 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 3B |
| CRC-16 - Low Byte        | 9C  |

The complete request data frame is: 01 05 00 05 FF 00 9C 3B

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 05 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 3B |
| CRC-16 - Low Byte        | 9C  |

The complete response data frame is: 01 05 00 05 FF 00 9C 3B

---

#### 1.2.1.7 CORE Write Turn ON Relay Driver 7

The Relay Module (Slave) shall turn ON the relay driver 7 when CORE (Master) sends the following message.







| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 06 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 3B |
| CRC-16 - Low Byte        | 6C  |

The complete request data frame is: 01 05 00 06 FF 00 6C 3B

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 06 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 3B |
| CRC-16 - Low Byte        | 6C  |

The complete response data frame is: 01 05 00 06 FF 00 6C 3B

---

#### 1.2.1.8 CORE Write Turn ON Relay Driver 8

The Relay Module (Slave) shall turn ON the relay driver 8 when CORE (Master) sends the following message.







| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 07 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | FB |
| CRC-16 - Low Byte        | 3D  |

The complete request data frame is: 01 05 00 07 FF 00 3D FB

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 07 |
| Coil Value - High Byte   | FF |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | FB |
| CRC-16 - Low Byte        | 3D  |

The complete response data frame is: 01 05 00 07 FF 00 3D FB

---

### 1.2.2 CORE Write Turn OFF Relay Driver

---

#### 1.2.2.1 CORE Write Turn OFF Relay Driver 1

The Relay Module (Slave) shall turn OFF the relay driver 1 when CORE (Master) sends the following message.







| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 00 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | CA |
| CRC-16 - Low Byte        | CD  |

The complete request data frame is: 01 05 00 00 00 00 CD CA

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 00 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | CA |
| CRC-16 - Low Byte        | CD  |

The complete response data frame is: 01 05 00 00 00 00 CD CA

---

#### 1.2.2.2 CORE Write Turn OFF Relay Driver 2

The Relay Module (Slave) shall turn OFF the relay driver 2 when CORE (Master) sends the following message.








| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 01 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 0A |
| CRC-16 - Low Byte        | 9C  |

The complete request data frame is: 01 05 00 01 00 00 9C 0A

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 01 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 0A |
| CRC-16 - Low Byte        | 9C  |

The complete response data frame is: 01 05 00 01 00 00 9C 0A

---

#### 1.2.2.3 CORE Write Turn OFF Relay Driver 3

The Relay Module (Slave) shall turn OFF the relay driver 3 when CORE (Master) sends the following message.








| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 02 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 0A |
| CRC-16 - Low Byte        | 6C  |

The complete request data frame is: 01 05 00 02 00 00 6C 0A

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 02 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 0A |
| CRC-16 - Low Byte        | 6C  |

The complete response data frame is: 01 05 00 02 00 00 6C 0A

---

#### 1.2.2.4 CORE Write Turn OFF Relay Driver 4

The Relay Module (Slave) shall turn OFF the relay driver 4 when CORE (Master) sends the following message.








| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 03 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | CA |
| CRC-16 - Low Byte        | 3D  |

The complete request data frame is: 01 05 00 03 00 00 3D CA

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 03 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | CA |
| CRC-16 - Low Byte        | 3D  |

The complete response data frame is: 01 05 00 03 00 00 3D CA

---

#### 1.2.2.5 CORE Write Turn OFF Relay Driver 5

The Relay Module (Slave) shall turn OFF the relay driver 5 when CORE (Master) sends the following message.








| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 04 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 0B |
| CRC-16 - Low Byte        | 8C  |

The complete request data frame is: 01 05 00 04 00 00 8C 0B

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 04 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 0B |
| CRC-16 - Low Byte        | 8C  |

The complete response data frame is: 01 05 00 04 00 00 8C 0B

---

#### 1.2.2.6 CORE Write Turn OFF Relay Driver 6

The Relay Module (Slave) shall turn OFF the relay driver 6 when CORE (Master) sends the following message.








| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 05 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | CB |
| CRC-16 - Low Byte        | DD  |

The complete request data frame is: 01 05 00 05 00 00 DD CB

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 05 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | CB |
| CRC-16 - Low Byte        | DD  |

The complete response data frame is: 01 05 00 05 00 00 DD CB

---

#### 1.2.2.7 CORE Write Turn OFF Relay Driver 7

The Relay Module (Slave) shall turn OFF the relay driver 7 when CORE (Master) sends the following message.








| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 06 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | CB |
| CRC-16 - Low Byte        | 2D  |

The complete request data frame is: 01 05 00 06 00 00 2D CB

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 06 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | CB |
| CRC-16 - Low Byte        | 2D  |

The complete response data frame is: 01 05 00 06 00 00 2D CB

---

#### 1.2.2.8 CORE Write Turn OFF Relay Driver 8

The Relay Module (Slave) shall turn OFF the relay driver 8 when CORE (Master) sends the following message.








| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 07 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 0B |
| CRC-16 - Low Byte        | 7C  |

The complete request data frame is: 01 05 00 07 00 00 7C 0B

The Relay Module (Slave) shall respond back to CORE (Master) with the following message when the request is accepted.

| Setting                  | Value (HEX)                          |
| ------------------------ | ------------------------------------ |
| Slave Address                 | 01 |
| Function Code            | 05 |
| Coil Address - High Byte | 00 |
| Coil Address - Low Byte  | 07 |
| Coil Value - High Byte   | 00 |
| Coil Value - Low Byte    | 00 |
| CRC-16 - High Byte       | 0B |
| CRC-16 - Low Byte        | 7C  |

The complete response data frame is: 01 05 00 07 00 00 7C 0B

---

## 1.3 CORE Read

---

### 1.3.1 CORE Read Status

---

#### 1.3.1.1 CORE Read Status Module Initializing

The Relay Module (Slave) shall report its status when CORE (Master) sends the following message.










| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the status "INITIALIZING", if in such state, using the following message.









| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | 00 |
| CRC-16 - High Byte                | 30 |
| CRC-16 - Low Byte                 | B9  |

The complete response data frame is: 01 04 02 00 00 B9 30

---

#### 1.3.1.2 CORE Read Status Module Ready

The Relay Module (Slave) shall report its status when CORE (Master) sends the following message.












| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the status "READY", if in such state, using the following message.











| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | 01 |
| CRC-16 - High Byte                | F0 |
| CRC-16 - Low Byte                 | 78  |

The complete response data frame is: 01 04 02 00 01 78 F0

---

#### 1.3.1.3 CORE Read Status Module Operating

The Relay Module (Slave) shall report its status when CORE (Master) sends the following message.













| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the status "OPERATING", if in such state, using the following message.












| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | 02 |
| CRC-16 - High Byte                | F1 |
| CRC-16 - Low Byte                 | 38  |

The complete response data frame is: 01 04 02 00 02 38 F1

---

#### 1.3.1.4 CORE Read Status Module Warning

The Relay Module (Slave) shall report its status when CORE (Master) sends the following message.














| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the status "WARNING", if in such state, using the following message.













| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | 03 |
| CRC-16 - High Byte                | 31 |
| CRC-16 - Low Byte                 | F9  |

The complete response data frame is: 01 04 02 00 03 F9 31

---

#### 1.3.1.5 CORE Read Status Module Fault

The Relay Module (Slave) shall report its status when CORE (Master) sends the following message.














| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the status "FAULT", if in such state, using the following message.













| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | 04 |
| CRC-16 - High Byte                | F3 |
| CRC-16 - Low Byte                 | B8  |

The complete response data frame is: 01 04 02 00 04 B8 F3

---

#### 1.3.1.6 CORE Read Status Module Maintenance

The Relay Module (Slave) shall report its status when CORE (Master) sends the following message.














| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the status "MAINTENANCE", if in such state, using the following message.













| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | 05 |
| CRC-16 - High Byte                | 33 |
| CRC-16 - Low Byte                 | 79  |

The complete response data frame is: 01 04 02 00 05 79 33

---

#### 1.3.1.7 CORE Read Status Module Offline

The Relay Module (Slave) shall report its status when CORE (Master) sends the following message.














| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the status "OFFLINE", if in such state, using the following message.













| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | 06 |
| CRC-16 - High Byte                | 32 |
| CRC-16 - Low Byte                 | 39  |

The complete response data frame is: 01 04 02 00 06 39 32

---

### 1.3.2 CORE Read Status Relay Driver

---

#### 1.3.2.1 CORE Read Status Relay Driver 1

CORE (Master) shall request to the Realy Module (Slave) the GPIO output state of Relay Driver 1 by sending the following message.















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the GPIO output state of Relay Driver 1 (0 or 1) using the following message.














| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | XX |
| CRC-16 - High Byte                | XX |
| CRC-16 - Low Byte                 | XX  |

The complete response data frame is: 01 04 02 00 XX XX XX

---

#### 1.3.2.2 CORE Read Status Relay Driver 2

CORE (Master) shall request to the Realy Module (Slave) the GPIO output state of Relay Driver 2 by sending the following message.















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the GPIO output state of Relay Driver 2 (0 or 1) using the following message.














| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | XX |
| CRC-16 - High Byte                | XX |
| CRC-16 - Low Byte                 | XX  |

The complete response data frame is: 01 04 02 00 XX XX XX

---

#### 1.3.2.3 CORE Read Status Relay Driver 3

CORE (Master) shall request to the Realy Module (Slave) the GPIO output state of Relay Driver 3 by sending the following message.
















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the GPIO output state of Relay Driver 3 (0 or 1) using the following message.















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | XX |
| CRC-16 - High Byte                | XX |
| CRC-16 - Low Byte                 | XX  |

The complete response data frame is: 01 04 02 00 XX XX XX

---

#### 1.3.2.4 CORE Read Status Relay Driver 4

CORE (Master) shall request to the Realy Module (Slave) the GPIO output state of Relay Driver 4 by sending the following message.
















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the GPIO output state of Relay Driver 4 (0 or 1) using the following message.















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | XX |
| CRC-16 - High Byte                | XX |
| CRC-16 - Low Byte                 | XX  |

The complete response data frame is: 01 04 02 00 XX XX XX

---

#### 1.3.2.5 CORE Read Status Relay Driver 5

CORE (Master) shall request to the Realy Module (Slave) the GPIO output state of Relay Driver 5 by sending the following message.
















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the GPIO output state of Relay Driver 5 (0 or 1) using the following message.















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | XX |
| CRC-16 - High Byte                | XX |
| CRC-16 - Low Byte                 | XX  |

The complete response data frame is: 01 04 02 00 XX XX XX

---

#### 1.3.2.6 CORE Read Status Relay Driver 6

CORE (Master) shall request to the Realy Module (Slave) the GPIO output state of Relay Driver 6 by sending the following message.
















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the GPIO output state of Relay Driver 6 (0 or 1) using the following message.















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | XX |
| CRC-16 - High Byte                | XX |
| CRC-16 - Low Byte                 | XX  |

The complete response data frame is: 01 04 02 00 XX XX XX

---

#### 1.3.2.7 CORE Read Status Relay Driver 7

CORE (Master) shall request to the Realy Module (Slave) the GPIO output state of Relay Driver 7 by sending the following message.
















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the GPIO output state of Relay Driver 7 (0 or 1) using the following message.















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | XX |
| CRC-16 - High Byte                | XX |
| CRC-16 - Low Byte                 | XX  |

The complete response data frame is: 01 04 02 00 XX XX XX

---

#### 1.3.2.8 CORE Read Status Relay Driver 8

CORE (Master) shall request to the Realy Module (Slave) the GPIO output state of Relay Driver 8 by sending the following message.
















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Starting Address - High Byte      | 00 |
| Starting Address - Low Byte       | 00 |
| Quantity of Registers - High Byte | 00 |
| Quantity of Registers - Low Byte  | 01 |
| CRC-16 - High Byte                | CA |
| CRC-16 - Low Byte                 | 31  |

The complete response data frame is: 01 04 00 00 00 01 31 CA

The Relay Module (Slave) shall respond to CORE (Master) with the GPIO output state of Relay Driver 8 (0 or 1) using the following message.















| Setting                           | Value (HEX)                          |
| --------------------------------- | ------------------------------------ |
| Slave Address                     | 01 |
| Function Code                     | 04 |
| Byte Count                        | 02 |
| Register Data - High Byte         | 00 |
| Register Data - Low Byte          | XX |
| CRC-16 - High Byte                | XX |
| CRC-16 - Low Byte                 | XX  |

The complete response data frame is: 01 04 02 00 XX XX XX

---

### 1.3.3 CORE Read Diagnostics

---

### 1.3.4 CORE Read Faults

---

## 1.4 CORE Execute

---

# 2. Module

---

## 2.1 Module Test

---


</body>

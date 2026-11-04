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

### 1.1.1 CORE Communication Software

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

### 1.1.2 CORE Communication Hardware

| Setting            | Value                                |
| ------------------ | ------------------------------------ |
| Physical interface | RS485 |
| Wires              | 2 wires (A, B) |

---

## 1.2 CORE Command

---

### 1.2.1 CORE Command Turn ON Relay Driver

---

#### 1.2.1.1 CORE Command Turn ON Relay Driver 1

| Setting            | Value                                |
| ------------------ | ------------------------------------ |
| Function code      | Write Single Coil (0x05) |

---

## 1.3 CORE Report

---

### 1.3.1 CORE Report Status

---

#### 1.3.1.1 CORE Report Status Initializing

---

# 2. Module

---

## 2.1 Module Test

---


</body>

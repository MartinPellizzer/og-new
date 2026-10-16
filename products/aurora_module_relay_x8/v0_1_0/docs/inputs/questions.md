<head>
<title>
Aurora: Module Relay x8
</title>
<subtitle>
Stakeholders Questions
</subtitle>
</head>
<rev>
Version, Date, Author, Description
0.1.0, 2026-07-02, Martin Pellizzer, Starting version
</rev>
<body>
# Questions

## Question 1
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 1 |
| Stakeholder Role | System Architect |
| Question ID | 1 |
| Question Text | What exactly is the responsibility of the Relay Module within Aurora? |



## Question 2
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 1 |
| Stakeholder Role | System Architect |
| Question ID | 2 |
| Question Text | Which functions of the overall Aurora system are allocated specifically to the Relay Module? |



## Question 3
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 1 |
| Stakeholder Role | System Architect |
| Question ID | 3 |
| Question Text | What behavior does the system require from each of the eight relay outputs? |



## Question 4
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 1 |
| Stakeholder Role | System Architect |
| Question ID | 4 |
| Question Text | What must happen to every relay output when communication with the CORE is lost? |



## Question 5
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 1 |
| Stakeholder Role | System Architect |
| Question ID | 5 |
| Question Text | What is the required system behavior if the Relay Module itself fails? |



## Question 6
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 2 |
| Stakeholder Role | CORE Firmware Engineer |
| Question ID | 6 |
| Question Text | Which responsibilities belong to the CORE and which responsibilities belong to the Relay Module? |



## Question 7
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 2 |
| Stakeholder Role | CORE Firmware Engineer |
| Question ID | 7 |
| Question Text | What commands must the CORE be able to send to the Relay Module? |



## Question 8
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 2 |
| Stakeholder Role | CORE Firmware Engineer |
| Question ID | 8 |
| Question Text | What information must the Relay Module provide back to the CORE? |



## Question 9
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 2 |
| Stakeholder Role | CORE Firmware Engineer |
| Question ID | 9 |
| Question Text | How should the CORE detect that communication with the Relay Module has been lost? |



## Question 10
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 2 |
| Stakeholder Role | CORE Firmware Engineer |
| Question ID | 10 |
| Question Text | What should the CORE do when communication with the Relay Module is lost? |



## Question 11
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 3 |
| Stakeholder Role | Electrical Engineer |
| Question ID | 11 |
| Question Text | What are the electrical specifications of the eight relay-driver outputs, based on the physical relays they must control? |



## Question 12
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 3 |
| Stakeholder Role | Electrical Engineer |
| Question ID | 12 |
| Question Text | What are the electrical characteristics of the physical relay coils connected to each of the eight driver outputs? |



## Question 13
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 3 |
| Stakeholder Role | Electrical Engineer |
| Question ID | 13 |
| Question Text | What is the required input supply voltage range, including tolerances and transient conditions? |



## Question 14
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 3 |
| Stakeholder Role | Electrical Engineer |
| Question ID | 14 |
| Question Text | What protection is required to handle the inductive voltage transient generated when a relay coil is de-energized? |



## Question 15
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 3 |
| Stakeholder Role | Electrical Engineer |
| Question ID | 15 |
| Question Text | What electrical behavior is required during power loss, brownout, and restoration of power? |



## Question 16
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 4 |
| Stakeholder Role | Safety Engineer |
| Question ID | 16 |
| Question Text | What safety functions, if any, are assigned specifically to the Relay Module? |



## Question 17
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 4 |
| Stakeholder Role | Safety Engineer |
| Question ID | 17 |
| Question Text | What is the required safe state for each of the eight relay outputs? |



## Question 18
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 4 |
| Stakeholder Role | Safety Engineer |
| Question ID | 18 |
| Question Text | What shall happen to each relay output when the Relay Module detects an internal fault? |



## Question 19
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 4 |
| Stakeholder Role | Safety Engineer |
| Question ID | 19 |
| Question Text | What shall happen to each relay output when communication with the CORE is lost? |



## Question 20
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 4 |
| Stakeholder Role | Safety Engineer |
| Question ID | 20 |
| Question Text | Which safety decisions must be made by the CORE, and which must be enforced locally by the Relay Module? |



## Question 21
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 5 |
| Stakeholder Role | Process Engineer |
| Question ID | 21 |
| Question Text | What process functions are controlled or influenced by the eight relay outputs of the Relay Module? |



## Question 22
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 5 |
| Stakeholder Role | Process Engineer |
| Question ID | 22 |
| Question Text | What is the required sequence of operations for starting ozone generation? |



## Question 23
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 5 |
| Stakeholder Role | Process Engineer |
| Question ID | 23 |
| Question Text | What is the required sequence of operations for stopping ozone generation? |



## Question 24
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 5 |
| Stakeholder Role | Process Engineer |
| Question ID | 24 |
| Question Text | What conditions must be satisfied before ozone generation is permitted to start? |



## Question 25
| Field              | Value                      |
| ------------------ | -------------------------- |
| Stakeholder ID | 5 |
| Stakeholder Role | Process Engineer |
| Question ID | 25 |
| Question Text | What process conditions require ozone generation to stop immediately? |


</body>

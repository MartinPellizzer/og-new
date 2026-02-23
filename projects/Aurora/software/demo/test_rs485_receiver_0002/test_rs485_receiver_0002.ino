#include <rs485.h>
HardwareSerial serial_rs485(1);
rs485_t rs485 = {};

#define HEARTBEAT_PIN 13
uint32_t heartbeat_millis_cur = 0;

// #define SENSOR1_RE_DE_PIN 16
// HardwareSerial Sensor1(1);
// #define BUFF_LEN 9
// uint8_t buff[BUFF_LEN] = { 0 };

#define MODULE_ID 0x02
#define RELAY_PIN 25


uint16_t modbusCRC(uint8_t *buffer, uint8_t length)
{
  uint16_t crc = 0xFFFF;

  for (uint8_t pos = 0; pos < length; pos++)
  {
    crc ^= (uint16_t)buffer[pos];

    for (int i = 0; i < 8; i++)
    {
      if (crc & 0x0001)
      {
        crc >>= 1;
        crc ^= 0xA001;
      }
      else
      {
        crc >>= 1;
      }
    }
  }

  return crc;
}

void setup() 
{
  Serial.begin(9600);
  
  pinMode(HEARTBEAT_PIN, OUTPUT);
  digitalWrite(HEARTBEAT_PIN, LOW);

  // Serial2.begin(9600, SERIAL_8N1, 27, 14);
  // Sensor1.begin(9600, SERIAL_8N1, 17, 4);  // RO, DI

  // pinMode(SENSOR1_RE_DE_PIN, OUTPUT);
  // digitalWrite(SENSOR1_RE_DE_PIN, LOW);
  
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  serial_rs485.begin(9600, SERIAL_8N1, rs485.pin_tx, rs485.pin_rx);
  pinMode(rs485.pin_re_de, OUTPUT);
  digitalWrite(rs485.pin_re_de, LOW);
  
  rs485_init(&rs485);
  
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);

}

void loop() 
{
  rs485_read(&rs485, serial_rs485);
  if (rs485.receiver_buffer_ready == 0x01)
  {
    if (rs485.receiver_buffer[0] == MODULE_ID)
    {
      Serial.println("ID: VALID");
      uint16_t crc = modbusCRC(rs485.receiver_buffer, 6);
    
      // Append CRC (LOW byte first!)
      uint8_t crc_high = (crc >> 8) & 0xFF;  // CRC High
      uint8_t crc_low = crc & 0xFF;         // CRC Low
      
      if (rs485.receiver_buffer[6] == crc_low && rs485.receiver_buffer[7] == crc_high)
      {
        Serial.println("CRC: VALID");

        uint8_t function_code = rs485.receiver_buffer[1];
        if (function_code == 0x05)
        {
          Serial.println("FUNCTION: VALID");

          uint8_t coil_high = rs485.receiver_buffer[2];
          uint8_t coil_low = rs485.receiver_buffer[3];

          if (coil_low == 0x00 && coil_high == 0x00)
          {
            Serial.println("COIL: VALID");

            uint8_t value_high = rs485.receiver_buffer[4];
            uint8_t value_low = rs485.receiver_buffer[5];

            if (value_high == 0xFF && value_low == 0x00)
            {
              Serial.println("VALUE: VALID ON");
              digitalWrite(RELAY_PIN, HIGH);
            }
            else if (value_high == 0x00 && value_low == 0x00)
            {
              Serial.println("VALUE: VALID OFF");
              digitalWrite(RELAY_PIN, LOW);
            }
            else
            {
              Serial.println("VALUE: FAIL");
            }
          }
          else
          {
            Serial.println("COIL: FAIL");
          }
        }
        else
        {
          Serial.println("FUNCTION: FAILED");
        }
      }
      else
      {
        Serial.println("CRC: FAILED");
      }
    } 
    else
    {
      Serial.println("ID: FALIED");
    } 

    rs485_receiver_buffer_debug(&rs485);
    rs485_receiver_buffer_clear(&rs485);
    
    // rs485_write(&rs485, serial_rs485);
    // rs485_sender_buffer_debug(&rs485);
    // rs485_sender_buffer_clear(&rs485);

    rs485.receiver_buffer_ready = 0;
  }
  
  if (millis() - heartbeat_millis_cur > 1000)
  {
    heartbeat_millis_cur = millis();
    digitalWrite(HEARTBEAT_PIN, !(digitalRead(HEARTBEAT_PIN)));
  }
}

#include <rs485.h>

HardwareSerial serial_rs485(1);

rs485_t rs485 = {};

// HardwareSerial Sender(1);
uint8_t state = 0;

uint8_t buff[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;

uint32_t timer = 0;

uint32_t timer_test = 0;

#define RE_DE_PIN 16

void setup() 
{
  Serial.begin(9600);
  // Serial2.begin(9600, SERIAL_8N1, 27, 14);
  // Sender.begin(9600, SERIAL_8N1, 17, 4);
  // pinMode(RE_DE_PIN, OUTPUT);

  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  serial_rs485.begin(9600, SERIAL_8N1, rs485.pin_tx, rs485.pin_rx);
  pinMode(rs485.pin_re_de, OUTPUT);
  digitalWrite(rs485.pin_re_de, LOW);
  
  rs485_init(&rs485);
}

void loop() 
{
  // transmit
  if (rs485.state_transmission == 1)
  {
    if (millis() - timer_test > 1000)
    {
      timer_test = millis();

      rs485.sender_buffer[0] = 123;
      rs485_write(&rs485, serial_rs485);
      rs485_sender_buffer_debug(&rs485);
      rs485_sender_buffer_clear(&rs485);
      
      rs485.state_transmission = 0;
      rs485.state_transmission_timer_millis = millis();
    }
  }
  // receive
  if (rs485.state_transmission == 0)
  {
    rs485_read(&rs485, serial_rs485);
    if (rs485.receiver_buffer_ready == 1)
    {
      rs485_receiver_buffer_debug(&rs485);
      int ack = rs485_receiver_buffer_ack(&rs485);
      if (ack == 1)
      {
        Serial.println("***********************************");
        Serial.println("OK: ACK VALID");
        Serial.println("***********************************");
        // modules[modules_i].online_cur = 1;
        // if (modules[modules_i].id == 1)
        // {
        //   modules[modules_i].value_cur = rs485.receiver_buffer[3];
        // }
      }
      rs485_receiver_buffer_clear(&rs485);
      rs485.receiver_buffer_ready = 0;
      rs485.state_transmission = 1;

      Serial.println();
      Serial.println();
    }
    rs485_read_timeout(&rs485);
    if (rs485.read_timeout_cur == 1)
    {
      rs485.read_timeout_cur = 0;
      // modules[modules_i].online_cur = 0;
      Serial.println("***********************************");
      Serial.println("ERR: ACK TIMEOUT");
      Serial.println("***********************************");
      Serial.println();
      Serial.println();
    }
  }
}


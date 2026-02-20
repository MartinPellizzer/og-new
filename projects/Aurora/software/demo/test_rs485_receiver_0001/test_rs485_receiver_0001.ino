#include <rs485.h>
HardwareSerial serial_rs485(1);
rs485_t rs485 = {};

// #define SENSOR1_RE_DE_PIN 16
// HardwareSerial Sensor1(1);
// #define BUFF_LEN 9
// uint8_t buff[BUFF_LEN] = { 0 };

void setup() 
{
  Serial.begin(9600);
  // Serial2.begin(9600, SERIAL_8N1, 27, 14);
  // Sensor1.begin(9600, SERIAL_8N1, 17, 4);  // RO, DI

  // pinMode(SENSOR1_RE_DE_PIN, OUTPUT);
  // digitalWrite(SENSOR1_RE_DE_PIN, LOW);
  
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  serial_rs485.begin(9600, SERIAL_8N1, rs485.pin_tx, rs485.pin_rx);
  pinMode(rs485.pin_re_de, OUTPUT);
  digitalWrite(rs485.pin_re_de, LOW);
  
  rs485_init(&rs485);
}

void loop() 
{
  rs485_read(&rs485, serial_rs485);
  if (rs485.receiver_buffer_ready == 1)
  {
    rs485_receiver_buffer_debug(&rs485);
    rs485_receiver_buffer_clear(&rs485);
    
    rs485.sender_buffer[0] = 0xFF;
    rs485.sender_buffer[1] = 0xFF;
    rs485.sender_buffer[2] = 0xFF;
    rs485_write(&rs485, serial_rs485);
    rs485_sender_buffer_debug(&rs485);
    rs485_sender_buffer_clear(&rs485);

    rs485.receiver_buffer_ready = 0;
  }
}

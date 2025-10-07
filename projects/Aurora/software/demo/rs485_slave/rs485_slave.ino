HardwareSerial serial_rs485(1);
typedef struct rs485_t {
  uint8_t PIN_RE_DE = 16;
  uint8_t PIN_TX = 17;
  uint8_t PIN_RX = 4;
  uint32_t new_data_state = 0;
  uint32_t new_data_timer = 0;
  uint8_t new_data_buffer[9] = {0};
  uint8_t new_data_buffer_i = 0;
} rs485_t;
rs485_t rs485 = {};

uint32_t timer_test = 0;

void rs485_read()
{
  if (rs485.new_data_state)
  {
    if (millis() - rs485.new_data_timer > 40)
    {
      rs485.new_data_buffer_i = 0;
      rs485.new_data_state = 0;
      Serial.println(rs485.new_data_buffer[0]);

      // NEXTION PRINT
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x30, 0x22, 0xff, 0xff, 0xff };
      _buffer[8] = (rs485.new_data_buffer[0]) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }

    }
  }
  
  if (serial_rs485.available() > 0)  
  {
    uint8_t c = serial_rs485.read();
    rs485.new_data_buffer[rs485.new_data_buffer_i] = c;
    rs485.new_data_buffer_i++;
    rs485.new_data_state = 1;
    rs485.new_data_timer = millis();
  }
}

void rs485_write()
{
    digitalWrite(rs485.PIN_RE_DE, HIGH);
    serial_rs485.write(2);
    delay(10);
    digitalWrite(rs485.PIN_RE_DE, LOW);
}

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  serial_rs485.begin(9600, SERIAL_8N1, rs485.PIN_TX, rs485.PIN_RX);
  pinMode(rs485.PIN_RE_DE, OUTPUT);
  digitalWrite(rs485.PIN_RE_DE, LOW);
}

void loop()
{
  rs485_read();
  // if (millis() - timer_test > 1000)
  // {
  //   timer_test = millis();
  //   rs485_write();
  // }
}


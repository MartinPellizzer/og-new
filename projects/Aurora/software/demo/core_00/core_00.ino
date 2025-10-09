HardwareSerial serial_rs485(1);
typedef struct rs485_t {
  uint8_t PIN_RE_DE = 16;
  uint8_t PIN_TX = 17;
  uint8_t PIN_RX = 4;
  uint32_t new_data_state = 0;
  uint32_t new_data_timer = 0;
  uint8_t sender_buffer[9] = {0};
  uint8_t sender_buffer_i = 0;
  uint8_t receiver_buffer[9] = {0};
  uint8_t receiver_buffer_i = 0;
  uint8_t receiver_buffer_ready = 0;
  int8_t state_transmission = 1;
  uint32_t state_transmission_timer_millis = 0;
} rs485_t;
rs485_t rs485 = {};

uint32_t timer_test = 0;

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  serial_rs485.begin(9600, SERIAL_8N1, rs485.PIN_TX, rs485.PIN_RX);
  pinMode(rs485.PIN_RE_DE, OUTPUT);
  digitalWrite(rs485.PIN_RE_DE, LOW);
}

int counter = 0;
int module_01_test_digit = 0;
uint32_t nextion_print_millis = 0;

void nextion_print()
{
  if (millis() - nextion_print_millis > 1000)
  {
    nextion_print_millis = millis();
    {
      uint8_t _buffer[] = { 0x74, 0x30, 0x2E, 0x74, 0x78, 0x74, 0x3D, 0x22, 0x4D, 0x4F, 0x44, 0x20, 0x30, 0x31, 0x3A, 0x20, 0x4F, 0x4E, 0x22, 0xff, 0xff, 0xff};
      _buffer[1] = (0) + 0x30;
      _buffer[13] = (0) + 0x30;
      for (uint8_t i = 0; i < sizeof(_buffer) / sizeof(uint8_t); i++) 
      {
        Serial2.write(_buffer[i]);
      }
    }
  }
}

void loop()
{
  // SET WRITE BUFFER
  if (millis() - timer_test > 1000)
  {
    timer_test = millis();
    counter += 1;
    if (counter > 9) counter = 0;
    {
      rs485.sender_buffer[1] = counter;
    }
  }

  rs485_manager();
  nextion_print();
}


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

void rs485_write(int digit)
{
    digitalWrite(rs485.PIN_RE_DE, HIGH);
    serial_rs485.write(digit);
    delay(10);
    digitalWrite(rs485.PIN_RE_DE, LOW);
}

void setup() 
{
  Serial.begin(9600);
  serial_rs485.begin(9600, SERIAL_8N1, rs485.PIN_TX, rs485.PIN_RX);
  pinMode(rs485.PIN_RE_DE, OUTPUT);
  digitalWrite(rs485.PIN_RE_DE, LOW);
}

int counter = 0;
void loop()
{
  // rs485_read();
  if (millis() - timer_test > 1000)
  {
    timer_test = millis();
    counter += 1;
    if (counter > 9) counter = 0;
    rs485_write(counter);
  }
}


#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

#define MODULE_ID 0

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
      for (int i = 0; i < 9; i++)
      {
        Serial.println(rs485.new_data_buffer[i]);
      }

      if (rs485.new_data_buffer[0] == MODULE_ID)
      {
        // LCD PRINT
        lcd.setCursor(0, 0);
        lcd.print("ID: ");
        lcd.print(MODULE_ID);
        lcd.setCursor(0, 1);
        lcd.print(rs485.new_data_buffer[1]);
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

  lcd.init();
  lcd.backlight();

  // lcd.setCursor(0, 0);
  // lcd.print("                ");
  // lcd.setCursor(0, 0);
  // lcd.print("PREMERE PULSANTE");
  // lcd.setCursor(0, 1);
  // lcd.print("                ");
  // lcd.setCursor(0, 1);
  // lcd.print("PER SANIFICARE");
}

void loop()
{
  rs485_read();
}


#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

#define MODULE_ID 1
#define RELAY_PIN 12

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
  int8_t state_transmission = 0;
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

  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);

  lcd.init();
  lcd.backlight();

  // LCD PRINT
  lcd.setCursor(0, 0);
  lcd.print("ID: ");
  lcd.print(MODULE_ID);
}

void loop()
{
  rs485_manager();
}


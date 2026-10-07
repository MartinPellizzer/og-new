// MASTER

#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

HardwareSerial Sender(1);
uint8_t state = 0;

uint8_t buff[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;

uint32_t timer = 0;

#define RE_DE_PIN 16


uint8_t count = 0;

void setup() 
{
  Serial.begin(9600);
  Sender.begin(9600, SERIAL_8N1, 17, 4);
  pinMode(RE_DE_PIN, OUTPUT);

  lcd.init();
  lcd.backlight();
}

void loop()
{
  delay(1000);
  count += 1;

  lcd.setCursor(0, 0);
  lcd.print("                ");
  lcd.setCursor(0, 0);
  lcd.print(count);
  
  // send serially
  digitalWrite(RE_DE_PIN, HIGH);
  for(int k = 0; k < 9; k++)
  {
    Sender.write(count);
  }
  delay(10);
}


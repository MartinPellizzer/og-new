// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6) 
const int potPin = 34;

// variable for storing the potentiometer value
int potValue = 0;


#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

uint32_t timer_test = 0;

void setup() {
  Serial.begin(9600);
  delay(1000);

  lcd.init();
  lcd.backlight();
}

void loop() {
  if (millis() - timer_test > 500)
  {
    timer_test = millis();

    potValue = analogRead(potPin);
    Serial.println(potValue);

    // clear lcd
    lcd.setCursor(0, 0);
    lcd.print("                ");
    lcd.setCursor(0, 1);
    lcd.print("                ");

    // display_debug_serial();

    lcd.setCursor(0, 0);
    lcd.print(potValue);
  }
}
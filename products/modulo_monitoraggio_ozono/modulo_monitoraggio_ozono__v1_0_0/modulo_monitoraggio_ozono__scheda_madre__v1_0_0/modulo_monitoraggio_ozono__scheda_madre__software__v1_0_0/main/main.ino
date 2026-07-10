// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6) 
const int PIN_1 = 34;
const int PIN_2 = 35;
const int PIN_3 = 32;
const int PIN_4 = 33;

// variable for storing the potentiometer value
int sens_val_1 = 0;
int sens_val_2 = 0;
int sens_val_3 = 0;
int sens_val_4 = 0;

#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

uint32_t timer_test = 0;

void setup()
{
  Serial.begin(9600);
  delay(1000);

  lcd.init();
  lcd.backlight();
}

void loop()
{
  if (millis() - timer_test > 500)
  {
    timer_test = millis();

    sens_val_1 = analogRead(PIN_1);
    Serial.println(sens_val_1);
    sens_val_2 = analogRead(PIN_2);
    Serial.println(sens_val_2);
    sens_val_3 = analogRead(PIN_3);
    Serial.println(sens_val_3);
    sens_val_4 = analogRead(PIN_4);
    Serial.println(sens_val_4);

    // clear lcd
    lcd.setCursor(0, 0);
    lcd.print("                ");
    lcd.setCursor(0, 1);
    lcd.print("                ");

    // display_debug_serial();

    lcd.setCursor(0, 0);
    lcd.print(sens_val_1);
    lcd.setCursor(0, 1);
    lcd.print(sens_val_2);
    lcd.setCursor(6, 0);
    lcd.print(sens_val_3);
    lcd.setCursor(6, 1);
    lcd.print(sens_val_4);

    Serial.println();
  }
}

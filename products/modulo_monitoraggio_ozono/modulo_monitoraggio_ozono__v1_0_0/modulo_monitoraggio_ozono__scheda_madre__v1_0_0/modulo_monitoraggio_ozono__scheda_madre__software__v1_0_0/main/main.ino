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

#define BUFFER_LEN 10
int buffer[BUFFER_LEN] = {0};
int buffer_index = 0;

uint32_t timer_test = 0;

void setup()
{
  Serial.begin(9600);
  delay(1000);

  lcd.init();
  lcd.backlight();
}

void buffer_print()
{
  for (int i = 0; i < BUFFER_LEN; i++)
  {
    Serial.print(buffer[i]);
    Serial.print(", ");
  }
  Serial.println();
}

void buffer_add(int val)
{
  buffer[buffer_index] = val;
  buffer_index += 1;
  if (buffer_index >= 10) buffer_index = 0;
}

int buffer_avg()
{
  int sum = 0;
  for (int i = 0; i < BUFFER_LEN; i++)
  {
    sum += buffer[i];
  }
  int avg = int(sum / BUFFER_LEN);
  return avg;
}

void loop()
{
  if (millis() - timer_test > 500)
  {
    timer_test = millis();

    // sens_val_1 = analogRead(PIN_1);
    // sens_val_2 = analogRead(PIN_2);
    sens_val_3 = analogRead(PIN_3);
    sens_val_4 = analogRead(PIN_4);

    buffer_add(sens_val_4);
    int avg = buffer_avg();
    buffer_print();

    // clear lcd
    lcd.setCursor(0, 0);
    lcd.print("                ");
    lcd.setCursor(0, 1);
    lcd.print("                ");

    // lcd.setCursor(0, 0);
    // lcd.print(sens_val_1);
    // lcd.setCursor(0, 1);
    // lcd.print(sens_val_2);
    lcd.setCursor(6, 0);
    lcd.print(avg);
    lcd.setCursor(6, 1);
    lcd.print(sens_val_4);

    // Serial.println(sens_val_1);
    // Serial.println(sens_val_2);
    Serial.println(avg);
    Serial.println(sens_val_4);
    Serial.println();
  }
}

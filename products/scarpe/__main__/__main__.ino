#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

#define COMPRESSOR_GPIO 5
#define OZONE_GENERATOR_GPIO 18
#define BUTTON_GPIO 19
#define SWITCH_GPIO 23
#define LIGHT_GPIO 12

int32_t cycle_millis = 0;
int32_t cycle_state = -1;


int32_t lcd_millis = 0;
int32_t lcd_seconds = 0;

void setup() 
{
  Serial.begin(9600);
  
  pinMode(BUTTON_GPIO, INPUT_PULLUP);
  pinMode(SWITCH_GPIO, INPUT_PULLUP);

  pinMode(COMPRESSOR_GPIO, OUTPUT);
  digitalWrite(COMPRESSOR_GPIO, LOW);
  pinMode(OZONE_GENERATOR_GPIO, OUTPUT);
  digitalWrite(OZONE_GENERATOR_GPIO, LOW);
  pinMode(LIGHT_GPIO, OUTPUT);
  digitalWrite(LIGHT_GPIO, LOW);

  lcd.init();
  lcd.backlight();

  lcd.setCursor(3,0);
  lcd.print("Hello, world!");
  lcd.setCursor(2,1);
  lcd.print("Ywrobot Arduino!");
  lcd.setCursor(0,2);
  lcd.print("Arduino LCM IIC 2004");
  lcd.setCursor(2,3);
  lcd.print("Power By Ec-yuan!");
}

int8_t button_state_old = 0;
int8_t button_state_tmp = 0;
int8_t button_state_cur = 0;
int32_t button_millis = 0;
uint8_t button_state_updated = 0;

int8_t switch_state_old = 0;
int8_t switch_state_tmp = 0;
int8_t switch_state_cur = 0;
int32_t switch_millis = 0;
uint8_t switch_state_updated = 0;

int8_t light_state_cur = 0;
int32_t light_millis = 0;

void loop()
{
  Serial.println(cycle_state);

  // if (millis() - light_millis > 3000)
  // {
  //   light_millis = millis();
  //   light_state_cur = !light_state_cur;
  //   digitalWrite(LIGHT_GPIO, light_state_cur);
  // }

  // button read
  button_state_tmp = digitalRead(BUTTON_GPIO);
  // Serial.print("BUTTON: ");
  // Serial.println(button_state_tmp);
  if (button_state_old != button_state_tmp)
  {
    button_state_old = button_state_tmp;
    if (millis() - button_millis > 4)
    {
      button_millis = millis();
      button_state_cur = button_state_tmp;
      button_state_updated = 1;
    }
  }
  
  // switch read
  switch_state_tmp = digitalRead(SWITCH_GPIO);
  // Serial.print("SWITCH: ");
  // Serial.println(switch_state_tmp);
  if (switch_state_old != switch_state_tmp)
  {
    switch_state_old = switch_state_tmp;
    if (millis() - switch_millis > 4)
    {
      switch_millis = millis();
      switch_state_cur = switch_state_tmp;
      switch_state_updated = 1;
    }
  }

  if (button_state_updated == 1 || switch_state_updated == 1) 
  {
    button_state_updated = 0;
    switch_state_updated = 0;
    if (switch_state_cur == 1) 
    {
      if (button_state_cur == 1) 
      {
        if (cycle_state == -1)
        {
          cycle_state = 0;
          cycle_millis = millis();
          digitalWrite(LIGHT_GPIO, HIGH);
        }
        else
        {
          cycle_state = -1;
          cycle_millis = millis();
          digitalWrite(COMPRESSOR_GPIO, LOW);
          digitalWrite(OZONE_GENERATOR_GPIO, LOW);
          digitalWrite(LIGHT_GPIO, LOW);
        }
      }
    }
    else
    {
      cycle_state = -1;
      cycle_millis = millis();
      digitalWrite(COMPRESSOR_GPIO, LOW);
      digitalWrite(OZONE_GENERATOR_GPIO, LOW);
      digitalWrite(LIGHT_GPIO, LOW);
    }
  }

  if (cycle_state == 0)
  {
    if (millis() - cycle_millis > 1000)
    {
      cycle_millis = millis();
      cycle_state = 1;
      digitalWrite(COMPRESSOR_GPIO, HIGH);
    }
  }

  if (cycle_state == 1)
  {
    if (millis() - cycle_millis > 6000)
    {
      cycle_millis = millis();
      cycle_state = 2;
      digitalWrite(COMPRESSOR_GPIO, LOW);
      digitalWrite(OZONE_GENERATOR_GPIO, HIGH);
    }
  }
  
  if (cycle_state == 2)
  {
    if (millis() - cycle_millis > 15000)
    {
      cycle_millis = millis();
      cycle_state = 3;
      digitalWrite(OZONE_GENERATOR_GPIO, LOW);
    }
  }
  
  if (cycle_state == 3)
  {
    if (millis() - cycle_millis > 15000)
    {
      cycle_millis = millis();
      cycle_state = 4;
      digitalWrite(OZONE_GENERATOR_GPIO, HIGH);
    }
  }
  
  if (cycle_state == 4)
  {
    if (millis() - cycle_millis > 15000)
    {
      cycle_millis = millis();
      cycle_state = 5;
      digitalWrite(OZONE_GENERATOR_GPIO, LOW);
    }
  }
  
  if (cycle_state == 5)
  {
    if (millis() - cycle_millis > 15000)
    {
      cycle_millis = millis();
      cycle_state = 6;
      digitalWrite(OZONE_GENERATOR_GPIO, HIGH);
    }
  }
  
  if (cycle_state == 6)
  {
    if (millis() - cycle_millis > 15000)
    {
      cycle_millis = millis();
      cycle_state = 7;
      digitalWrite(OZONE_GENERATOR_GPIO, LOW);
    }
  }
  
  if (cycle_state == 7)
  {
    if (millis() - cycle_millis > 6000)
    {
      cycle_millis = millis();
      cycle_state = -1;
      digitalWrite(COMPRESSOR_GPIO, LOW);
      digitalWrite(OZONE_GENERATOR_GPIO, LOW);
      digitalWrite(LIGHT_GPIO, LOW);
    }
  }



  // draw lcd
  if (cycle_state == 1)
  {
    if (millis() - lcd_millis > 1000)
    {
      lcd_millis = millis();
      lcd.setCursor(0,0);
      lcd.print(lcd_seconds);
      lcd_seconds += 1;
    }
  }

  
  // Serial.print("MISO 19: ");
  // Serial.println(digitalRead(BUTTON_GPIO));
  // Serial.print("MOSI 23: ");
  // Serial.println(digitalRead(SWITCH_GPIO));
  // Serial.println();
}
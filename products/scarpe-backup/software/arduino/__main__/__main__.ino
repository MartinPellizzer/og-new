#include <LiquidCrystal_I2C.h>
int lcdColumns = 16;
int lcdRows = 2;
LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);  

uint32_t starting_millis_curr = 0;

uint8_t fan_pin = 13;
uint32_t fan_millis_curr = 0;
uint32_t fan_millis_timer = 3000;

uint8_t ozone_pin = 2;
uint32_t ozone_1_millis_curr = 0;
uint32_t ozone_1_rest_millis_curr = 0;

uint8_t humidity_pin = 5;
uint32_t humidity_millis_curr = 0;
uint32_t humidity_rest_millis_curr = 0;

uint32_t ozone_2_millis_curr = 0;
uint32_t ozone_2_rest_millis_curr = 0;


uint32_t button_debounce_millis_curr = 0;


enum cycle_state_enum {
  OFF, STARTING, FAN, 
  OZONE_1, OZONE_1_REST, 
  HUMIDITY, HUMIDITY_REST, 
  OZONE_2, OZONE_2_REST,
  END
};
cycle_state_enum cycle_state = OFF;

uint8_t state_curr = 0;



void setup()
{
  lcd.init();
  lcd.backlight();

  pinMode(fan_pin, OUTPUT);
  pinMode(ozone_pin, OUTPUT);
  pinMode(humidity_pin, OUTPUT);
  
  pinMode(25, OUTPUT);
  pinMode(26, INPUT);

  digitalWrite(25, 1);

  Serial.begin(9600);
}

int lcd_refresh = 1;

uint32_t seconds = 0;
uint32_t seconds_millis_curr = 0;

int cycle_on = 0;

int button_pressed_oneshot = 0;

void loop()
{
  int button_state = digitalRead(26);
  if (button_state == 0)
  {
    button_pressed_oneshot = 0;
    button_debounce_millis_curr = millis();
  }
  else
  {
    if (button_pressed_oneshot == 0)
    {
      if ((millis() - button_debounce_millis_curr) > 40)
      {
        button_pressed_oneshot = 1;
        Serial.println("clicked");
        
        if (cycle_state == OFF) 
        {
          cycle_state = STARTING;
          Serial.println("STARTING STATE");
          starting_millis_curr = millis();
          seconds_millis_curr = millis();
          seconds = 0;
          lcd_refresh = 1;
        }
        else
        {
          digitalWrite(fan_pin, 0);
          digitalWrite(ozone_pin, 0);
          digitalWrite(humidity_pin, 0);
          cycle_state = OFF;
          Serial.println("OFF STATE");
          lcd_refresh = 1;
        }
      }
    }
  }
  
  if (cycle_state == OFF) 
  {
    if (lcd_refresh)
    {
      lcd_refresh = 0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("OFF");
    }
  }
  
  if (cycle_state == STARTING) 
  {
    if (lcd_refresh)
    {
      lcd_refresh = 0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("STARTING");
      lcd.setCursor(0, 1);
      lcd.print(3);
    }
    if ((millis() - seconds_millis_curr) > 1000) 
    {
        seconds_millis_curr = millis();
        seconds += 1;
        int32_t countdown = 3 - seconds;
        if (countdown < 0) {countdown = 0;}
        lcd.setCursor(0, 1);
        lcd.print("                ");
        lcd.setCursor(0, 1);
        lcd.print(countdown);
    }
    if ((millis() - starting_millis_curr) > 3000) 
    {
      digitalWrite(fan_pin, 1);
      cycle_state = FAN;
      Serial.println("FAN STATE");
      fan_millis_curr = millis();
      seconds_millis_curr = millis();
      seconds = 0;
      lcd_refresh = 1;
    }
  }
  if (cycle_state == FAN) 
  {
    if (lcd_refresh)
    {
      lcd_refresh = 0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("VENTOLA");
      lcd.setCursor(0, 1);
      lcd.print(3);
    }
    if ((millis() - seconds_millis_curr) > 1000) 
    {
        seconds_millis_curr = millis();
        seconds += 1;
        int32_t countdown = 3 - seconds;
        if (countdown < 0) {countdown = 0;}
        lcd.setCursor(0, 1);
        lcd.print("                ");
        lcd.setCursor(0, 1);
        lcd.print(countdown);
    }
    if ((millis() - fan_millis_curr) > 3000) 
    {
      digitalWrite(ozone_pin, 1);
      cycle_state = OZONE_1;
      Serial.println("OZONE_1 STATE");
      ozone_1_millis_curr = millis();
      seconds_millis_curr = millis();
      seconds = 0;
      lcd_refresh = 1;
    }
  }
  if (cycle_state == OZONE_1) 
  {
    if (lcd_refresh)
    {
      lcd_refresh = 0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("OZONO 1 ON");
      lcd.setCursor(0, 1);
      lcd.print(10);
    }
    if ((millis() - seconds_millis_curr) > 1000) 
    {
        seconds_millis_curr = millis();
        seconds += 1;
        int32_t countdown = 10 - seconds;
        if (countdown < 0) {countdown = 0;}
        lcd.setCursor(0, 1);
        lcd.print("                ");
        lcd.setCursor(0, 1);
        lcd.print(countdown);
    }
    if ((millis() - ozone_1_millis_curr) > 10000) 
    {
      digitalWrite(ozone_pin, 0);
      cycle_state = OZONE_1_REST;
      Serial.println("OZONE_1_REST STATE");
      ozone_1_rest_millis_curr = millis();
      seconds_millis_curr = millis();
      seconds = 0;
      lcd_refresh = 1;
    }
  }
  if (cycle_state == OZONE_1_REST) 
  {
    if (lcd_refresh)
    {
      lcd_refresh = 0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("OZONO 1 OFF");
      lcd.setCursor(0, 1);
      lcd.print(3);
    }
    if ((millis() - seconds_millis_curr) > 1000) 
    {
        seconds_millis_curr = millis();
        seconds += 1;
        int32_t countdown = 3 - seconds;
        if (countdown < 0) {countdown = 0;}
        lcd.setCursor(0, 1);
        lcd.print("                ");
        lcd.setCursor(0, 1);
        lcd.print(countdown);
    }
    if ((millis() - ozone_1_rest_millis_curr) > 3000) 
    {
      digitalWrite(humidity_pin, 1);
      cycle_state = HUMIDITY;
      Serial.println("HUMIDITY STATE");
      humidity_millis_curr = millis();
      seconds_millis_curr = millis();
      seconds = 0;
      lcd_refresh = 1;
    }
  }
  if (cycle_state == HUMIDITY) 
  {
    if (lcd_refresh)
    {
      lcd_refresh = 0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("UMIDITA' ON");
      lcd.setCursor(0, 1);
      lcd.print(10);
    }
    if ((millis() - seconds_millis_curr) > 1000) 
    {
        seconds_millis_curr = millis();
        seconds += 1;
        int32_t countdown = 10 - seconds;
        if (countdown < 0) {countdown = 0;}
        lcd.setCursor(0, 1);
        lcd.print("                ");
        lcd.setCursor(0, 1);
        lcd.print(countdown);
    }
    if ((millis() - humidity_millis_curr) > 10000) 
    {
      digitalWrite(humidity_pin, 0);
      cycle_state = HUMIDITY_REST;
      Serial.println("HUMIDITY_REST STATE");
      humidity_rest_millis_curr = millis();
      seconds_millis_curr = millis();
      seconds = 0;
      lcd_refresh = 1;
    }
  }
  if (cycle_state == HUMIDITY_REST) 
  {
    if (lcd_refresh)
    {
      lcd_refresh = 0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("UMIDITA' OFF");
      lcd.setCursor(0, 1);
      lcd.print(3);
    }
    if ((millis() - seconds_millis_curr) > 1000) 
    {
        seconds_millis_curr = millis();
        seconds += 1;
        int32_t countdown = 3 - seconds;
        if (countdown < 0) {countdown = 0;}
        lcd.setCursor(0, 1);
        lcd.print("                ");
        lcd.setCursor(0, 1);
        lcd.print(countdown);
    }
    if ((millis() - humidity_rest_millis_curr) > 3000) 
    {
      digitalWrite(ozone_pin, 1);
      cycle_state = OZONE_2;
      Serial.println("OZONE_2 STATE");
      ozone_2_millis_curr = millis();
      seconds_millis_curr = millis();
      seconds = 0;
      lcd_refresh = 1;
    }
  }
  if (cycle_state == OZONE_2) 
  {
    if (lcd_refresh)
    {
      lcd_refresh = 0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("OZONO 2 ON");
      lcd.setCursor(0, 1);
      lcd.print(10);
    }
    if ((millis() - seconds_millis_curr) > 1000) 
    {
        seconds_millis_curr = millis();
        seconds += 1;
        int32_t countdown = 10 - seconds;
        if (countdown < 0) {countdown = 0;}
        lcd.setCursor(0, 1);
        lcd.print("                ");
        lcd.setCursor(0, 1);
        lcd.print(countdown);
    }
    if ((millis() - ozone_2_millis_curr) > 10000) 
    {
      digitalWrite(ozone_pin, 0);
      cycle_state = OZONE_2_REST;
      Serial.println("OZONE_2_REST STATE");
      ozone_2_rest_millis_curr = millis();
      seconds_millis_curr = millis();
      seconds = 0;
      lcd_refresh = 1;
    }
  }
  if (cycle_state == OZONE_2_REST) 
  {
    if (lcd_refresh)
    {
      lcd_refresh = 0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("OZONO 2 OFF");
      lcd.setCursor(0, 1);
      lcd.print(3);
    }
    if ((millis() - seconds_millis_curr) > 1000) 
    {
        seconds_millis_curr = millis();
        seconds += 1;
        int32_t countdown = 3 - seconds;
        if (countdown < 0) {countdown = 0;}
        lcd.setCursor(0, 1);
        lcd.print("                ");
        lcd.setCursor(0, 1);
        lcd.print(countdown);
    }
    if ((millis() - ozone_2_rest_millis_curr) > 3000) 
    {
      digitalWrite(fan_pin, 0);
      cycle_state = OFF;
      Serial.println("OFF STATE");
      lcd_refresh = 1;
    }
  }
}
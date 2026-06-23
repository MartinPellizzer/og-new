/*
OXYGEN SENSOR -> ESP32: PINOUT
VIN -> 5V
RX0 -> 17
TX0 -> 4
GND -> GND
*/

#define SENSOR_OXYGEN_BUFF_LEN 12

#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

typedef struct sensor_oxygen_t {
  uint8_t buff[SENSOR_OXYGEN_BUFF_LEN] = { 0 };
  int8_t buff_i = 0;
  float concentration = -1;
  float flow = -1;
  float temperature = -1;
} sensor_oxygen_t;
sensor_oxygen_t sensor_oxygen = {};

uint8_t new_data = 0;

uint32_t timer = 0;

uint32_t timer_test = 0;

#define RE_DE_PIN 16

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  // Serial2.begin(9600, SERIAL_8N1, 17, 4);
  // Serial2.begin(9600);
  pinMode(RE_DE_PIN, OUTPUT);
  
  lcd.init();
  lcd.backlight();
}

const int potPin = 34;

int potValue = 0;

void loop() 
{
  // Reading potentiometer value
  potValue = analogRead(potPin);
  Serial.println(potValue);
  delay(500);

}


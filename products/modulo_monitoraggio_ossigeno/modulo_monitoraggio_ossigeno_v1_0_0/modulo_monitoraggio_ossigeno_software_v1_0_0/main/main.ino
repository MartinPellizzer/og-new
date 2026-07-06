/*
OXYGEN SENSOR -> ESP32: PINOUT
VIN -> 5V
RX0 -> 17
TX0 -> 4
GND -> GND
*/


#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

////////////////////////////////////////
// US1010 (sensore ossigeno)
////////////////////////////////////////
#define US1010_BUFF_LEN 12
typedef struct us1010_t {
  uint8_t buff[US1010_BUFF_LEN] = { 0 };
  int8_t buff_i = 0;
  float concentration = -1;
  float flow = -1;
  float temperature = -1;
  uint8_t new_data_received = 0;
  uint32_t new_data_timer = 0;
  uint8_t err = 0;
} us1010_t;
us1010_t us1010 = {};

// ERROR (ERR) CODES:
// ERR_0 -> NO ERROR
// ERR_1 -> CHECKSUM ERROR



uint32_t timer_test = 0;

#define RE_DE_PIN 16

#define HEARTBEAT_PIN 13
typedef struct heartbeat_t {
  uint32_t millis_cur = 0;
  uint32_t millis_timer = 500;
} heartbeat_t;
heartbeat_t heartbeat = {};

////////////////////////////////////////
// US1010 (sensore ossigeno)
////////////////////////////////////////

void us1010_init()
{
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  pinMode(RE_DE_PIN, OUTPUT);
}

void us1010_debug_serial()
{
  for (int k = 0; k < US1010_BUFF_LEN; k++)
  {
    Serial.print(us1010.buff[k]);
    Serial.print(", ");
  }
  Serial.println();
}

unsigned char us1010_checksum(unsigned char *i, unsigned char ln)
{
  unsigned char j, tempq = 0;
  i += 1;
  for (j = 0; j < (ln - 2); j++)
  {
    tempq += *i;
    i++;
  }
  tempq = (~tempq) + 1; return (tempq);
}

void us1010_run()
{
  if (us1010.new_data_received)
  {
    if (millis() - us1010.new_data_timer > 40)
    {
      us1010.buff_i = 0;
      us1010.new_data_received = 0;

      // us1010_debug_serial();

      
      // TODO: fix checksum function
      // Serial.println(us1010_checksum(us1010.buff, 12));
      // if (us1010_checksum(us1010.buff, 12) == us1010.buff[11]) 
      if (1)
      {
        us1010.concentration = float(us1010.buff[3]*256+us1010.buff[4])/10;
        us1010.flow          = float(us1010.buff[5]*256+us1010.buff[6])/10;
        us1010.temperature   = float(us1010.buff[7]*256+us1010.buff[8])/10;
        us1010.err = 0;
      }
      else
      {
        us1010.concentration = -1;
        us1010.flow          = -1;
        us1010.temperature   = -1;
        us1010.err = 1;
      }

      for(int k = 0; k < US1010_BUFF_LEN; k++)
      {
        us1010.buff[k] = 0;
      }
    }
  }

  if (Serial2.available() > 0)  
  {
    uint8_t c = Serial2.read();
    us1010.buff[us1010.buff_i] = c;
    us1010.buff_i++;
    us1010.new_data_received = 1;
    us1010.new_data_timer = millis();
  }
}


void heartbeat_init()
{
  pinMode(HEARTBEAT_PIN, OUTPUT);
}

void heartbeat_run()
{
  if (millis() - heartbeat.millis_cur > heartbeat.millis_timer)
  {
    heartbeat.millis_cur = millis();
    digitalWrite(HEARTBEAT_PIN, !digitalRead(HEARTBEAT_PIN));
  }
}

void display_init()
{  
  lcd.init();
  lcd.backlight();
}

void display_debug_serial()
{
  Serial.println("one second passed...");
  Serial.print("concentration: ");
  Serial.print(us1010.concentration, 2);
  Serial.print(" Vol %");
  Serial.println();
  Serial.print("flow: ");
  Serial.print(us1010.flow, 2);
  Serial.print(" L/min");
  Serial.println();
  Serial.print("temperature: ");
  Serial.print(us1010.temperature, 2);
  Serial.print(" °C");
  Serial.println();
  Serial.println();
}

void display_run()
{  
  if (millis() - timer_test > 1000)
  {
    timer_test = millis();

    // clear lcd
    lcd.setCursor(0, 0);
    lcd.print("                ");
    lcd.setCursor(0, 1);
    lcd.print("                ");

    // display_debug_serial();

    if (us1010.err == 0)
    {
      lcd.setCursor(0, 0);
      lcd.print("O:");
      lcd.print(us1010.concentration, 1);
      lcd.print("%");
      lcd.print(" ");
      lcd.print("T:");
      lcd.print(us1010.temperature, 1);
      lcd.print("C");
      lcd.setCursor(0, 1);
      lcd.print("F:");
      lcd.print(us1010.flow, 1);
      lcd.print("L/min");
    }
    else if (us1010.err == 1)
    {
      lcd.setCursor(0, 0);
      lcd.print("ERR_1:");
      lcd.setCursor(0, 1);
      lcd.print("CHECKSUM");
    }
  }
}

void setup() 
{
  Serial.begin(9600);
  us1010_init();
  // rs485_init();
  display_init();
  heartbeat_init();
}


void loop() 
{
  us1010_run();
  display_run();
  heartbeat_run();
}


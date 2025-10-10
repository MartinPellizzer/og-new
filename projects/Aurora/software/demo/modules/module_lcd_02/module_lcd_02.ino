// MODULE: 02 - SD CARD

#include "FS.h"
#include "SD.h"
#include "SPI.h"

#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

#define MODULE_ID 2
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

#define SD_CD_PIN 15
typedef struct sd_card_t 
{
  int8_t inserted_old = -2;
  int8_t inserted_tmp = -1;
  int8_t inserted_cur = 0;
  int8_t inserted_state_changed = 0;
} sd_card_t;
sd_card_t sd_card = {};

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
  lcd.print("ID:");
  lcd.print(MODULE_ID);
  lcd.print(" MOD:SD");
  
  rs485.sender_buffer[0] = 0xFF;
  rs485.sender_buffer[1] = 0xFF;
  rs485.sender_buffer[2] = 0xFF;

  if (!SD.begin())
  {
    Serial.println("Card Mount Failed");
    return;
  }
  uint8_t cardType = SD.cardType();

  if (cardType == CARD_NONE)
  {
    Serial.println("No SD card attached");
    return;
  }
}

uint32_t inserted_timer_millis = 0;
void sd_card_inserted()
{
  sd_card.inserted_tmp = !digitalRead(SD_CD_PIN);
  if (sd_card.inserted_old != sd_card.inserted_tmp)
  {
    sd_card.inserted_old = sd_card.inserted_tmp;
    inserted_timer_millis = millis();
  }
  if (millis() - inserted_timer_millis > 40)
  {
    sd_card.inserted_cur = sd_card.inserted_tmp;
    sd_card.inserted_state_changed = 1;
  }
}


uint32_t test_timer_millis = 0;
int counter = 0;
void loop()
{
  sd_card_inserted();
  if (sd_card.inserted_state_changed == 1)
  {
    sd_card.inserted_state_changed = 0;
    lcd.setCursor(0, 1);
    lcd.print("CD:");
    lcd.print(sd_card.inserted_cur);
  }

  if (millis() - test_timer_millis > 1000)
  {
    test_timer_millis = millis();

    counter += 1;
    counter %= 10;

    char char_arr[1];
    sprintf(char_arr, "%d", counter);
    file_write(SD, "/hello.txt", char_arr);
    String file_content = file_read(SD, "/hello.txt");

    lcd.setCursor(5, 1);
    lcd.print("VAL:");
    lcd.print(file_content);
  }
}


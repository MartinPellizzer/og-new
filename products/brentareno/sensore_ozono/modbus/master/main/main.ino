// MASTER

#include <ModbusMaster.h>
ModbusMaster node;

#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);

HardwareSerial Sender(1);
uint8_t state = 0;

uint8_t buff[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;

uint32_t timer = 0;

#define RE_DE_PIN 16

void preTransmission()
{
  digitalWrite(RE_DE_PIN, HIGH);
}

void postTransmission()
{
  digitalWrite(RE_DE_PIN, LOW);
}

uint8_t count = 0;

void setup() 
{
  Serial.begin(9600);
  Sender.begin(9600, SERIAL_8N1, 17, 4);
  pinMode(RE_DE_PIN, OUTPUT);
  digitalWrite(RE_DE_PIN, LOW);

  // use Serial (port 0); initialize Modbus communication baud rate
  // Sender.begin(9600);

  // communicate with Modbus slave ID 23 over Serial (port 0)
  node.begin(23, Sender);
  node.preTransmission(preTransmission);
  node.postTransmission(postTransmission);

  lcd.init();
  lcd.backlight();
}

int led = 0;
int ret = 0;

void loop()
{
  ret = node.readInputRegisters(0x7531, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    Serial.print("analog read: ");
    Serial.println(nn);
  }

  // ret = node.readDiscreteInputs(0x4001, 16);
  // if (ret == node.ku8MBSuccess)
  // {
  //   unsigned int nn = node.getResponseBuffer(0);
  //   Serial.print("digital read: ");
  //   Serial.println(nn, BIN);
  // }

  // ret = node.writeSingleCoil(0x00C, led);
  // led = !led;
  delay(1000);

  if (0)
  {
    // delay(1000);
    count += 1;

    lcd.setCursor(0, 0);
    lcd.print("                ");
    lcd.setCursor(0, 0);
    lcd.print(count);
    
    // // send serially
    // digitalWrite(RE_DE_PIN, HIGH);
    // for(int k = 0; k < 9; k++)
    // {
    //   Sender.write(count);
    // }
    // delay(10);

    static uint32_t i;
    uint8_t j, result;
    uint16_t data[6];
    
    i++;
    
    // set word 0 of TX buffer to least-significant word of counter (bits 15..0)
    node.setTransmitBuffer(0, lowWord(i));
    
    // set word 1 of TX buffer to most-significant word of counter (bits 31..16)
    node.setTransmitBuffer(1, highWord(i));
    
    // slave: read (6) 16-bit registers starting at register 2 to RX buffer
      result = node.readHoldingRegisters(0, 1);

    
    // do something with data if read is successful
    if (result == node.ku8MBSuccess)
    {
        data[0] = node.getResponseBuffer(0);
    }
  }
}


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

  // communicate with Modbus slave ID 1 over Serial (port 0)
  node.begin(1, Sender);
  node.preTransmission(preTransmission);
  node.postTransmission(postTransmission);

  lcd.init();
  lcd.backlight();
}

int led = 0;
int ret = 0;

void loop()
{
  
  const char* address_status_device = "40101";
  uint16_t address_status_device_zero_based = atoi(address_status_device) - 40001;
  ret = node.readInputRegisters(address_status_device_zero_based, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    if (nn == 0)
    {
      Serial.println("analog read 0: INITIALIZING");
      lcd.setCursor(0, 0);
      lcd.print("                ");
      lcd.setCursor(0, 0);
      lcd.print("INITIALIZING");
    }
    else if (nn == 1)
    {
      Serial.println("analog read 1: READY");
      lcd.setCursor(0, 0);
      lcd.print("                ");
      lcd.setCursor(0, 0);
      lcd.print("READY");
    }
    else if (nn == 2)
    {
      Serial.println("analog read 2: OPERATING");
      lcd.setCursor(0, 0);
      lcd.print("                ");
      lcd.setCursor(0, 0);
      lcd.print("OPERATING");
    }
    else if (nn == 3)
    {
      Serial.println("analog read 3: WARNING");
      lcd.setCursor(0, 0);
      lcd.print("                ");
      lcd.setCursor(0, 0);
      lcd.print("WARNING");
    }
    else if (nn == 4)
    {
      Serial.println("analog read 4: FAULT");
      lcd.setCursor(0, 0);
      lcd.print("                ");
      lcd.setCursor(0, 0);
      lcd.print("FAULT");
    }
    else if (nn == 5)
    {
      Serial.println("analog read 5: MAINTENANCE");
      lcd.setCursor(0, 0);
      lcd.print("                ");
      lcd.setCursor(0, 0);
      lcd.print("MAINTENANCE");
    }
    else if (nn == 6)
    {
      Serial.println("analog read 6: OFFLINE");
      lcd.setCursor(0, 0);
      lcd.print("                ");
      lcd.setCursor(0, 0);
      lcd.print("OFFLINE");
    }
  }

  const char* address_status_relay_driver_1 = "00001";
  uint16_t address_status_relay_driver_1_zero_based = atoi(address_status_relay_driver_1) - 00001;
  
  // COILS

  const char* address_coil_1 = "00001";
  uint16_t address_coil_1_zero_based = atoi(address_coil_1) - 1;
  const char* address_coil_2 = "00002";
  uint16_t address_coil_2_zero_based = atoi(address_coil_2) - 1;
  const char* address_coil_3 = "00003";
  uint16_t address_coil_3_zero_based = atoi(address_coil_3) - 1;
  const char* address_coil_4 = "00004";
  uint16_t address_coil_4_zero_based = atoi(address_coil_4) - 1;
  const char* address_coil_5 = "00005";
  uint16_t address_coil_5_zero_based = atoi(address_coil_5) - 1;
  const char* address_coil_6 = "00006";
  uint16_t address_coil_6_zero_based = atoi(address_coil_6) - 1;
  const char* address_coil_7 = "00007";
  uint16_t address_coil_7_zero_based = atoi(address_coil_7) - 1;
  const char* address_coil_8 = "00008";
  uint16_t address_coil_8_zero_based = atoi(address_coil_8) - 1;
  
  // WRITE
  ret = node.writeSingleCoil(address_coil_1_zero_based, led);
  ret = node.writeSingleCoil(address_coil_2_zero_based, led);
  ret = node.writeSingleCoil(address_coil_3_zero_based, led);
  ret = node.writeSingleCoil(address_coil_4_zero_based, led);
  ret = node.writeSingleCoil(address_coil_5_zero_based, led);
  ret = node.writeSingleCoil(address_coil_6_zero_based, led);
  ret = node.writeSingleCoil(address_coil_7_zero_based, led);
  ret = node.writeSingleCoil(address_coil_8_zero_based, led);

  // READ
  lcd.setCursor(0, 0);
  lcd.print("                ");
  ret = node.readDiscreteInputs(address_coil_1_zero_based, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    Serial.print("digital read RELAY_DRIVER_1_PIN:");
    Serial.println(nn);
    lcd.setCursor(0, 1);
    lcd.print(nn);
  }
  ret = node.readDiscreteInputs(address_coil_2_zero_based, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    Serial.print("digital read RELAY_DRIVER_2_PIN:");
    Serial.println(nn);
    lcd.setCursor(1, 1);
    lcd.print(nn);
  }
  ret = node.readDiscreteInputs(address_coil_3_zero_based, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    Serial.print("digital read RELAY_DRIVER_3_PIN:");
    Serial.println(nn);
    lcd.setCursor(2, 1);
    lcd.print(nn);
  }
  ret = node.readDiscreteInputs(address_coil_4_zero_based, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    Serial.print("digital read RELAY_DRIVER_4_PIN:");
    Serial.println(nn);
    lcd.setCursor(3, 1);
    lcd.print(nn);
  }
  ret = node.readDiscreteInputs(address_coil_5_zero_based, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    Serial.print("digital read RELAY_DRIVER_5_PIN:");
    Serial.println(nn);
    lcd.setCursor(4, 1);
    lcd.print(nn);
  }
  ret = node.readDiscreteInputs(address_coil_6_zero_based, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    Serial.print("digital read RELAY_DRIVER_6_PIN:");
    Serial.println(nn);
    lcd.setCursor(5, 1);
    lcd.print(nn);
  }
  ret = node.readDiscreteInputs(address_coil_7_zero_based, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    Serial.print("digital read RELAY_DRIVER_7_PIN:");
    Serial.println(nn);
    lcd.setCursor(6, 1);
    lcd.print(nn);
  }
  ret = node.readDiscreteInputs(address_coil_8_zero_based, 1);
  if (ret == node.ku8MBSuccess)
  {
    int nn = node.getResponseBuffer(0);
    Serial.print("digital read RELAY_DRIVER_8_PIN:");
    Serial.println(nn);
    lcd.setCursor(7, 1);
    lcd.print(nn);
  }

  led = !led;

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


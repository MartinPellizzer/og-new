// SLAVE


HardwareSerial Sender(1);
uint8_t state = 0;

uint8_t buff[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;

uint32_t timer = 0;

#define RE_DE_PIN 16

#include <ModbusSlave.h>
Modbus slave(Sender, 23, RE_DE_PIN);

#define LED_PIN 13

void setup() 
{
  Serial.begin(9600);
  Sender.begin(9600, SERIAL_8N1, 17, 4);
  pinMode(RE_DE_PIN, OUTPUT);
  digitalWrite(RE_DE_PIN, LOW);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // slave.cbVector[CB_WRITE_COILS] = writeDigitalOut;
  slave.cbVector[CB_READ_COILS] = readDigital;
  slave.cbVector[CB_READ_DISCRETE_INPUTS] = readDigital;

  slave.begin(9600);

}

int led_state = 0;

void loop() 
{
  slave.poll();
  // digitalWrite(LED_PIN, led_state);
  // led_state = !led_state;
  // delay(1000);

  if (0)
  {
  if (new_data)
  {
    if (millis() - timer > 40)
    {
      i = 0;
      new_data = 0;
      for(int k = 0; k < 9; k++)
      {
        Serial.print(buff[k]);
        Serial.print(",");
      }
      Serial.println();
    }
  }
  if (Sender.available() > 0)  
  {
    uint8_t c = Sender.read();
    buff[i] = c;
    i++;
    new_data = 1;
    timer = millis();
  }
    
  }
}
uint8_t readDigital(uint8_t fc, uint16_t address, uint16_t length, void* data)

}

uint8_t writeDigitalOut(uint8_t fc, uint16_t address, uint16_t length, void* data)
{
  Serial.print("FC=05: ");
  Serial.println(fc);
  Serial.println(address);
  Serial.println(length);

  if (address == 12)
  {
    digitalWrite(LED_PIN, slave.readCoilFromBuffer(0));
  }
  return STATUS_OK;
}

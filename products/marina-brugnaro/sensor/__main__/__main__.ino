HardwareSerial Sender(1);
uint8_t state = 0;

uint8_t buff[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;

uint32_t timer = 0;

uint32_t timer_test = 0;

#define RE_DE_PIN 16

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  Sender.begin(9600, SERIAL_8N1, 17, 4);
  // Serial2.begin(9600);
  pinMode(RE_DE_PIN, OUTPUT);
}

unsigned char FucCheckSum(unsigned char *i, unsigned char ln)
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

void loop() 
{
  if (millis() - timer_test > 1000)
  {
    timer_test = millis();
      Serial.println("one second passed...");
  }

  if (new_data)
  {
    if (millis() - timer > 40)
    {
      i = 0;
      new_data = 0;

      int ppb = 0;      

      // get ppb from sensor
      if (FucCheckSum(buff, 9) == buff[8]) 
      {
        ppb = buff[4] * 256 + buff[5];
      }

      // send serially
      digitalWrite(RE_DE_PIN, HIGH);
      for(int k = 0; k < 9; k++)
      {
        Sender.write(buff[k]);
      }
      for(int k = 0; k < 9; k++)
      {
        Serial.println(buff[k]);
      }
      delay(10);
      digitalWrite(RE_DE_PIN, LOW);
      for(int k = 0; k < 9; k++)
      {
        buff[k] = 0;
      }

      if (ppb >= 10000)
      {
        ppb = 9999;
      } 
      
      Serial.print(ppb);
    }
  }

  if (Serial2.available() > 0)  
  {
    uint8_t c = Serial2.read();
    buff[i] = c;
    i++;
    new_data = 1;
    timer = millis();
  }

}


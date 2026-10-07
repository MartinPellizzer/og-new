HardwareSerial Sender(1);
uint8_t state = 0;

uint8_t buff[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;

uint32_t timer = 0;

#define RE_DE_PIN 16

void setup() 
{
  Serial.begin(9600);
  Sender.begin(9600, SERIAL_8N1, 17, 4);
  pinMode(RE_DE_PIN, OUTPUT);
  digitalWrite(RE_DE_PIN, LOW);
}

void loop() 
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


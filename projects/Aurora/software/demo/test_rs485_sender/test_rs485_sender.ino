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
  pinMode(RE_DE_PIN, OUTPUT);
}

void loop() 
{
  if (millis() - timer_test > 1000)
  {
    timer_test = millis();

    buff[0] = !buff[0];

    // send serially
    digitalWrite(RE_DE_PIN, HIGH);
    for(int k = 0; k < 9; k++)
    {
      Sender.write(buff[k]);
    }
    delay(10);
    digitalWrite(RE_DE_PIN, LOW);

    for(int k = 0; k < 9; k++)
    {
      Serial.print(buff[k]);
      Serial.print(",");
    }
    Serial.println();

    // for(int k = 0; k < 9; k++)
    // {
    //   buff[k] = 0;
    // }
  }
}


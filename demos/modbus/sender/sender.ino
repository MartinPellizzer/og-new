#define RE_DE_PIN 16

HardwareSerial Sender(1);
uint8_t buff_sender[9] = {0};
uint32_t timer_query = 0;

void setup()
{
  Serial.begin(9600);
  Sender.begin(9600, SERIAL_8N1, 17, 4);
  pinMode(RE_DE_PIN, OUTPUT);
}

void loop()
{
  if (millis() - timer_query > 1000)
  {
    timer_query = millis();

    buff_sender[0] = 20;
    buff_sender[1] = 21;
    buff_sender[2] = 22;
    buff_sender[3] = 23;
    buff_sender[4] = 24;
    buff_sender[5] = 25;
    buff_sender[6] = 26;
    buff_sender[7] = 27;
    buff_sender[8] = 28;

    digitalWrite(RE_DE_PIN, HIGH);
    for(int k = 0; k < 9; k++)
    {
      Sender.write(buff_sender[k]);
      Serial.print(buff_sender[k]);
    }
    Serial.println();
    delay(10);
    digitalWrite(RE_DE_PIN, LOW);
  }
}

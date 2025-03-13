#define RE_DE_PIN 16

HardwareSerial RS485(1);
uint8_t buff_sender[9] = {0};
uint32_t timer_query = 0;
uint8_t buff_receiver[9] = {0};
uint8_t i = 0;
uint8_t new_data = 0;
uint32_t timer_receiver = 0;


void setup()
{
  Serial.begin(9600);
  RS485.begin(9600, SERIAL_8N1, 17, 4);
  pinMode(RE_DE_PIN, OUTPUT);
  digitalWrite(RE_DE_PIN, LOW);
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

    Serial.print("MASTER SENDER: ");
    digitalWrite(RE_DE_PIN, HIGH);
    for(int k = 0; k < 9; k++)
    {
      RS485.write(buff_sender[k]);
      Serial.print(buff_sender[k]);
        Serial.print(", "); 
    }
    Serial.println();
    delay(10);
    digitalWrite(RE_DE_PIN, LOW);
  }

  if (new_data)
  {
    if (millis() - timer_receiver > 40)
    {
      i = 0;
      new_data = 0;
      Serial.print("MASTER RECEIVER: ");
      for(int k = 0; k < 9; k++)
      {
        Serial.print(buff_receiver[k]);
        Serial.print(", ");
      }
      Serial.println();
    }
  }
  
  if (RS485.available() > 0)  
  {
    uint8_t c = RS485.read();
    buff_receiver[i] = c;
    i++;
    new_data = 1;
    timer_receiver = millis();
  }
}

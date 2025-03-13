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
  RS485.begin(9600, SERIAL_8N1, 17, 14);
  pinMode(RE_DE_PIN, OUTPUT);
  digitalWrite(RE_DE_PIN, LOW);

}

void loop() 
{
  if (new_data)
  {
    if (millis() - timer_receiver > 40)
    {
      i = 0;
      new_data = 0;
      Serial.print("SLAVE RECEIVER: ");
      for(int k = 0; k < 9; k++)
      {
        Serial.print(buff_receiver[k]);
        Serial.print(", ");
      }
      Serial.println();
      
      buff_sender[0] = 30;
      buff_sender[1] = 31;
      buff_sender[2] = 32;
      buff_sender[3] = 33;
      buff_sender[4] = 34;
      buff_sender[5] = 35;
      buff_sender[6] = 36;
      buff_sender[7] = 37;
      buff_sender[8] = 38;

      Serial.print("SLAVE SENDER: ");
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

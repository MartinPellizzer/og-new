HardwareSerial RS485(1);

#define BUFF_LEN 9
uint8_t buff[BUFF_LEN] = {0};
uint8_t i = 0;
uint8_t new_data = 0;
uint32_t timer = 0;
uint32_t timer_no_signal = 0;

#define RE_DE_PIN 16

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
    if (millis() - timer > 40)
    {
      i = 0;
      new_data = 0;

      for(int k = 0; k < 9; k++)
      {
        Serial.print(buff[k]);
        Serial.print(", ");
      }
      Serial.println();
    }
  }   

  if (RS485.available() > 0)  
  {
    uint8_t c = RS485.read();
    buff[i] = c;
    i++;
    new_data = 1;
    timer = millis();
  }
}

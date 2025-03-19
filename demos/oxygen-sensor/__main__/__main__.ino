HardwareSerial serial_oxygen(1);

#define BUFF_LEN 20
uint8_t buff[BUFF_LEN] = {0};
uint8_t i = 0;
uint8_t new_data = 0;
uint32_t timer = 0;

void setup() 
{
  Serial.begin(9600);
  serial_oxygen.begin(9600, SERIAL_8N1, 17, 4);
}

void loop() 
{
  if (new_data)
  {
    // if (millis() - timer > 40)
    // {
    //   i = 0;
    //   new_data = 0;
      
    //   for(int i = 0; i < BUFF_LEN; i++) 
    //   {
    //       Serial.print(buff[i]);
    //       Serial.print(", ");
    //   }
    //   Serial.println();
    // }
  }  
  if (serial_oxygen.available() > 0)  
  {
    uint8_t c = serial_oxygen.read();
    Serial.print(c);
    // buff[i] = c;
    // i++;
    // new_data = 1;
    // timer = millis();
  }

}

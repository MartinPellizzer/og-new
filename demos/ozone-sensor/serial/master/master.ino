HardwareSerial serial_modbus(1);
#define BUFF_LEN 20
uint8_t buff[BUFF_LEN] = {0};
uint8_t i = 0;
uint8_t new_data = 0;
uint32_t timer = 0;

void setup() 
{
  Serial.begin(9600);
  serial_modbus.begin(9600, SERIAL_8N1, 17, 4);
  Serial.println("started");
}

void loop() 
{
  if (new_data)
  {
    if (millis() - timer > 40)
    {
      i = 0;
      new_data = 0;
      
      for(int i = 0; i < BUFF_LEN; i++) 
      {
          Serial.print(buff[i]);
          Serial.print(", ");
      }
      Serial.println();

      // Serial.print(buff[3]);
      // Serial.print(", ");
      // Serial.print(buff[4]);
      // Serial.println();

      // Serial.print(buff[5]);
      // Serial.print(", ");
      // Serial.print(buff[6]);
      // Serial.println();

      // Serial.print(buff[7]);
      // Serial.print(", ");
      // Serial.print(buff[8]);
      // Serial.println();

      float oxygen_percentage = float(buff[3]*256+buff[4])/10;
      Serial.print("OXYGEN PERCENTAGE: ");
      Serial.print(oxygen_percentage, 2);
      Serial.print(" Vol %");
      Serial.println();

      float flow_rate = float(buff[5]*256+buff[6])/10;
      Serial.print("FLOW RATE: ");
      Serial.print(flow_rate, 2);
      Serial.print(" L/min");
      Serial.println();
      
      float gas_temperature = float(buff[7]*256+buff[8])/10;
      Serial.print("GAS TEMPERATURE: ");
      Serial.print(gas_temperature, 2);
      Serial.print(" °C");
      Serial.println();
      
      // for(int i = 0; i < BUFF_LEN; i++) 
      // {
      //     Serial.print(buff[i]);
      //     Serial.print(", ");
      // }
      // Serial.println();
    }
  }  
  if (serial_modbus.available() > 0)  
  {
    uint8_t c = serial_modbus.read();
    buff[i] = c;
    i++;
    new_data = 1;
    timer = millis();
  }
}

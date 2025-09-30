#define SENSOR_OXYGEN_BUFF_LEN 12
typedef struct sensor_oxygen_t {
  uint8_t buff[SENSOR_OXYGEN_BUFF_LEN] = { 0 };
  int8_t buff_i = 0;
  float concentration = -1;
  float flow = -1;
  float temperature = -1;
} sensor_oxygen_t;
sensor_oxygen_t sensor_oxygen = {};


uint8_t new_data = 0;

uint32_t timer = 0;

uint32_t timer_test = 0;

#define RE_DE_PIN 16

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
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
    // Serial.println("one second passed...");
    Serial.print("concentration: ");
    Serial.print(sensor_oxygen.concentration, 2);
    Serial.print(" Vol %");
    Serial.println();
    Serial.print("flow: ");
    Serial.print(sensor_oxygen.flow, 2);
    Serial.print(" L/min");
    Serial.println();
    Serial.print("temperature: ");
    Serial.print(sensor_oxygen.temperature, 2);
    Serial.print(" °C");
    Serial.println();
    Serial.println();
  }

  if (new_data)
  {
    if (millis() - timer > 40)
    {
      sensor_oxygen.buff_i = 0;
      new_data = 0;

      // for(int k = 0; k < SENSOR_OXYGEN_BUFF_LEN; k++)
      // {
      //   Serial.print(sensor_oxygen.buff[k]);
      //   Serial.print(", ");
      // }
      // Serial.println();
      
      sensor_oxygen.concentration = float(sensor_oxygen.buff[3]*256+sensor_oxygen.buff[4])/10;
      sensor_oxygen.flow = float(sensor_oxygen.buff[5]*256+sensor_oxygen.buff[6])/10;
      sensor_oxygen.temperature = float(sensor_oxygen.buff[7]*256+sensor_oxygen.buff[8])/10;

      for(int k = 0; k < SENSOR_OXYGEN_BUFF_LEN; k++)
      {
        sensor_oxygen.buff[k] = 0;
      }
    }
  }

  if (Serial2.available() > 0)  
  {
    uint8_t c = Serial2.read();
    sensor_oxygen.buff[sensor_oxygen.buff_i] = c;
    sensor_oxygen.buff_i++;
    new_data = 1;
    timer = millis();
  }

}


#define SENSOR1_RE_DE_PIN 16
HardwareSerial Sensor1(1);
#define BUFF_LEN 9
uint8_t buff[BUFF_LEN] = { 0 };

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  Sensor1.begin(9600, SERIAL_8N1, 17, 4);  // RO, DI

  pinMode(SENSOR1_RE_DE_PIN, OUTPUT);
  digitalWrite(SENSOR1_RE_DE_PIN, LOW);
}

void loop() 
{
  if (Sensor1.available() > 0) 
  {
    uint8_t c = Sensor1.read();
    Serial.println(c);
  }
}

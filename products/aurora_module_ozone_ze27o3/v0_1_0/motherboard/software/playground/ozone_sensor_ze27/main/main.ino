HardwareSerial Sender(1);
#define RE_DE_PIN 16
#define SENSOR_BUFF_LEN 9
typedef struct sensor_t {
  uint8_t buff[SENSOR_BUFF_LEN] = { 0 };
  uint8_t buff_i = 0;
  uint8_t buff_ready = 0;
  uint32_t buff_timer = 0;
  int16_t ppb_old = -1;
  int16_t ppb_cur = -1;
} sensor_t;
sensor_t sensor = {};

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

uint8_t checksum_valid() 
{
  if (FucCheckSum(sensor.buff, SENSOR_BUFF_LEN) == sensor.buff[SENSOR_BUFF_LEN-1]) 
  {
    return 1;
  }
  return 0;
}

uint8_t ppb_get() 
{
  int16_t ppb = sensor.buff[4] * 256 + sensor.buff[5];
  return ppb;
}

void ze27o3_listen()
{
  if (Serial2.available() > 0)
  {
    uint8_t c = Serial2.read();
    sensor.buff[sensor.buff_i] = c;
    sensor.buff_i += 1;
    sensor.buff_ready = 1;
    sensor.buff_timer = millis();
  }
}

int8_t ze27o3_ready()
{
  if (sensor.buff_ready && millis() - sensor.buff_timer > 40)
  {
    return 1;
  }
  return 0;
}

void ze27o3_write()
{
  digitalWrite(RE_DE_PIN, HIGH);
  for(int i = 0; i < SENSOR_BUFF_LEN; i++)
  {
    Sender.write(sensor.buff[i]);
  }
  delay(10);
  digitalWrite(RE_DE_PIN, LOW);
}

void ze27o3_debug()
{
    int16_t ppb = ppb_get();
    Serial.print("PPB: ");
    Serial.println(ppb);

    Serial.print("BUFF: ");
    for(int i = 0; i < SENSOR_BUFF_LEN; i++)
    {
      Serial.print(sensor.buff[i]);
      Serial.print(", ");
    }
    Serial.println();
    Serial.println();
}

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  Sender.begin(9600, SERIAL_8N1, 17, 4);
  pinMode(RE_DE_PIN, OUTPUT);
  digitalWrite(RE_DE_PIN, LOW);
}

void loop() 
{
  ze27o3_listen();

  if (ze27o3_ready())
  {
    sensor.buff_i = 0;
    sensor.buff_ready = 0;

    // CHECKSUM
    if (checksum_valid())
    {
      Serial.println("CHECKSUM: VALID");

      // SEND ZE27O3 RS485
      ze27o3_write();

      // SEND PPB 0-10V
      // TODO
    }
    else
    {
      Serial.println("CHECKSUM: ERROR");
    }

    ze27o3_debug();
  }
}


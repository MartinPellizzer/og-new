#define R1_PIN 13
#define R2_PIN 18
#define R3_PIN 19
#define R4_PIN 23
#define R5_PIN 32
#define R6_PIN 33
#define R7_PIN 25
#define R8_PIN 26

HardwareSerial rs485_aurora(1);
#define RS485_AURORA_RE_DE_PIN 16

#define SENSOR1_RE_DE_PIN 26
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

typedef struct heartbeat_t {
  const uint8_t HEARTBEAT_PIN = 35; // ERR: gpio 35 can't be output
  uint32_t timer_millis_cur = 0;
  uint32_t timer_millis_max = 500;
} heartbeat_t;
heartbeat_t heartbeat = {};

typedef struct button_t {
  const uint8_t BUTTON_PIN = 27;
} button_t;
button_t button = {};

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
  if (rs485_aurora.available() > 0)
  {
    uint8_t c = rs485_aurora.read();
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
  pinMode(R1_PIN, OUTPUT);
  pinMode(R2_PIN, OUTPUT);
  pinMode(R3_PIN, OUTPUT);
  pinMode(R4_PIN, OUTPUT);
  pinMode(R5_PIN, OUTPUT);
  pinMode(R6_PIN, OUTPUT);
  pinMode(R7_PIN, OUTPUT);
  pinMode(R8_PIN, OUTPUT);
  pinMode(R8_PIN, OUTPUT);
  // pinMode(26, OUTPUT);
  // pinMode(13, OUTPUT);
  // // pinMode(15, OUTPUT);
  // // pinMode(5, OUTPUT);
  // pinMode(32, OUTPUT);
  // pinMode(33, OUTPUT);
  // pinMode(18, OUTPUT);
  // pinMode(19, OUTPUT);
  // pinMode(23, OUTPUT);
  // pinMode(27, OUTPUT);
  // pinMode(35, INPUT);
  // // digitalWrite(25, HIGH);
  // delay(10000);
  
  // pinMode(heartbeat.HEARTBEAT_PIN, OUTPUT);

  pinMode(button.BUTTON_PIN, INPUT);
  
  rs485_aurora.begin(9600, SERIAL_8N1, 17, 4);  // RO, DI
  pinMode(RS485_AURORA_RE_DE_PIN, OUTPUT);
  digitalWrite(RS485_AURORA_RE_DE_PIN, LOW);
  
  Serial2.begin(9600, SERIAL_8N1, 27, 14);  // RO, DI
  pinMode(SENSOR1_RE_DE_PIN, OUTPUT);
  digitalWrite(SENSOR1_RE_DE_PIN, LOW);
}

void loop() 
{
  if (millis() - heartbeat.timer_millis_cur > heartbeat.timer_millis_max)
  {
    heartbeat.timer_millis_cur = millis();
    digitalWrite(heartbeat.HEARTBEAT_PIN, !digitalRead(heartbeat.HEARTBEAT_PIN));
    // Serial.println("here");
  }
  // digitalWrite(32, !digitalRead(32));
  // delay(1000);
  // digitalWrite(33, !digitalRead(33));
  // delay(1000);
  // digitalWrite(R1_PIN, !digitalRead(R1_PIN));
  // delay(1000);
  // digitalWrite(R2_PIN, !digitalRead(R2_PIN));
  // delay(1000);
  // digitalWrite(R3_PIN, !digitalRead(R3_PIN));
  // delay(1000);
  // digitalWrite(R4_PIN, !digitalRead(R4_PIN));
  // delay(1000);
  // digitalWrite(R5_PIN, !digitalRead(R5_PIN));
  // delay(1000);
  // digitalWrite(R6_PIN, !digitalRead(R6_PIN));
  // delay(1000);
  // digitalWrite(R7_PIN, !digitalRead(R7_PIN));
  // delay(1000);
  // digitalWrite(R8_PIN, !digitalRead(R8_PIN));
  // delay(1000);
  // digitalWrite(26, !digitalRead(26));
  // delay(1000);
  // digitalWrite(13, !digitalRead(13));
  // delay(1000);
  // // digitalWrite(15, !digitalRead(15));
  // // delay(1000);
  // // digitalWrite(5, !digitalRead(5));
  // // delay(1000);
  // digitalWrite(18, !digitalRead(18));
  // delay(1000);
  // digitalWrite(19, !digitalRead(19));
  // delay(1000);
  // digitalWrite(23, !digitalRead(23));
  // delay(1000);
  // digitalWrite(27, !digitalRead(27));
  // delay(1000);
  // digitalWrite(27, !digitalRead(27));
  // delay(1000);
  if (digitalRead(button.BUTTON_PIN) == 0)
  {
    Serial.println("button pressed");
  }

  ze27o3_listen();
  
  if (ze27o3_ready())
  {
    Serial.println("here");
    sensor.buff_i = 0;
    sensor.buff_ready = 0;

    // CHECKSUM
    if (checksum_valid())
    {
      Serial.println("CHECKSUM: VALID");

      // SEND ZE27O3 RS485
      // rs485_aurora_write();

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




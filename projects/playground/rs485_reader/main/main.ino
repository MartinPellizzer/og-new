///////////////////////////////////////////////////////////////////////
// ;sensor
///////////////////////////////////////////////////////////////////////
#define SENSOR1_RE_DE_PIN 16
HardwareSerial Sensor1(1);
#define BUFF_LEN 9
uint8_t buff[BUFF_LEN] = { 0 };
uint8_t i = 0;
uint8_t sensor_new_data = 0;
uint32_t timer = 0;
uint32_t timer_no_signal = 0;
uint32_t sensor_connected_millis = 0;
int sensor_connected_seconds = 0;
typedef struct sensor_t {
  int16_t ppb_old = -2;
  int16_t ppb_cur = -1;
  int8_t is_connected = 0;
  int16_t target_ppb_old = -2;
  int16_t target_ppb_tmp = -1;
  int16_t target_ppb_cur = 100;
  int8_t delta_perc_old = -2;
  int8_t delta_perc_tmp = -1;
  int8_t delta_perc_cur = 20;
} sensor_t;
sensor_t sensor = {};

void clear_buffer(uint8_t buff[], uint8_t len) 
{
  for (int i = 0; i < len; i++) buff[i] = 0;
}

void sensor_update() 
{
  // check if sensor is connected, otherwise update state/val
  if (sensor.is_connected == 1) 
  {
    if (millis() - sensor_connected_millis > 1000) 
    {
      sensor_connected_millis = millis();
      sensor_connected_seconds += 1;
      if (sensor_connected_seconds > 5)
      {
        sensor.is_connected = 0;
        sensor.ppb_old = -2;
        sensor.ppb_cur = -1;
      }
    }
  }

  if (sensor_new_data) 
  {
    
      Serial.print("here");
    if (millis() - timer > 40) 
    {
      // for (int i = 0; i < BUFF_LEN; i++)
      // {
      //   Serial.print(buff[i]);
      //   Serial.print(", ");
      // }
      // Serial.println();

      timer_no_signal = millis();
      i = 0;
      sensor_new_data = 0;
      sensor.ppb_cur = 0;
      if (checksum(buff, 9) == buff[8]) 
      {
        sensor.ppb_cur = buff[4] * 256 + buff[5];
        sensor_connected_millis = millis();
        sensor_connected_seconds = 0;
        sensor.is_connected = 1;
        // Serial.println(sensor.ppb_cur);
      }
      clear_buffer(buff, BUFF_LEN);
    }
  }
  if (Sensor1.available() > 0) 
  {
    uint8_t c = Sensor1.read();
    //Serial.println(c);
    buff[i] = c;
    i++;
    sensor_new_data = 1;
    timer = millis();
  }
}

unsigned char checksum(unsigned char *i, unsigned char ln) {
  unsigned char j, tempq = 0;
  i += 1;
  for (j = 0; j < (ln - 2); j++) {
    tempq += *i;
    i++;
  }
  tempq = (~tempq) + 1;
  return (tempq);
}

void sensor_ozone_manager()
{
  sensor_update();
}

uint32_t debug_millis_cur = 0;

void debug_manager()
{
  // ;debug
  if (millis() - debug_millis_cur > 1000) 
  {
    debug_millis_cur = millis();
    
    // Serial.print("external_input.state_cur: ");
    // Serial.println(external_input.state_cur);
    // Serial.print("external_input.is_abilitated_cur: ");
    // Serial.println(external_input.is_abilitated_cur);
    // Serial.print("sensor_temperature.state_cur: ");
    // Serial.println(sensor_temperature.state_cur);

    // Serial.print("o3_sensor_alarm.is_over_max_cur: ");
    // Serial.println(o3_sensor_alarm.is_over_max_cur);
    // Serial.print("o3_sensor_alarm.alarm_millis_cur: ");
    // Serial.println(millis() - o3_sensor_alarm.alarm_millis_cur);
    // Serial.print("o3_sensor_alarm.is_alarm_cur: ");
    // Serial.println(o3_sensor_alarm.is_alarm_cur);
    // Serial.print("o3_sensor_alarm.ppb_cur: ");
    // Serial.println(o3_sensor_alarm.ppb_cur);
    // Serial.print("o3_sensor_alarm.ppb_alarm_cur: ");
    // Serial.println(o3_sensor_alarm.ppb_alarm_cur);

    // Serial.print("sensor_temperature.state_cur: ");
    // Serial.println(sensor_temperature.state_cur);
    // Serial.print("external_input.is_abilitated_cur: ");
    // Serial.println(external_input.is_abilitated_cur);
    // Serial.print("external_input.state_cur: ");
    // Serial.println(external_input.state_cur);

    // Serial.println();

    // for (int i = 0; i < PASSWORD_DIGITS_NUM; i++)
    // {
    //   Serial.print(password.digits_cur[i]);
    // }
    // Serial.println();
    // Serial.println(password.digit_counter);
    // Serial.println();
    
    // Serial.println(nextion.page_cur);

    // Serial.println(o3_sensor_alarm.ppb_cur);
    // Serial.println(cycle.mode_tmp);
    Serial.println(sensor.ppb_cur);
  }
}


void setup() 
{  
  Serial.begin(9600);

  Sensor1.begin(9600, SERIAL_8N1, 17, 4);  // RO, DI
  pinMode(SENSOR1_RE_DE_PIN, OUTPUT);
  digitalWrite(SENSOR1_RE_DE_PIN, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  sensor_ozone_manager();

  debug_manager();

}

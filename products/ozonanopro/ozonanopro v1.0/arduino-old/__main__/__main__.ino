#include <HardwareSerial.h>

HardwareSerial serial_oxygen(1);

#define SERIAL_OXYGEN_RX_GPIO 2
#define SERIAL_OXYGEN_TX_GPIO 15

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
} sensor_t;
sensor_t sensor = {};

const uint8_t OXYGEN_BUFFER_SIZE = 20;
typedef struct oxygen_t {
  uint8_t receiver_buff[OXYGEN_BUFFER_SIZE] = { 0 };
  uint8_t receiver_buff_index = 0;
  uint32_t receiver_timer = 0;
  uint32_t bytestream_buff_index = 0;
  uint8_t bytestream_receiving = 0;
} oxygen_t;
oxygen_t oxygen = {};

#define pin_flow 25
#define pin_nanobubble_pump 5
#define pin_booster_pump 18
#define pin_oxygen_concentrator 19
#define pin_ozone_generator 23

int cycle_state = -1;
uint32_t cycle_millis = 0;

typedef struct power_t {
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} power_t;
power_t power = {};

typedef struct valve_bypass_t {
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} valve_bypass_t;
valve_bypass_t valve_bypass = {};

typedef struct flow_switch_t {
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} flow_switch_t;
flow_switch_t flow_switch = {};

typedef struct pump_booster_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
} pump_booster_t;
pump_booster_t pump_booster = {};

typedef struct pump_nano_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
} pump_nano_t;
pump_nano_t pump_nano = {};

typedef struct oxygen_concentrator_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} oxygen_concentrator_t;
oxygen_concentrator_t oxygen_concentrator = {};

typedef struct ozone_generator_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} ozone_generator_t;
ozone_generator_t ozone_generator = {};

///////////////////////////////////////////////////////////////////////
// ;nextion
///////////////////////////////////////////////////////////////////////
const uint8_t BUFFER_SIZE = 20;
typedef struct nextion_t {  
  uint8_t inputs_buff[BUFFER_SIZE];
  uint8_t bytestream_receiving = 0;
  uint32_t bytestream_millis = 0;
  uint32_t bytestream_buff_index = 0;
  int16_t page_old = -1;
  int16_t page_cur = 0;
} nextion_t;
nextion_t nextion = {};

void cycle_starting()
{
  if (cycle_state == 0)
  {
    if (millis() - cycle_millis > 1000)
    {
      cycle_state = 1;
      pump_booster.state_cur = 1;
      pump_nano.state_cur = 1;
      digitalWrite(pin_booster_pump, HIGH);
      digitalWrite(pin_nanobubble_pump, HIGH);
      cycle_millis = millis();
    }
  }
  if (cycle_state == 1)
  {
    if (millis() - cycle_millis > 3000)
    {
      cycle_state = 2;
      oxygen_concentrator.state_cur = 1;
      oxygen_concentrator.nextion_refresh = 1;
      digitalWrite(pin_oxygen_concentrator, HIGH);
      cycle_millis = millis();
    }
  }
  if (cycle_state == 2)
  {
    if (millis() - cycle_millis > 3000)
    {
      cycle_state = 3;
      ozone_generator.state_cur = 1;
      ozone_generator.nextion_refresh = 1;
      digitalWrite(pin_ozone_generator, HIGH);
      cycle_millis = millis();
    }
  }
}

void cycle_terminating()
{
  if (cycle_state == 100)
  {
    if (millis() - cycle_millis > 1000)
    {
      cycle_state = -1;
      pump_booster.state_cur = 0;
      pump_nano.state_cur = 0;
      oxygen_concentrator.state_cur = 0;
      oxygen_concentrator.nextion_refresh = 1;
      ozone_generator.state_cur = 0;
      ozone_generator.nextion_refresh = 1;
      digitalWrite(pin_nanobubble_pump, LOW);
      digitalWrite(pin_booster_pump, LOW);
      digitalWrite(pin_oxygen_concentrator, LOW);
      digitalWrite(pin_ozone_generator, LOW);
      cycle_millis = millis();
    }
  }
}

void cycle_manager()
{
  cycle_starting();
  cycle_terminating();
}

void oxygen_sensor_manager() {
  if (oxygen.bytestream_receiving) {
    if (millis() - oxygen.receiver_timer > 40) {
      oxygen.receiver_buff_index = 0;
      oxygen.bytestream_receiving = 0;

      for (int i = 0; i < OXYGEN_BUFFER_SIZE; i++) {
        Serial.print(oxygen.receiver_buff[i]);
        Serial.print(", ");
      }
      Serial.println();

      float oxygen_percentage = float(oxygen.receiver_buff[3] * 256 + oxygen.receiver_buff[4]) / 10;
      Serial.print("OXYGEN PERCENTAGE: ");
      Serial.print(oxygen_percentage, 2);
      Serial.print(" Vol %");
      Serial.println();

      float flow_rate = float(oxygen.receiver_buff[5] * 256 + oxygen.receiver_buff[6]) / 10;
      Serial.print("FLOW RATE: ");
      Serial.print(flow_rate, 2);
      Serial.print(" L/min");
      Serial.println();

      float gas_temperature = float(oxygen.receiver_buff[7] * 256 + oxygen.receiver_buff[8]) / 10;
      Serial.print("GAS TEMPERATURE: ");
      Serial.print(gas_temperature, 2);
      Serial.print(" °C");
      Serial.println();
    }
  }
  if (serial_oxygen.available() > 0) {
    uint8_t c = serial_oxygen.read();
    oxygen.receiver_buff[oxygen.receiver_buff_index] = c;
    oxygen.receiver_buff_index++;
    oxygen.bytestream_receiving = 1;
    oxygen.receiver_timer = millis();
  }
}

void clear_buffer(uint8_t buff[], uint8_t len) 
{
  for (int i = 0; i < len; i++) buff[i] = 0;
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
    if (millis() - timer > 40) 
    {
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
        Serial.println(sensor.ppb_cur);
      }
      clear_buffer(buff, BUFF_LEN);
    }
  }
  if (Sensor1.available() > 0) 
  {
    uint8_t c = Sensor1.read();
    Serial.println(c);
    buff[i] = c;
    i++;
    sensor_new_data = 1;
    timer = millis();
  }
}

void setup() {
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  Sensor1.begin(9600, SERIAL_8N1, 17, 4);  // RO, DI
  pinMode(SENSOR1_RE_DE_PIN, OUTPUT);
  digitalWrite(SENSOR1_RE_DE_PIN, LOW);

  pinMode(pin_flow, INPUT_PULLUP);
  pinMode(pin_booster_pump, OUTPUT);
  pinMode(pin_oxygen_concentrator, OUTPUT);
  pinMode(pin_ozone_generator, OUTPUT);
  pinMode(pin_nanobubble_pump, OUTPUT);

  delay(3000);
  nextion.page_cur = 1;
  Serial.println("started");
}

void loop() {
  // TODO: implement logic of power
  power.state_cur = 1;
  power.state_old = power.state_cur;
  power.nextion_refresh = 1;

  // TODO: implement logic of valve_bypass
  valve_bypass.state_cur = 0;
  valve_bypass.state_old = valve_bypass.state_cur;
  valve_bypass.nextion_refresh = 1;

  flow_switch.state_cur = digitalRead(pin_flow);
  if (flow_switch.state_old != flow_switch.state_cur) {
    flow_switch.state_old = flow_switch.state_cur;
    flow_switch.nextion_refresh = 1;
    if (flow_switch.state_cur == 0) {
      cycle_state = 0;
      cycle_millis = millis();
    } else {
      cycle_state = 100;
      cycle_millis = millis();
    }
  }

  cycle_manager();

  
  sensor_update();

  nextion_update();
  oxygen_sensor_manager();
}
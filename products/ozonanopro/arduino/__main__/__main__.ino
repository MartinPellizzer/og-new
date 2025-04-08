///////////////////////////////////////////////////////////////////////
// ;oxygen sensor
///////////////////////////////////////////////////////////////////////
HardwareSerial oxygen_sensor_serial(1);
#define OXYGEN_SENSOR_RE_DE_GPIO 16
#define OXYGEN_SENSOR_RX_GPIO 17
#define OXYGEN_SENSOR_TX_GPIO 4
#define OXYGEN_SENSOR_BUFF_LEN 12
typedef struct oxygen_sensor_t {
  uint8_t receiver_buff[OXYGEN_SENSOR_BUFF_LEN] = { 0 };
  uint8_t receiver_buff_index = 0;
  uint32_t receiver_timer = 0;
  uint32_t receiver_timer_no_signal = 0;
  int8_t is_connected = 0;
  uint32_t connected_millis = 0;
  uint32_t connected_seconds = 0;
  uint8_t bytestream_receiving = 0;
  uint8_t bytestream_received = 0;
  int16_t concentration_old = -2;
  int16_t concentration_cur = -1;
  int16_t flow_old = -2;
  int16_t flow_cur = -1;
  int16_t temperature_old = -2;
  int16_t temperature_cur = -1;
} oxygen_sensor_t;
oxygen_sensor_t oxygen_sensor = {};

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
  int16_t starting_delay_millis = 0;
  int8_t started = 0;
} nextion_t;
nextion_t nextion = {};

///////////////////////////////////////////////////////////////////////
// ;sensors
///////////////////////////////////////////////////////////////////////
typedef struct flow_switch_t {
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} flow_switch_t;
flow_switch_t flow_switch = {};

typedef struct pressure_switch_t {
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} pressure_switch_t;
pressure_switch_t pressure_switch = {};

typedef struct valve_input_t {
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} valve_input_t;
valve_input_t valve_input = {};

typedef struct valve_bypass_t {
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} valve_bypass_t;
valve_bypass_t valve_bypass_1 = {};
valve_bypass_t valve_bypass_2 = {};

typedef struct pump_booster_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} pump_booster_t;
pump_booster_t pump_booster = {};

typedef struct pump_nano_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
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

typedef struct solenoid_t {  
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
} solenoid_t;
solenoid_t solenoid = {};

#define VALVE_INPUT_GPIO 5
#define PUMP_BOOSTER_GPIO 18
#define PUMP_NANO_GPIO 19
#define FLOW_SWITCH_GPIO 25
#define PRESSURE_SWITCH_GPIO 26
#define VALVE_BYPASS_1_GPIO 2
#define VALVE_BYPASS_2_GPIO 13

#define OXYGEN_CONCENTRATOR_GPIO 32
#define OZONE_GENERATOR_GPIO 33
#define SOLENOID_GPIO 23

typedef struct cycle_t {  
  uint16_t state_old = -1;
  uint16_t state_cur = 0;
  uint16_t pressure_switch_state_old = -1;
  uint16_t pressure_switch_state_cur = 0;
  uint16_t flow_switch_state_old = -1;
  uint16_t flow_switch_state_cur = 0;
} cycle_t;
cycle_t cycle = {};

uint32_t cycle_millis = 0;

void valve_input_state_update(uint8_t val)
{
  valve_input.state_cur = val;
  if (valve_input.state_old != valve_input.state_cur) 
  {
    valve_input.state_old = valve_input.state_cur;
    valve_input.nextion_refresh = 1;
    if (valve_input.state_cur == 1) { digitalWrite(VALVE_INPUT_GPIO, HIGH); }
    else { digitalWrite(VALVE_INPUT_GPIO, LOW); }
  }
}

void valve_bypass_1_state_update(uint8_t val)
{
  valve_bypass_1.state_cur = val;
  if (valve_bypass_1.state_old != valve_bypass_1.state_cur) 
  {
    valve_bypass_1.state_old = valve_bypass_1.state_cur;
    valve_bypass_1.nextion_refresh = 1;
    if (valve_bypass_1.state_cur == 1) { digitalWrite(VALVE_BYPASS_1_GPIO, HIGH); }
    else { digitalWrite(VALVE_BYPASS_1_GPIO, LOW); }
  }
}

void valve_bypass_2_state_update(uint8_t val)
{
  valve_bypass_2.state_cur = val;
  if (valve_bypass_2.state_old != valve_bypass_2.state_cur) 
  {
    valve_bypass_2.state_old = valve_bypass_2.state_cur;
    valve_bypass_2.nextion_refresh = 1;
    if (valve_bypass_2.state_cur == 1) { digitalWrite(VALVE_BYPASS_2_GPIO, HIGH); }
    else { digitalWrite(VALVE_BYPASS_2_GPIO, LOW); }
  }
}

void pressure_switch_state_update()
{
  pressure_switch.state_cur = !digitalRead(PRESSURE_SWITCH_GPIO);
  if (pressure_switch.state_old != pressure_switch.state_cur) 
  {
    pressure_switch.state_old = pressure_switch.state_cur;
    pressure_switch.nextion_refresh = 1;
    cycle.pressure_switch_state_cur = pressure_switch.state_cur;
  }
}

void flow_switch_state_update()
{
  flow_switch.state_cur = !digitalRead(FLOW_SWITCH_GPIO);
  if (flow_switch.state_old != flow_switch.state_cur) 
  {
    flow_switch.state_old = flow_switch.state_cur;
    flow_switch.nextion_refresh = 1;
    cycle.flow_switch_state_cur = flow_switch.state_cur;
  }
}

void pump_booster_state_update(uint8_t val)
{
  pump_booster.state_cur = val;
  if (pump_booster.state_old != pump_booster.state_cur) 
  {
    pump_booster.state_old = pump_booster.state_cur;
    pump_booster.nextion_refresh = 1;
    if (pump_booster.state_cur == 1) { digitalWrite(PUMP_BOOSTER_GPIO, HIGH); }
    else { digitalWrite(PUMP_BOOSTER_GPIO, LOW); }
  }
}

void pump_nano_state_update(uint8_t val)
{
  pump_nano.state_cur = val;
  if (pump_nano.state_old != pump_nano.state_cur) 
  {
    pump_nano.state_old = pump_nano.state_cur;
    pump_nano.nextion_refresh = 1;
    if (pump_nano.state_cur == 1) { digitalWrite(PUMP_NANO_GPIO, HIGH); }
    else { digitalWrite(PUMP_NANO_GPIO, LOW); }
  }
}

void oxygen_concentrator_state_update(uint8_t val)
{
  oxygen_concentrator.state_cur = val;
  if (oxygen_concentrator.state_old != oxygen_concentrator.state_cur) 
  {
    oxygen_concentrator.state_old = oxygen_concentrator.state_cur;
    oxygen_concentrator.nextion_refresh = 1;
    if (oxygen_concentrator.state_cur == 1) { digitalWrite(OXYGEN_CONCENTRATOR_GPIO, HIGH); }
    else { digitalWrite(OXYGEN_CONCENTRATOR_GPIO, LOW); }
  }
}
void ozone_generator_state_update(uint8_t val)
{
  ozone_generator.state_cur = val;
  if (ozone_generator.state_old != ozone_generator.state_cur) 
  {
    ozone_generator.state_old = ozone_generator.state_cur;
    ozone_generator.nextion_refresh = 1;
    if (ozone_generator.state_cur == 1) { digitalWrite(OZONE_GENERATOR_GPIO, HIGH); }
    else { digitalWrite(OZONE_GENERATOR_GPIO, LOW); }
  }
}

void solenoid_state_update(uint8_t val)
{
  solenoid.state_cur = val;
  if (solenoid.state_old != solenoid.state_cur) 
  {
    solenoid.state_old = solenoid.state_cur;
    solenoid.nextion_refresh = 1;
    if (solenoid.state_cur == 1) { digitalWrite(SOLENOID_GPIO, HIGH); }
    else { digitalWrite(SOLENOID_GPIO, LOW); }
  }
}

void cycle_update()
{
  if (cycle.pressure_switch_state_old != cycle.pressure_switch_state_cur || cycle.flow_switch_state_old != cycle.flow_switch_state_cur )
  {
    cycle.pressure_switch_state_old = cycle.pressure_switch_state_cur;
    cycle.flow_switch_state_old = cycle.flow_switch_state_cur;
    if (pressure_switch.state_cur == 1)
    {
      valve_input_state_update(0);
      valve_bypass_1_state_update(0);
      valve_bypass_2_state_update(1);
      oxygen_concentrator_state_update(0);
      ozone_generator_state_update(0);
      solenoid_state_update(0);
      cycle.state_cur = 200;
      // cycle.state_cur = 300;
    }
    else if (pressure_switch.state_cur == 0)
    {
      if (flow_switch.state_cur == 1)
      {
        valve_input_state_update(1);
        valve_bypass_1_state_update(1);
        valve_bypass_2_state_update(0);
        cycle.state_cur = 100;
      }
      if (flow_switch.state_cur == 0)
      {
        valve_input_state_update(1);
        valve_bypass_1_state_update(1);
        valve_bypass_2_state_update(0);
        oxygen_concentrator_state_update(0);
        ozone_generator_state_update(0);
        solenoid_state_update(0);
        cycle.state_cur = 0;
      }
    }
    cycle_millis = millis();
  }

  if (cycle.state_cur == 0)
  {
    valve_input_state_update(1);
    pump_booster_state_update(1);
    if (millis() - cycle_millis > 1000)
    {
      cycle_millis = millis();
      cycle.state_cur = 1;
    }
  }
  else if (cycle.state_cur == 1)
  {
    pump_nano_state_update(1);
    if (millis() - cycle_millis > 19000)
    {
      cycle_millis = millis();
      cycle.state_cur = 2;
    }
  }
  else if (cycle.state_cur == 100)
  {
    valve_input_state_update(1);
    pump_booster_state_update(1);
    if (millis() - cycle_millis > 1000)
    {
      cycle_millis = millis();
      cycle.state_cur = 101;
    }
  }
  else if (cycle.state_cur == 101)
  {
    pump_nano_state_update(1);
    if (millis() - cycle_millis > 1000)
    {
      cycle_millis = millis();
      cycle.state_cur = 102;
    }
  }
  else if (cycle.state_cur == 102)
  {
    oxygen_concentrator_state_update(1);
    ozone_generator_state_update(1);
    solenoid_state_update(1);
  }
  else if (cycle.state_cur == 200)
  {
    pump_booster_state_update(1);
    if (millis() - cycle_millis > 1000)
    {
      cycle_millis = millis();
      cycle.state_cur = 201;
    }
  }
  else if (cycle.state_cur == 201)
  {
    pump_nano_state_update(1);
    if (millis() - cycle_millis > 19000)
    {
      cycle_millis = millis();
      cycle.state_cur = 202;
    }
  }
  else
  {
    pump_booster_state_update(0);
    pump_nano_state_update(0);
  }

}

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);

  pinMode(FLOW_SWITCH_GPIO, INPUT_PULLUP);
  pinMode(PRESSURE_SWITCH_GPIO, INPUT_PULLUP);
  pinMode(VALVE_INPUT_GPIO, OUTPUT);
  digitalWrite(VALVE_INPUT_GPIO, LOW);
  pinMode(PUMP_BOOSTER_GPIO, OUTPUT);
  digitalWrite(PUMP_BOOSTER_GPIO, LOW);
  pinMode(PUMP_NANO_GPIO, OUTPUT);
  digitalWrite(PUMP_NANO_GPIO, LOW);
  pinMode(VALVE_BYPASS_1_GPIO, OUTPUT);
  digitalWrite(VALVE_BYPASS_1_GPIO, LOW);
  pinMode(VALVE_BYPASS_2_GPIO, OUTPUT);
  digitalWrite(VALVE_BYPASS_2_GPIO, LOW);

  pinMode(OXYGEN_CONCENTRATOR_GPIO, OUTPUT);
  digitalWrite(OXYGEN_CONCENTRATOR_GPIO, LOW);
  pinMode(OZONE_GENERATOR_GPIO, OUTPUT);
  digitalWrite(OZONE_GENERATOR_GPIO, LOW);
  pinMode(SOLENOID_GPIO, OUTPUT);
  digitalWrite(SOLENOID_GPIO, LOW);
  
  oxygen_sensor_serial.begin(9600, SERIAL_8N1, OXYGEN_SENSOR_RX_GPIO, OXYGEN_SENSOR_TX_GPIO);  // RO, DI
  pinMode(OXYGEN_SENSOR_RE_DE_GPIO, OUTPUT);
  digitalWrite(OXYGEN_SENSOR_RE_DE_GPIO, LOW);

  nextion.page_cur = 1;
  Serial.println("setup");
}

void loop() 
{
  flow_switch_state_update();
  pressure_switch_state_update();
  oxygen_sensor_manager();

  cycle_update();

  if (nextion.started == 0)
  {
    if (millis() - nextion.starting_delay_millis > 3000)
    {
      nextion.started = 1;
      nextion.page_cur = 1;
    }
  }
  if (nextion.started == 1)
  {
    nextion_update();
  }

  // Serial.print("FLOW SWITCH: ");
  // Serial.println(digitalRead(FLOW_SWITCH_GPIO));
  // Serial.print("PRESSURE SWITCH: ");
  // Serial.println(digitalRead(PRESSURE_SWITCH_GPIO));

}
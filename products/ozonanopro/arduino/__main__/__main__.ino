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

#define PUMP_VALVE_GPIO 5
#define PUMP_BOOSTER_GPIO 18
#define PUMP_NANO_GPIO 19
#define FLOW_SWITCH_GPIO 25
#define PRESSURE_SWITCH_GPIO 26
#define VALVE_BYPASS_1_GPIO 2
#define VALVE_BYPASS_2_GPIO 13

uint16_t cycle_state = 0;
uint32_t cycle_millis = 0;

void cycle_starting()
{
  if (cycle_state == 0)
  {
    digitalWrite(PUMP_VALVE_GPIO, HIGH);
    
    digitalWrite(PUMP_BOOSTER_GPIO, HIGH);
    pump_booster.state_cur = 0;
    if (pump_booster.state_old != pump_booster.state_cur) 
    {
      pump_booster.state_old = pump_booster.state_cur;
      pump_booster.nextion_refresh = 1;
    }

    if (millis() - cycle_millis > 1000)
    {
      cycle_millis = millis();
      cycle_state = 1;
    }
  }
  else if (cycle_state == 1)
  {
    digitalWrite(PUMP_NANO_GPIO, HIGH);
    if (millis() - cycle_millis > 19000)
    {
      cycle_millis = millis();
      cycle_state = 2;
    }
  }
  else
  {
    digitalWrite(PUMP_VALVE_GPIO, LOW);
    
    digitalWrite(PUMP_BOOSTER_GPIO, LOW);
    pump_booster.state_cur = 1;
    if (pump_booster.state_old != pump_booster.state_cur) 
    {
      pump_booster.state_old = pump_booster.state_cur;
      pump_booster.nextion_refresh = 1;
    }
    digitalWrite(PUMP_NANO_GPIO, LOW);
  }

}

void cycle_manager()
{
  cycle_starting();  
}

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);

  pinMode(FLOW_SWITCH_GPIO, INPUT_PULLUP);
  pinMode(PRESSURE_SWITCH_GPIO, INPUT_PULLUP);

  pinMode(PUMP_VALVE_GPIO, OUTPUT);
  digitalWrite(PUMP_VALVE_GPIO, LOW);

  pinMode(PUMP_BOOSTER_GPIO, OUTPUT);
  digitalWrite(PUMP_BOOSTER_GPIO, LOW);

  pinMode(PUMP_NANO_GPIO, OUTPUT);
  digitalWrite(PUMP_NANO_GPIO, LOW);

  pinMode(VALVE_BYPASS_1_GPIO, OUTPUT);
  digitalWrite(VALVE_BYPASS_1_GPIO, LOW);
  pinMode(VALVE_BYPASS_2_GPIO, OUTPUT);
  digitalWrite(VALVE_BYPASS_1_GPIO, LOW);
  
  oxygen_sensor_serial.begin(9600, SERIAL_8N1, OXYGEN_SENSOR_RX_GPIO, OXYGEN_SENSOR_TX_GPIO);  // RO, DI
  pinMode(OXYGEN_SENSOR_RE_DE_GPIO, OUTPUT);
  digitalWrite(OXYGEN_SENSOR_RE_DE_GPIO, LOW);

  nextion.page_cur = 1;
  Serial.println("setup");
}

void loop() 
{
  oxygen_sensor_manager();

  cycle_manager();

  if (nextion.started == 0)
  {
    if (millis() - nextion.starting_delay_millis > 2000)
    {
      nextion.started = 1;
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

  flow_switch.state_cur = digitalRead(FLOW_SWITCH_GPIO);
  if (flow_switch.state_old != flow_switch.state_cur) 
  {
    flow_switch.state_old = flow_switch.state_cur;
    flow_switch.nextion_refresh = 1;
  }

  pressure_switch.state_cur = digitalRead(PRESSURE_SWITCH_GPIO);
  if (pressure_switch.state_old != pressure_switch.state_cur) 
  {
    pressure_switch.state_old = pressure_switch.state_cur;
    pressure_switch.nextion_refresh = 1;
    if (pressure_switch.state_cur == 1)
    {
      valve_bypass_1.state_cur = 1;
      if (valve_bypass_1.state_old != valve_bypass_1.state_cur) 
      {
        valve_bypass_1.state_old = valve_bypass_1.state_cur;
        valve_bypass_1.nextion_refresh = 1;
        digitalWrite(VALVE_BYPASS_1_GPIO, HIGH);
      }
      valve_bypass_2.state_cur = 0;
      if (valve_bypass_2.state_old != valve_bypass_2.state_cur) 
      {
        valve_bypass_2.state_old = valve_bypass_2.state_cur;
        valve_bypass_2.nextion_refresh = 1;
        digitalWrite(VALVE_BYPASS_2_GPIO, LOW);
      }
    }
    else
    {
      valve_bypass_1.state_cur = 0;
      if (valve_bypass_1.state_old != valve_bypass_1.state_cur) 
      {
        valve_bypass_1.state_old = valve_bypass_1.state_cur;
        valve_bypass_1.nextion_refresh = 1;
        digitalWrite(VALVE_BYPASS_1_GPIO, LOW);
      }
      valve_bypass_2.state_cur = 1;
      if (valve_bypass_2.state_old != valve_bypass_2.state_cur) 
      {
        valve_bypass_2.state_old = valve_bypass_2.state_cur;
        valve_bypass_2.nextion_refresh = 1;
        digitalWrite(VALVE_BYPASS_2_GPIO, HIGH);
      }
    }
  }
}
// OZONANOPRO 2.2

// OUTPUTS
#define RO_VI 13
#define RO_VO 15
#define RO_VB 5
#define RO_PB 25
#define RO_PN 26
#define RO_O2 18
#define RO_O3 19
#define RO_SO 23

// INPUTS
#define RI_P 33

enum Nextion_Pages {
  P_SPLASH,
  P_HOME,
  P_SET,
};

enum Cycle_States {
  CICLE_0,
  CICLE_1,
  CICLE_2,
  CICLE_3,
};

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

///////////////////////////////////////////////////////////////////////
// ;cycle
///////////////////////////////////////////////////////////////////////
typedef struct cycle_t {
  int8_t state_vi_old = -2;
  int8_t state_vi_tmp = -1;
  int8_t state_vi_cur = 0;

  int8_t state_vo_old = -2;
  int8_t state_vo_tmp = -1;
  int8_t state_vo_cur = 0;

  int8_t state_vb_old = -2;
  int8_t state_vb_tmp = -1;
  int8_t state_vb_cur = 0;

  int8_t state_pb_old = -2;
  int8_t state_pb_tmp = -1;
  int8_t state_pb_cur = 0;

  int8_t state_pn_old = -2;
  int8_t state_pn_tmp = -1;
  int8_t state_pn_cur = 0;

  int8_t state_o2_old = -2;
  int8_t state_o2_tmp = -1;
  int8_t state_o2_cur = 0;

  int8_t state_o3_old = -2;
  int8_t state_o3_tmp = -1;
  int8_t state_o3_cur = 0;

  int8_t state_so_old = -2;
  int8_t state_so_tmp = -1;
  int8_t state_so_cur = 0;

  int8_t mode_old = -2;
  int8_t mode_tmp = -1;
  int8_t mode_cur = 0;

  uint16_t state_old = -1;
  uint16_t state_cur = 0;
  uint16_t pressure_switch_state_old = -1;
  uint16_t pressure_switch_state_cur = 0;
  uint16_t flow_switch_state_old = -1;
  uint16_t flow_switch_state_cur = 0;
  int32_t bypass_millis_cur = 0;
  int32_t bypass_timer_cur = 15000;
  int32_t ozone_millis_cur = 0;
  int32_t ozone_timer_cur = 3000;

  int8_t state_onoff_old = -2;
  int8_t state_onoff_tmp = -1;
  int8_t state_onoff_cur = 0;
} cycle_t;
cycle_t cycle = {};

int32_t debug_millis_cur = 0;

///////////////////////////////////////////////////////////////////////
// ;cycle
///////////////////////////////////////////////////////////////////////
typedef struct settings_t {
  int16_t pressure_delay_mills_old = -2;
  int16_t pressure_delay_mills_tmp = -1;
  int16_t pressure_delay_mills_cur = 0;
} settings_t;
settings_t settings = {};

///////////////////////////////////////////////////////////////////////
// ;pressure switch
///////////////////////////////////////////////////////////////////////
typedef struct pressure_switch_t {
  int8_t state_old = -1;
  int8_t state_cur = 0;
  int8_t nextion_refresh = 0;
  uint32_t trigger_counter = 0;
  uint32_t trigger_debounce_millis = 0;
  uint32_t trigger_debounce_millis_delay = 50;

} pressure_switch_t;
pressure_switch_t pressure_switch = {};


void pressure_switch_state_update()
{
  int reading = !digitalRead(RI_P);

  if (reading != pressure_switch.state_old) 
  {
    pressure_switch.trigger_debounce_millis = millis();
  }

  if ((millis() - pressure_switch.trigger_debounce_millis) > settings.pressure_delay_mills_cur) 
  {
    if (reading != pressure_switch.state_cur) 
    {
      pressure_switch.state_cur = reading;
      pressure_switch.nextion_refresh = 1;
      cycle.pressure_switch_state_cur = pressure_switch.state_cur;
      if (pressure_switch.state_cur == 0)
      {
        pressure_switch.trigger_counter += 1;
        Serial.println(pressure_switch.trigger_counter);
      }
    }
  }

  pressure_switch.state_old = reading;
}


void debug()
{
}

void setup() 
{
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  
  pinMode(RO_VI, OUTPUT);
  digitalWrite(RO_VI, 0);
  pinMode(RO_VO, OUTPUT);
  digitalWrite(RO_VO, 0);
  pinMode(RO_VB, OUTPUT);
  digitalWrite(RO_VB, 0);
  pinMode(RO_PB, OUTPUT);
  digitalWrite(RO_PB, 0);
  pinMode(RO_PN, OUTPUT);
  digitalWrite(RO_PN, 0);
  pinMode(RO_O2, OUTPUT);
  digitalWrite(RO_O2, 0);
  pinMode(RO_O3, OUTPUT);
  digitalWrite(RO_O3, 0);
  pinMode(RO_SO, OUTPUT);
  digitalWrite(RO_SO, 0);

  pinMode(RI_P, INPUT_PULLUP);

  delay(3000);
  nextion.page_cur = P_HOME;
  Serial.println("setup");
}

void loop() 
{
  pressure_switch_state_update();

  // ;cycle
  cycle_manager();
  
  // ;nextion
  nextion_manager();

  debug();
}
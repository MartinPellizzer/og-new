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

enum Nextion_Pages {
  P_SPLASH,
  P_HOME,
  P_PASSWORD,
  P_SET_OPERATOR,
  P_SET_OZONOGROUP,
  P_POWER,
  P_CAL_EN,
  P_CAL_TIME,
  P_CAL_ADD,
  P_CAL_DEL,
  P_CAL_ADD_ERR_NEG,
  P_CAL_ADD_ERR_OVR,
  P_CLK,
  P_CLK_DATE,
  P_CLK_TIME,
  P_EXT,
  P_SENSOR_ALARM,
  P_OZONE_ALARM,
  P_TEMPERATURE_ALARM,
  P_TEMPERATURE,
  P_CYCLE_CUSTOM,
  P_CYCLE_CUSTOM_OPERATION_NUM,
};

void setup()
{
  Serial.begin(9600);

  // NEXTION INIT
  Serial2.begin(9600, SERIAL_8N1, 27, 14);
  delay(3000);
  nextion.page_cur = 1;
  Serial.println("setup");

}

void loop() 
{
  nextion_manager();

}

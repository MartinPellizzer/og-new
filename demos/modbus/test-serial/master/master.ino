HardwareSerial serial_modbus(1);

const uint8_t MASTER_SENDER_BUFF_SIZE = 8; 
const uint8_t MASTER_RECEIVER_BUFF_SIZE = 7; 

typedef struct modbus_t {
  uint8_t sender_buff[MASTER_SENDER_BUFF_SIZE] = {0};
  uint8_t sender_buff_index = 0;
  uint32_t sender_timer = 0;
  uint8_t receiver_buff[MASTER_RECEIVER_BUFF_SIZE] = {0};
  uint8_t receiver_buff_index = 0;
  uint32_t receiver_timer = 0;
  uint8_t bytestream_receiving = 0;
  uint8_t bytestream_received = 0;
  uint8_t device_id = 0x00;
} modbus_t;
modbus_t modbus = {};

uint8_t query_pressure_analog_in[MASTER_SENDER_BUFF_SIZE] = {0x16, 0x04, 0x00, 0x12, 0x00, 0x01, 0x00, 0x00};

void setup() 
{
  Serial.begin(9600);
  serial_modbus.begin(9600, SERIAL_8N1, 17, 4);
  modbus_crc16(query_pressure_analog_in, MASTER_SENDER_BUFF_SIZE-2);
}

void loop() 
{
  if (millis() - modbus.sender_timer > 1000)
  {
    modbus.sender_timer = millis();
    modbus_write(query_pressure_analog_in, MASTER_SENDER_BUFF_SIZE);
    Serial.print("MODBUS SEND:    ");
    modbus_print_hex(query_pressure_analog_in, MASTER_SENDER_BUFF_SIZE);
  }

  modbus_read();
  if (modbus.bytestream_received)
  {
    modbus.bytestream_received = 0;
    
    Serial.print("MODBUS RECEIVE: ");
    modbus_print_hex(modbus.receiver_buff, MASTER_RECEIVER_BUFF_SIZE);

    uint8_t crc_valid = modbus_crc16_check(modbus.receiver_buff, MASTER_RECEIVER_BUFF_SIZE-2);
    if (crc_valid == 1)
    {
      Serial.println("CRC OK");
      uint8_t ozone_val_hb = modbus.receiver_buff[3];
      uint8_t ozone_val_lb = modbus.receiver_buff[4];
      uint16_t ozone_val = uint8x2_to_uint16(ozone_val_hb, ozone_val_lb);
      Serial.print("OZONE VAL: ");
      Serial.println(ozone_val);
    }
    else
    {
      Serial.println("ERROR: CRC FAIL");
    }
  }
}

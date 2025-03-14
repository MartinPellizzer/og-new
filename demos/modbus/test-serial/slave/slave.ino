#include <SoftwareSerial.h>

SoftwareSerial serial_modbus(2, 3);

const uint8_t SLAVE_SENDER_BUFF_SIZE = 7; 
const uint8_t SLAVE_RECEIVER_BUFF_SIZE = 8; 

typedef struct modbus_t {
  uint8_t sender_buff[SLAVE_SENDER_BUFF_SIZE] = {0};
  uint8_t sender_buff_index = 0;
  uint32_t sender_timer = 0;
  uint8_t receiver_buff[SLAVE_RECEIVER_BUFF_SIZE] = {0};
  uint8_t receiver_buff_index = 0;
  uint32_t receiver_timer = 0;
  uint8_t bytestream_receiving = 0;
  uint8_t bytestream_received = 0;
  uint8_t device_id = 0x00;
} modbus_t;
modbus_t modbus = {};

uint8_t error_buff[8] = {0};

int16_t ozone_val = 765;


void setup()
{
  Serial.begin(9600);
  serial_modbus.begin(9600);
  Serial.println("serial init");
  modbus.device_id = 0x16;
}

void modbus_process_query()
{
  uint8_t id = modbus.receiver_buff[0];
  uint8_t command = modbus.receiver_buff[1];
  uint8_t address = modbus.receiver_buff[3];
  uint8_t blocks = modbus.receiver_buff[5];
  uint8_t buff_data[2] = {0};
  uint16_to_uint8x2(buff_data, 2, ozone_val);

  if (command == 0x04 && address == 0x12 && blocks == 0x01)
  {
    modbus.sender_buff[0] = id;
    modbus.sender_buff[1] = command;
    modbus.sender_buff[2] = 0x02;
    modbus.sender_buff[3] = buff_data[0];
    modbus.sender_buff[4] = buff_data[1];
    modbus_crc16(modbus.sender_buff, SLAVE_SENDER_BUFF_SIZE-2);
  }
}



void loop()
{
  modbus_read();
  if (modbus.bytestream_received)
  {
    modbus.bytestream_received = 0;
    
    uint8_t crc_valid = modbus_crc16_check(modbus.receiver_buff, SLAVE_RECEIVER_BUFF_SIZE-2);
    if (crc_valid == 1)
    {
      Serial.println("CRC OK");
      uint8_t id_valid = modbus_match_id();
      if (id_valid == 1)
      {
        Serial.println("ID OK");
        modbus_process_query();
        modbus_write(modbus.sender_buff, SLAVE_SENDER_BUFF_SIZE);
        Serial.print("MODBUS SEND:    ");
        modbus_print_hex(modbus.sender_buff, SLAVE_SENDER_BUFF_SIZE);
        Serial.println();
      }
      else
      {
        Serial.println("ERROR: ID FAIL");
        modbus_write(error_buff, SLAVE_RECEIVER_BUFF_SIZE);
      }
    }
    else
    {
      Serial.println("ERROR: CRC FAIL");
      modbus_write(error_buff, SLAVE_RECEIVER_BUFF_SIZE);
    }
    Serial.print("MODBUS RECEIVE: ");
    modbus_print_hex(modbus.receiver_buff, SLAVE_RECEIVER_BUFF_SIZE);
  }
}

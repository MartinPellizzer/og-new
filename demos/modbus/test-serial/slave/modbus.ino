// use the same following settings for all RS485 devices in the same network
uint32_t baud_rate = 9600;
uint8_t n_data_bits = 8;
uint8_t n_stop_bits = 1;
uint8_t parity = 0;

void modbus_write(uint8_t *buf, int len) 
{
  for(int pos = 0; pos < len; pos++)
  {
    serial_modbus.write(buf[pos]);
  }
}

void modbus_read() 
{
  if (serial_modbus.available() > 0) 
  {
    uint8_t c = serial_modbus.read();
    modbus.receiver_buff[modbus.receiver_buff_index] = c;
    modbus.receiver_buff_index++;
    modbus.bytestream_receiving = 1;
    modbus.receiver_timer = millis();
  }

  if (modbus.bytestream_receiving) 
  {
    if (millis() - modbus.receiver_timer > 40) 
    {
      modbus.receiver_buff_index = 0;
      modbus.bytestream_receiving = 0;
      modbus.bytestream_received = 1;
    }
  }
}

void modbus_print_hex(uint8_t *buf, int len) 
{
  for(int i = 0; i < len; i++)
  {
    Serial.print("0x");
    Serial.print(buf[i], HEX);
    Serial.print(" ");
  }
  Serial.println();
}

void modbus_print_dec(uint8_t *buf, int len) 
{
  for(int i = 0; i < len; i++)
  {
    Serial.print(buf[i]);
    Serial.print(" ");
  }
  Serial.println();
}

//////////////////////////////////////////////////
// CRC
//////////////////////////////////////////////////
void modbus_crc16(uint8_t *buf, int len)
{
  uint16_t crc = modbus_crc16_calculate(buf, len);
  modbus_crc16_update(buf, len, crc);
}

uint16_t modbus_crc16_calculate(uint8_t *buf, int len) 
{
  uint16_t crc = 0xFFFF;
  for (int pos = 0; pos < len; pos++) 
  {
    crc ^= (uint16_t)buf[pos];
    for (int i = 8; i != 0; i--) 
    {
      if ((crc & 0x0001) != 0) 
      {
        crc >>= 1;
        crc ^= 0xA001;
      }
      else 
      {
        crc >>= 1;
      }
    }
  }
  return crc;
}

void modbus_crc16_update(uint8_t *buf, int len, uint16_t crc)
{
    uint8_t highByte = (crc >> 8) & 0xFF;
    uint8_t lowByte = crc & 0xFF;
    buf[len] = lowByte;
    buf[len+1] = highByte;
}


uint8_t modbus_crc16_check(uint8_t *buf, int len)
{
  uint8_t crc_valid = 0;
  uint16_t crc_cur = modbus_crc16_calculate(buf, len);
  uint8_t crc_cur_hb = (crc_cur >> 8) & 0xFF;
  uint8_t crc_cur_lb = crc_cur & 0xFF;
  uint8_t crc_old_hb = buf[len+1];
  uint8_t crc_old_lb = buf[len];
  if (crc_cur_hb == crc_old_hb && crc_cur_lb == crc_old_lb)
  {
    crc_valid = 1;
  }
  else
  {
    crc_valid = 0;
  }
  return crc_valid;
}

uint8_t modbus_match_id()
{
  uint8_t id_valid = 0;
  if (modbus.receiver_buff[0] == modbus.device_id)
  {
    id_valid = 1;
  }
  return id_valid;
}


void uint16_to_uint8x2(uint8_t *buf, int len, uint16_t val)
{
  if (len == 2)
  {
    uint8_t high_byte = (val >> 8) & 0xFF;
    uint8_t low_byte = val & 0xFF;
    buf[0] = high_byte;
    buf[1] = low_byte;
  }
} 

uint16_t uint8x2_to_uint16(uint8_t high_byte, uint8_t low_byte)
{
  uint16_t res = (high_byte << 8) + low_byte;
  return res;
} 
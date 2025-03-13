void setup() {
  Serial.begin(9600);

  Serial.println();
  Serial.println();
  // Example Modbus query data (without CRC)
  uint8_t data[] = { 0x01, 0x03, 0x02, 0x00, 0x00 };  // Slave address, function code, data...

  // Length of the Modbus query (excluding CRC)
  size_t length = sizeof(data) / sizeof(data[0]);

  // Calculate CRC for the query data
  uint16_t crc = modbus_crc16(data, length);

  // Print the CRC in hexadecimal format
  Serial.print("CRC: 0x");
  Serial.println(crc, HEX);  // Print CRC as hex

  // Split the 16-bit value into two 8-bit values
  uint8_t highByte = (crc >> 8) & 0xFF;  // Extract high byte
  uint8_t lowByte = crc & 0xFF;          // Extract low byte

  // Print both 8-bit values
  Serial.print("High byte: 0x");
  Serial.println(highByte, HEX);

  Serial.print("Low byte: 0x");
  Serial.println(lowByte, HEX);

  uint8_t data_final[] = { 0x01, 0x03, 0x02, 0x00, 0x00, lowByte, highByte };

  for (int i = 0; i < sizeof(data_final); i++) {
    Serial.print("0x");
    Serial.print(data_final[i], HEX);
    Serial.print(" ");
  }
}

void loop() {

  delay(1000);
}

uint16_t modbus_crc16(uint8_t *buf, int len)
{
  uint16_t crc = 0xFFFF;
  for (int pos = 0; pos < len; pos++) {
    crc ^= (uint16_t)buf[pos];
    for (int i = 8; i != 0; i--) {
      if ((crc & 0x0001) != 0) {
        crc >>= 1;
        crc ^= 0xA001;
      }
      else
        crc >>= 1;
    }
  }
  return crc;  
}
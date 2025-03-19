#include <SoftwareSerial.h>
SoftwareSerial serial_modbus(2, 3);

void setup() 
{
  serial_modbus.begin(9600);
}

void loop() 
{
  serial_modbus.write(0x31);
  delay(1000);
}

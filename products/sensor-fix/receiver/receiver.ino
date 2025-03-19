HardwareSerial Receiver(1);

#define BUFF_LEN 9
uint8_t buff[BUFF_LEN] = {0};
uint8_t i = 0;
uint8_t new_data = 0;
uint32_t timer = 0;
uint32_t timer_no_signal = 0;

#define RE_DE_PIN 16

void setup() 
{
  // SERAIL DEBUG
  Serial.begin(9600);

  // RS485
  Receiver.begin(9600, SERIAL_8N1, 17, 14);
  pinMode(RE_DE_PIN, OUTPUT);
  digitalWrite(RE_DE_PIN, LOW);
}

void loop() 
{
  Serial.println("test");
  // read rs485, convert in 0-10v, output 0-10v
  if (new_data)
  {
    if (millis() - timer > 40)
    {
      timer_no_signal = millis();

      i = 0;
      new_data = 0;

      int ppb = 0;      

      if (checksum(buff, 9) == buff[8]) 
      {
        ppb = buff[4] * 256 + buff[5];
      }
      
      clear_buffer(buff, BUFF_LEN);
    }
  }   

  if (Receiver.available() > 0)  
  {
    uint8_t c = Receiver.read();
    buff[i] = c;
    i++;
    new_data = 1;
    timer = millis();
  }
}

void clear_buffer(uint8_t buff[], uint8_t len)
{
  for(int i = 0; i < len; i++) buff[i] = 0;
}

unsigned char checksum(unsigned char *i, unsigned char ln)
{
  unsigned char j, tempq = 0;
  i += 1;
  for (j = 0; j < (ln - 2); j++)
  {
    tempq += *i;
    i++;
  }
  tempq = (~tempq) + 1; return (tempq);
}

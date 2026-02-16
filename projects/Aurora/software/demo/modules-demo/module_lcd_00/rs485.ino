// MODULE: 00

void rs485_read()
{
  if (rs485.new_data_state)
  {
    if (millis() - rs485.new_data_timer > 40)
    {
      rs485.receiver_buffer_i = 0;
      rs485.new_data_state = 0;
      rs485.receiver_buffer_ready = 1;
    }
  }
  
  if (serial_rs485.available() > 0)  
  {
    uint8_t c = serial_rs485.read();
    rs485.receiver_buffer[rs485.receiver_buffer_i] = c;
    rs485.receiver_buffer_i++;
    rs485.new_data_state = 1;
    rs485.new_data_timer = millis();
  }
}

void rs485_write()
{
    digitalWrite(rs485.PIN_RE_DE, HIGH);
    for (int i = 0; i < 9; i++)
    {
      serial_rs485.write(rs485.sender_buffer[i]);
    }
    delay(10);
    digitalWrite(rs485.PIN_RE_DE, LOW);
    rs485.state_transmission = 0;
    rs485.state_transmission_timer_millis = millis();
}

void rs485_read_debug()
{
  //DEBUG SERIAL
  Serial.println("DATA RECEIVED");
  for (int i = 0; i < 9; i++)
  {
    Serial.print(rs485.receiver_buffer[i]);
    Serial.print(", ");
  }
  Serial.println();
  Serial.println();
}

void rs485_write_debug()
{
  //DEBUG SERIAL
  Serial.println("DATA RECEIVED");
  for (int i = 0; i < 9; i++)
  {
    Serial.print(rs485.sender_buffer[i]);
    Serial.print(", ");
  }
  Serial.println();
  Serial.println();
}

void lcd_read_print()
{
  // LCD PRINT
  lcd.setCursor(0, 0);
  lcd.print("ID:");
  lcd.print(MODULE_ID);
  lcd.print(" MOD:RELE");
  lcd.setCursor(0, 1);
  lcd.print(rs485.receiver_buffer[1]);
}

void rs485_command_execute()
{
  digitalWrite(RELAY_PIN, rs485.receiver_buffer[1]);
}

void rs485_manager()
{
  rs485_read();
  if (rs485.receiver_buffer_ready == 1)
  {
    rs485.receiver_buffer_ready = 0;

    rs485_read_debug();

    if (rs485.receiver_buffer[0] == MODULE_ID)
    {
      // EXECUTE COMMAND ASKED BY CORE
      lcd_read_print();
      rs485_command_execute();
      
      // SEND ACK TO CORE
      rs485_write();
    }
  }
}
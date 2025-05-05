
void calendar_order_add_ascending() 
{
  for (int i = 0; i < CALENDAR_TIMERS_NUM; i++) 
  {
    if (calendar_days[day_curr][i] == -1) 
    {
      calendar_days[day_curr][i] = cycle_seconds_tmp;
      int32_t calendar_tmp[CALENDAR_TIMERS_NUM] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 };
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++) 
      {
        Serial.print(calendar_days[day_curr][j]);
        Serial.print(", ");
      }
      Serial.println();
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++) 
      {
        Serial.print(calendar_tmp[j]);
        Serial.print(", ");
      }
      Serial.println();
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++) 
      {
        int32_t max_val = -1;
        int max_index = 0;
        for (int k = 0; k < CALENDAR_TIMERS_NUM; k++) 
        {
          if (max_val < calendar_days[day_curr][k]) 
          {
            max_val = calendar_days[day_curr][k];
            max_index = k;
          }
        }
        calendar_days[day_curr][max_index] = -1;
        calendar_tmp[j] = max_val;
      }
      for (int j = CALENDAR_TIMERS_NUM - 1; j >= 0; j--) 
      {
        Serial.print(calendar_tmp[j]);
        Serial.print(", ");
      }
      Serial.println();
      int valid_num_index = 0;
      for (int j = CALENDAR_TIMERS_NUM - 1; j >= 0; j--) 
      {
        if (calendar_tmp[j] != -1) 
        {
          calendar_days[day_curr][valid_num_index] = calendar_tmp[j];
          valid_num_index += 1;
        }
        // eeprom_address = 100 + (day_curr*100) + bo?
      }
      
      Serial.print("day: ");
      Serial.println(day_curr);
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
      {
        int16_t timer = calendar_days[day_curr][j];
        Serial.print(j);
        Serial.print(" ");
        Serial.println(timer);
      }
      Serial.println();
      // TODO
      for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
      {
        int32_t timer = calendar_days[day_curr][j];
        int eeprom_address_hour = 100 + (day_curr*100) + (j*2);
        int eeprom_address_minute = 100 + (day_curr*100) + (j*2+1);
        if (timer != -1)
        {
          uint8_t hour = timer / 3600;
          uint8_t minute = timer % 3600 / 60;
          Serial.print("hour: ");
          Serial.println(hour);
          Serial.print("minute: ");
          Serial.println(minute);
          EEPROM.write(eeprom_address_hour, hour);
          EEPROM.write(eeprom_address_minute, minute);
          EEPROM.commit();
        }
        else
        {
          EEPROM.write(eeprom_address_hour, 255);
          EEPROM.write(eeprom_address_minute, 255);
          EEPROM.commit();
        }
      }
      break;
    }
  }
}

// TODO
void calendar_delete_and_order_ascending(int delete_index) 
{
  calendar_days[day_curr][delete_index] = -1;
  for (int i = delete_index; i < CALENDAR_TIMERS_NUM - 1; i++) 
  {
    calendar_days[day_curr][i] = calendar_days[day_curr][i + 1];
    uint32_t timer = calendar_days[day_curr][i];
    int eeprom_address_hour = 100 + (day_curr*100) + (i*2);
    int eeprom_address_minute = 100 + (day_curr*100) + (i*2+1);
    if (timer != -1)
    {
      uint8_t hour = timer / 3600;
      uint8_t minute = timer % 3600 / 60;
      EEPROM.write(eeprom_address_hour, hour);
      EEPROM.write(eeprom_address_minute, minute);
      EEPROM.commit();
    }
    else
    {
      EEPROM.write(eeprom_address_hour, 255);
      EEPROM.write(eeprom_address_minute, 255);
      EEPROM.commit();
    }
  }
  calendar_days[day_curr][CALENDAR_TIMERS_NUM - 1] = -1;
  int eeprom_address_hour = 100 + (day_curr*100) + ((CALENDAR_TIMERS_NUM - 1)*2);
  int eeprom_address_minute = 100 + (day_curr*100) + ((CALENDAR_TIMERS_NUM - 1)*2+1);
  EEPROM.write(eeprom_address_hour, 255);
  EEPROM.write(eeprom_address_minute, 255);
  EEPROM.commit();

/*
  for (int j = 0; j < CALENDAR_TIMERS_NUM; j++)
  {
    int16_t timer = calendar_days[0][j];
    int eeprom_address_hour = 100 + (0*100) + (j*2);
    int eeprom_address_minute = 100 + (0*100) + (j*2+1);
    if (timer != -1)
    {
      uint8_t hour = timer / 3600;
      uint8_t minute = timer % 3600 / 60;
      EEPROM.write(eeprom_address_hour, hour);
      EEPROM.write(eeprom_address_minute, minute);
      EEPROM.commit();
    }
    else
    {
      EEPROM.write(eeprom_address_hour, 255);
      EEPROM.write(eeprom_address_minute, 255);
      EEPROM.commit();
    }
  }
  */
}

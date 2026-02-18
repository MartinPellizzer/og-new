// 2026-02-13 09:45 Formato standard internazionale (ISO 8601)

int sd_dir_exists(fs::FS &fs, const char * dirname)
{
  File root = fs.open(dirname);
  if (!root)
  {
    Serial.println("Directory DOESN'T Exists");
    return 0;
  }
  if (!root.isDirectory())
  {
    Serial.println("NOT a Directory");
    return 0;
  }
  Serial.println("Directory Found");
  return 1;
}

void sd_list_dir(fs::FS &fs, const char * dirname, uint8_t levels)
{
  Serial.printf("Listing directory: %s\n", dirname);

  File root = fs.open(dirname);
  if (!root)
  {
    Serial.println("Failed to open directory");
    return;
  }
  if (!root.isDirectory())
  {
    Serial.println("Not a directory");
    return;
  }

  File file = root.openNextFile();
  while (file)
  {
    if (file.isDirectory())
    {
      Serial.print("  DIR : ");
      Serial.println(file.name());
      if(levels)
      {
        sd_list_dir(fs, file.name(), levels -1);
      }
    }
    else 
    {
      Serial.print("  FILE: ");
      Serial.print(file.name());
      Serial.print("  SIZE: ");
      Serial.println(file.size());
    }
    file = root.openNextFile();
  }
}

void sd_create_dir(fs::FS &fs, const char * path)
{
  Serial.printf("Creating Dir: %s\n", path);

  if(fs.mkdir(path))
  {
    Serial.println("Dir created");
  } 
  else 
  {
    Serial.println("mkdir failed");
  }
}

bool sd_read_last_row_and_split(fs::FS &fs, const char *path)
{
  File file = fs.open(path);
  if (!file) {
    Serial.println("Failed to open CSV file");
    return false;
  }

  char lineBuffer[MAX_LINE_LENGTH];
  int idx = 0;

  // Read entire file and keep overwriting lastRow
  while (file.available()) {
    char c = file.read();

    if (c == '\n') {
      lineBuffer[idx] = '\0';
      strncpy(lastRow, lineBuffer, MAX_LINE_LENGTH);
      idx = 0;
    }
    else if (c != '\r' && idx < MAX_LINE_LENGTH - 1) {
      lineBuffer[idx++] = c;
    }
  }

  // Handle file without trailing newline
  if (idx > 0) {
    lineBuffer[idx] = '\0';
    strncpy(lastRow, lineBuffer, MAX_LINE_LENGTH);
  }

  file.close();

  // -------- SPLIT BY COMMAS --------
  fieldCount = 0;

  char *token = strtok(lastRow, ",");
  while (token != NULL && fieldCount < MAX_FIELDS) {
    fields[fieldCount++] = token;
    token = strtok(NULL, ",");
  }

  return true;
}

void sd_card_write_row(const char * filepath) 
{
  // Serial.printf("Appending to file: %s\n", filepath);
  file = SD.open(filepath, FILE_APPEND);
  if (!file)
  {
    // Serial.println("Failed to open file for appending");
  }
  else
  {
    char _buff[LINE_SIZE] = {0};
    int16_t ppb_cur = sensor.ppb_cur;
    if (ppb_cur < 0) ppb_cur = 0;
    snprintf(_buff,
            LINE_SIZE,
            "%04u,%02u,%02u,%02u,%02u,%04u\n",
            rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur,
            ppb_cur
    );
    file.print(_buff);
    file.close();
  }
}

void update_hour_buff(uint16_t year, uint16_t month, uint16_t day, uint16_t hour, uint16_t minute, int32_t avg)
{
    // Shift buffers down (start from bottom!)
    for (int i = LINES - 1; i > 0; i--)
    {
        for (int j = 0; j < LINE_SIZE; j++)
        {
            sd_hour_nextion_lines_buff[i][j] = sd_hour_nextion_lines_buff[i - 1][j];
        }
    }

    // Write new formatted string in position 0
    int hour_prev = hour - 1;
    if (hour_prev < 0) hour_prev = 23;

    snprintf(sd_hour_nextion_lines_buff[0],
             LINE_SIZE,
             "%01u|%04u-%02u-%02u %02u-%02u %04u ",
             0, year, month, day, hour_prev, hour, avg);

    // Extra safety (guarantee termination)
    sd_hour_nextion_lines_buff[0][LINE_SIZE - 1] = '\0';
}

void update_minute_buff(int err)
{
    // Shift buffers down (start from bottom!)
    for (int i = LINES - 1; i > 0; i--)
    {
        for (int j = 0; j < LINE_SIZE; j++)
        {
            sd_minute_nextion_lines_buff[i][j] = sd_minute_nextion_lines_buff[i - 1][j];
        }
    }

    // Write new formatted string in position 0
    int16_t ppb_cur = sensor.ppb_cur;
    if (ppb_cur < 0) ppb_cur = 0;
    snprintf(sd_minute_nextion_lines_buff[0],
            LINE_SIZE,
            "%01u|%04u-%02u-%02u %02u:%02u %04u ",
            err, 
            rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur,
            ppb_cur
    );

    // Extra safety (guarantee termination)
    sd_minute_nextion_lines_buff[0][LINE_SIZE - 1] = '\0';
}

void sd_minute_line_cur_buff_write()
{
    int16_t ppb_cur = sensor.ppb_cur;
    if (ppb_cur < 0) ppb_cur = 0;
    snprintf(sd_minute_line_cur_buff,
            LINE_SIZE,
            "%04u-%02u-%02u %02u:%02u %04u ",
            rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur,
            ppb_cur
    );

    // Extra safety (guarantee termination)
    sd_minute_line_cur_buff[LINE_SIZE - 1] = '\0';
}

void sd_minute_manager()
{
  if (sd_card.buff_minute_old != sd_card.buff_minute_cur)
  {
    sd_card.buff_minute_old = sd_card.buff_minute_cur;

    sd_minute_line_cur_buff_write();
    
    if (sd_card.tried_to_initialize)
    {
      // create "year" folder (if it doesn't exists already)
      {
        char _buff[LINE_SIZE] = {0};
        snprintf(_buff, LINE_SIZE, "/%04u", rtc.year_cur);
        int exists = sd_dir_exists(SD, _buff);
        if (exists == 0)
        {
          sd_create_dir(SD, _buff);
        }
      }
      // create "month" subfolder (if it doesn't exists already)
      {
        char _buff[LINE_SIZE] = {0};
        snprintf(_buff, LINE_SIZE, "/%04u/%02u", rtc.year_cur, rtc.month_cur);
        int exists = sd_dir_exists(SD, _buff);
        if (exists == 0)
        {
          sd_create_dir(SD, _buff);
        }
      }
      // write line in "day" csv file
      {
        char _buff[LINE_SIZE] = {0};
        snprintf(_buff, LINE_SIZE, "/%04u/%02u/%02u.csv", rtc.year_cur, rtc.month_cur, rtc.day_cur);
        sd_card_write_row(_buff);
      }
      // read last line in "day" csv file
      {
        char _buff[LINE_SIZE] = {0};
        snprintf(_buff, LINE_SIZE, "/%04u/%02u/%02u.csv", rtc.year_cur, rtc.month_cur, rtc.day_cur);
        if (sd_read_last_row_and_split(SD, _buff)) 
        {
          // Serial.println("Last row split values:");

          // for (int i = 0; i < fieldCount; i++) 
          // {
          //   Serial.print("Field ");
          //   Serial.print(i);
          //   Serial.print(": ");
          //   Serial.println(fields[i]);
          // }

          {
            char _buff[LINE_SIZE] = {0};
            snprintf(_buff,
                  LINE_SIZE,
                  "%04u-%02u-%02u %02u:%02u %04u ",
                  atoi(fields[0]),
                  atoi(fields[1]),
                  atoi(fields[2]),
                  atoi(fields[3]),
                  atoi(fields[4]),
                  atoi(fields[5])
            );
            // Serial.println("OLD BUFFER:");
            // Serial.println(sd_minute_line_cur_buff);
            // Serial.println("NEW BUFFER:");
            // Serial.println(_buff);

            if (strcmp(_buff, sd_minute_line_cur_buff) == 0) 
            {
                // Serial.println("Buffers are identical");
                update_minute_buff(0);
                sd_card.last_state_cur = 0;
            } 
            else 
            {
              // Serial.println("Buffers are different");
              // err: write/read values don't match?
              update_minute_buff(3);
              sd_card.last_state_cur = 3;
            }
          }
        }
        else
        {
          // err: can't read file? (maybe file doesn't exists?)
          update_minute_buff(2);
          sd_card.last_state_cur = 2;
        }
      }
    }
    else
    {
      // err: sd not inserted?
      update_minute_buff(1);
      sd_card.last_state_cur = 1;
    }

    // for (int i = 0; i < LINES; i++)
    // {
    //   Serial.println(sd_minute_nextion_lines_buff[i]);
    // }
    // Serial.println();

    sd_card.nextion_update = 1;
  }
}

void sd_hour_manager() 
{
  
  if (sd_card.buff_hour_minute_old != sd_card.buff_hour_minute_cur)
  {
    sd_card.buff_hour_minute_old = sd_card.buff_hour_minute_cur;

    // add sensor reading to hour buff
    int16_t ppb_cur = sensor.ppb_cur;
    if (ppb_cur < 0) ppb_cur = 0;
    sd_hour_buff[sd_hour_buff_i] = ppb_cur;
    sd_hour_buff_i += 1;
  }

  if (sd_card.buff_hour_hour_old != sd_card.buff_hour_hour_cur)
  {
    sd_card.buff_hour_hour_old = sd_card.buff_hour_hour_cur;
    
    int32_t sum = 0;

    for (int i = 0; i < 60; i++)
    {
      // Serial.print(sd_hour_buff[i]);
      // Serial.print(", ");
      sum += (int32_t)sd_hour_buff[i];
    }
    // Serial.println();

    int32_t avg = (int32_t)(sum / 60);
    // Serial.println(avg);
    
    sd_hour_buff_i = 0;

    update_hour_buff(rtc.year_cur, rtc.month_cur, rtc.day_cur, rtc.hour_cur, rtc.minute_cur, avg);

    // for (int i = 0; i < LINES; i++)
    // {
    //     Serial.println(sd_hour_nextion_lines_buff[i]);
    // }
    // Serial.println();

    sd_card.nextion_update = 1;
  }
}

void sd_card_init() 
{
  sd_card.inserted_cur = (digitalRead(sd_card.pin_cd) == LOW) ? 1 : 0;

  if (sd_card.inserted_cur)
  {
    if (!sd_card.tried_to_initialize)
    {
      sd_card.tried_to_initialize = 1;
      if (!SD.begin()) 
      {
        // Serial.println("Card Mount Failed");
        sd_card.last_state_cur = 1;
      }
      else 
      {
        // Serial.println("Card Mounted");
        sd_card.last_state_cur = 0;
      }
    }
  }
  else
  {
    if (sd_card.tried_to_initialize)
    {
      SD.end();
      sd_card.tried_to_initialize = 0;
      // Serial.println("Card Unmounted");
    }
    sd_card.last_state_cur = 1;
  }
}

void sd_manager() 
{
  sd_card_init();
  
  sd_minute_manager();
  sd_hour_manager();
}
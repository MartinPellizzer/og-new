void valve_1_open()
{
    digitalWrite(RO_7, 1);
}

void valve_1_close()
{
    digitalWrite(RO_7, 0);
}

void valve_2_open()
{
    digitalWrite(RO_8, 1);
}

void valve_2_close()
{
    digitalWrite(RO_8, 0);
}

void valves_manager()
{
  if (power.power_cur == 0)
  {
    valve_1_close();
    valve_2_open();
  }
  else if (power.power_cur == 1)
  {
    valve_1_open();
    valve_2_close();
  }
  else if (power.power_cur == 2)
  {
    valve_1_close();
    valve_2_open();
  }
}
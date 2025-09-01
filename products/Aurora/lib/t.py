from lib import g
from lib import layout

def template_gen(template):
    template = template.replace('[product_name]', g.PRODUCT_NAME)
    template = template.replace('[application_main]', g.APPLICATION_MAIN)
    template = template.replace('[environment_list]', layout.list_unordered(g.ENVIRONMENT_LIST))
    template = template.replace('[application_list]', layout.list_unordered(g.APPLICATION_LIST))
    template = template.replace('[interface_type]', g.INTERFACE_TYPE)
    template = template.replace('[ozone_output_min]', g.OZONE_OUTPUT_MIN)
    template = template.replace('[ozone_output_max]', g.OZONE_OUTPUT_MAX)
    template = template.replace('[input_voltage_value]', g.INPUT_VOLTAGE_VALUE)
    template = template.replace('[input_voltage_unit]', g.INPUT_VOLTAGE_UNIT)
    template = template.replace('[input_voltage_type]', g.INPUT_VOLTAGE_TYPE)
    template = template.replace('[input_power_max_value]', g.INPUT_POWER_MAX_VALUE)
    template = template.replace('[input_power_max_unit]', g.INPUT_POWER_MAX_UNIT)
    template = template.replace('[operating_temperature_min]', g.OPERATING_TEMPERATURE_MIN)
    template = template.replace('[operating_temperature_max]', g.OPERATING_TEMPERATURE_MAX)
    template = template.replace('[operating_temperature_unit]', g.OPERATING_TEMPERATURE_UNIT)
    template = template.replace('[operating_humidity_min]', g.OPERATING_HUMIDITY_MIN)
    template = template.replace('[operating_humidity_max]', g.OPERATING_HUMIDITY_MAX)
    template = template.replace('[operating_humidity_unit]', g.OPERATING_HUMIDITY_UNIT)
    template = template.replace('[operating_time_min]', g.OPERATING_TIME_MIN)
    template = template.replace('[operating_time_max]', g.OPERATING_TIME_MAX)
    template = template.replace('[operating_time_unit]', g.OPERATING_TIME_UNIT)
    return template

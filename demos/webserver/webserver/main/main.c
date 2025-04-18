#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>

#include "freertos/FreeRTOS.h"

#include "rgb_led.h"

void app_main(void)
{
    while (true) 
    {
        printf("LED 1\n");
        rgb_led_wifi_app_started();
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        printf("LED 2\n");
        rgb_led_http_server_started();
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        printf("LED 3\n");
        rgb_led_wifi_connected();
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

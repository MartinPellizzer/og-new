# See the build system documentation in IDF programming guide
# for more information about component CMakeLists.txt files.

idf_component_register(
    SRCS main.c rgb_led.c wifi_app.c
    INCLUDE_DIRS "."
)

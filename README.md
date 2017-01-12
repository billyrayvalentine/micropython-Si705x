README.md
# micropython-Si705x
A MicroPython library for the I2C [Silicon Labs Si705x](http://www.silabs.com/products/sensors/temperature-sensors/Pages/temperature-sensors.aspx) series of temperature sensors.  
This library should work with the Si7050 Si7051 Si7053 Si7054 Si7055

**This module has currently only been tested on the Si7055 please report your milage**

# Methods
There are only three methods:
```get_temperature``` - Perform a measurement and return the temperature in Celcius
```get_model``` - Return the hardware model e.g. Si7055
```get_firmware_version``` - Return the hex value of the firmware version

# Example in REPL
```python
>>> from machine import Pin, I2C
>>> from Si705x import Si705x
>>> i2c = I2C(scl=Pin(5), sda=Pin(4))
>>> sensor = Si705x(i2c)
>>> sensor.get_temperature()
23.82838
>>> sensor.get_model()
'Si7055'
>>> sensor.get_firmware_version()
'0x20'
```

# License
MIT


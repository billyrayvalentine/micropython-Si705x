# Si705x.py
# Copyright (c) 2017 Ben Sampson https://github.com/billyrayvalentine
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
Micropython class to get data from the Silcon Labs Si705x digital
Temperature Sensor

Example usage:

    from machine import Pin, I2C
    from Si705x import Si705x
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    sensor = Si705x(i2c)
    sensor.get_temperature()

"""
import time


class Si705x:
    """Si705x class for Si705x Temperature Sensors

    Args:
        i2c: A configured machine.I2C instance
        address: Si705x address.  Defaults to 0x40

    """

    def __init__(self, i2c, address=0x40):
        self._i2c = i2c
        self.address = address

        self._temp_code = bytearray(2)

    def get_temperature(self, delay=10):
        """Return temperature in Celcius

        Args:
            delay: Time in ms to wait for sensor to take a measurement
        """

        buf = bytearray(2)

        self._i2c.writeto(self.address, b'\xF3')
        time.sleep_ms(delay)
        self._i2c.readfrom_into(self.address, buf)

        # Keep temp in object for potential debug
        self._temp_code = buf[0] << 8 | buf[1]

        return self._temp_code * 175.72 / 65536 - 46.85

    def get_firmware_version(self):
        """Return the hex value of the firmware version"""

        self._i2c.writeto(self.address, b'\x84\xB8')
        return hex(self._i2c.readfrom(0x40, 1)[0])

    def get_model(self):
        """Return a string identifying the hardware model e.g. Si7055"""

        self._i2c.writeto(self.address, b'\xFC\xC9')
        model = int(self._i2c.readfrom(0x40, 1)[0])
        return "Si70" + str(model)

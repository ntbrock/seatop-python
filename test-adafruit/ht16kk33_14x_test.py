# Basic example of setting digits on a LED segment display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

import time

# Import all board pins.
import board
import busio

# Import the HT16K33 LED segment module.
from adafruit_ht16k33 import segments

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

## 14 segment display
display = segments.Seg14x4(i2c, address=0x71)


# Clear the display.
display.fill(0)

# Can just print a number
display.print('SSE ')
display.brightness = 0.2

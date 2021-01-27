#!/usr/bin/env python3
# Import all pins
import time
import board
import busio
from adafruit_ht16k33 import matrix

# Create the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED bargraph class.
bicolor = matrix.Matrix8x8x2(i2c, address=0x77)

# color mapping shortcut
OFF = 0
GREEN = 1
RED = 2
YELLOW = 3

# Edges of an 8x8 matrix
col_max = 8
row_max = 8

# Turn all pixels off
bicolor.fill(OFF)
col = 0
row = 0

# Fill the entrire bicolor, with each color
bicolor.fill(GREEN)
time.sleep(0.1)
bicolor.brightness = 0.9

time.sleep(0.1)
bicolor.brightness = 0.8

time.sleep(0.1)
bicolor.brightness = 0.7

time.sleep(0.1)
bicolor.brightness = 0.6

time.sleep(0.1)
bicolor.brightness = 0.5

time.sleep(0.1)
bicolor.brightness = 0.4

time.sleep(0.1)
bicolor.brightness = 0.3

time.sleep(0.1)
bicolor.brightness = 0.2

time.sleep(0.1)
bicolor.brightness = 0.1

time.sleep(0.1)
bicolor.brightness = 0.0

bicolor.fill(OFF)


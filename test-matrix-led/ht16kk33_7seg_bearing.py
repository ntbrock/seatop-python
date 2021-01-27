#!/usr/bin/env python
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

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)
# Or this creates a 14 segment alphanumeric 4 character display:
# Clear the display.
display.fill(0)
display.brightness = 0.1

increment = 0

while True:

  increment = ( increment + 1 ) % 60

  print(f"increment: {increment:03d}")

  # Bearing 
  display.print(f"00:{increment:03d}")

  time.sleep(1.0)


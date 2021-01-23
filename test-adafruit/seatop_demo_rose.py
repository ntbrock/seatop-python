#!/usr/bin/env python
#
# seaptop compass rose
#
# WHAT is up cats!?  This is my first re-interpretation of the adafruit demos.
# Sitting in the master suite at vagabond, my trusty pi t-cobbler and breadboard by my side
# snoozin dogs, stressful job, Terry Gross brain NPR on beside me
# Remembering the coolest 486 graphics demos shipped via BBS / shareware
#

import time
import board
import busio
from adafruit_ht16k33 import segments
from adafruit_ht16k33 import matrix

# Color constants
OFF = 0
RED = 1
GREEN = 2
YELLOW = 3

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# 7 segment display
seg7 = segments.Seg7x4(i2c, address=0x70)

# 14 segment display
seg14 = segments.Seg14x4(i2c, address=0x71)

# Bicolor
bicolor = matrix.Matrix8x8x2(i2c, address=0x77)                             
row_max=8
col_max=8

# Clear the displays
seg7.fill(0)
seg14.fill(0)
bicolor.fill(0)

# Can just print a number
seg14.print('NNE ')
seg14.brightness = 0.2

# set the Green center
bicolor[3,3] = GREEN
bicolor[4,3] = GREEN
bicolor[4,4] = GREEN
bicolor[3,4] = GREEN

bicolor.brightness = 0.2

# degree loop





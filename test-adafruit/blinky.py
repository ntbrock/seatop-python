#!/bin/env python3

import time
import board
from digitalio import DigitalInOut, Direction


blink_freq = 2
blink_count = 0

# setup Pi pins as output for LEDs
green_led = DigitalInOut(board.D18)
red_led = DigitalInOut(board.D23)
green_led.direction = Direction.OUTPUT
red_led.direction = Direction.OUTPUT

def blink():
    global blink_count

    green_led.value = True
    red_led.value = False
    time.sleep(blink_freq)

    green_led.value = False
    red_led.value = True
    time.sleep(blink_freq)

    print("blink")
    print(blink_count)
    blink_count = blink_count + 1 
 
while True:
    blink()


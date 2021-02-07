#!/usr/bin/env python
# https://learn.adafruit.com/circuitpython-digital-inputs-and-outputs/digital-outputs

import board
import pulseio
import time

import digitalio

led = digitalio.DigitalInOut(board.D18)
led.direction = digitalio.Direction.OUTPUT

switch = digitalio.DigitalInOut(board.D23)
switch.direction = digitalio.Direction.INPUT

# led only test
"""
while True:
	time.sleep(0.5)
	led.value = True
	time.sleep(0.5)
	led.value = False
"""

# offsides
while True:
	s = switch.value
	led.value = not s
	time.sleep(0.5)
	print(f"switch: {switch.value}")


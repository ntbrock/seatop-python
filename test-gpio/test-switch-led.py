#!/usr/bin/env python
# https://learn.adafruit.com/circuitpython-digital-inputs-and-outputs/digital-outputs

import board
import pulseio
import time

import digitalio

led = digitalio.DigitalInOut(board.D21)
led.direction = digitalio.Direction.OUTPUT

switch = digitalio.DigitalInOut(board.D20)
switch.direction = digitalio.Direction.INPUT

led.value = True
time.sleep(0.5)
led.value = False

while True:
	s = switch.value
	led.value = not s
	time.sleep(0.5)
	print(f"switch: {switch.value}")





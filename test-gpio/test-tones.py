#!/usr/bin/env python
# https://learn.adafruit.com/using-piezo-buzzers-with-circuitpython-arduino/circuitpython

import board
import pulseio
import time

buzzer = pulseio.PWMOut(board.D24, variable_frequency=True)
buzzer.frequency = 440

OFF = 0
ON = 2**15

buzzer.duty_cycle = ON
time.sleep(0.3)

buzzer.duty_cycle = OFF



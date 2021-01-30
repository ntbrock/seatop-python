#!/usr/bin/env python
# Measure distances using gps

import board
import time

import adafruit_gps
import serial

import busio
from adafruit_ht16k33 import segments
from adafruit_ht16k33 import matrix

import digitalio
import pulseio

from turfpy import measurement
from geojson import Point, Feature


#---------------------------------------------------------------
# Hardware Constants

## gps
uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial
# Turn on the basic GGA and RMC info (what you typically want)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
# Set update rate to once a second (1hz) which is what you typically want.
gps.send_command(b"PMTK220,1000")

## i2c
i2c = busio.I2C(board.SCL, board.SDA)

## 14 segment display
alphaLed = segments.Seg14x4(i2c, address=0x71)
alphaLed.brightness = 0.1
alphaLed.fill(0)

## 7 segment display
numberLed = segments.Seg7x4(i2c, address=0x70)
numberLed.brightness = 0.1
numberLed.fill(0)

## 8x8 matrix display
matrixLed = matrix.Matrix8x8x2(i2c, address=0x77)
matrixLed.fill(0)

## color mapping shortcut
MATRIX_OFF = 0
MATRIX_GREEN = 1
MATRIX_RED = 2
MATRIX_YELLOW = 3


## User Input
markLed = digitalio.DigitalInOut(board.D21)
markLed.direction = digitalio.Direction.OUTPUT

markSwitch = digitalio.DigitalInOut(board.D20)
markSwitch.direction = digitalio.Direction.INPUT

## User Sounds
buzzer = pulseio.PWMOut(board.D16 ) # rpi no support , variable_frequency=True)
buzzer.frequency = 440 
BUZZER_OFF = 0
BUZZER_ON = 2**15


#---------------------------------------------------------------
# Start Up 

version = "0.0.2"
print("app-star-ruler 0.0.2")

numberLed.print(f" {version}")


"""
- Meta Start:
	waiting for fix..  markLed = off
	numberLed: coutning up seconds.ms since start
	alphaLed says: "Fix"
	Fix acquired
"""





## Variables:
## 	markLocation = [ lat, long ]



"""
State machine:
	Gps fix yes/no
		If no gps fix, led is dark
		if yes gps fix, led is pulsing 

	Button pressed yes/no
		LED is on
		If button is pressed, showing distance / bearing to where you pressed the button
		If button is not pressed, showing time of day

	If distance > 10 feet  beep 1/second
	> 20 feet beep  2/second
	> 30 feet  3/second
"""

"""
- Meta Start:
	waiting for fix..  markLed = off
	numberLed: coutning up seconds.ms since start
	alphaLed says: "Fix"
	Fix acquired
"""

"""
- Meta Loop:
	If markswitch False
		Show time of day
		Pulse Led

	Event: When Markswitch Pressed,
		set markLocation = gps location

	Calculate: 
		disstance between markLocation + gps location

	If markSwitch True
		numberLed = Distance F
		alphaLed = Bearing M/T

	if ( distance > 10 ft )
		Pulse buzzer  distance * 0.1 Hz 

	Event: When markswitch is released,
		Go back to time of day mode.


+ Bonus = data logging

+ Bonus = tide chart on 8x8
"""




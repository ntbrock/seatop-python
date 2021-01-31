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
alphaLed.brightness = 0.8
alphaLed.fill(0)

## 7 segment display
numberLed = segments.Seg7x4(i2c, address=0x70)
numberLed.brightness = 0.8
numberLed.fill(0)

## 8x8 matrix display
# 2021jan30 dock deom - matrix turned off
#matrixLed = matrix.Matrix8x8x2(i2c, address=0x77)
#matrixLed.fill(0)

## color mapping shortcut
MATRIX_OFF = 0
MATRIX_GREEN = 1
MATRIX_RED = 2
MATRIX_YELLOW = 3


## User Input
markLed = digitalio.DigitalInOut(board.D18)
markLed.direction = digitalio.Direction.OUTPUT
markLed.value = False

markSwitch = digitalio.DigitalInOut(board.D23)

markSwitch.direction = digitalio.Direction.INPUT

## User Sounds
buzzer = pulseio.PWMOut(board.D24) # rpi no support , variable_frequency=True)
buzzer.frequency = 440 
BUZZER_OFF = 0
BUZZER_ON = 2**15


#---------------------------------------------------------------
# Start Up 

version = "0.0.3"
print("app-star-ruler 0.0.2")

numberLed.print(f" {version}")
alphaLed.print("WFIX")

timeStart = timeLast = timeNow = time.monotonic()

"""
Meta Start:
	waiting for fix..  markLed = off
	numberLed: coutning up seconds.ms since start
	alphaLed says: "Fix"
	Fix acquired
"""

gps.update()
while not gps.has_fix:
	timeNow = time.monotonic()
	time.sleep(0.5)
	gps.update()
	# Every second print out current location details if there's a fix.
	if timeNow - timeLast >= 1.0:
		timeLast = timeNow
		timeDiff = int(timeNow - timeStart)
		numberLed.print(f"{timeDiff:04d}")
		print(f"waiting on fix {timeDiff:04d}")


#---------------------------------------------------------------
# Loop

markPrevious = False
markLat = 0
markLon = 0
loopCount = 0

while True: 
	loopCount = loopCount + 1
	# Gps management
	gps.update()

#	If markswitch False, logic is no longer inverted on Gpio D23
	if not markSwitch.value:
		markPrevious = False

	
#	Show time of day
		hour = gps.timestamp_utc.tm_hour
		min = gps.timestamp_utc.tm_min
		sec = gps.timestamp_utc.tm_sec
		numberLed.print(f"{hour:02d}:{min:02d}")
		alphaLed.print(f"{sec:02d}Z*")

#	Pulse Led
		if loopCount % 4 == 0 :
			markLed.value = True
			time.sleep(0.25)
			markLed.value = False
			time.sleep(0.25)
		else:
			time.sleep(0.5)


	else: 
		markLed.value = True
		time.sleep(0.5)

#	Event: When Markswitch Pressed,
#		set markLocation = gps location

		markEvent = False
		if not markPrevious:
			markEvent = True
			# tiny buzz on activation
			buzzer.duty_cycle = BUZZER_ON
			time.sleep(0.2)
			buzzer.duty_cycle = BUZZER_OFF


		markPrevious = True
		roundCoordinates = 6

		if markEvent:
			markLat = round(gps.latitude,roundCoordinates)
			markLon = round(gps.longitude,roundCoordinates)

#	Where inthe world am I?
		nowLat = round(gps.latitude,roundCoordinates)
		nowLong = round(gps.longitude,roundCoordinates)

#	Calculate: 
#		distance between markLocation + gps location
#		distance returned in km

		markFeature = Feature(geometry=Point((markLat, markLon)))
		nowFeature = Feature(geometry=Point((nowLat, nowLong)))
		
#		numberLed = Distance F
		distance = round(measurement.distance(markFeature, nowFeature),roundCoordinates)
		feet = int(distance * 3280.84)
		print(f"distance raw: {distance}km  feet: {feet}  mark: {markLat} {markLon}  now: {nowLat} {nowLong}  ")
		numberLed.print(f"{int(feet): 3d}F")

#		alphaLed = Bearing M/T
		offset = -90
		bearing = measurement.bearing(markFeature,nowFeature)
		if bearing < 0:
			bearing = 360 + bearing + offset
		alphaLed.print(f"{int(bearing):03d}T")

#	If markSwitch True

#	if ( distance > 10 ft )
#		Pulse buzzer  distance * 0.1 Hz 

#	Event: When markswitch is released,
#		Go back to time of day mode.



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
+ Bonus = data logging

+ Bonus = tide chart on 8x8
"""




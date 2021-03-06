#!/usr/bin/env python
#
# Satellite backed nightstand clock
# Inspiration: https://en.wikipedia.org/wiki/Sputnik_1
# wishlist, based on position , do a tide/moon indicator on the 14 segment matrix

import time
import board
import busio
import serial
import adafruit_gps
from adafruit_ht16k33 import segments

# USB Gps  Check your baud rates, if invalid, lib says "no fix"
uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)

# Turn on the basic GGA and RMC info (what you typically want)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
# Set update rate to once a second (1hz) which is what you typically want.
gps.send_command(b"PMTK220,1000")

# I2C for LED matrix displays
i2c = busio.I2C(board.SCL, board.SDA)
sevenDisplay = segments.Seg7x4(i2c, address=0x70)
# init the 7 segment numerical display for time
sevenDisplay.fill(0)
sevenDisplay.brightness = 0.1

# init the 14 segement alpha display
alphaDisplay = segments.Seg14x4(i2c, address=0x71)
alphaDisplay.fill(0)
alphaDisplay.brightness = 0.1


# Main loop runs forever printing the location, etc. every second.
last_print = time.monotonic()
while True:
	# Make sure to call gps.update() every loop iteration and at least twice
	# as fast as data comes from the GPS unit (usually every second).
	# This returns a bool that's true if it parsed new data (you can ignore it
	# though if you don't care and instead look at the has_fix property).
	gps.update()
	# Every second print out current location details if there's a fix.
	current = time.monotonic()
	if current - last_print >= 1.0:
		last_print = current
	if not gps.has_fix:
		# Try again if we don't have a fix yet.
		print("Waiting for fix...")
		continue
	# We have a fix! (gps.has_fix is true)
	# Print out details about the fix like location, date, etc.
	print("=" * 40)  # Print a separator line.
	print(
		"Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
		gps.timestamp_utc.tm_mon,  # Grab parts of the time from the
		gps.timestamp_utc.tm_mday,  # struct_time object that holds
		gps.timestamp_utc.tm_year,  # the fix time.  Note you might
		gps.timestamp_utc.tm_hour,  # not get all data like year, day,
		gps.timestamp_utc.tm_min,  # month!
		gps.timestamp_utc.tm_sec,
		)
	)
	print("Latitude: {0:.6f} degrees".format(gps.latitude))
	print("Longitude: {0:.6f} degrees".format(gps.longitude))
	print("Fix quality: {}".format(gps.fix_quality))
	# Some attributes beyond latitude, longitude and timestamp are optional
	# and might not be present.  Check if they're None before trying to use!
	if gps.satellites is not None:
		print("# satellites: {}".format(gps.satellites))
	if gps.altitude_m is not None:
		print("Altitude: {} meters".format(gps.altitude_m))
	if gps.speed_knots is not None:
		print("Speed: {} knots".format(gps.speed_knots))
	if gps.track_angle_deg is not None:
		print("Track angle: {} degrees".format(gps.track_angle_deg))
	if gps.horizontal_dilution is not None:
		print("Horizontal dilution: {}".format(gps.horizontal_dilution))
	if gps.height_geoid is not None:
		print("Height geo ID: {} meters".format(gps.height_geoid))

	# do the work
	hour = gps.timestamp_utc.tm_hour
	min = gps.timestamp_utc.tm_min       
	sec = gps.timestamp_utc.tm_sec

	sevenDisplay.print(f"{hour:02d}:{min:02d}")

	alphaDisplay.print(f"{sec:02d}Z*")

	time.sleep(0.5)


# eof		

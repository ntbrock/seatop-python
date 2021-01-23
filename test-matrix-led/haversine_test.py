## Geography Library Trials
# I think I may call this project "Seatop Sentinel" but may change my mind later :)
# 2021Jan04 Taylor Brockman - MIT License, Open Source
#
# tl;dr  I tried four python geo-position libraries and I like two of them: haversine && turfpy
#
# This rant is within the design phase of a new standalone marine electronic device for
# mariners that helps monitor their vessel's position at anchor and get alerted as soon as
# anything BAD is happening!
#
# Here's why I'm doing this =>
# Typical anchor alarms built into multifunction displays (MFD) are, in my personal experience:
#   1. hard to hear
#   2. driven by low power piezoelectric buzzers
#   3. often located in far away places (cockpit, where it's wet and cold)
#   4. drawing down house batteries all night
#
# "Seatop Sentinel" is a marine electronic device that will reliably notify and alarm
# you and your crew when your vessel's position changes uncomfortably.
#
# (One way to uncomfortably: "your boat is trending to move outside a set radius distance")
# (Another way: "we are all going to die!")
#
# Anchor with confidence, watch your position from the comfort of your cozy bunk.
# When something is wrong, make sure you get woken up so you can take care of it.
#
# Anchor with confidence, watch your position from the comfort of your cozy bunk.
#
# <aside>
# I have a special story about "reading at anchor" one morning on a 40 degree angle
# list because our J120 drug anchor after the tide reversed in a marsh creek.  I was
# engrossed into Wiseman + Hicks "Death Gate Cycle: Book 1: Dragon Wing", sipping coffee,
# totally fine as the tide fell and than begin to rise.  I appreciate that D/V "Dragon Wing"
# (D/V = Dragon Vessel) is approximately the size of S/V Illyria and just as complex to
# operate, I am sure!
# </>
#
# **Seatop Sentinel** empowers the skipper to:
# - Safely deploy and quickly retrieve your anchoring ground tackle
# - Monitor the length of rode deployed while anchoring
# - Ensure your anchor set is stable
#   (HOWTO: just monitor distance while backing down in reverse, if no SOG then you're set!)
# - Quickly dial in the radius to the alarm distance to suit your conditions
#   (Remember when our electronic gadgets had real knobs?  This one does! Enjoy!)
# - Mark the exact location where you drop anchor <-- This is important!!
#
#
#
# You can customize everything, starting with choosing your favorite 'Alarm Tone'
# from our provided catalog.  Advanced users can go all the way to shelling into
# the Raspberry pi to run sudo.  You could enable support for Navionics on tablets
# and smartphones so you can even see your position on the chart!
# Go to sleep nerd, it will be fine.
#


#
# position logger designed for use by mariners
# at anchor to ensure the ship's position is known to be within bounds.


# --------------------------------------------------------------
# Popular Destinations

## location = (lat, lon)
lyon = (45.7597, 4.8422)  # France
paris = (48.8567, 2.3508) # France
charleston = (32.7765, -079.931) # South Carolina
shelby = (35.2924, -081.5356) # North Carolina
charlotte = (35.2271, -080.8431) # NC
bermuda = ( 32.3078, -064.7505) # Atlantic Ocean
sumter = ( 32.7523, -079.8747 ) # Charleston Harbor
bohicket = ( 32.6058, -080.1560 ) # Daysail South

startPoint = sumter
stopPoint = bohicket


# --------------------------------------------------------------
# Library 1 haversine
from haversine import haversine, Unit


havdist = haversine(startPoint, stopPoint, unit = Unit.NAUTICAL_MILES)
print(f"Haversine distance in nm: {havdist}")
# >> 392.2172595594006  # in kilometers

#haversine(lyon, paris, unit=Unit.MILES)
#>> 243.71201856934454  # in miles

# you can also use the string abbreviation for units:
#haversine(lyon, paris, unit='mi')
#>> 243.71201856934454  # in miles

#haversine(lyon, paris, unit=Unit.NAUTICAL_MILES)
#>> 211.78037755311516  # in nautical miles

# --------------------------------------------------------------
# Library 2 pyproj
#import pyproj
#import math

#geodesic = pyproj.Geod(ellps='WGS84')
#fwd_azimuth,back_azimuth,distance = geodesic.inv(startPoint[0], startPoint[1], stopPoint[0], stopPoint[1])
#print(f"Pyproj distance: {distance}")
#print(f"Pyproj fwd_azimuth: {fwd_azimuth}")
# print(f"Pyproj fwd_azimuth red: {math.radians(fwd_azimuth)}")
#print(f"Pyproj fwd_azimuth deg: {math.degrees(fwd_azimuth)}")

# --------------------------------------------------------------
# Library 3
#from geographiclib.geodesic import Geodesic
#def get_bearing(lat1, lat2, long1, long2):
#    brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
#    return brng

#b = get_bearing(startPoint[0], startPoint[1], stopPoint[0], stopPoint[1])
#print(f"Geographic Lib: {b}")


# --------------------------------------------------------------
# Library 4 Turfpy

from turfpy import measurement
from geojson import Point, Feature
start = Feature(geometry=Point((startPoint[1], startPoint[0])))
end = Feature(geometry=Point((stopPoint[1], stopPoint[0])))
bearing = measurement.bearing(start,end)
if bearing < 0:
    bearing = 360 + bearing

print(f"Turfpy bearing: {bearing}")


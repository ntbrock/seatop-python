# Worklog 2021Jan28

lets build the starclock!

adafruit_gps.mpy


https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries

https://github.com/adafruit/Adafruit_CircuitPython_GPS/releases

https://circuitpython.readthedocs.io/projects/gps/en/latest/

## This works:
pip3 install adafruit-circuitpython-gps


## First gps clock 

https://circuitpython.readthedocs.io/projects/gps/en/latest/


## NEMA

RMC is Recommended Minimum Navigation Information.

Here’s an explanation of RMC:

                                                           12
       1         2 3       4 5        6 7   8   9   10   11|
       |         | |       | |        | |   |   |    |   | |
$--RMC,hhmmss.ss,A,llll.ll,a,yyyyy.yy,a,x.x,x.x,xxxx,x.x,a*hh

    Time (UTC)
    Status, V = Navigation receiver warning
    Latitude
    N or S
    Longitude
    E or W
    Speed over ground, knots
    Track made good, degrees true
    Date, ddmmyy
    Magnetic Variation, degrees
    E or W
    Checksum


## Timezones

https://pypi.org/project/timezonefinder/

sudo apt install llvm-9
LLVM_CONFIG=llvm-config-9 pip install llvmlite

LLVM_CONFIG=llvm-config-9 pip install timezonefinder[numba]




## Lunar phaases

https://pypi.org/project/pylunar/
https://pylunar.readthedocs.io/en/latest/usage.html



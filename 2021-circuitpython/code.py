# 2021Feb07 Dog Food Timer

from adafruit_circuitplayground import cp
import time

# 10 hours = 10 LEDs
countdown_seconds = 60*60*10 # 10 hour production
#countdown_seconds = 60 # 1 minute test


Rdefault = 0
Gdefault = 0
Bdefault = 0

# Countdown illumination
Ron = 10
Gon = 10
Bon = 200

R = Rdefault
G = Gdefault
B = Bdefault

cp.pixels.brightness = 0.03

pressed_count = 0
pressed_prior = False
pressed = False
pressed_time = time.monotonic()

up_threshold = 6

while True:

    # adafruit acceleration sample
    x, y, z = cp.acceleration
    #print((x, y, z))

    up = ( abs(x) + abs(y) )

    # ether button pressed?
    if up > up_threshold:
        pressed = True
    else:
        pressed = False


    # Detect state change
    if not pressed_prior and pressed:
        pressed_count += 1
        pressed_time = time.monotonic()
    # reset state to latest value
    pressed_prior = pressed

    elapsed = time.monotonic() - pressed_time

    pixel_count = pressed_count % 10
#    pixel_count = int(elapsed*5.0 % 10) + 1
    if not pressed:
        pixel_count = 0

    # time math
    leds_illuminated = ( ( countdown_seconds - elapsed ) / countdown_seconds ) * 10

    print(f"elapsed: {elapsed} leds: {leds_illuminated}")

    for led in range(0, 10):
        if ( leds_illuminated > led ):
            cp.pixels[led] = (Ron,Gon,Bon)
        else:
            cp.pixels[led] = (Rdefault, Gdefault, Bdefault)


    time.sleep(0.5)

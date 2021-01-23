# 2021Jan23 Brockman Neopixel Demo

from adafruit_circuitplayground import cp
import time

Rdefault = 0
Gdefault = 0
Bdefault = 0

R = Rdefault
G = Gdefault
B = Bdefault
    
cp.pixels.brightness = 0.03

pressed_count = 0
pressed_prior = False
pressed = False
pressed_time = 0

while True:
    
    # ether button pressed?
    if cp.button_a or cp.button_b:
        pressed = True
    else:
        pressed = False
    
    # which button pressed, for colorization
    if cp.button_a:
        R = 255
    else: 
        R = Rdefault
        
    if cp.button_b:
        G = 255
    else:
        G = Gdefault
        
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
    
    print(f"pressed_count: {pressed_count} pixel_count = {pixel_count}")
    
    if pressed:
        cp.pixels[pixel_count-1] = (R,G,B)
    else:
        # cp.pixels.fill((R, G, B))
        False
        
        
    time.sleep(0.05)



Worklog 2021Jan30

## Gpio 

Got a simple buzzer and switch/led test working


## star-ruler

Let's build my first public demonstration that I could show during maintenance day tomorrow morning at the dock!


* Add a coin cell to the gps modle for faster fixes


Star ruler will run on the rpi4 dev breadboard.

- Start on boot
- State machine:
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

- Constants:
	gps
	numberLed
	alphaLed
	markLed
	markSwitch
	buzzer

- Variables:
	markLocation = [ lat, long ]


- Meta Start:
	waiting for fix..  markLed = off
	numberLed: coutning up seconds.ms since start
	alphaLed says: "Fix"
	Fix acquired

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



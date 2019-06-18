#! /usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()

# this script will clear any LEDS left in the 'on' state that a 
# different script may have left on

print ('Clearing LEDs')

sense.clear()

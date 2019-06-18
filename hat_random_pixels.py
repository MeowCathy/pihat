#! /usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()
import time
import random



#input # times to run
n = int(input('Enter a number:\t'))

#loop
for i in range(n):
    #assign a random integer between 0 and 255 to a variable named cr,cg,cb
    #colour
    cr = random.randint(0,255)
    cg= random.randint(0,255)
    cb = random.randint(0,255)

    #assign a random integer between 0 and 7 to a variable named rx,ry
    #position
    rx = random.randint(0,7)
    ry = random.randint(0,7)  

    sense.set_pixel(rx,ry,(cr,cg,cb))
    time.sleep(0.1)
    sense.clear()

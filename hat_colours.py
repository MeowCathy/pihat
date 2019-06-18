#! /usr/bin/env python
#this script will define colours for scrolling message on the pi HAT
from sense_hat import SenseHat
sense = SenseHat()

#use RGB to define colours
yellow = (255,255,0)
blue = (0,0,255)

speed = 0.05

message = "Hello World!"

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

sense.clear()

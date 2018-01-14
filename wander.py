#!/usr/bin/env python
                  

from gopigo import *
import time
import easygopigo3 as easy


gpg = easy.EasyGoPiGo3(use_mutex=True)
my_Distance_portI2C = easy.DistanceSensor('I2C', gpg, use_mutex=True)

STOP = 150 # Distance from obstacle where the GoPiGo should stop
look_angle = 90

time.sleep(0.1)

print "Press ENTER to start"

raw_input() # Wait for input to start
fwd() # Start moving

# start
while True:
    dist =  my_Distance_portI2C.read_mm()
    if dist == STOP:
        stop()
	break
    else:
        print(dist)
    time.sleep(0.1)
# stopped

# find new path
look_angle = 180 
dist_left = []
dist_right = []
while look_angle >= 0:
    servo(look_angle)
    look_angle -= 5
    time.sleep(0.1)
    dist = my_Distance_portI2C.read_mm()
    if look_angle > 90:
	dist_left.append(dist)
    elif look_angle < 90:
	dist_right.append(dist)

# reset look_angle
look_angle = 180 

avg_dist_left = sum(dist_left)/len(dist_left)
avg_dist_right = sum(dist_right)/len(dist_right)

# TO DO
# go in the direction with the most space

# No space?
# reverse


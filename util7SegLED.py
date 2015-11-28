#import time

#--- selection of import based on the package ---
''' 1. with RPi.GPIO'''
import RPi.GPIO as GPIO
''' 2. without RPi.GPIO'''
#from dummyGPIO import CDummyGPIO
#GPIO = CDummyGPIO()
#-----------------

'''
v0.2  2015/11/28
	- add info7seg_allOff()
v0.1  2015/11/28
	- add info7seg_init()
	- add info7seg_on()
'''

GPIO.setmode(GPIO.BOARD)

#-------------------
#[User Configuration]
# (Change according to the cable connections)
#
# Pin # of RPi2
#  to Pin# of 7seg LED a..h
#
# > case.1 assignment so that user can connect starting from #2
#   of C-361SR to left upper pin of RPi2 GPIO port downward
pinnum=[21, 19, 15, 11, 07, 03, 05, 13]


#-------------------
#[Do no change followings]
# onoff bit (7segment led > a..g)
onoff=[ 
[True,  True, True, True,  True,      True,  False, False ], # disp 0
[False, True, True, False, False,     False, False, False ], # disp 1
[True,  True, False, True,  True,      False,  True, False ], # disp 2
[True,  True, True,  True, False,      False, True, False], # disp 3
[False, True, True, False, False,      True, True,  False ], # disp 4
[True, False, True, True, False,       True,  True, False], # disp 5
[True, False, True, True,  True,       True, True, False], # disp 6
[True, True, True, False, False,       True, False, False], # disp 7
[True, True, True,  True,  True,       True, True, False], # disp 8
[True, True, True,  True,  False,       True, True, False], # disp 9
[False, False, False, False, False,     False, False, True], # disp .
]
# TODO: 0z > add out of range display
# TODO: 0z > add all off function
#-------------------

def info7seg_init():
	for idx in range(0, len(pinnum)): 
		GPIO.setup(pinnum[idx], GPIO.OUT) # a..h

def info7seg_on(number):
	for idx in range(0, len(pinnum)): # a..h
		GPIO.output(pinnum[idx], onoff[number][idx])

def info7seg_allOff():
	for idx in range(0, len(pinnum)): # a..h
		GPIO.output(pinnum[idx], False)

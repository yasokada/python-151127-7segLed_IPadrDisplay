from util7SegLED import info7seg_init, info7seg_on, info7seg_allOff
from util7SegLED import info7seg_decimalPoint
import time

'''
v0.2  2015/11/28
  - extract method to disp_0_9_DP()
  - use all off function
v0.1  2015/11/28
  - display 0..9 and decimal point
'''

def disp_0_9_DP(intvl):
	while True:
		for idx in range(0, 11):
			info7seg_on(idx)
			time.sleep(intvl)

info7seg_init()

for loop in range(0,3):
	info7seg_decimalPoint()
	time.sleep(0.5)
	info7seg_allOff()
	time.sleep(0.5)

disp_0_9_DP(0.5)

from util7SegLED import info7seg_init, info7seg_on
import time

'''
v0.2  2015/11/28
  - use all off function
v0.1  2015/11/28
  - display 0..9 and decimal point
'''

while True:
	info7seg_init()
	for idx in range(0, 11):
		info7seg_on(idx)
		time.sleep(2)

	info7seq_allOff()
	time.sleep(2)
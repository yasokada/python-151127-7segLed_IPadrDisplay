from util7SegLED import info7seg_init, info7seg_on
import time

while True:
	info7seg_init()
	for idx in range(0, 10):
		info7seg_on(idx)
		time.sleep(2)

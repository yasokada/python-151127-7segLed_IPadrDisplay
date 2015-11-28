from util7SegLED import info7seg_init, info7seg_on, info7seg_allOff
from util7SegLED import info7seg_decimalPoint
from util7SegLED import info7seg_onOff
from util7SegLED import info7seg_onDecimalPointOff
import time

'''
v0.2  2015/11/28
  - add disp_ipAddress()
  - extract method to disp_0_9_DP()
  - use all off function
v0.1  2015/11/28
  - display 0..9 and decimal point
'''

def disp_0_9_DP(intvl):
	while True:
		for idx in range(0, 11):
			info7seg_onOff(idx, intvl)

def disp_ipAddress(ipadr, intvl_sec):
	for idx in range(0, len(ipadr)):
		if "." in ipadr[idx]:
			info7seg_onDecimalPointOff(intvl_sec)
		else:
			val = int(ipadr[idx])
			info7seg_onOff(val, intvl_sec)

info7seg_init()

for loop in range(0,3):
	info7seg_onDecimalPointOff(0.5)
	info7seg_allOff()
	time.sleep(0.5)

disp_ipAddress("192.168", 0.5)

disp_0_9_DP(0.5)

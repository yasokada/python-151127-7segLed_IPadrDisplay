#!/usr/bin/env python
from util7SegLED import info7seg_init, info7seg_on, info7seg_allOff
from util7SegLED import info7seg_decimalPoint
from util7SegLED import info7seg_onOff
from util7SegLED import info7seg_onDecimalPointOff
from utilNetworkIP import NetworkIP_get_ipAddress_eth0
import time

'''
v0.4  2015/12/05
  - return error IP when the network is not available
v0.3  2015/11/28
  - add wait (10sec) to avoid failure at /etc/rc.local auto start
v0.2  2015/11/28
  - disp IP address using utilNetworkIP
  - add disp_ipAddress()
  - extract method to disp_0_9_DP()
  - use all off function
v0.1  2015/11/28
  - display 0..9 and decimal point
'''

def disp_0_9_DP(intvl):
	for idx in range(0, 11):
		info7seg_onOff(idx, intvl)

def disp_ipAddress(ipadr, intvl_sec):
	for idx in range(0, len(ipadr)):
		if "." in ipadr[idx]:
			info7seg_onDecimalPointOff(intvl_sec)
		else:
			val = int(ipadr[idx])
			info7seg_onOff(val, intvl_sec)

time.sleep(10) # to avoid failure at /etc/rc.local auto start

ipadr = NetworkIP_get_ipAddress_eth0()

info7seg_init()

disp_0_9_DP(0.5) # initial test

for loop in range(0,3):
	info7seg_onDecimalPointOff(0.5)
	info7seg_allOff()
	time.sleep(0.5)

while True:
	disp_ipAddress(ipadr, 0.5)
	info7seg_allOff()
	time.sleep(2.0)


import socket
import fcntl
import struct

'''
v0.2  2015/12/05
	- return kErrorIP when the network is not available
v0.1  2015/11/28
	- add NetworkIP_get_ipAddress_eth0()
	- add get_ip_address()
'''

kErrorIP = "0.0.0.0"

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
    except:
        return kErrorIP

def NetworkIP_get_ipAddress_eth0():
	return get_ip_address('eth0')



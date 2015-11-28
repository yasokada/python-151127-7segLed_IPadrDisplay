import socket
import fcntl
import struct

'''
v0.1  2015/11/28
	- add NetworkIP_get_ipAddress_eth0()
	- add get_ip_address()
'''

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def NetworkIP_get_ipAddress_eth0():
	return get_ip_address('eth0')



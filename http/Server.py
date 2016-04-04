import socket
import fcntl
import struct

def gethostbyname():
    return socket.gethostbyname(socket.gethostname())

def getipaddress(ifname):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

if __name__ == '__main__':
    print  getipaddress('lo')
    print  getipaddress('eth0')


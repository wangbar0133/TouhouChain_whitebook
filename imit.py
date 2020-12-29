import socket
import time

def get_host_ip():
    """返回本机IP地址"""
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ss.connect(('8.8.8.8', 8070))
        ip = ss.getsockname()[0]
    finally:
        ss.close()
    return ip



HOST = '192.168.1.255'
PORT = 9999
ADDR = (HOST, PORT)
udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpCliSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
data = bytes((str(time.asctime( time.localtime(time.time()))) + '      ObjectTransparants').encode('utf-8'))
while True:
    udpCliSock.sendto(data, ADDR)
    print('sus')
    time.sleep(6)

#udpCliSock.close()

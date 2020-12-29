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

HOST = get_host_ip()
PORT = 8000
ADDR = (HOST, PORT)
BUFSIZE = 20000


udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpCliSock.bind(('', PORT))
udpCliSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    data=b"Robot Online!"
    print("sending -> %s" %data)

    try:
        data, ADDR = udpCliSock.recvfrom(BUFSIZE)
        if  data:
            print(data)
        time.sleep(0.2)
    except Exception as E:
        continue
udpCliSock.close()
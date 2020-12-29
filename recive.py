import socket
import time

PORT = 9999
udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpCliSock.bind(('', PORT))
udpCliSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
while True:
    try:
        #print('sus')
        data, address = udpCliSock.recvfrom(4096)
        print(data)
    except:
        pass
    time.sleep(1)
from socket import *

HOST = '127.0.0.1'
PORT = 12567
BUFS = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFS)
    if not data:
        break
    print data

udpCliSock.close()

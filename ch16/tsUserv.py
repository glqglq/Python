from socket import *
from time import ctime
HOST = ''
PORT = 12567
BUFS = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'wating for message'
    data,addr = udpSerSock.recvfrom(BUFS)
    udpSerSock.sendto('[%s] %s'%(ctime(),data),addr)
    print '...received from and returned to:',addr,data

udpSerSock.close()
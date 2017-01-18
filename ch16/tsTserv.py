from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


print 'waiting for connection...'
tcpCliSock,addr = tcpSerSock.accept()

#zhineng you yige kehuduan lianjie 
while True:
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
	print data
    tcpCliSock.send('[%s] %s'%(ctime(),data))
tcpCliSock.close()
tcpSerSock.close()
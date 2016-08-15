#! /usr/bin/env python
from socket import *
from time import ctime
#import sqlite3

HOST = ''
PORT = 12348
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)

tcpSerSock.settimeout(1)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    try:
        print 'waiting for connection'
        tcpCliSock, addr = tcpSerSock.accept() #create and bind client
        print '...connected from: ', addr
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            #if not data:
            #	break
            #tcpCliSock.send('[%s] %s' % (ctime(), data))
            print data
            #else:
            #sentData = 'get'
            #if not sentData:
            #    break
            tcpCliSock.send('sentData')
    except KeyboardInterrupt:	
        tcpCliSock.close()
        tcpSerSock.close()
        exit(0)

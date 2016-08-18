#! /usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
#from time import ctime
import zichidb
from thread import *

HOST = ''
PORT = 12338
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)

#function for handling multi-connections
def clientthrd(conn):
    #conn.send('connected to %s',HOST)
    #tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    while True:
        
        data = conn.recv(1024)
        print data
        reply = 'OK...' + data
        if not data:
            break
        conn.sendall(reply)
    conn.close()

#tcpSerSock.settimeout(10)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
zdb = zichidb.zichidb()

while True:
    try:
        print 'waiting for connection'

        #create and bind client
        tcpCliSock, addr = tcpSerSock.accept() 
        print '...connected from: ', addr

        #while True:
            #tcpCliSock, addr = tcpSerSock.accept() 
            #print '...connected from: ', addr
            #data = tcpCliSock.recv(BUFSIZ)
        start_new_thread(clientthrd, (tcpCliSock,))
         
    except KeyboardInterrupt:	
        tcpCliSock.close()
        tcpSerSock.close()
        exit(0)

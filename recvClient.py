#! /usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
from time import ctime
import ZichiDB
#import sqlite3

HOST = ''
PORT = 12341
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)

tcpSerSock.settimeout(10)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
zdb = ZichiDB.ZichiDB()

while True:
    try:
        print 'waiting for connection'

        #create and bind client
        tcpCliSock, addr = tcpSerSock.accept() 
        print '...connected from: ', addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            #print type(data)
            #go back to the first while loop
            if not data:
            	break
            #tcpCliSock.send('[%s] %s' % (ctime(), data))
            print data
            zdb.insert(data)
            zdb.printdata();
            
            #else:
            #sentData = 'get'
            #if not sentData:
            #    break
            cmd = zdb.send()
            tcpCliSock.send(cmd)
    except KeyboardInterrupt:	
        tcpCliSock.close()
        tcpSerSock.close()
        exit(0)

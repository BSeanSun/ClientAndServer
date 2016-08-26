#!/usr/bin/env python

from socket import *

HOST = '192.168.1.3'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
print "client set"
tcpCliSock.connect(ADDR)
print "connection established"

while True:
    data = raw_input('>')
    if not data:
        break
    tcpCliSock.send(data)
    #data = tcpCliSock.recv(BUFSIZ)
    #if not data:
    #    break
    #print data

tcpCliSock.close()


#! /usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
#from time import ctime
import zichidb
#import 

HOST = ''
PORT = 11230
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)

tcpSerSock.settimeout(10)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
zdb = zichidb.zichidb()

def Byte2Hex(byteStr):
    return ' '.join(["%02X" % ord(x) for x in byteStr]).strip()

while True:
    try:
        print 'waiting for connection'

        #create and bind client
        tcpCliSock, addr = tcpSerSock.accept() 
        print '...connected from: ', addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            #go back to the first while loop
            if not data:
            	break
            #tcpCliSock.send('[%s] %s' % (ctime(), data))
            print type(data)
            
            #print data.decode("hex")
            decodedHex = Byte2Hex(data)
            
            hexToInt = decodedHex.split(' ')
            print hexToInt
            for i in xrange(3,len(hexToInt)-1,1):
                for j in xrange(4,len(hexToInt),1):
                    #print int(hexToInt[i]*0x100+hexToInt[j],16)
            
                    print hexToInt[i],hexToInt[j]     
            #for hex16 in hexToInt:
                #print hex16
            #    print int(hex16,16)
            #if not hex16:
            #    break
            
             
            #    print int(hex16,16)
                #hexToInt = hexToInt.append(int(hex16,16))
            #zdb.insert(hexToInt)
            #zdb.printdata();
            
            #else:
            #sentData = 'get'
            #if not sentData:
            #    break
            #cmd = zdb.send()
            #tcpCliSock.sendall(cmd)
    except KeyboardInterrupt:	
        tcpCliSock.close()
        tcpSerSock.close()
        exit(0)

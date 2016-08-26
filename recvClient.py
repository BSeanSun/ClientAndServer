#! /usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
#from time import ctime
import zichidb
#import 

HOST = ''
PORT = 11241
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
                        
            #print data.decode("hex")
            decodedHex = Byte2Hex(data)
            
            hexToInt = decodedHex.split(' ')
            print hexToInt
            thi = []
            for i in xrange(3,len(hexToInt)-3,2):
                res = int(hexToInt[i],16)*256 + int(hexToInt[i+1],16)
                print res
                thi.append(res)
            if thi[0] < 300:
                print thi[0]  
            #for hex16 in hexToInt:
                #print hex16
            #    print int(hex16,16)
            if not data:
                break
            
             
            #    print int(hex16,16)
                #hexToInt = hexToInt.append(int(hex16,16))
            zdb.insert(thi)
            zdb.printdata()
            #if zdb.checkTemp() > 30:
            #if True:
            """    HOST = '192.168.1.3'
                PORT = 8080
                BUFSIZ = 1024
                ADDR = (HOST, PORT)

                tcpCliSock = socket(AF_INET, SOCK_STREAM)
                print "client set"
                tcpCliSock.connect(ADDR)
                print "connection established"  
                tcpCliSock.send('hlkATat+GW=0,0 \r')     """ 
            #else:
            #sentData = 'get'
            #if not sentData:
            #    break
            #cmd = zdb.send()
            #tcpCliSock.sendall(cmd)
#except KeyboardInterrupt:	
    finally:
#tcpCliSock.close()
        tcpSerSock.close()
#exit(0)

#! /usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
import mysqlDB
import time
#import realtimePlot
#import MySQLdb
import emailAlert



HOST = ''
PORT = 11246
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)

tcpSerSock.settimeout(10)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
zdb = mysqlDB.mysqlDB()
#xList = [0]
#yList = [0]
def Byte2Hex(byteStr):
    return ' '.join(["%02X" % ord(x) for x in byteStr]).strip()

while True:
    try:
        print 'waiting for connection'

        #create and bind client
        tcpCliSock, addr = tcpSerSock.accept() 
        print '...connected from: ', addr
        #plt.draw()
        while True:
            
            data = tcpCliSock.recv(BUFSIZ)
            #go back to the first while loop
            if not data:
            	break
                        
            #print data.decode("hex")
            decodedHex = Byte2Hex(data) #Byte2Hex func
            
            hexToInt = decodedHex.split(' ') #Hex2Int and split temp, hum, illm
            
            thi = [] #refreshed for each data stream
            for i in xrange(3,len(hexToInt)-3,2):
                res = int(hexToInt[i],16)*256 + int(hexToInt[i+1],16)
                #print res
                thi.append(res)

            #call email alert func
            if thi[1] < 0:
                emailAlert.alert() 
            
            if not data:
                break
            #yList.append(thi[1]/100.0)  #y-axis
            #xList.append(xList[-1] + 1) #x-axis
            #realtimePlot.realtimePlot(xList[-10:-1], yList[-10:-1])  #draw plot
             
            #    print int(hex16,16)
                #hexToInt = hexToInt.append(int(hex16,16))
            
            zdb.insert(thi)
            zdb.printdata()
            time.sleep(10)
           
#except KeyboardInterrupt:	
    finally:
        #rptorelay.close()
        tcpSerSock.close()
#exit(0)

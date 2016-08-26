import sqlite3
import os
from time import ctime

class zichidb:
    """create and manipulate the DB"""
    conn = sqlite3.connect('zichi.db')
    c = conn.cursor()

    def __init__(self):
                #global conn = sqlite3.connect('zichi.db')
        #c = conn.cursor()
        #if os.path.isfile('zichi.db') == False:
        self.c.execute('''CREATE TABLE IF NOT EXISTS thidata
	                 (time text, temp real, humidity real, illum real)''')
        
    def insert(self, data):
        #thi = data.split(' ')
        illum, temp, humid = data[0],data[1]/100.0,data[2]/100.0
        self.c.execute("INSERT INTO thidata VALUES (?,?,?,?)", (ctime(), illum, temp, humid))

    def printdata(self):
        
        for row in self.c.execute('SELECT * FROM thidata'):
            print row
    
    def checkTemp(self):
        total = 0
        for tmp in self.c.execute('SELECT temp FROM thidata DESC LIMIT 5'):
            total = tmp + total
        return total/5.0
    
    def send(self):
        dataSent = ''
        for row in self.c.execute('SELECT * FROM thidata'):
            for col in range(0, len(row)):
                dataSent = dataSent + str(row[col])+' '

        return dataSent

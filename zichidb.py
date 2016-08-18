import sqlite3
import os

class zichidb:
    """create and manipulate the DB"""
    conn = sqlite3.connect('zichi.db')
    c = conn.cursor()

    def __init__(self):
                #global conn = sqlite3.connect('zichi.db')
        #c = conn.cursor()
        #if os.path.isfile('zichi.db') == False:
        self.c.execute('''CREATE TABLE IF NOT EXISTS thidata
	                 (temp real, humidity real, illum real)''')
        
    def insert(self, thi):
        temp, humid, illum = thi.split(' ')
        self.c.execute("INSERT INTO thidata VALUES (?,?,?)", (temp, humid, illum))

    def printdata(self):
        
        for row in self.c.execute('SELECT * FROM thidata ORDER BY temp'):
            print row

    def send(self):
        dataSent = ''
        for row in self.c.execute('SELECT * FROM thidata'):
            for col in range(0, len(row)):
                dataSent = dataSent + str(row[col])+' '

        return dataSent

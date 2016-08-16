import sqlite3
import os

class ZichiDB:
    """create and manipulate the DB"""
    conn = sqlite3.connect('zichi.db')
    c = conn.cursor()

    def __init__(self):
        #pass
        #global conn = sqlite3.connect('zichi.db')
        #c = conn.cursor()
        #if os.path.isfile('zichi.db') == False:
        self.c.execute('''CREATE TABLE IF NOT EXISTS thidata
	                 (date text, temp text, humidity text, illum real)''')
        
    def insert(self, thi):
        self.c.execute("INSERT INTO thidata VALUES (2006-01-05,25,60,600)")

    def printdata(self):
        
        for row in self.c.execute('SELECT * FROM thidata ORDER BY temp'):
            print row

    def send(self):
        dataSent = ''
        for row in self.c.execute('SELECT * FROM thidata ORDER BY temp'):
            dataSent = dataSent.join(row)
        return dataSent


import sqlite3
import os
conn = sqlite3.connect('zichi.db')
c = conn.cursor()
if os.path.isfile('zichi.db') == False:
    c.execute('''CREATE TABLE thidata
	             (date text, temp text, humidity text, illum real)''')

# Insert a row of data
else:
    #conn = sqlite3.connect('zichi.db')
    #c = conn.cursor()
    c.execute("INSERT INTO thidata VALUES ('2006-01-05','25','60',600)")

for row in c.execute('SELECT * FROM thidata ORDER BY temp'):
    print (row)

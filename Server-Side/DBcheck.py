import sqlite3

conn = sqlite3.connect('isdn.db')
c = conn.cursor()

c.execute("select num from isdn")
title = c.fetchall()
print(title)

conn.commit()
conn.close()

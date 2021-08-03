import sqlite3
import os
import json

cwd = os.getcwd()
jsonPath = cwd + "/pivot.json"

conn = sqlite3.connect('isdn.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS isdn''')
c.execute('''DROP TABLE IF EXISTS isdn_high''')
c.execute('''DROP TABLE IF EXISTS isdn_low''')
c.execute("create table isdn(num int,title txt,author txt,datetime int)")
c.execute("create table isdn_high(num int)")
c.execute("create table isdn_low(num int)")

conn.commit()
conn.close()

data = {}

with open(jsonPath,mode="w") as f:
    json.dump(data,f,indent=4)

import xml.etree.ElementTree as ET
import urllib
import time
import requests
from bs4 import BeautifulSoup
import lxml
import sqlite3
import os
import json
import statistics
import schedule

#table isdn(num int,title txt,author txt,datetime int)

#カレントディレクトリを取得
cwd = os.path.split(os.path.realpath(__file__))[0]
jsonPath = cwd + "/pivot.json"

#過去に登録したことがあるか
def Authentication(num):
    #Pivotの読み込み
    with open(jsonPath) as d:
        f = d.read()
        data = json.loads(f)

    #json内部に検索キャッシュが存在したら利用する。
    if not "pivot" in data.keys():
        pivot = 0
    else:
        pivot = data["pivot"]

    conn = sqlite3.connect('isdn.db')
    c = conn.cursor()

    if num >= pivot:
        print("high")
        c.execute("select num from isdn_high where num = ?",(num,))
    else:
        print("low")
        c.execute("select num from isdn_low where num = ?",(num,))
    check = c.fetchone()
    print(check)
    if check:
        print("Authentication:True")
        return True
    else:
        print("Authentication:False")
        return False

#Pivotの生成
def PivotCreate():
    conn = sqlite3.connect('isdn.db')
    c = conn.cursor()

    c.execute('select num from isdn')
    rawIdList = c.fetchall()
    rawIdList.sort()

    idList = [id[0] for id in rawIdList]

    with open(jsonPath) as d:
        f = d.read()
        data = json.loads(f)

    pivot = statistics.median_high(idList)
    pivotPoint = idList.index(pivot)
    data = {}
    data["pivot"] = pivot
    ids = [rawIdList[pivotPoint:],rawIdList[:pivotPoint]]
    with open(jsonPath,mode="w") as f:
    	json.dump(data,f,indent=4)

    conn.close()
    print(pivot)
    print(pivotPoint)
    return ids

def DataBaseAdd(HLIdList):
    conn = sqlite3.connect('isdn.db')
    c = conn.cursor()

    c.execute('''DROP TABLE IF EXISTS isdn_high''')
    c.execute('''DROP TABLE IF EXISTS isdn_low''')
    c.execute("create table isdn_high(num int)")
    c.execute("create table isdn_low(num int)")
    c.executemany('insert into isdn_high(num) values (?)',HLIdList[0])
    c.executemany('insert into isdn_low(num) values (?)',HLIdList[1])
    conn.commit()
    conn.close()

def Scraping():
    print("start")
    rootURL = "https://isdn.jp/xml"

    r = requests.get("https://isdn.jp/list.php")
    #BeautifulSoupの機能でHTMLを読み込み
    soup = BeautifulSoup(r.content, "lxml")

    workList = soup.find("div",{"id":"main"})

    rawList = workList.findAll("a")

    URLs = []

    for raw in workList.findAll("a"):
        URLs.append(raw.get("href"))

    for URL in URLs:
        url = rootURL + URL
        req = urllib.request.Request(url)

        with urllib.request.urlopen(req) as response:
            XmlData = response.read()

        tree = ET.fromstring(XmlData)
        isdn = int(URL.replace("/",""))
        title = tree.find('.//{https://isdn.jp/schemas/0.1}product-name').text
        author = tree.find('.//{https://isdn.jp/schemas/0.1}publisher-name').text
        date = int(tree.find('.//{https://isdn.jp/schemas/0.1}issue-date').text.replace("-",""))
        print(isdn,title,author,date)
        if Authentication(isdn) == False:
            conn = sqlite3.connect('isdn.db')
            c = conn.cursor()

            c.execute('insert into isdn(num,title,author,datetime) values (?,?,?,?)',(isdn,title,author,date))

            conn.commit()
            conn.close()

        time.sleep(1)
    DataBaseAdd(PivotCreate())
    print("finish")

schedule.every().day.at("00:05").do(Scraping)

if __name__ == "__main__":
    Scraping()
    while True:
        schedule.run_pending()
        time.sleep(60)

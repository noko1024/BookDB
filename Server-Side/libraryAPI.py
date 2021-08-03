import datetime
import requests
import sqlite3
from flask import Flask,request,make_response,jsonify
import urllib
import xml.etree.ElementTree as ET
import re
import os
import base64

#table isdn(num int,title txt,author txt,datetime int)

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += "HIGH:!DH:!aNULL"

app = Flask(__name__)

here = os.path.dirname(__file__)
database = os.path.join(here,"isdn.db")

#ここで開通チェックしてどうぞ！！！！！！！！！！！！！！！！！！！！！！！！！！！！
#開通チェックなんかReturnしてくれるんか？
#"ver0.1 <- return"　頑張れ

@app.route("/info")
def infos():
    return("現在API全体に障害が発生しています。復旧作業を実施しております。\nAPIに関する情報はこちらで続けてお伝えします。ご迷惑をおかけして申し訳ございません。")

@app.route("/api/")
def check():
    return make_response("ver0.1")

@app.route("/api/searchIsdn")
def Isdn():
    try:
        isdn = request.args.get('isdn', default = 0, type = int)

        conn = sqlite3.connect(database)
        c = conn.cursor()

        c.execute('select num,title,author from isdn where num == ?',(isdn,))

        searchList = c.fetchall()

        conn.commit()
        conn.close()
        data = {
            "search":searchList
        }

        return make_response(jsonify(data))
    except Exception as e:
        errorType = "type:" + str(type(e))
        errorArgs = "args:" + str(e.args)
        errorRaw = "raw:" + str(e)
        cwd = "cwd:" + os.getcwd()
        data = { "エラー内容":errorType + errorArgs + errorRaw + cwd}
        return make_response(jsonify(data))

#title=ketword ->条件無指定(部分一致)
#title=^keyword ->前方一致
#title=exactkeyword ->完全一致
#https://iss.ndl.go.jp/api/opensearch?cnt=10&title=^%E3%81%82&mediatype=1

@app.route("/api/searchIsdnTitle")
def IsdnTitle():
    title = request.args.get('title', default = None, type = str)

    data = {"search":[]}
    if not title:
        return make_response(jsonify(data))

    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute('select num,title,author from isdn where title like ? limit 10',(title+"%",))

    searchList = c.fetchall()

    conn.commit()
    conn.close()
    data = {
        "search":searchList
    }

    return make_response(jsonify(data))


@app.route("/api/searchIsbn")
def Isbn():
    isbn = request.args.get('isbn', default = 0, type = int)

    url = "https://iss.ndl.go.jp/api/opensearch?cnt=1&isbn={isbn}&mediatype=1"
    #https://iss.ndl.go.jp/api/opensearch?cnt=1&isbn=9784041069516&mediatype=1
    url = url.format(isbn=isbn)
    req = requests.get(url)

    namespaces = {
    'dc': "http://purl.org/dc/elements/1.1/"
    }

    tree = ET.fromstring(req.text)
    title = tree.find('.//item/title').text
    author = tree.find('.//item/author').text
    publisher = tree.findall('.//dc:publisher',namespaces)[0].text

    data = {
        "search":[[title,author,publisher]]
    }

    return make_response(jsonify(data))

@app.route("/api/searchIsbnTitle")
def IsbnTitle():
    title = request.args.get('title', default = None, type = str)

    data = {"search":[]}
    if not title:
        return make_response(jsonify(data))

    #ここでAPIコール
    url = "https://iss.ndl.go.jp/api/opensearch?cnt=10&title={title}&mediatype=1"
    title = urllib.parse.quote(title)
    url = url.format(title=title)
    req = requests.get(url)

    namespaces = {
    'dc': "http://purl.org/dc/elements/1.1/"
    }
    bookDataList = []
    count = 0

    tree = ET.fromstring(req.text)
    itemlist = tree.findall('.//item')
    for item in itemlist:
        title = item.find('./title').text
        try:
            author = item.find('author').text
        except:
            author = ""
        publisher = tree.findall('.//dc:publisher',namespaces)[count].text
        print(title,author,publisher)
        count += 1
        bookDataList.append([title,author,publisher])

    print(bookDataList)

    data = {
        "search":bookDataList
    }

    return make_response(jsonify(data))

if __name__ == "__main__":
	app.run()

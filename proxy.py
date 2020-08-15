#url ="https://iss.ndl.go.jp/api/sru?operation=searchRetrieve&maximumRecords=10&query=title%3d%22%e6%a1%9c%22%20AND%20from=%222018%22"

#2020/08/07
#プロキシ情報を要求し外部ネットワークとの接続を確立可能か検証する。→成功

import os
import requests
import getpass

print("Return contents and http status code.")
ID = input("Please proxy loginID >")
PASS = getpass.getpass("Please proxy loginPassword >")
PROXY = input("Please proxy IPaddess:port >")

proxies = {
    "https":"http://"+ID+":"+PASS+"@"+PROXY,
    "http":"http://"+ID+":"+PASS+"@"+PROXY
    }

while True:
    try:
        url = input("Please request URL >")
        if url =="exit":
            os._exit(0)
        if url.startswith != "http://" or url.startswith != "https://":
            url = "http://"+url
        
        proxies = None
        
        response = requests.get(url,proxies=proxies)
        print(response.text)
        print(response.status_code)
        input()
    except:
        import traceback
        print("reasons:")
        traceback.print_exc()
        print("failed connection!")
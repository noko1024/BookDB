
#システム全般に関わるライブラリ
import os
import threading

#外部通信に関わるライブラリ
#import bs4
import requests

#kivyに関するライブラリ
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


#buildメソッドをoverride
class MainApp(App):
    

#https://pyky.github.io/kivy-doc-ja/guide/basic.html  
class ProxyRequestApp(App):

class StandbyApp(App):
    


class APICall:
    def __init__(self,proxyFlag,ProxyID,ProxyPASS,ProxyIP,ProxyPort):
        #APICallに必要な共通情報を宣言
        #途中にプロキシ変更回すなら必要そう...?(インスタンス化するんだからいらないんじゃね？)
        #------------------------------
        self.ProxyFlag = proxyFlag
        self.ID = ProxyID
        self.PASS = ProxyPASS
        self.IP = ProxyIP
        self.PORT = ProxyPort
        #------------------------------
        self.proxies = {
        "https":"http://%s:%s@%s:%s" % (self.ID,self.PASS,self.IP,self.PORT),
        "http":"http://%s:%s@%s:%s" % (self.ID,self.PASS,self.IP,self.PORT)
        }

    #asyncio使いたい→スレッドになりそう。
    #https://note.crohaco.net/2019/python-asyncio/
    def ndlCall(self,query):
            maximum ="10"
            URL ="https://iss.ndl.go.jp/api/sru?operation=searchRetrieve&maximumRecords="+maximum+"&query=" +query.encode("utf-8")
            
            response = requests.get(url,proxies=proxies)


#プログラム全体の初期化とユーザーへの情報要求
def init():
    pass


#プログラム開始の起点
def main():
    #App().run()
    UI()

if __name__ == "__main__":
    init()
    main()

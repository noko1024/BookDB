#モジュールのimport準備
import os
import sys

#Main.pyまでのフルパスを取得し__file__でsplit
basepath = os.path.split(os.path.realpath(__file__))[0]
#ライブラリを保存したディレクトリを指定し有効化
sys.path.insert(0, os.path.join(basepath, 'backlib')

#システム全般に関わるライブラリ
import threading
import pathlib
import json
import sqlite3
#https://ymgsapo.com/2019/08/05/cryptography-python/#i
import cryptography
#import pycrypto
#エラー音とか？
#import pygame
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
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget

proxyInstance = "incetanceData"


#kivyLangを引数化して制御したい。

#buildメソッドをoverride
#MainAppはメインウィンドウ起動時以外で回したくない。
#→initメソッドで回すBUTインスタンスは欲しい。
#ANS Mainメソッドの引数をinit()にする。

#すべての変数をMainAppの管理下に置く必要はない。
#あくまでも呼び出しを行うだけ。

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


#ユーザーからの結果をreturnしたい
#initで実行できない。
#インスタンス.run()は何が帰る？
#返したいものAPIConnのインスタンス

#https://pyky.github.io/kivy-doc-ja/guide/basic.html
#https://qiita.com/penta2019/items/a500630608960752a914

#
class ProxyRequestApp(App,Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.instance = None
    
    def build(self):
        Window.size = (400, 200)
        return 

    def activateButtonClicked(self):
        global proxyInstance
        print(type(self.ids.text1.text))
        proxyInstance = APICall(False)
        proxyChk_Thread = threading.Thread(target=proxyInstance.connectionChk())
        userStandby_Thread = threading.Thread(target=StandbyApp().run())
        proxyChk_Thread.start()
        userStandby_Thread.start()
        proxyChk_Thread.join()
        userStandby_Thread.join()
    
    def run(self,**kwargs):
        super().run(**kwargs)

        return "PIP",self.instance

#起動時パスワード認証
class AuthRequestApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

#汎用的にしたい
class StandbyApp(App):
#resonとか表示させる?いつ止める？
# →スレッドで回してjoinさせる？
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def build(self):
        return


class ErrorApp(App):
    pass

#設定ファイル(config.json),DB(books.db)に決め打ち
class FileIO:
    def __init__(self):
        self.basePath = basepath
        self.configPath = os.path.join(basepath,"config.json")
        self.dbPath = os.path.join(basepath,"books.db")
    

    def existsChk(self):
        return os.path.exists(self.configPath),os.path.exists(self.dbPath)

    def configInit(self):
        pass

    def configRead(self,keys=None):
    #keyはList
        try:
            #keysがNoneなら
            if keys is None:
                pass
            else:
                for key in keys:
                    pass
        
        #ファイルが存在しない時
        except FileNotFoundError:
            pass
        #ファイルにアクセスできない時
        except:
            pass

        return
    
    def configWrite(self,key,value):
        pass

    def dbInit(self):
        pass        


class APICall:
    def __init__(self,proxyFlag,ProxyID=None,ProxyPASS=None,ProxyIP=None,ProxyPort=None):
        #APICallに必要な共通情報を宣言
        #途中にプロキシ変更回すなら必要そう...?(インスタンス化するんだからいらないんじゃね？)
        #------------------------------
        self.ProxyFlag = proxyFlag
        self.ID = ProxyID
        self.PASS = ProxyPASS
        self.IP = ProxyIP
        self.PORT = ProxyPort
        #------------------------------
        if proxyFlag == True:
            self.proxies = {
            "https":"http://%s:%s@%s:%s" % (self.ID,self.PASS,self.IP,self.PORT),
            "http":"http://%s:%s@%s:%s" % (self.ID,self.PASS,self.IP,self.PORT)
            }
    def connectionChk(self):
        response = requests.get("https://ctf.noko1024.net/")
        print(response.text)
        print(response.status_code)
    #通信成功の可否とHTMLステータスコード,コンテンツを返す。
        return response.status_code,response.text


    
    #asyncio使いたい→スレッドになりそう。
    #https://note.crohaco.net/2019/python-asyncio/
    def ndlCall(self,query):
            maximum ="10"
            URL ="https://iss.ndl.go.jp/api/sru?operation=searchRetrieve&maximumRecords="+maximum+"&query=" +query.encode("utf-8")
            
            response = requests.get(url,proxies=proxies)


#プログラム全体の初期化とユーザーへの情報要求
#起動時にパスワード求めてフレーズを基にAESを復号→文字列切り出し＆演算で成功したか確認
def init():
    #プロキシの要求→(接続の確認)→ファイルの存在確認→設定ファイルの読み込み(or生成)→retunでAPIのインスタンスを返す
    IO = FileIO()
    config,db = IO.existsChk()
    if config is False:
        print("import TH")
        ProxyRequestApp().run()

        print("return="+str(initProxy.instance))
    else:
        auth = IO.configRead(["Proxy"])
        AuthRequestApp().run()
        
    
    return


#プログラム開始の起点
def main():
    #App().run()
    UI()

if __name__ == "__main__":
    main(init())

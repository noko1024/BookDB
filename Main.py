
#システム全般に関わるライブラリ
import os
import threading
import pathlib
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

class ProxyRequestApp(App):
    def __init__(self):
        pass

    def build(self):
        return

    

#汎用的にしたい
class StandbyApp(App):
#resonとか表示させる?いつ止める？
# →スレッドで回してjoinさせる？
    def __init__(self):
        pass

    def build(self):
        return

class ErrorApp(App):
    pass

#設定ファイル(),DB(.db)に決め打ち
class FileIO:
    def __init__(self):
        self.currentPath = os.getcwd()
    
    def existsChk(self,filePath):
        #filePathが絶対パスであるかどうか
        if not filePath.is_absolute():
            #でないなら相対パスを絶対パスに変換
            filePath = filePath.resolve()
        os.path.exists()
    def DBinit(self):
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
    
    #通信成功の可否とHTMLステータスコード,コンテンツを返す。
        return 


    
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
    
    initProxy = ProxyRequestApp().run()

    return


#プログラム開始の起点
def main():
    #App().run()
    UI()

if __name__ == "__main__":
    main(init())

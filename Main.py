
#システム全般にかかわるライブラリ
import os
import sys
import threading
import json
import pathlib
import sqlite3
basepath = os.path.split(os.path.realpath(__file__))[0]

#外部通信に関わるライブラリ
#import bs4
import requests

import tkinter
#PyQt
import PyQt5
from PyQt5 import QtCore,QtGui,uic,QtWidgets
sys.path.insert(0, os.path.join(basepath, 'data/ui',))
import proxyUI
#Main.pyまでのフルパスを取得し__file__でsplit
basepath = os.path.split(os.path.realpath(__file__))[0]
#ライブラリを保存したディレクトリを指定し有効化
sys.path.insert(0, os.path.join(basepath, 'data/lib',))

#システム全般に関わるライブラリ
#https://ymgsapo.com/2019/08/05/cryptography-python/#i
import cryptography


#最悪省いて良い機能
#ユーザー認証(ログイン時),

#ロードマップ
#図書データCall機能,図書データ一覧表示機能,削除機能,proxy認証


proxyInstance = "incetanceData"
threadFlag = False
tk = tkinter.Tk()
tk.geometry("400x400")

#kivyLangを引数化して制御したい。

#buildメソッドをoverride
#MainAppはメインウィンドウ起動時以外で回したくない。
#→initメソッドで回すBUTインスタンスは欲しい。
#ANS Mainメソッドの引数をinit()にする。

#すべての変数をMainAppの管理下に置く必要はない。
#あくまでも呼び出しを行うだけ。

"""
class MainApp():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
"""

#ユーザーからの結果をreturnしたい
#initで実行できない。

#返したいものAPIConnのインスタンス

#https://pyky.github.io/kivy-doc-ja/guide/basic.html
#https://qiita.com/penta2019/items/a500630608960752a914

#D:\Language\Python\Scripts\pyuic5.exe -x  --output=proxyUI.py proxy.ui



class ProxyRequestApp(proxyUI.Ui_Dialog):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.instance = proxyInstance

        self.proxyUse = False

        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)
        self.Dialog.show()
        print(self.app.exec_())
        
    

    def ProxyStatus(self,Flag):
        #トグルスイッチ毎に呼び出し
        
        self.proxyUse = Flag
        self.InputID.text()
        

    def OKBtnPush(self):
        global proxyInstance
        global threadFlag

        if self.proxyUse is True:
            proxyInstance = APICall(True)
        proxyInstance = APICall(False)
        Standby = StandbyApp()
        Thread = threading.Thread(target=proxyInstance.connectionChk)
        Thread.start()
        StandbyApp().show()
        self.Dialog.close()



"""
        proxyInstance = APICall(False)
        Standby = StandbyApp()
        userStandby_Thread = threading.Thread(target=Standby.show)

        print("SS")
        userStandby_Thread.start()
        print("SSS")
        proxyInstance.connectionChk()
        print("END")

        Standby.Flag = True
        print("EX"+str(threadFlag)) 
        self.Dialog.close()
"""



#起動時パスワード認証
class AuthRequestApp():
    def __init__(self):
        pass


class AuthInputApp():
    def __init__(self):
        pass


#汎用的にしたい
class StandbyApp():
#resonとか表示させる?いつ止める？
# →スレッドで回してjoinさせる？
    def __init__(self):
        pass
    def show(self):

        def ExitObserver():
            tk.after(500,ExitObserver)
            if threadFlag is True:
                tk.destroy()
                return

        ExitObserver()
        tk.mainloop()
    


class ErrorApp():
    def __init__(self):
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
        
        #ファイルにアクセスできない時
        except:
            pass

        return
    
    def configWrite(self,key,value):
        pass

    #ID(id) int,作品名(title) txt,出版社名(publisher) txt,発行日(issueDate) int 入架日(addStackDate) int,ジャンル  
    def dbInit(self):
        conn = sqlite3.connect("Book.db")
        c = conn.curser()
        c.execute("CREATE TABLE books(id int,title text,writer text,publisher text,issueDate int,addStackDate int,BN-group int,BN-all)")
        conn.commit()
        conn.close()
    
    def dbadd(self,title,publisher,issue,):
        conn = sqlite3.connect("Book.db")
        c = conn.cursor()
    
    def dbread(self,id):
        conn = sqlite3.connect("Book.db")
        c = conn.cursor()
        c.execute("select id from id where id = ?,")

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
        try:
            response = requests.get("https://ctf.noko1024.net/")
            print(response.text)
            print(response.status_code)
        except:
            pass
        finally:
            print("EX")
            global threadFlag
            threadFlag = True
            return
    #通信成功の可否とHTMLステータスコード,コンテンツを返す。
        return response.status_code,response.text


    def AllCall(self,APIFlag,query):
        pass

    
    #asyncio使いたい→スレッドになりそう。
    #https://note.crohaco.net/2019/python-asyncio/
    
    ##次回以降のアップデートで追加## 
    def ndlCall(self,query):
            maximum ="10"
            URL ="https://iss.ndl.go.jp/api/sru?operation=searchRetrieve&maximumRecords="+maximum+"&query=" +query.encode("utf-8")
            
            response = requests.get(URL,proxies=proxies)
    #############################

#プログラム全体の初期化とユーザーへの情報要求
#起動時にパスワード求めてフレーズを基にAESを復号→文字列切り出し＆演算で成功したか確認
def init():
    #StandbyApp()
    #プロキシの要求→(接続の確認)→ファイルの存在確認→設定ファイルの読み込み(or生成)→retunでAPIのインスタンスを返す
    IO = FileIO()
    config,db = IO.existsChk()
    if config is False:
        print("import TH")
        ProxyRequestApp()

    else:
        auth = IO.configRead(["Proxy"])
        AuthRequestApp().show
        
    
    return


#プログラム開始の起点
def main():
    #App().run()
    #UI()
    pass

if __name__ == "__main__":
    init()
    main()

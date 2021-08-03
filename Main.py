#プログラムが正常に動作しない場合は　https://elecbookapi.noko1024.net/info をご覧ください
#--第二演習室でないと動作しません。--

#システム全般にかかわるライブラリ
import os
import sys
import threading
import json
import pathlib
import sqlite3

from requests.models import Response
basepath = os.path.split(os.path.realpath(__file__))[0]

#外部通信に関わるライブラリ
#import bs4
import requests

import tkinter
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
#PyQt
import PyQt5
from PyQt5 import QtCore,QtGui,uic,QtWidgets
from PyQt5.QtCore import QDate, QDateTime
sys.path.insert(0, os.path.join(basepath, 'data/ui',))
import proxyUI
import Mainwindow
import authRequestUI
import authUI
#Main.pyまでのフルパスを取得し__file__でsplit
basepath = os.path.split(os.path.realpath(__file__))[0]
#ライブラリを保存したディレクトリを指定し有効化
#sys.path.insert(0, os.path.join(basepath, 'data/lib',))

#システム全般に関わるライブラリ
#https://ymgsapo.com/2019/08/05/cryptography-python/#i
#import cryptography



#最悪省いて良い機能
#ユーザー認証(ログイン時),

#ロードマップ
#図書データCall機能,図書データ一覧表示機能,削除機能,proxy認証


proxyInstance = "incetanceData"
proxyReturn = None
threadFlag = False
tk = tkinter.Tk()
tk.geometry("400x400")
DB = [[]]
SearchFlag = False
#kivyLangを引数化して制御したい。

#buildメソッドをoverride
#MainAppはメインウィンドウ起動時以外で回したくない。
#→initメソッドで回すBUTインスタンスは欲しい。
#ANS Mainメソッドの引数をinit()にする。

#すべての変数をMainAppの管理下に置く必要はない。
#あくまでも呼び出しを行うだけ。


class MainApp(Mainwindow.Ui_MainWindow):
    def __init__(self):

        self.API = proxyInstance
        self.DB = DB
        self.selectNum = 0
        self.nowTable =""
        #どちらのAPIをCallするか isbn=>NDL isbn=>ISDN
        self.choice = "Isbn"
        self.titleCheckbox = False
        self.BNCheckbox = False
        


        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        
        self.TableWindowAdd()

        self.MainWindow.show()
        self.app.exec_()


    def Search(self):
        ANS = None
        #ISBN/ISDN or 書名のどちらを選択したか 
        #どちらもFalseの場合はtitleを利用する
        if self.titleCheckbox is False and self.BNCheckbox is False:
            queue = self.choice+"Title"+"?title="+self.inputTitle.text()
            print(queue)
            print("Allfalse")
            ANS = self.API.AllCall(queue)
        

        #どちらもTrueの場合はtitleを利用する
        elif self.titleCheckbox is True and self.BNCheckbox is True:
            queue = self.choice+"Title"+"?title="+self.inputTitle.text()
            ANS = self.API.AllCall(queue)
        
        elif self.titleCheckbox is True:
            queue = self.choice+"Title"+"?title="+self.inputTitle.text()
            ANS = self.API.AllCall(queue)
        
        elif self.BNCheckbox is True:
            queue =self.choice+"?"+self.choice.lower()+"="+self.inputBN.text()
            ANS = self.API.AllCall(queue)
        
        self.TableWindowAdd(self.choice.lower(),ANS)
        





    def TableWindowAdd(self,APIrule=None,addList=None):
        global SearchFlag 
        if addList is None:
            #print("SUSSSUS")
            addList = FileIO().dbread()
            SearchFlag = False
            
        else:
            SearchFlag =True

            self.tableWidget.setRowCount(0)
            print(len(addList))
            self.nowTable = addList
            i = 0
            self.tableWidget.setRowCount(len(addList))
            if APIrule =="isbn":
                for value in addList:
                    print(value)
                    #タイトル
                    self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(value[0]))
                    #発行者
                    self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(value[1]))
                    #発行者
                    self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(value[2]))

                    i+=1
                return
                
            elif APIrule == "isdn":
                for value in addList:
                    print(value)
                    #ISBN/ISDN
                    self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(value[0])))
                    #タイトル
                    self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(value[1]))
                    #発行者
                    self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(value[2]))
                    i+=1
                return
            


        #testCode
        self.tableWidget.setRowCount(0)
        print(len(addList))
        self.nowTable = addList
        i = 0
        self.tableWidget.setRowCount(len(addList))
        for value in addList:
            print(value)
            #ISBN/ISDN
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(value[6])))
            #タイトル
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(value[1]))
            #作者
            self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(value[2]))
            #発行者
            self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(value[3]))
            #発行日
            self.tableWidget.setItem(i,4,QtWidgets.QTableWidgetItem(value[4]))
            #入架日
            self.tableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(value[5]))
            i+=1


    def Add(self):
        #要素選択 or 入力された時
        print("day")
        print(self.inputAddStackDate.date().toString())
        FileIO().dbadd(self.inputTitle.text(),self.inputCreator.text(),self.inputPublisher.text(),self.inputIssueDate.date().toPyDate() ,self.inputAddStackDate.date().toPyDate(),self.inputBN.text())

        self.TableWindowAdd()
        pass
        
        #???
        #self.tableWidget.update()
        print("S")
        pass

    def Remove(self):
        if SearchFlag ==True:
            self.TableWindowAdd()
            return
        print("remove")
        try:
            FileIO().dbremove(self.nowTable[self.selectNum][0])
        
        #連続押しによるout of range回避
        except IndexError:
            pass

        self.TableWindowAdd()
        

    def CheckBox(self,trig):
        if trig == "BN":
            self.BNCheckbox = not self.BNCheckbox
        elif trig == "Title":
            self.titleCheckbox = not self.titleCheckbox
        print("OK")
        pass

    def Choice(self,choice):
        self.choice=choice
        print("OK")
        pass

    def DBSelect(self):
        try:
            self.selectNum = self.tableWidget.selectedItems()[0].row()
        except:
            self.selectNum =""
        
        try:
            self.inputBN.setText(str(self.nowTable[self.selectNum][6]))
        except:
            self.inputBN.setText("")
        try:
            self.inputTitle.setText(str(self.nowTable[self.selectNum][1]))
        except:
            self.inputTitle.setText("")
        try:
            self.inputCreator.setText(str(self.nowTable[self.selectNum][2]))
        except:
            self.inputCreator.setText("")
        try:
            self.inputPublisher.setText(str(self.nowTable[self.selectNum][3]))
        except:
            self.inputPublisher.setText("")

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
        self.app.exec()
        main()
        

    def ProxyStatus(self,Flag):
        #トグルスイッチ毎に呼び出し
        
        self.proxyUse = Flag
        self.InputID.text()
        

    def OKBtnPush(self):
        global proxyInstance
        global threadFlag

        if self.proxyUse is False:
            proxyInstance = APICall(False)
        else:
            print("-------------------------")
            print(self.InputID.text())
            print(self.InputPassword.text())
            print(self.InputIP.text())
            print(self.InputPort.text())
            print("-------------------------")
            proxyInstance = APICall(True,self.InputID.text(),self.InputPassword.text(),self.InputIP.text(),self.InputPort.text())
        

        Thread = threading.Thread(target=proxyInstance.connectionChk)
        Thread.start()
        StandbyApp().show()
        print("ReturnIS")
        print(proxyReturn)

        if proxyReturn[0] == True:
            self.Dialog.close()
        else:
            ErrorApp("ネットワーク接続エラー","ネットワークへ正常に接続できませんでした。\n時間をおいて再試行するか、ネットワーク管理者へ以下のコードを連絡してください。\nCode "+proxyReturn[1]+":"+proxyReturn[2])




#起動時パスワード認証
class AuthRequestApp(authRequestUI.Ui_Dialog):
    def __init__(self):
        self.AUTHPASS = "" 
    
    def show(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)
        self.Dialog.show()
        self.app.exec()
        

    def OKBtnPush(self):
        print(self.InputPassword.text())
        pass


class AuthInputApp(authUI.Ui_Dialog):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        Dialog.show()
        app.exec()
    
    def OKBtnPush(self):
        print(self.InputPassword.text())
        pass
    
    

class Crypto():
    def __init__(self):
        pass

    #暗号化
    def Encrypt(self):
        pass
    #復号化
    def Decrypt(self):
        pass

    
#汎用的にしたい
class StandbyApp():
#resonとか表示させる?いつ止める？
# →スレッドで回してjoinさせる？
    def __init__(self):
        pass
    def show(self):
        #描画処理

        def ExitObserver():
            tk.after(500,ExitObserver)
            if threadFlag is True:
                tk.destroy()
                return

        ExitObserver()
        tk.mainloop()
    


class ErrorApp():
    def __init__(self,title,message):
        tk = tkinter.Tk()
        messagebox.showwarning(title,message)
        sys.exit()
        pass


#設定ファイル(config.json),DB(books.db)に決め打ち
class FileIO:
    def __init__(self):
        self.basePath = basepath
        self.configPath = os.path.join(basepath,"config.json")
        self.dbPath = os.path.join(basepath,"Books.db")
        print(self.dbPath)

    def existsChk(self):
        print(os.path.exists(self.configPath),os.path.exists(self.dbPath))
        return os.path.exists(self.configPath),os.path.exists(self.dbPath)

    def configInit(self):
        data = {}
        with open(self.configPath,mode="w") as f:
            json.dump(data,f,indent=4)


    def configRead(self,keys=None):

        try:
            with open(self.configPath) as f:
                config = f.read()
                config = json.loads(config)
        #ファイルにアクセスできない時
        except FileNotFoundError:
            return [False,"FileNotFoundError"]
        
        except:
            return [False]
        
        #keysがNoneなら
        if keys is None:
            return [True,config]
        
        else:   
            returnConfig = [True]
            dicts = {}
            for key in keys:
                value = config.get(key)
                if value:
                    dicts[key] = value

            returnConfig = returnConfig.append(dicts)
            return returnConfig


    
    def configWrite(self,key,value):
        pass

    #ID(id) int,作品名(title) txt,出版社名(publisher) txt,発行日(issueDate) int 入架日(addStackDate) int,ジャンル  
    def dbInit(self):
        conn = sqlite3.connect("Books.db")
        c = conn.cursor()
        c.execute("CREATE TABLE books(id int,title text,creator text,publisher text,issueDate None,addStackDate None,BN int)")
        conn.commit()
        conn.close()

    def dbadd(self,title="",creator="",publisher="",issueDate="",addStackData="",BN=""):
        if title =="" and creator =="" and publisher =="" and issueDate =="" and addStackData =="" and BN=="":
            return
        conn = sqlite3.connect("Books.db")
        c = conn.cursor()
        #Check
        #c.execute("select max(id) from books")
        c.execute("select * from books")
        print("DBDB")
        id = 0
        try:
            id = len(c.fetchall())
            #id = int(list(c.fetchall()[0])[0])
            print(id)
            print("ID")
        except TypeError:
            print("IDNONE")
            pass
        print("----------")
        print(id)
        print(title)
        print(creator)
        print(publisher)
        print(issueDate)
        print(addStackData)
        print(BN)
        print("---------")
        c.execute('insert into books(id,title,creator,publisher,issueDate,addStackDate,BN) values(?,?,?,?,?,?,?)',(id,title,creator,publisher,issueDate,addStackData,BN))
        conn.commit()
        print("COMMIT")
        conn.close()
        
    
    def dbread(self,id=None,key=None,value=None):
        conn = sqlite3.connect("Books.db")
        c = conn.cursor()
        #全聚徳
        if id is None and key is None:
            #NonCALL(ALL)
            print("allSelect")
            c.execute("select * from books")
            print("select GOTO Re")
            return c.fetchall()
        elif key is None:
            #IDCALL
            pass
        elif key and value:
            pass

    def dbremove(self,id):
        conn = sqlite3.connect("Books.db")
        c = conn.cursor()
            
        c.execute("delete from books where id=?",(id,))
        conn.commit()
        conn.close()
        
        

        #c.execute("select id from id where id = ?,")

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
        self.proxies = None
        #------------------------------
        if proxyFlag == True:
            self.proxies = {
            "https":"http://%s:%s@%s:%s" % (self.ID,self.PASS,self.IP,self.PORT),
            "http":"http://%s:%s@%s:%s" % (self.ID,self.PASS,self.IP,self.PORT)
            }
    def connectionChk(self):
        global threadFlag
        global proxyReturn
        try:
            response = None
            print(self.ProxyFlag)
            if self.ProxyFlag == False:
                
                response = requests.get("https://elecbookapi.noko1024.net/api/")
            else:
                response = requests.get("https://elecbookapi.noko1024.net/api/",proxies=self.proxies)
                print(response)


            print(response.text)
            print(response.status_code)
            print(response.reason)

            threadFlag = True
            
            proxyReturn = [True,response.text]
        except:
            #print(response.text)
            #print(response.status_code)
            #print(response.reason)
            threadFlag = True
            try:
                proxyReturn =  [False,response.status_code,response.reason]
            except:
                proxyReturn =  [False,"001","サーバーからのレスポンスを取得できません"]
    #通信成功の可否とHTMLステータスコード,コンテンツを返す。

        return 


    def AllCall(self,query):
        
        URL = "https://elecbookapi.noko1024.net/api/search{Call}"
        URL = URL.format(Call=query)
        print(URL)
        
        response = None
        if self.ProxyFlag is True:
            response = requests.get(URL,proxies=self.proxies)
        else:
            response = requests.get(URL)
        

        response = json.loads(response.text)
        print(response)
        value = response.get("search")
        return value


        
    


    
    #asyncio使いたい→スレッドになりそう。
    #https://note.crohaco.net/2019/python-asyncio/
    
    ##次回以降のアップデートで追加## 
    def ndlCall(self,query):
        maximum ="10"
        URL ="https://iss.ndl.go.jp/api/sru?operation=searchRetrieve&maximumRecords="+maximum+"&query=" +query.encode("utf-8")
        
        response = requests.get(URL,proxies=self.proxies)





    #############################

#プログラム全体の初期化とユーザーへの情報要求
#起動時にパスワード求めてフレーズを基にAESを復号→文字列切り出し＆演算で成功したか確認
def init():
    #StandbyApp()
    #プロキシの要求→(接続の確認)→ファイルの存在確認→設定ファイルの読み込み(or生成)→retunでAPIのインスタンスを返す
    IO = FileIO()
    config,db = IO.existsChk()
    print("DB")
    print(db)
    if db is False:
        IO.dbInit()

    ProxyRequestApp()

    return
    #暗号化機能実装見送り(ソルトの保持に安全性を担保できない)
    if config is False:
        print("configFalse")
        IO.configInit()
        ProxyRequestApp()
        AuthInputApp()
        authDict = {}
        if proxyInstance.ProxyFlag is True:

            authDict.update(ID=proxyInstance.ID,PASS=proxyInstance.PASS,IP=proxyInstance.IP,PORT=proxyInstance.PORT)

        
        

    else:
        print("ConfigTrue")
        auth = IO.configRead(["Proxy"])
        print(auth)
        AuthRequestApp().show()
        print("END")
        
    


#プログラム開始の起点
def main():
    print("PASS")
    MainApp()
    pass

if __name__ == "__main__":
    init()
    #main()

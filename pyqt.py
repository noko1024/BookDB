import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sip

import tkinter

import threading
import winsound


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle('Main')

        buttonThread = QPushButton("Thread",self)
        buttonThread.move = (100,100)

        #buttonPlay = QPushButton("Play",self)
        #buttonPlay.move = (10,20)
        
        #buttonPlay.clicked.connect(self.onClickPlay)
        buttonThread.clicked.connect(self.onClickThread)
        


    def onClickThread(self):
        print("Main_thread_click")
        tks=secondTkinter()
        thread =threading.Thread(target=tks.show)
        thread.setDaemon(True)
        thread.start()
        pass
        thread_show = threading.Thread(target=SecondWindow().show)
        thread_show.setDaemon(True)
        thread_show.start()
        print("thread_start")
    
    def onClickPlay(self):
        print("Main_play_click")
        thread_play = threading.Thread(target=MusicPlay().play)
        thread_play.setDaemon(True)
        thread_play.start()
        print("thread_start")

class MusicPlay():
    
    def play(self):
        path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'kaf.wav')
        winsound.PlaySound(path,winsound.SND_FILENAME)

class secondTkinter():
    def __init__(self):
        thread =threading.Thread(target=self.show)
        thread.setDaemon(True)
        thread.start()
    
    def show(self):
        tk = tkinter.Tk()
        tk.geometry("200x200")
        label=tkinter.Label(tk,text="Hello World")
        label.place(x=100,y=100)
        tkinter.mainloop()
        pass


class SecondWindow(QWidget):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)

        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle('Second')

        button = QPushButton("Click",self)
        
        button.clicked.connect(self.on_click)
        self.show()
    def on_click(self):
        print("success")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

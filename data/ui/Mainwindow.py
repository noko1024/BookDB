# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1131, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 190, 1131, 490))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.BNCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.BNCheckBox.setGeometry(QtCore.QRect(20, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BNCheckBox.setFont(font)
        self.BNCheckBox.setObjectName("BNCheckBox")
        self.inputBN = QtWidgets.QLineEdit(self.centralwidget)
        self.inputBN.setGeometry(QtCore.QRect(130, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        self.inputBN.setFont(font)
        self.inputBN.setText("")
        self.inputBN.setObjectName("inputBN")
        self.titleCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.titleCheckBox.setGeometry(QtCore.QRect(20, 100, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleCheckBox.setFont(font)
        self.titleCheckBox.setObjectName("titleCheckBox")
        self.inputTitle = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTitle.setGeometry(QtCore.QRect(130, 100, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        self.inputTitle.setFont(font)
        self.inputTitle.setText("")
        self.inputTitle.setObjectName("inputTitle")
        self.labelWriter = QtWidgets.QLabel(self.centralwidget)
        self.labelWriter.setGeometry(QtCore.QRect(320, 40, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelWriter.setFont(font)
        self.labelWriter.setObjectName("labelWriter")
        self.inputCreator = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCreator.setGeometry(QtCore.QRect(390, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.inputCreator.setFont(font)
        self.inputCreator.setObjectName("inputCreator")
        self.labelPublisher = QtWidgets.QLabel(self.centralwidget)
        self.labelPublisher.setGeometry(QtCore.QRect(320, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPublisher.setFont(font)
        self.labelPublisher.setObjectName("labelPublisher")
        self.labelIssueDate = QtWidgets.QLabel(self.centralwidget)
        self.labelIssueDate.setGeometry(QtCore.QRect(580, 40, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelIssueDate.setFont(font)
        self.labelIssueDate.setObjectName("labelIssueDate")
        self.labelAddStackData = QtWidgets.QLabel(self.centralwidget)
        self.labelAddStackData.setGeometry(QtCore.QRect(580, 100, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelAddStackData.setFont(font)
        self.labelAddStackData.setObjectName("labelAddStackData")
        self.serchButton = QtWidgets.QPushButton(self.centralwidget)
        self.serchButton.setGeometry(QtCore.QRect(960, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.serchButton.setFont(font)
        self.serchButton.setObjectName("serchButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(960, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(960, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.removeButton.setFont(font)
        self.removeButton.setObjectName("removeButton")
        self.inputPublisher = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPublisher.setGeometry(QtCore.QRect(390, 100, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        self.inputPublisher.setFont(font)
        self.inputPublisher.setText("")
        self.inputPublisher.setObjectName("inputPublisher")
        self.inputIssueDate = QtWidgets.QDateEdit(self.centralwidget)
        self.inputIssueDate.setGeometry(QtCore.QRect(650, 40, 131, 31))
        self.inputIssueDate.setObjectName("inputIssueData")
        self.inputAddStackDate = QtWidgets.QDateEdit(self.centralwidget)
        self.inputAddStackDate.setGeometry(QtCore.QRect(650, 100, 131, 31))
        self.inputAddStackDate.setObjectName("inputAddStackDate")
        self.choiceFanzine = QtWidgets.QRadioButton(self.centralwidget)
        self.choiceFanzine.setGeometry(QtCore.QRect(810, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choiceFanzine.setFont(font)
        self.choiceFanzine.setObjectName("choiceFanzine")
        self.choiceCommercial = QtWidgets.QRadioButton(self.centralwidget)
        self.choiceCommercial.setGeometry(QtCore.QRect(810, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choiceCommercial.setFont(font)
        self.choiceCommercial.setObjectName("choiceCommercial")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        self.serchButton.clicked.connect(self.Search)
        self.addButton.clicked.connect(self.Add)
        self.removeButton.clicked.connect(self.Remove)
        self.BNCheckBox.clicked.connect(lambda:self.CheckBox("BN"))
        self.titleCheckBox.clicked.connect(lambda:self.CheckBox("Title"))
        self.choiceCommercial.clicked.connect(lambda:self.Choice("Isbn"))
        self.choiceFanzine.clicked.connect(lambda:self.Choice("Isdn"))
        self.tableWidget.cellClicked['int','int'].connect(self.DBSelect)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.serchButton.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ISBN/ISDN"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "書名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "著作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "発行者"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "発行日"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "入架日"))
        self.BNCheckBox.setText(_translate("MainWindow", "ISBN/ISDN"))
        self.titleCheckBox.setText(_translate("MainWindow", "書名"))
        self.labelWriter.setText(_translate("MainWindow", "著作者"))
        self.labelPublisher.setText(_translate("MainWindow", "発行者"))
        self.labelIssueDate.setText(_translate("MainWindow", "発行日"))
        self.labelAddStackData.setText(_translate("MainWindow", "入架日"))
        self.serchButton.setText(_translate("MainWindow", "検索"))
        self.addButton.setText(_translate("MainWindow", "登録"))
        self.removeButton.setText(_translate("MainWindow", "削除"))
        self.choiceFanzine.setText(_translate("MainWindow", "同人誌"))
        self.choiceCommercial.setText(_translate("MainWindow", "商業誌"))
        self.actionExit.setText(_translate("MainWindow", "終了"))

    def Search(self):
        print("OK")
        pass
        a = self.inputTitle.te

        

    def Add(self,addList):
        #testCode
        item = "ppppppppppppppppp"
        n = 0
        n+=1
        
        
        #???
        #self.tableWidget.update()
        print("S")
        pass

    def Remove(self):
        print("OK")
        pass

    def CheckBox(self):
        print("OK")
        pass

    def Choice(self):
        print("OK")
        pass

    def DBSelect(self):
        print("OK")
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

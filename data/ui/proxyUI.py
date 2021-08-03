# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proxy.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 228)
        self.ProxyEnableButton = QtWidgets.QRadioButton(Dialog)
        self.ProxyEnableButton.setGeometry(QtCore.QRect(10, 100, 145, 16))
        self.ProxyEnableButton.setObjectName("ProxyEnableButton")
        self.ProxyDisableButton = QtWidgets.QRadioButton(Dialog)
        self.ProxyDisableButton.setGeometry(QtCore.QRect(10, 50, 151, 16))
        self.ProxyDisableButton.setAutoRepeatDelay(300)
        self.ProxyDisableButton.setObjectName("ProxyDisableButton")
        self.OKButton = QtWidgets.QPushButton(Dialog)
        self.OKButton.setGeometry(QtCore.QRect(480, 200, 75, 23))
        self.OKButton.setObjectName("OKButton")
        self.InputIP = QtWidgets.QLineEdit(Dialog)
        self.InputIP.setGeometry(QtCore.QRect(20, 200, 121, 20))
        self.InputIP.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.InputIP.setInputMask("")
        self.InputIP.setText("")
        self.InputIP.setObjectName("InputIP")
        self.InputPort = QtWidgets.QLineEdit(Dialog)
        self.InputPort.setGeometry(QtCore.QRect(170, 200, 121, 20))
        self.InputPort.setText("")
        self.InputPort.setObjectName("InputPort")
        self.InputPassword = QtWidgets.QLineEdit(Dialog)
        self.InputPassword.setGeometry(QtCore.QRect(170, 150, 121, 20))
        self.InputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.InputPassword.setText("")
        self.InputPassword.setObjectName("InputPassword")
        self.InputID = QtWidgets.QLineEdit(Dialog)
        self.InputID.setGeometry(QtCore.QRect(20, 150, 121, 20))
        self.InputID.setText("")
        self.InputID.setObjectName("InputID")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 130, 50, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 130, 50, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 50, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 180, 50, 12))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.OKButton.clicked.connect(self.OKBtnPush)
        self.ProxyDisableButton.clicked.connect(lambda:self.ProxyStatus(False))
        self.ProxyEnableButton.clicked.connect(lambda:self.ProxyStatus(True))
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ProxyEnableButton.setText(_translate("Dialog", "プロキシ認証を使用する。"))
        self.ProxyDisableButton.setText(_translate("Dialog", "プロキシ認証を使用しない"))
        self.OKButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "ログインID"))
        self.label_2.setText(_translate("Dialog", "パスワード"))
        self.label_3.setText(_translate("Dialog", "IPアドレス"))
        self.label_4.setText(_translate("Dialog", "Port番号"))
    
    #override用
    def OKBtnPush(self):
        pass
    def ProxyStatus(self,Flag):
        
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

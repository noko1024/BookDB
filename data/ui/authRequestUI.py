# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AuthRequest.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 228)
        self.OKButton = QtWidgets.QPushButton(Dialog)
        self.OKButton.setGeometry(QtCore.QRect(480, 200, 75, 23))
        self.OKButton.setObjectName("OKButton")
        self.InputPassword = QtWidgets.QLineEdit(Dialog)
        self.InputPassword.setGeometry(QtCore.QRect(60, 140, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InputPassword.setFont(font)
        self.InputPassword.setText("")
        self.InputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.InputPassword.setObjectName("InputPassword")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.OKButton.clicked.connect(self.OKBtnPush)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def OKBtnPush(self):
        pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.OKButton.setText(_translate("Dialog", "OK"))
        self.label_2.setText(_translate("Dialog", "パスワードを入力してください"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

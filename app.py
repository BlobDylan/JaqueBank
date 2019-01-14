import handlePassword
import getPassword
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from dia import Ui_Dialog2
#from login_func import *


class Ui_MainWindow(object):
    def openDialog(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        #id = login(self.lineEdit.text(),self.lineEdit_2.text())
        #t = get_website_names(id)
        x = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setMinimumSize(QtCore.QSize(480, 640))
        MainWindow.setMaximumSize(QtCore.QSize(480, 640))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 30, 381, 91))
        self.textBrowser.setObjectName("textBrowser")

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 190, 461, 401))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: handlePassword.copy_to_clipboard(x))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)

        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 461, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openDialog)

        self.horizontalLayout.addWidget(self.pushButton)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 170, 461, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        #id = login(self.lineEdit.text(),self.lineEdit_2.text())
        #t = get_website_names(id)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600; color:#bf0e01;\">Jaque</span><span style=\" font-size:48pt; font-weight:600; color:#a6a6a6;\">Bank</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Copy"))
        self.pushButton_2.setText(_translate("MainWindow", "example"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))

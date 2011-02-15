#!/usr/bin/env python

###
###
### Author : Hiemanshu Sharma <mail@theindiangeek.in>
###
### komedia.py
###
### App to read online comics
###
###
### Config is stored in ~/.komedia
###

from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
import sys
from lxml import html
import os
from urllib2 import urlopen
import ConfigParser
import random
#import getLatest
import close 

__author__ = "Hiemanshu Sharma <mail@theindiangeek.in>"
version = 0.1

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(959, 562)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 20, 161, 491))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textEdit_2 = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout.addWidget(self.textEdit_2)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 771, 491))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.webView = QtWebKit.QWebView(self.verticalLayoutWidget_2)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_2.addWidget(self.webView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuConfig = QtGui.QMenu(self.menubar)
        self.menuConfig.setObjectName(_fromUtf8("menuConfig"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Comics = QtGui.QAction(MainWindow)
        self.actionSave_Comics.setObjectName(_fromUtf8("actionSave_Comics"))
        self.actionExport_Config = QtGui.QAction(MainWindow)
        self.actionExport_Config.setObjectName(_fromUtf8("actionExport_Config"))
        self.actionImport_Config = QtGui.QAction(MainWindow)
        self.actionImport_Config.setObjectName(_fromUtf8("actionImport_Config"))
        self.actionVerify_Config = QtGui.QAction(MainWindow)
        self.actionVerify_Config.setObjectName(_fromUtf8("actionVerify_Config"))
        self.actionCreating_Config = QtGui.QAction(MainWindow)
        self.actionCreating_Config.setObjectName(_fromUtf8("actionCreating_Config"))
        self.actionAbout_Komedia = QtGui.QAction(MainWindow)
        self.actionAbout_Komedia.setObjectName(_fromUtf8("actionAbout_Komedia"))
        self.menuFile.addAction(self.actionSave_Comics)
        self.menuConfig.addAction(self.actionExport_Config)
        self.menuConfig.addAction(self.actionImport_Config)
        self.menuConfig.addAction(self.actionVerify_Config)
        self.menuHelp.addAction(self.actionCreating_Config)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Komedia)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.textEdit.setText("XKCD is a webcomic of Romance, Math, Sarcasm and Language")

        config = ConfigParser.ConfigParser()
        config.read(os.path.expanduser("~/.komedia"))
        if not config.has_section("xkcd"):
            config.add_section("xkcd")
#        self.comicid = getLatest.comicid()
#        config.set("xkcd", "comicid", self.comicid)
     
        self.comicid = int(config.get("xkcd", "comicid", raw=True))
        self.latest = int(config.get("xkcd", "comicid", raw=True))
#        MainWindow.xkcd()

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), MainWindow.prevComic)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), MainWindow.nextComic)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), MainWindow.randComic)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Komedia", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Alt Text", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "About Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Link to Comic", None, QtGui.QApplication.UnicodeUTF8))
#        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Date of Publishing", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Previous Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Next Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Random Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfig.setTitle(QtGui.QApplication.translate("MainWindow", "Config", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Comics.setText(QtGui.QApplication.translate("MainWindow", "Save Comics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_Config.setText(QtGui.QApplication.translate("MainWindow", "Export Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Config.setText(QtGui.QApplication.translate("MainWindow", "Import Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVerify_Config.setText(QtGui.QApplication.translate("MainWindow", "Verify Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreating_Config.setText(QtGui.QApplication.translate("MainWindow", "Creating Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Komedia.setText(QtGui.QApplication.translate("MainWindow", "About Komedia", None, QtGui.QApplication.UnicodeUTF8))
        
class Komedia(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def xkcd(self):
        self.page_url = "http://xkcd.com/%s/" % self.ui.comicid
        page = html.parse(urlopen(self.page_url)).getroot()
       
        image_url = page.cssselect("div.s > img")[0].attrib['src']
        alt = page.cssselect("div.s img")[1].attrib['title']
       
        self.ui.textEdit_2.setText(alt)
        self.ui.webView.setUrl(QtCore.QUrl(_fromUtf8(image_url)))
        self.ui.lineEdit.setText(self.page_url)

    def prevComic(self):
        self.ui.comicid = self.ui.comicid - 1
        self.xkcd()

    def nextComic(self):
        self.ui.comicid = self.ui.comicid + 1
#        if self.ui.comicid <= int(self.ui.latest):
#            self.xkcd()
#        else:
        dlg = QtGui.QDialog()
        dialog = close.Ui_Dialog()
        dialog.setupUi(dlg)
        dlg.exec_()
            
    def randComic(self):
        self.ui.comicid = random.randrange(1,self.ui.latest+1,1)
        self.xkcd()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Komedia()
    myapp.show()
    sys.exit(app.exec_())

#!/usr/bin/env python

import gui
from PyQt4 import QtCore, QtGui
import sys
import os
from xkcd import XKCD
from dilbert import Dilbert

class Komedia(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        for i in ['Dilbert', 'XKCD']:
            self.ui.comboBox.addItem(i)
        if not os.path.exists(os.path.expanduser('~/.komedia')):
            os.mkdir(os.path.expanduser('~/.komedia'))
#        self.dilbert = Dilbert()
#        self.xkcd = XKCD()
#        self.comicData = Dilbert.comic(self.dilbert)
#        self.loadComic()
#        self.comic = 'Dilbert'

    def changeComic(self, text):
        text = str(text)
        if text == 'Dilbert':
            self.comicData = Dilbert.comic(self.dilbert)
            self.comic = 'Dilbert'
            self.loadComic()
        else:
            if text == 'XKCD':
                self.comicData = XKCD.comic(self.xkcd)
                self.loadComic()
                self.comic = 'XKCD'
    
    def loadComic(self):
        self.ui.textEdit.setText(self.comicData[0])
        self.ui.textEdit_2.setText(self.comicData[1])
        self.ui.webView.setUrl(QtCore.QUrl(self.comicData[2]))
        self.ui.lineEdit.setText(self.comicData[3])

    def nextComic(self):
        if self.comic == 'Dilbert':
           self.comicData = Dilbert.nextComic(self.dilbert)
        else:
           if self.comic == 'XKCD':
               self.comicData = XKCD.nextComic(self.xkcd)
        if self.comicData != None:
            self.loadComic()

    def prevComic(self):
        if self.comic == 'Dilbert':
            self.comicData = Dilbert.prevComic(self.dilbert)
        else:
            if self.comic == 'XKCD':
                self.comicData = XKCD.prevComic(self.xkcd)
        if self.comicData != None:
            self.loadComic()

    def randComic(self):
        if self.comic == 'Dilbert':
            self.comicData = Dilbert.randComic(self.dilbert)
        else:
            if self.comic == 'XKCD':
                self.comciData = XKCD.randComic(self.xkcd)
        if self.comicData != None:
            self.loadComic()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Komedia()
    myapp.show()
    sys.exit(app.exec_())

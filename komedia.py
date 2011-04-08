#!/usr/bin/env python

import gui
from PyQt4 import QtCore, QtGui
import sys
import os
from xkcd import XKCD

class Komedia(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem('XKCD')
        if not os.path.exists(os.path.expanduser('~/.komedia')):
            os.mkdir(os.path.expanduser('~/.komedia'))
        self.xkcd = XKCD()
        self.comicData = XKCD.comic(self.xkcd)
        self.changeComic()

    def changeComic(self):
        self.ui.textEdit.setText(self.comicData[0])
        self.ui.textEdit_2.setText(self.comicData[1])
        self.ui.webView.setUrl(QtCore.QUrl(self.comicData[2]))
        self.ui.lineEdit.setText(self.comicData[3])

    def nextComic(self):
        self.comicData = XKCD.nextComic(self.xkcd)
        self.changeComic()

    def prevComic(self):
        self.comicData = XKCD.prevComic(self.xkcd)
        self.changeComic()

    def randComic(self):
        print 'Blah Blah Blah'

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Komedia()
    myapp.show()
    sys.exit(app.exec_())

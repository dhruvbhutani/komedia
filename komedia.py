#!/usr/bin/env python

import gui
from PyQt4 import QtCore, QtGui
import sys


class Komedia(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
	QtGui.QWidget.__init__(self, parent)
	self.ui = gui.Ui_MainWindow()
	self.ui.setupUi(self)

    def changeComic(self):
        print 'Insert Comic viewing code here'

    def nextComic(self):
        print 'show next comic'

    def prevComic(self):
        print 'show previous comic'

    def randComic(self):
        print 'display a random dated comic'

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Komedia()
    myapp.show()
    sys.exit(app.exec_())

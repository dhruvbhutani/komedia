#!/usr/bin/env python

###
###
### Author : Hiemanshu Sharma <mail@theindiangeek.in>
###
### xkcd.py
###
### XKCD Plugin for komedia
###
###
### Config is stored in ~/.komedia
###

import sys
from lxml import html
import os
from urllib2 import urlopen
import ConfigParser
import random
import getLatest
import close 

class XKCD(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if not os.path.exists(os.path.expanduser('~/.komedia')):
            os.mkdir(os.path.expanduser('~/.komedia'))
        if not os.path.exists(os.path.expanduser('~/.komedia/xkcd')):
            os.mkdir(os.path.expanduser('~/.komedia/xkcd'))
        
    def xkcd(self):
	self.ui.textEdit.setText("XKCD is a webcomic of Romance, Math, Sarcasm and Language")
        image_path = "~/.komedia/xkcd/%s.png" % self.ui.comicid
        self.config1 = ConfigParser.ConfigParser()
        if not os.path.exists(os.path.expanduser(image_path)):
            self.page_url = "http://xkcd.com/%s/" % self.ui.comicid
            page = html.parse(urlopen(self.page_url)).getroot()
            image_url = page.cssselect("div.s > img")[0].attrib['src']
            alt = page.cssselect("div.s img")[1].attrib['title']
            image = urlopen(image_url)
            op = open(os.path.expanduser(image_path), 'wb')
            op.write(image.read())
            op.close()
            if not self.config1.read(os.path.expanduser("~/.komedia/xkcd/alts")):
                self.config1.add_section("xkcd")
                self.config1.set("xkcd", str(self.ui.comicid), alt)
                self.config1.write(open(os.path.expanduser('~/.komedia/xkcd/alts'), 'w'))
            else:
                self.config1.read(os.path.expanduser('~/.komedia/xkcd/alts'))
                self.config1.set("xkcd", str(self.ui.comicid), alt)
                self.config1.write(open(os.path.expanduser('~/.komedia/xkcd/alts'), 'w'))
        else:
            self.config1.read(os.path.expanduser('~/.komedia/xkcd/alts'))
            alt = self.config1.get("xkcd", str(self.ui.comicid))
            self.page_url = "http://xkcd.com/%s/" % self.ui.comicid
        
        self.ui.textEdit_2.setText(alt)
        imagepath = "file://%s" % (os.path.expanduser(image_path))
        self.ui.webView.setUrl(QtCore.QUrl(_fromUtf8(imagepath)))
        self.ui.lineEdit.setText(self.page_url)

    def prevComic(self):
        self.ui.comicid = self.ui.comicid - 1
        self.xkcd()

    def nextComic(self):
        self.ui.comicid = self.ui.comicid + 1
        if self.ui.comicid <= int(self.ui.latest):
            self.xkcd()
        else:
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

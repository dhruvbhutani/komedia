#!/usr/bin/env python

###
###
### garfield.py
###
### Gets links from dilbert.com for comics, includes every comic ever written
###
###
###

from PyQt4 import QtCore, QtGui
from lxml import html
from urllib2 import urlopen
import random
import first, last
import os
from datetime import date, timedelta

class Garfield():
    
    def __init__(self):
        if not os.path.exists(os.path.expanduser('~/.komedia/garfield')):
            os.mkdir(os.path.expanduser('~/.komedia/garfield'))
        self.comicid = '%s/%s/%s' %(date.today().year, date.today().month, date.today().day)
        self.comicStart = 
        self.comicEnd = self.comicid

    def comic(self):
        self.obj = ['Garfield is a comic about ...']
        self.obj.append('No Alt text available for this comic')
        image_path = '~/.komedia/garfield/%s.png' %self.comicid
        if not os.path.exists(os.path.expanduser(image_path)):
            self.page_url = 'http://gocomics.com/garfield/%s' %self.comicid
            page = html.parse(urlopen(self.page_url)).getroot()
            image_link = page.cssselect('').attrib.['src']
            image_url = 'http://gocomics.com/%s' %image_link
            image = urlopen(image_url)
            op = open(os.path.expanduser(image_path))
            op.write(image.read())
            op.close
        imagepath = 'file://%s' %(os.path.expanduser(image_path))
        self.obj.append(imagepath)
        page_url = 'http://gocomics.com/garfield/%s' %str(self.comicid)
        self.obj.append(page_url)
        return self.obj

    def prevComic(self):
        if self.comicid == self.comicStart:
            dlg = QtGui.QDialog()
            dialog = fisrt.Ui_Dialog()
            dialog.setupUi(dlg)
            dlg.exec_()
        else:
            self.comicid -= timedelta(days=1)
            return self.comic()

    def nextComic(self):
        if self.comicid == self.comicEnd:
            dlg = QtGui.QDialog()
            dialog = last.Ui_Dialog()
            dialog.setupUi(dlg)
            dlg.exec_()
        else:
            self.comicid += timedelta(days=1)
            return self.comic()

    def randComic(self):
        delta = self.comicEnd - self.comicStart
        rand = str(delta)
        rand1 = rand[0:4]
        rand2 = int(rand1)
        dateDiff = int(float(random.random()) * rand2)
        self.comicid = self.comicStart + timedelta(days = dateDiff)
        return self.comic()

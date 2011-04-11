#!/usr/bin/env python

###
###
### dilbert.py
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


class Dilbert():

    def __init__(self):
        if not os.path.exists(os.path.expanduser('~/.komedia/dilbert')):
            os.mkdir(os.path.expanduser('~/.komedia/dilbert'))
        self.comicid = date.today()

    def comic(self):
        self.obj = ['Dilbert is a comic about ...']
        self.obj.append('No Alt text available for this comic')
        image_path = '~/.komedia/dilbert/%s.gif' %self.comicid
        if not os.path.exists(os.path.expanduser(image_path)):
            self.page_url = 'http://dilbert.com/fast/%s' %self.comicid
            page = html.parse(urlopen(self.page_url)).getroot()
            image_link = page.cssselect('div.LGT_SiteWrapper > img')[0].attrib['src']
            image_url = 'http://dilbert.com%s' %image_link
            image = urlopen(image_url)
            op = open(os.path.expanduser(image_path), 'wb')
            op.write (image.read())
            op.close
        imagepath = 'file://%s' %(os.path.expanduser(image_path))
        self.obj.append(imagepath)
        page_url = 'http://dilbert.com/strips/%s' %str(self.comicid)
        self.obj.append(page_url)
        return self.obj

    def prevComic(self):
        if self.comicid == date(1989, 4, 16):
            dlg = QtGui.QDialog()
            dialog = last.Ui_Dialog()
            dialog.setupUi(dlg)
            dlg.exec_()
        else:
            self.comicid -= timedelta(days=1)
        return self.comic()

    def nextComic(self):
        if self.comicid == date.today():
            dlg = QtGui.QDialog()
            dialog = last.Ui_Dialog()
            dialog.setupUi(dlg)
            dlg.exec_()
        else:
            self.comicid += timedelta(days=1)
            return self.comic()

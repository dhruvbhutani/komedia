###
###
### Author : Hiemanshu Sharma <mail@theindiangeek.in>
###
### xkcd.py
###
### XKCD Plugin for komedia

import sys
from lxml import html
import os
from urllib2 import urlopen
import ConfigParser
import random
import close

class XKCD():

    def __init__(self):
        if not os.path.exists(os.path.expanduser('~/.komedia/xkcd')):
            os.mkdir(os.path.expanduser('~/.komedia/xkcd'))
        self.comicid = 883

    def comic(self):
        self.obj = ['XKCD is a webcomic of Romance, Math, Sarcasm and Language']
        image_path = '~/.komedia/xkcd/%s.png' % self.comicid
        self.config = ConfigParser.ConfigParser()
        if not os.path.exists(os.path.expanduser(image_path)):
            self.page_url = 'http://xkcd.com/%s/' %self.comicid
            page = html.parse(urlopen(self.page_url)).getroot()
            image_url = page.cssselect('div.s img')[1].attrib['src']
            alt = page.cssselect('div.s img')[1].attrib['title']
            image = urlopen(image_url)
            op = open(os.path.expanduser(image_path), 'wb')
            op.write(image.read())
            op.close
            if not os.path.exists(os.path.expanduser('~/.komedia/xkcd/alts')):
                self.config.add_section('xkcd')
                self.config.set('xkcd', str(self.comicid), alt)
                self.config.write(open(os.path.expanduser('~/.komedia/xkcd/alts'), 'w'))
            else:
                self.config.read(os.path.expanduser('~/.komedia/xkcd/alts'))
                self.config.set('xkcd', str(self.comicid), alt)
                self.config.write(open(os.path.expanduser('~/.komedia/xkcd/alts'), 'w'))
        else:
            self.config.read(os.path.expanduser('~/.komedia/xkcd/alts'))
            alt = self.config.get('xkcd', str(self.comicid))
        
        self.obj.append(alt)
        imagepath = 'file://%s' % (os.path.expanduser(image_path))
        self.obj.append(imagepath)
        page_url = 'http://xkcd.com/%s' %self.comicid
        self.obj.append(page_url)
        return self.obj

    def prevComic(self):
        self.comicid -= 1
        return self.comic()

    def nextComic(self):
        self.comicid += 1
        return self.comic()


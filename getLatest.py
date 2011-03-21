#!/usr/bin/env python

###
###
### Author : Hiemanshu Sharma <mail@theindiangeek.in>
###
### getLatest.py
###
### Gets the Comic ID of the latest comic on xkcd.com
### 
###

from lxml import html
from urllib2 import urlopen

def comicid(self):
    page = html.parse(urlopen("http://xkcd.com")).getroot()
    h = page.cssselect("h3")[0].text
    latest = h[46:-1]
    return latest

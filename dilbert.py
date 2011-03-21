#!/usr/bin/env python

###
###
### dilbert.py
###
### Gets links from dilbert.com for comics, includes every comic ever written
###
###
###

from lxml import html
from urllib2 import urlopen
import random

def genrand():
    year = random.randrange(1989,2012,1)
    month = random.randrange(1,13,1)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
	day = random.randrange(1,32,1)
    else:
	if month == 4 or month == 6 or month == 9 or month == 11:
	    day = random.randrange(1,31,1)
	else:
	    if year % 4 == 0:
		day = random.randrange(1,30,1)
	    else:
		day = random.randrange(1,29,1)
    date = "%s-%s-%s" %(year, month, day)
    return date

def getlink(date):
    page_url = "http://www.dilbert.com/strips/%s/" %date
    page = html.parse(urlopen(page_url)).getroot()
    image_link = page.cssselect("div.STR_Container > input")[0].attrib['value']
    image_url = "http://dilbert.com%s" %image_link
    return image_url
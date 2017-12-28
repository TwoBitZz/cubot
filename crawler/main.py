# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-
#!/usr/bin/python

import time
import datetime
import mysql.connector as mysql
# database connection
db = mysql.connect(user="root", password="", database="cubot")
# create a cursor for the select
cur = db.cursor()

import BeautifulSoup as soup
import urllib2
from urllib2 import urlopen as ureq
print('Trying to load notifications...')
uocnot = 'http://www.universityofcalicut.info/index2.php?option=com_content&task=view&id=744'
uocwebclient = ureq(uocnot)
print('[Done]')
print('Trying to load timetable')
uoctimetable = 'http://www.universityofcalicut.info/index2.php?option=com_content&task=view&id=745'
soupnot = uocnotdata = ureq(uocnot).read()
print('[Done]')
uocwebclient.close()
print(uocnotdata)
type(uocnotdata)
tds = soupnot.find_all('td')
for t in tds:
    names = t.contents[0]
    docLink = link.get('href')
print(names)
#cur.execute("INSERT INTO cubot.user(chatid,name) VALUES (%s,%s)", (chat_id, username))
# db.commit()

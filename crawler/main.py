# -*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import unicode_literals
import time
from datetime import datetime
import mysql.connector as mysql
import bs4
from bs4 import BeautifulSoup
from unidecode import unidecode
import urllib2
import requests
from urllib2 import urlopen as ureq

# database connection
db = mysql.connect(user="root", password="", database="cubot")
cur = db.cursor()

notificationdocs = []
notifications = []
print('Trying to load notifications...')
uocnot = 'http://www.universityofcalicut.info/index2.php?option=com_content&task=view&id=744'
r = requests.get(uocnot)
print('Trying to load timetable')
uoctimetable = 'http://www.universityofcalicut.info/index2.php?option=com_content&task=view&id=745'
print('[Done]')
# html_doc contains webpage
page_text = unidecode(r.text)
page_text = r.text.encode('ascii', 'ignore')
page_soupy = BeautifulSoup(page_text, 'html.parser')
print('Page title says : ' + page_soupy.title.string)
page_soupy.find_all('a')
for link in page_soupy.findAll('a'):
    # got links to pdfs
    print('found link ' + link.get('href'))
    notificationdocs.append(link.get('href'))
    temp = u'null'
    notifications.append(link.string)
    try:
        temp = link.string
        print temp
    except:
        print 'fixing unicode error'
        temp = temp.encode('latin_1')
        print temp
# add links and text to database from those arrays
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
i = 0
for items in notifications:
    doclink = notificationdocs[i]
    i = i + 1
    try:
        text = items
        cur.execute("INSERT IGNORE INTO cubot.updates (date,text,type,link) VALUES (%s,%s,%s,%s)", (str(
            timestamp), text, 'Notification', str(doclink)))
        db.commit()
    except:
        text = u'sample'
        text = items.encode('latin_1')
        text.strip()
        cur.execute("INSERT IGNORE INTO cubot.updates (date,text,type,link) VALUES (%s,%s,%s,%s)", (str(
            timestamp), text, 'Notification', str(doclink)))
        db.commit()


# close the cursor
cur.close()
# close the connection
db.close()

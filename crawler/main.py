# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import unicode_literals
import time
import datetime
import mysql.connector as mysql
# database connection
db = mysql.connect(user="root", password="", database="cubot")
# create a cursor for the select
cur = db.cursor()
from bs4 import BeautifulSoup
import urllib2
import requests
from urllib2 import urlopen as ureq
print('Trying to load notifications...')
uocnot = 'http://www.universityofcalicut.info/index2.php?option=com_content&task=view&id=744'
r = requests.get(uocnot)
print('Trying to load timetable')
uoctimetable = 'http://www.universityofcalicut.info/index2.php?option=com_content&task=view&id=745'
soupnot = html_doc = ureq(uocnot).read()
print('[Done]')
# html_doc contains webpage
soup = BeautifulSoup(html_doc, 'html.parser')
page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
page_soupy = BeautifulSoup(page_text, 'html.parser')
tds = page_soupy.find_all('td')
print('Page title says : ' + page_soupy.title.string)
page_soupy.find_all('a')
for link in page_soupy.findAll('a'):
    print('found link ' + link.get('href'))
    temp = link.find('a').text()
    # contains links to pdfs
# print(page_soupy.get_text())
#cur.execute("INSERT INTO cubot.user(chatid,name) VALUES (%s,%s)", (chat_id, username))
# db.commit()

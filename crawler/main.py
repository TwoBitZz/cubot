# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-
#!/usr/bin/python

import time
import datetime
import mysql.connector as mysql
# database connection
db = mysqldb.connect(user="root", password="", database="cubot")
# create a cursor for the select
cur = db.cursor()

import BeautifulSoup as soup
from urllib2 import urlopen as ureq
uocnot = 'http://www.universityofcalicut.info/index2.php?option=com_content&task=view&id=744'
uocwebclient = ureq(uocnot)
uoctimetable = 'http://www.universityofcalicut.info/index2.php?option=com_content&task=view&id=745'
#cur.execute("INSERT INTO cubot.user(chatid,name) VALUES (%s,%s)", (chat_id, username))
# db.commit()

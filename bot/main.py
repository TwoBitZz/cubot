# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-
#!/usr/bin/python

import os  # do some os function
import sys  # ^^^^
import time  # purpose of random generating
import json  # reading json files or objects
import random  # rantom number generating
import datetime  # -----
import telepot  # handle msgs
import wget  # downloading some files
import wave  # reading wave files
import speech_recognition as sr  # purpose is converting voice to text
import urllib  # accessing some urls
from subprocess import call  # do some os commands
from random import randint  # random integer generations
from telepot.loop import MessageLoop  # handle recieved msg and sent msg
import mysql.connector as mysqldb  # connecing program to mysqldb
import nltk  # noun splitter
nltk.download('punkt')  # to set auto download
nltk.download('averaged_perceptron_tagger')
# sent to reply, keyboard
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, RegexHandler, ConversationHandler)

# connecing to db
db = mysqldb.connect(user="root", password="", database="cubot")
# create a cursor for the select
cur = db.cursor()

# voice convertion


def audiotowav(fpath, fullpath, chat_id, first_name, last_name, username, date, time):

    # convert .ogg to .wave
    call(["ffmpeg", "-i", fullpath, "/tmp/cubot/" + fpath + ".wav"])
    os.remove(fullpath)

    # convert .wave to .txt
    AUDIO_FILE = "/tmp/cubot/" + fpath + ".wav"
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    try:
        stt = r.recognize_google(audio)
        command = text(stt, chat_id, first_name,
                       last_name, username, date, time)
        return(command)
    except sr.UnknownValueError:
        stt = "CU_Bot could not understand audio"
        return(stt)
    except sr.RequestError as e:
        stt = "Could not request results from CU_Bot service. sorry for the interruption."
        # print stt
        return(stt)


def voice(fid, chat_id, first_name, last_name, username, date, time):
    # request for file id...
    url = 'https://api.telegram.org/bot351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA/getFile?file_id=' + fid
    wget.download(url, '/tmp/temp.html')

    # request for file path
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    data = data['result']

    # take a file path

    if 'file_path' in data:
        fpath = data['file_path']

    fpath.encode('latin_1')
    fullpath = '/tmp/cubot/' + fpath + '.ogg'
    print ('file saved in ' + fullpath)

    # directory make...
    dir = os.path.dirname('/tmp/cubot/voice/')
    if not os.path.exists(dir):
        os.makedirs(dir)

    # download voice
    url1 = 'https://api.telegram.org/file/bot351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA/' + fpath
    wget.download(url1, fullpath)
    print 'sucessfully downloaded'
    reply = audiotowav(fpath, fullpath, chat_id,
                       first_name, last_name, username)
    return(reply)


def audio(fid, chat_id, first_name, last_name, username, date, time):
    # request for file id...
    url = 'https://api.telegram.org/bot351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA/getFile?file_id=' + fid
    wget.download(url, '/tmp/temp.html')

    # request for file path
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    data = data['result']

    # take a file path
    if 'file_path' in data:
        fpath = data['file_path']

    fpath.encode('latin_1')
    fullpath = '/tmp/cubot/' + fpath
    print ('file saved in ' + fullpath)

    # directory make...
    dir = os.path.dirname('/tmp/cubot/music/')
    if not os.path.exists(dir):
        os.makedirs(dir)

    # download voice
    url1 = 'https://api.telegram.org/file/bot351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA/' + fpath
    wget.download(url1, fullpath)
    print 'sucessfully downloaded'
    reply = audiotowav(fpath, fullpath, chat_id,
                       first_name, last_name, username, date, time)
    return(reply)


# text msg checking


def text(command, chat_id, first_name, last_name, username, date, time):
    command = command.lower()
    command = command.encode('utf-8')
    positive = ['fine', 'good', 'k', 'ok',
                'alright', 'cool', 'nice', 's', 'yes']

    greetings = ['hi', 'hai', 'hloii', 'hey', 'hello',
                 'howdy', 'hi', 'oi', 'hoy', 'hi', 'hai', 'hey', 'hello',
                 'howdy', 'oi', 'hoy', 'ai', 'hei', 'hloo', 'hii',
                              'kooi', 'hallo', 'hlo', 'hy', '👋']
    reply_greetings = ['howdy', 'How are you',
                       'Hi', 'Hey', 'Howdy', 'Hello', '👋']

    msg1 = ['do you know me', 'you know me', 'do you know my name', 'know me',
            'what is my name', 'who am i', 'my name']
    reply_msg1 = ['howdy ', 'How are you ',
                  'Hi ', 'Hey ', 'Howdy ', 'Hello ', 'You are my Friend ', '👋 ']

    msg2 = ['❤️', 'i love you', 'love you', 'love u', 'i love u']
    reply_msg2 = ['😳 No.... ', 'Let me be your friend  🤝 ',
                  'Love you to... ', 'I am your personal assistant. I cant love you ',
                  'What the hell are you talking about ? ', '❤️ ', 'You are my Friend ',
                  'sorry ! i am not interested']

    msg3 = ['made ❤️ with', 'who developed you', 'who developed you?',
            'who developed you ?', 'developers',
            'makers', 'who made you', 'developer team']

    msg4 = ['how are you', 'how r u ?', 'how is life', 'how do you do',
            'how are u', 'how r u', 'how do u do',
            'how are you ?', 'how r you ?', 'how do you do ?',
            'how are u ?', 'how is life ?', 'how do u do ?',
            'how are you?', 'how do you do?',
            'how are u?', 'how is life?', 'how do u do?']

    if command in greetings:
        idx = randint(0, reply_greetings.__len__() - 1)
        print 'selecting index ' + str(idx)
        greet = reply_greetings[idx]

    elif command in msg1:
        idx = randint(0, reply_msg1.__len__() - 1)
        print 'selecting index ' + str(idx)
        greet = reply_msg1[idx]
        greet = greet + first_name

    elif command in positive:
        idx = randint(0, reply_msg1.__len__() - 1)
        print 'selecting index ' + str(idx)
        greet = positive[idx]

    elif command == '/start':
        greet = 'Hello ' + first_name
        cur.execute("INSERT IGNORE INTO cubot.user(chatid,first_name,last_name,username,date,time) VALUES (%s,%s,%s,%s,%s,%s)",
                    (chat_id, first_name, last_name, username, date, time))
        db.commit()

    elif command in msg2:
        idx = randint(0, reply_msg2.__len__() - 1)
        print 'selecting index ' + str(idx)
        greet = reply_msg2[idx]

    elif command == 'what can you do':
        greet = 'I can help you to access notifications and circulars from the website of Calicut University \n \nBelieve it or not i can download your hallticket/results for you 😁'

    elif command == 'what is your name':
        greet = 'I am Calicut University bot \n \n My nick name is CU_Bot 😁'

    elif command in msg3:
        greet = 'Well, that is a good thing to ask \n \n Team Four_BitZz developed me as their final year project, They are awesome !'
    elif command in msg4:
        greet = 'I am Fine. \n\n What about you'
    else:
        # msg splitting
        tokens = nltk.word_tokenize(command)
        tokens = nltk.pos_tag(tokens)
        tokens = [word for word, pos in tokens
                  if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
        tokens = [x.lower() for x in tokens]
        #tokens = str(tokens)
        l = tokens.__len__() - 1
        print l
        print 'message : ' + str(tokens)
        greet = 'that was Confusing \n\n Sorry! iam still a learning kid! '
        print 'Advanced request from user'
        print 'calling handler...'
    return(greet)


# main function


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #chat_id = msg['chat']['id']
    datim = msg['date']
    date = datetime.datetime.fromtimestamp(
        int(datim)).strftime('%Y-%m-%d')
    time = datetime.datetime.fromtimestamp(
        int(datim)).strftime('%H:%M:%S')
    try:
        username = msg['from']['username']
    except:
        username = 'not set'
    try:
        first_name = msg['from']['first_name']
    except:
        first_name = 'not set'
    try:
        last_name = msg['from']['last_name']
    except:
        last_name = 'not set'

    first_name.encode('latin_1')
    last_name.encode('latin_1')
    print 'chatid      : %s' % chat_id
    print 'first_name  : %s' % first_name + ' last_name : ' + last_name
    print 'Got type    : %s' % content_type
    print 'send date   : %s' % date
    print 'send time   : %s' % time
    #---------------------------------------
    if content_type == 'text':
        command = msg['text']
        command = text(command, chat_id, first_name,
                       last_name, username, date, time)
        bot.sendMessage(chat_id, command)

    elif content_type == 'sticker':
        command = msg['sticker']
        bot.sendMessage(chat_id, 'Aww! looks good')

    elif content_type == 'document':
        command = msg['document']
        bot.sendMessage(chat_id, 'I cant read it right now')

    # voice recoganizing...
    elif content_type == 'voice':
        command = msg['voice']
        # take a file id
        if 'file_id' in command:
            fid = command['file_id']

        reply = voice(fid, chat_id, first_name,
                      last_name, username, date, time)
        print 'voice text is : ' + reply
        bot.sendMessage(chat_id, reply)

    elif content_type == 'location':
        command = msg['location']
        bot.sendMessage(chat_id, 'what are you doing there ?')

    elif content_type == 'photo':
        bot.getFile()
        command = msg['photo']
        bot.sendMessage(chat_id, 'This is awesome 😘')

    elif content_type == 'video_note':
        command = msg['video_note']
        bot.sendMessage(chat_id, 'you are awesome 😘')

    elif content_type == 'audio':
        command = msg['audio']
        # take a file id
        if 'file_id' in command:
            fid = command['file_id']
        reply = audio(fid, chat_id, first_name,
                      last_name, username, date, time)
        bot.sendMessage(chat_id, reply)

    elif content_type == 'video':
        command = msg['video']
        bot.sendMessage(chat_id, 'Iam not able to understand this video 😊')

    else:
        command = msg['document']
        bot.sendMessage(
            chat_id, 'Iam not able to understand this file!')

    print 'Got command : %s' % command


bot = telepot.Bot('351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA')
MessageLoop(bot, handle).run_as_thread()


print 'I am listening ...'

while 1:
    time.sleep(10)
# close the curso
cur.close()
# close the connection
db.close()

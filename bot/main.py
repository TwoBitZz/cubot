# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import sys
import time
import json
import random
import datetime
import telepot
import wget
import wave
import speech_recognition as sr
from subprocess import call
import urllib
from random import randint
from telepot.loop import MessageLoop
import mysql.connector as mysqldb
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import requests
db = mysqldb.connect(user="root", password="", database="cubot")
# create a cursor for the select
cur = db.cursor()


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
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
    print 'first_name : %s' % first_name + ' last_name : ' + last_name
    print 'Got type: %s' % content_type

    if content_type == 'text':
        command = msg['text']
        command = command.lower()
        command = command.encode('utf-8')

        positive = ['fine', 'good', 'k', 'ok',
                    'alright', 'cool', 'nice', 's', 'yes']

        greetings = ['hi', 'hai', 'hey', 'hello',
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

        msg4 = ['how are you', 'how is life', 'how do you do',
                'how are u', 'how r u', 'how do u do',
                'how are you ?', 'how r you ?', 'how do you do ?',
                'how are u ?', 'how is life ?', 'how do u do ?',
                'how are you?', 'how do you do?',
                'how are u?', 'how is life?', 'how do u do?']

        if command in greetings:
            idx = randint(0, reply_greetings.__len__() - 1)
            print 'selecting index ' + str(idx)
            greet = reply_greetings[idx]
            bot.sendMessage(chat_id, greet)

        elif command in msg1:
            idx = randint(0, reply_msg1.__len__() - 1)
            print 'selecting index ' + str(idx)
            greet = reply_msg1[idx]
            bot.sendMessage(chat_id, greet + first_name)

        elif command in positive:
            idx = randint(0, reply_msg1.__len__() - 1)
            print 'selecting index ' + str(idx)
            greet = positive[idx]
            bot.sendMessage(chat_id, greet)

        elif command == '/start':
            bot.sendMessage(chat_id, 'Hello ' + first_name)
            cur.execute(
                "INSERT IGNORE INTO cubot.user(chatid,first_name,last_name,username) VALUES (%s,%s,%s,%s)", (chat_id, first_name, last_name, username))
            db.commit()

        elif command in msg2:
            idx = randint(0, reply_msg2.__len__() - 1)
            print 'selecting index ' + str(idx)
            greet = reply_msg2[idx]
            bot.sendMessage(chat_id, greet)

        elif command == 'what can you do':
            bot.sendMessage(
                chat_id, 'I can help you to access notifications and circulars from the website of Calicut University')
            bot.sendMessage(
                chat_id, 'Believe it or not i can download your hallticket/results for you 😁')

        elif command in msg3:
            bot.sendMessage(chat_id, 'Well, that is a good thing to ask')
            bot.sendMessage(
                chat_id, 'Team Four_BitZz developed me as their final year project, They are awesome !')
        elif command in msg4:
            bot.sendMessage(chat_id, 'I am Fine.')
            bot.sendMessage(chat_id, 'What about you')

        else:
            bot.sendMessage(chat_id, 'that was Confusing')
            bot.sendMessage(chat_id, 'Sorry! iam still a learning kid! ')
            print 'Advanced request from user'
            print 'calling handler...'

    elif content_type == 'sticker':
        command = msg['sticker']
        bot.sendMessage(chat_id, 'Aww! looks good')

    elif content_type == 'document':
        command = msg['document']
        bot.sendMessage(chat_id, 'I cant read it right now')

    elif content_type == 'voice':
        command = msg['voice']
        # take a file id
        if 'file_id' in command:
            fid = command['file_id']

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
        fullpath = '/tmp/cubot/' + fpath + '.ogg'
        fullpath.encode('latin_1')
        print ('file saved in ' + fullpath)

        # directory make...
        dir = os.path.dirname('/tmp/cubot/voice/')
        if not os.path.exists(dir):
            os.makedirs(dir)

        # download voice
        url1 = 'https://api.telegram.org/file/bot351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA/' + fpath
        wget.download(
            url1, fullpath)

        # convert .ogg to .wave
        call(["ffmpeg", "-i", fullpath, "/tmp/cubot/" + fpath + ".wav"])
        os.remove(fullpath)
        # convert .wave to .ogg
        AUDIO_FILE = "/tmp/cubot/" + fpath + ".wav"
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file
        try:
             stt = r.recognize_google(audio)
        except sr.UnknownValueError:
            stt = "CU_Bot could not understand audio"
        except sr.RequestError as e:
            print(
                stt="Could not request results from CU_Bot service. sorry for the interruption."
        handle(stt)

    elif content_type == 'location':
        command=msg['location']
        bot.sendMessage(chat_id, 'what are you doing there ?')

    elif content_type == 'photo':
        bot.getFile()
        command=msg['photo']
        bot.sendMessage(chat_id, 'This is awesome 😘')

    elif content_type == 'video_note':
        command=msg['video_note']
        bot.sendMessage(chat_id, 'you are awesome 😘')

    elif content_type == 'audio':
        command=msg['audio']
        bot.sendMessage(chat_id, 'feeling good 😊')

    elif content_type == 'video':
        command=msg['video']
        bot.sendMessage(chat_id, 'Iam not able to understand this video 😊')

    else:
        command=msg['document']
        bot.sendMessage(
            chat_id, 'Iam not able to understand this file!')

    print 'Got command: %s' % command


bot=telepot.Bot('351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA')
MessageLoop(bot, handle).run_as_thread()


print 'I am listening ...'

while 1:
    time.sleep(10)
# close the curso
cur.close()
# close the connection
db.close()

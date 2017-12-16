# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-
#!/usr/bin/python

import time
import random
import datetime
import telepot
from random import randint
from telepot.loop import MessageLoop
import mysql.connector as mariadb

db = mariadb.connect(user="root", password="", database="cubot")
# create a cursor for the select
cur = db.cursor()


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #chat_id = msg['chat']['id']
    username = msg['from']['first_name']

    print 'username : %s' % username
    print 'Got type: %s' % content_type

    if content_type == 'text':
        command = msg['text']
        command = command.lower()
        command = command.encode('utf-8')

        # Greetings
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
                      'sorry ! i am not interested  ']

        msg3 = ['made ❤️ with', 'who developed you', 'who developed you?',
                'who developed you ?', 'developers',
                'makers', 'who maked you', 'developer team']

        msg4 = ['how are you', 'how hope you', 'how do you do',
                'how are u', 'how hope u', 'how do u do',
                'how are you ?', 'how hope you ?', 'how do you do ?',
                'how are u ?', 'how hope u ?', 'how do u do ?'
                'how are you?', 'how hope you?', 'how do you do?',
                'how are u?', 'how hope u?', 'how do u do?']

        if command in greetings:
            idx = randint(0, reply_greetings.__len__() - 1)
            print 'selecting index ' + str(idx)
            greet = reply_greetings[idx]
            bot.sendMessage(chat_id, greet)

        elif command in msg1:
            idx = randint(0, reply_msg1.__len__() - 1)
            print 'selecting index ' + str(idx)
            greet = reply_msg1[idx]
            bot.sendMessage(chat_id, greet + username)

        elif command == '/start':
            bot.sendMessage(
                chat_id, 'Hello ' + username)
            cur.execute(
                "INSERT INTO cubot.user(chatid,name) VALUES (%s,%s)", (chat_id, username))
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
            bot.sendMessage(chat_id, 'And You')

        else:
            bot.sendMessage(chat_id, 'that was Confusing')
            # done translating
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
        bot.sendMessage(chat_id, 'You have a beautiful voice 😘')

    elif content_type == 'location':
        command = msg['location']
        bot.sendMessage(chat_id, 'what are you doing there ?')

    elif content_type == 'photo':
        command = msg['photo']
        bot.sendMessage(chat_id, 'This is awesome 😘')

    elif content_type == 'video_note':
        command = msg['video_note']
        bot.sendMessage(chat_id, 'you are awesome 😘')

    elif content_type == 'audio':
        command = msg['audio']
        bot.sendMessage(chat_id, 'feeling good 😊')

    elif content_type == 'video':
        command = msg['video']
        bot.sendMessage(chat_id, 'Iam not able to understand this video 😊')

    else:
        command = msg['document']
        bot.sendMessage(
            chat_id, 'Iam not able to understand this file!')

    print 'Got command: %s' % command

# close the cursor
# cur.close()
# close the connection
#db.close ()


bot = telepot.Bot('351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA')
MessageLoop(bot, handle).run_as_thread()


print 'I am listening ...'

while 1:
    time.sleep(10)

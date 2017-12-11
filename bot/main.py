# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-
import time
import random
import datetime
import telepot
from random import randint
from telepot.loop import MessageLoop


def handle(msg):
    chat_id = msg['chat']['id']
    username = msg['from']['first_name']
    command = msg['text']
    command = command.lower()
    command = command.encode('utf-8')
    print 'username : %s' % username
    print 'Got command: %s' % command
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
                       'Love you to... ', 'I am your personal assistant. I cant love you ', 'What the hell you talking ', '❤️ ', 'You are my Friend ', 'sorry ! i am not interested  ']

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
            chat_id, 'Hello '+username)

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

    elif command in msg3 :
        bot.sendMessage(chat_id, 'Well, that is a good thing to ask')
        bot.sendMessage(
            chat_id, 'Team Four_BitZz developed me as their final year project, They are awesome !')
    elif command in msg3 :
        bot.sendMessage(chat_id, 'I am Fine.')
        bot.sendMessage(chat_id, 'And You')

    else:
        bot.sendMessage(chat_id, 'that was Confusing')
        # done translating
        bot.sendMessage(chat_id, 'Sorry! iam still a learning kid! ')
        print 'Advanced request from user'
        print 'calling handler...'


bot = telepot.Bot('351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA')
MessageLoop(bot, handle).run_as_thread()

print 'I am listening ...'

while 1:
    time.sleep(10)

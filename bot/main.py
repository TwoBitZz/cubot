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
    username = msg['from']['username']
    command = msg['text']
    command = command.lower()
    command = command.encode('utf-8')
    print 'Got command: %s' % command
    # Greetings
    greetings = ['hi', 'hai', 'hey', 'hello',
                 'howdy', 'hi', 'oi', 'hoy', 'hi', 'hai', 'hey', 'hello',
                 'howdy', 'oi', 'hoy','ai', 'hei', 'hloo', 'hii',
                              'kooi', 'hallo', 'hlo', 'hy', '👋']
    reply_greetings = ['howdy', 'How are you',
                       'Hi', 'Hey', 'Howdy', 'Hello', '👋']

    if command in greetings:
        idx = randint(0, reply_greetings.__len__() - 1)
        print 'selecting index ' + str(idx)
        greet = reply_greetings[idx]
        bot.sendMessage(chat_id, greet)

    elif command == 'do you know me':
        bot.sendMessage(
            chat_id, 'You are my Friend')
        bot.sendMessage(chat_id, username)
    elif command == '❤️':
        bot.sendMessage(
            chat_id, 'Love You to  😁')

    elif command == 'i love you':
        bot.sendMessage(
            chat_id, 'Love You to  😁')

    elif command == 'love you':
        bot.sendMessage(
            chat_id, 'Love You to  😁')

    elif command == 'what can you do':
        bot.sendMessage(
            chat_id, 'I can help you to access notifications and circulars from the website of Calicut University')
        bot.sendMessage(
            chat_id, 'Believe it or not i can download your hallticket/results for you 😁')

    elif command == 'who developed you':
        bot.sendMessage(chat_id, 'Well, that is a good thing to ask')
        bot.sendMessage(
            chat_id, 'Team Four_BitZz developed me as their final year project, They are awesome !')

    else:
        bot.sendMessage(chat_id, 'that was Confusing')
        bot.sendMessage(chat_id, 'sorry! njan kooduthal padichondirikukayanu') # please tranclate
        print 'Advanced request from user'
        print 'calling handler...'


bot = telepot.Bot('351057354:AAFk5gALlI2AqCqcCh4EAwR35BzSs1Kq8bA')
MessageLoop(bot, handle).run_as_thread()

print 'I am listening ...'

while 1:
    time.sleep(10)

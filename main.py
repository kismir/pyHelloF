# -*- coding: utf-8 -*-
import config
import telebot
import time
from gglSearch import query

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            rec=query(m.text)
            bot.send_message(m.chat.id, rec)

if __name__ == '__main__':
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)
     while True:
         time.sleep(100)

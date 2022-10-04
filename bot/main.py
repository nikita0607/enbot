import telebot
import schedule
import threading
from threading import Thread
import time, datetime
from datetime import datetime
from time import sleep

from telebot import types


some_id = -807099752
bot = telebot.TeleBot("5588347087:AAH3-qJmgvb6BYid-AzH4G_bEl2cb2pnsw0", threaded=True)




def schedule_checker():  # рассылка
    while True:
        schedule.run_pending()
        sleep(1)

def func_to_run():
    return bot.send_message(some_id, 'Привет, Никита додик?')


@bot.message_handler(commands = ['start'])
def welcome(message):


    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да")
    item2 = types.KeyboardButton("Конечно")
    markup.add(item1, item2)
    print(message.chat.id)


    bot.send_message(message.chat.id, 'Привет, Никита додик?', reply_markup=markup)

#
schedule.every().day.at("16:00").do(func_to_run)
Thread(target=schedule_checker).start()
bot.polling(none_stop=True)

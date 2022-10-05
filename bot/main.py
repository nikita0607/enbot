import telebot
import schedule
import threading

from threading import Thread
from time import sleep
from abc import ABC, abstractmethod

from telebot import types

from typing import Dict, Tuple




class Chat:
    def __init__(self, chat_id: int, admin_id: int):
        self.chat_id = chat_id
        self.admin_id = admin_id
        self.questions = []


class Carusel(ABC):
    @abstractmethod
    def step(self, message: types.Message) -> Tuple[str, types.ReplyKeyboardMarkup]:
        pass


class SelectorCarusel(Carusel):
    def __init__(self):
        self.step_num = 0
 
    def step(self, message: types.Message) -> Tuple[str, types.ReplyKeyboardMarkup]:
        if step == 0:
            pass

    
bot = telebot.TeleBot("5588347087:AAH3-qJmgvb6BYid-AzH4G_bEl2cb2pnsw0", threaded=True)
chats: Dict[int, Chat] = {}
admins: Dict[int, Chat] = {}

def schedule_checker():  # рассылка
    while True:
        schedule.run_pending()
        sleep(1)


def func_to_run():
    return bot.send_message(some_id, 'Привет, Никита додик?')


@bot.message_handler(commands=['start'])
def welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Добавить вопрос")
    markup.add(item1)

    chat_id = message.chat.id

    if chat_id in chats:
        return
    
    chat = Chat(chat_id, message.from_user.id)
    
    print(message.chat.id)
    print(message.from_user.id)

    chats[chat_id] = chat
    admins[chat.admin_id] = chat
    bot.send_message(chat.admin_id, 'Welcome!', reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text=="Добавить вопрос")
def add_question(message: types.Message):
    if message.from_user.id not in admins:
        return
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кружочки")
    item2 = types.KeyboardButton("ке кружочки")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Next sppee", reply_markup=markup)


Thread(target=schedule_checker).start()
bot.polling(none_stop=True)

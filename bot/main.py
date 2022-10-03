import telebot

from telebot import types


bot = telebot.TeleBot("5588347087:AAH3-qJmgvb6BYid-AzH4G_bEl2cb2pnsw0")


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    pass


@bot.chat_join_request_handler()
def make_some(message: types.ChatJoinRequest):
    print("request!")
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)


bot.polling(none_stop=True)

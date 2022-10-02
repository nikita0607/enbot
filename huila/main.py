import telebot


from telebot import types

bot = telebot.TeleBot("5588347087:AAH3-qJmgvb6BYid-AzH4G_bEl2cb2pnsw0")

@bot.message_handler(commands = ['start'])
def welcome(message):


    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да")
    item2 = types.KeyboardButton("Конечно")
    markup.add(item1, item2)


    bot.send_message(message.chat.id, 'Привет, Никита додик?', reply_markup=markup)

bot.polling(none_stop=True)

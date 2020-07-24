import telebot
import config
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from commands import start
from commands import info

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'старт'])
def send_start_message(message):
    try:
        params = start.construct_message(message)
        bot.send_message(chat_id=params.chat_id, 
            text=params.text, 
            reply_markup=params.reply_markup)

    except AttributeError as e:
        bot.send_message(config.ADMIN_ID, repr(e))
        bot.send_message(chat_id=message.chat.id, text='Command is unavailable now. Sorry for this problem.')


@bot.message_handler(commands=['info', 'инфо', 'информация'])
def send_info_message(message):
    try:
        params = info.construct_message(message)
        bot.send_message(chat_id=params.chat_id,
            text=params.text,
            reply_markup=params.reply_markup)
    except AttributeError as e:
        bot.send_message(config.ADMIN_ID, repr(e))
        bot.send_message(chat_id=message.chat.id, text='Command is unavailable now. Sorry for this problem.')


print('started')
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except: 
        print('Connection failed')
        time.sleep(5)
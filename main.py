from telebot.types import ReplyKeyboardMarkup
from shared import bot
import sqlite3

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_keyboard.add('ثبت نام', 'ورود', 'نام چنل ها')

reply_keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

connection = sqlite3.connect('sqlite3.db', check_same_thread=False)
cursor = connection.cursor()

messages_list = []


def welcome(message):
    bot.reply_to(message, 'سلام به ربات مانی خوش اومدی. نظرت با ثبت نام چیه؟', reply_markup=reply_keyboard)


def channels_name(message):
    cursor.execute('SELECT * FROM channels')
    results = cursor.fetchall()
    for result in results:
        reply_keyboard2.add(result[1])
    reply_keyboard2.add('share')
    bot.send_message(message.chat.id, 'hhhh', reply_markup=reply_keyboard2)


def channel_name_selected(message):
    cursor.execute('SELECT * FROM channels WHERE channel_name == ?', (message.text,))
    channel = cursor.fetchall()
    messages_list.append(channel[0][2])
    bot.send_message(message.chat.id, 'appended!')

from telebot.types import ReplyKeyboardMarkup
from shared import bot

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_keyboard.add('ثبت نام', 'ورود', 'مهمان')


def welcome(message):
    bot.reply_to(message, 'سلام به ربات مانی خوش اومدی. نظرت با ثبت نام چیه؟', reply_markup=reply_keyboard)

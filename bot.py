from authentication import register, login
from main import welcome
from shared import bot


@bot.message_handler(commands=['start'])
def handle_welcome(message):
    welcome(message)


@bot.message_handler(func=lambda message: message.text == 'ثبت نام')
def handle_register(message):
    register(message)


@bot.message_handler(func=lambda message: message.text == 'ورود')
def handle_login(message):
    login(message)


bot.polling()

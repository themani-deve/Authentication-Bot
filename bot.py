from authentication import register, login
from main import welcome, channels_name, channel_name_selected
from shared_post import share_message
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


@bot.message_handler(func=lambda message: message.text == 'نام چنل ها')
def handle_channels_name(message):
    channels_name(message)


@bot.message_handler(func=lambda message: message.text == 'share')
def handle_share_message(message):
    from main import messages_list
    print(messages_list)
    share_message(message)


@bot.message_handler(func=lambda message: True)
def handle_send_message(message):
    channel_name_selected(message)


bot.polling()

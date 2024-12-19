from shared import bot
from telebot.types import ReplyKeyboardMarkup
from Custom_Apps.timer import timer

time_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
time_keyboard.row('10:00 AM', '11:00 AM', '12:00 PM')
time_keyboard.row('1:00 PM', '2:00 PM', '3:00 PM')
time_keyboard.add('Now')

user_data = {}


def share_message(message, messages):
    user_id = message.chat.id
    bot.send_message(user_id, 'پیام رو جهت ارسال بنویسید')
    user_data[user_id] = {"channels_id": messages}
    bot.register_next_step_handler(message, what_time)


def what_time(message):
    user_id = message.chat.id
    user_data[user_id]['text'] = message.text
    bot.send_message(user_id, 'چه زمانی ارسال کنم؟', reply_markup=time_keyboard)
    bot.register_next_step_handler(message, message_timer)


def message_timer(message):
    user_id = message.chat.id
    if message.text == 'Now':
        message_text(user_data[user_id]['channels_id'], user_data[user_id]['text'], user_id)
    else:
        x = timer(1)
        if x:
            message_text(user_data[user_id]['channels_id'], user_data[user_id]['text'], user_id)


def message_text(channels, text, user_id):
    for channel in channels:
        bot.send_message(channel, text)
    bot.send_message(user_id, 'پیام‌ها ارسال شدند!')

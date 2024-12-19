from shared import bot


def share_message(message):
    bot.send_message(message.chat.id, 'پیام رو جهت ارسال بنویسید')

from shared import bot
import sqlite3

connection = sqlite3.connect('user.db', check_same_thread=False)
cursor = connection.cursor()

sample_data_query = """
    INSERT INTO users (first_name, phone_number, password)
    values (?, ?, ?)
"""

info = []


def register(message):
    bot.send_message(message.chat.id, 'نام شما چیست؟')
    bot.register_next_step_handler(message, receive_phone_number)


def receive_phone_number(message):
    info.append(message.text)
    bot.reply_to(message, f'بسیار خب {message.text} شماره تلفن شما چنده؟')
    bot.register_next_step_handler(message, receive_password)


def receive_password(message):
    cursor.execute('SELECT * FROM users WHERE phone_number == ?', (message.text,))
    phone_number = cursor.fetchall()
    if phone_number:
        bot.reply_to(message, 'شماره موبایل وارد شده تکراری است. دوباره تلاش کنید.')
        bot.register_next_step_handler(message, receive_password)
    else:
        info.append(message.text)
        bot.send_message(
            message.chat.id, 'خب الان وقتشه که یه پسورد برای خودت انتخاب کنی تا بعدش بتونی از این ربات استفاده کنی'
        )
        bot.register_next_step_handler(message, send_saved_message)


def send_saved_message(message):
    info.append(message.text)
    bot.send_message(message.chat.id, 'اطلاعات شما در دیتابیس ثبت شد.')

    tuple_info = tuple(info)
    sample_data = tuple_info

    with sqlite3.connect('user.db') as connection:
        cursor = connection.cursor()
        cursor.execute(sample_data_query, sample_data)
    info.clear()


def login(message):
    bot.send_message(message.chat.id, 'لطفا شماره تلفن خود را وارد کنید.')
    bot.register_next_step_handler(message, check_phone_number)


def check_phone_number(message):
    cursor.execute('SELECT * FROM users WHERE phone_number == ?', (message.text,))
    result = cursor.fetchall()
    if result:
        info.append(result)
        bot.send_message(message.chat.id, 'بسیار خب حالا پسوردتو وارد کن')
        bot.register_next_step_handler(message, check_password)
    else:
        bot.reply_to(message, 'کاربری یافت نشد')
        bot.register_next_step_handler(message, check_phone_number)


def check_password(message):
    if message.text == info[0][0][3]:
        bot.send_message(message.chat.id, f'خوش اومدید {info[0][0][1]}')
        info.clear()
    else:
        bot.send_message(message.chat.id, 'رمز عبور نادرست است')
        bot.register_next_step_handler(message, check_password)

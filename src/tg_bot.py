import telebot
from telebot import types

# your key for tg bot
bot = telebot.TeleBot('')
report_id = '-1001890350973'


def buttons():
    keyboard = types.InlineKeyboardMarkup()
    help_btn = types.InlineKeyboardButton(text='/help', callback_data='1')
    start_btn = types.InlineKeyboardButton(text='/start', callback_data='2')
    about_btn = types.InlineKeyboardButton(text='/about me', callback_data='3')
    keyboard.add(help_btn)
    keyboard.add(start_btn)
    keyboard.add(about_btn)
    return keyboard


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = buttons()
    bot.send_message(
        message.chat.id, 'Добрый день, я бот сообщества Flats.by',
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def buttons_resp(call):
    keyboard = buttons()
    if call.data == '1':
        bot.send_message(
            chat_id=call.message.chat.id,
            text='Опишите свою проблему или вопрос, а я отправлю ее администратору и он обязательно свяжется с Вами'
        )
    if call.data == '2':
        bot.send_message(
            chat_id=call.message.chat.id,
            text='Добрый день, я бот сообщества Flats.by',
            reply_markup=keyboard
        )
    if call.data == '3':
        bot.send_message(
            chat_id=call.message.chat.id,
            text='Добрый день, я чат-бот созданный на языке программирования Python разработчиком из Беларуси.'
                 'Я являюсь проектом и телеграмм-постером группы Flats.by. Мой функционал еще очень мал, но меня '
                 'совершенствуют и улучшают каждый день. А пока посмотрите список команд, которые я умею сейчас.',
            reply_markup=keyboard
        )


def send_post(message):
    bot.send_message(report_id, message, parse_mode='html')


bot.polling(none_stop=True)
import telebot
from telebot import types

bot = telebot.TeleBot('5468350236:AAFvmQA5hlbmRnp9ojVgWjUx7oBKxgCO_dU')


def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетите веб сайт!",
                                          url="https://www.youtube.com/watch?v=HodO2eBEz_8&list=PL0lO_mIqDDFUdlTc097-1A9IBchtJEggp"))
    bot.send_message(message.chat.id, 'Перейдите на обучающий сайт', reply_markup=markup)


@bot.message_handler(commands=["help"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетите веб сайт!",
                                          url="https://www.youtube.com/watch?v=HodO2eBEz_8&list=PL0lO_mIqDDFUdlTc097-1A9IBchtJEggp"))
    bot.send_message(message.chat.id, 'Перейдите на обучающий сайт', reply_markup=markup)



@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    if message.from_user.last_name is None:
        mess = f'Привет, {message.from_user.first_name}'
    else:
        mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess)




@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, "И тебе привет")
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}")
    elif message.text == 'photo':
        photo = open('4848.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Вот твое фото")
    else:
        echo_all(message)


bot.polling(none_stop=True)

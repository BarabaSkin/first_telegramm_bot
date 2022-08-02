import telebot

bot = telebot.TeleBot('5468350236:AAFvmQA5hlbmRnp9ojVgWjUx7oBKxgCO_dU')


def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    if message.from_user.last_name is None:
        mess = mess = f'Привет, {message.from_user.first_name}'
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


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chet.id, 'Вау, крутое фото!', )


bot.polling(none_stop=True)

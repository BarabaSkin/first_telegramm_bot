import telebot

bot = telebot.TeleBot('5468350236:AAFvmQA5hlbmRnp9ojVgWjUx7oBKxgCO_dU')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    if message.from_user.last_name is None:
        mess = mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Сам справишься')


bot.polling(none_stop=True)

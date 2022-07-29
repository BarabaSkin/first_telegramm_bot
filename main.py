import telebot

bot = telebot.TeleBot('5468350236:AAFvmQA5hlbmRnp9ojVgWjUx7oBKxgCO_dU')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Сам справишься')

bot.polling(none_stop=True)

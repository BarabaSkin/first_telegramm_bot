import telebot

bot = telebot.TeleBot('5468350236:AAFvmQA5hlbmRnp9ojVgWjUx7oBKxgCO_dU')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    if message.from_user.last_name is None:
        mess = mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, f"Я тебя не понимаю", parse_mode='html')


bot.polling(none_stop=True)

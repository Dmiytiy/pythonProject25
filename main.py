import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])

def start(message):
    mess = f'ПРивет,<b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if message.text == "hello":
        bot.send_message(message.chat.id, "Итебе привет", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"твой Id{message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


bot.polling(none_stop =True)
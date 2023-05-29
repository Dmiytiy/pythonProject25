
import telebot
import random
from telebot import types

# Загрузка списка комплиментов из файла word.txt
with open("complimate.txt", "r", encoding="utf-8") as file:
    compliments = [line.strip() for line in file]

# Создание объекта бота
bot = telebot.TeleBot('5886486249:AAFJ6utGmbnqnc6yh1uv92ytJyL-A_7tejc')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    compliment = types.KeyboardButton("комплименты")
    stop = types.KeyboardButton("остановись")
    markup.add(compliment, stop)
    bot.reply_to(message, "Привет! Я бот, который делает комплименты. Нажми 'комплименты', чтобы получить комплимент.", reply_markup=markup)

# Обработчик кнопки "комплименты"
@bot.message_handler(func=lambda message: message.text == "комплименты")
def send_compliment(message):
    compliment = random.choice(compliments)
    bot.reply_to(message, compliment)

# Обработчик кнопки "остановись"
@bot.message_handler(func=lambda message: message.text == "остановись")
def compliment_button(message):
    with open("picture.png", "rb") as image_file:
        image = image_file.read()
        bot.send_photo(message.chat.id, photo=image)

# Запуск бота
bot.polling(none_stop=True)

import config
import telebot
from telebot import types

bot = telebot.TeleBot(token=config.token)

@bot.message_handler(commands=['start'])
def Welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton('Кто я')
    item2 = types.KeyboardButton('Рисунки')
    item3 = types.KeyboardButton('Контакты')
    item4 = types.KeyboardButton('Контакты')
    item5 = types.KeyboardButton('Контакты')
    item6 = types.KeyboardButton('Контакты')

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, "Привет! Добро пожаловать ко мне в гости.", reply_markup=markup)

@bot.message_handler(commands=['Кто я'])
def About(message):
    bot.send_message(message.chat.id, "Я, Вера,\nя креативный художник. Мне 10 лет ")
@bot.message_handler(commands=['command2'])
def Location(message):
    bot.send_message(message.chat.id, "Я, живу во Всеволжске. Это город в Ленинградской области")

@bot.message_handler(content_types=['text'])
def answer(message):
    file = open('logs.txt', 'a')
    file.writelines(f"{message.chat.first_name} {message.chat.last_name}: {message.text}\n")
    file.close()

    if message.text == "Привет":
        bot.send_message(message.chat.id, "Привет, дружище!")
    elif message.text == 'Кто я':
        bot.send_message(message.chat.id, "Я, Вера.\nЯ креативный художник.\nМне 10 лет. ")
    elif message.text == "Как дела?":
        bot.send_message(message.chat.id, "У меня всё отлично!")
    elif message.text == 'Рисунки':
        image = open('cans.PNG', 'rb')
        bot.send_photo(message.chat.id, image)

    else:
        bot.send_message(message.chat.id, "Я пока не понимаю такие команды.")

bot.polling(non_stop= True)
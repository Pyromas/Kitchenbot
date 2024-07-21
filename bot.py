import telebot
from telebot import types

bot = telebot.TeleBot( '7341826848:AAGHyThrnMmblwrfKEEdCp1CZC0QSe7-zsU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Recepts")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я бот-помощник для кулинарии. Здесь есть команда, receps которая может помочь вам выбрать подходящую кухню. Также внизу есть кнопки с кухнями. IT = Итальянская кухня, UK = Украинская кухня и так далее. Вы также можете перейти по [ссылке](https://github.com/Pyromas/Kitchenbot/tree/main).Tам есть информация о боте", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Recepts':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('CH')
        btn2 = types.KeyboardButton('FR')
        btn3 = types.KeyboardButton('UK')
        btn4 = types.KeyboardButton('IT')
        btn5 = types.KeyboardButton('NR')
        btn6 = types.KeyboardButton('GR')
        markup.row(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, 'Какую кухню вы хотели бы выбрать?', reply_markup=markup)

    elif message.text == 'CH':
        bot.send_message(message.from_user.id, 'Пожалуйста, перейдите по [ссылке](https://www.russianfood.com/recipes/bytype/?fid=132)', parse_mode='Markdown')

    elif message.text == 'FR':
        bot.send_message(message.from_user.id, 'Пожалуйста, перейдите по [ссылке](https://www.russianfood.com/recipes/bytype/?fid=102)', parse_mode='Markdown')

    elif message.text == 'UK':
        bot.send_message(message.from_user.id, 'Пожалуйста, перейдите по [ссылке](https://www.russianfood.com/recipes/bytype/?fid=104)', parse_mode='Markdown')

    elif message.text == 'IT':
        bot.send_message(message.from_user.id, 'Пожалуйста, перейдите по [ссылке](https://www.russianfood.com/recipes/bytype/?fid=102)', parse_mode='Markdown')

    elif message.text == 'NR':
        bot.send_message(message.from_user.id, 'Пожалуйста, перейдите по [ссылке](https://www.russianfood.com/recipes/bytype/?fid=146)', parse_mode='Markdown')

    elif message.text == 'GR':
        bot.send_message(message.from_user.id, 'Пожалуйста, перейдите по [ссылке](https://www.russianfood.com/recipes/bytype/?fid=134)', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)

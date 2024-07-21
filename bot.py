import telebot
from telebot import types

bot = telebot.TeleBot('7341826848:AAGHyThrnMmblwrfKEEdCp1CZC0QSe7-zsU')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Recepts")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я  бот-помошник dla kulinarii.Sdes est kommand kotoraia vam mochet pomoch./recepts - pomochet vibrat podhodiachiu kuhnu.Takche vnisu est knopki kuchni.IT = Итальянская кухня,UK = Украинская кухня.Itak dalee.Takche vi mochete pereiti po + '[ссылке](https://www.russianfood.com/recipes/bytype/?fid=132)' ", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Recepts':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('CH')
        btn2 = types.KeyboardButton('FR')
        btn3 = types.KeyboardButton('UK')
        btn4 = types.KeyboardButton('IT')
        btn5 = types.KeyboardButton('NR')
        btn6 = types.KeyboardButton('GR')
        markup.row(btn1, btn2, btn3, btn4,btn5,btn6)
        bot.send_message(message.from_user.id, 'Kakuiu kucniu vi hoteli bi vibrat', reply_markup=markup) #ответ бота


    elif message.text == 'CH':
        bot.send_message(message.from_user.id, 'Pochaluista pereidite po ssilke.Tam est mnochestvo receptov' + '[ссылке](https://www.russianfood.com/recipes/bytype/?fid=132)' , parse_mode='Markdown')

    elif message.text == 'FR':
        bot.send_message(message.from_user.id, 'Pochaluista pereidite po ssilke.Tam est mnochestvo receptov' + '[ссылке](https://www.russianfood.com/recipes/bytype/?fid=102)', parse_mode='Markdown')

    elif message.text == 'UK':
        bot.send_message(message.from_user.id, 'Pochaluista pereidite po ssilke.Tam est mnochestvo receptov' + '[ссылке](https://www.russianfood.com/recipes/bytype/?fid=104)', parse_mode='Markdown')

    elif message.text == 'UK':
        bot.send_message(message.from_user.id, 'Pochaluista pereidite po ssilke.Tam est mnochestvo receptov' + '[ссылке](https://www.russianfood.com/recipes/bytype/?fid=102)', parse_mode='Markdown')

    elif message.text == 'NR':
        bot.send_message(message.from_user.id, 'Pochaluista pereidite po ssilke.Tam est mnochestvo receptov' + '[ссылке](https://www.russianfood.com/recipes/bytype/?fid=146)', parse_mode='Markdown')
        
    elif message.text == 'GR':
        bot.send_message(message.from_user.id, 'Pochaluista pereidite po ssilke.Tam est mnochestvo receptov' + '[ссылке](https://www.russianfood.com/recipes/bytype/?fid=134)', parse_mode='Markdown')
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть

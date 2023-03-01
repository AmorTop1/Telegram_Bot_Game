import json
import telebot
from telebot import types

with open('settings.json') as _file:
    settings = json.load(_file)

token = settings.get('bot').get('token')
bot = telebot.TeleBot(token=token)
menu_message_id = None
calls = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Почати")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Привіт! Я телеграм бот який вибере тобі мобільну гру. Нажми на кнопку.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text.startswith('Почати'))
def arrr(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_1 = types.KeyboardButton('Аркади')
    item_2 = types.KeyboardButton('Вікторини')
    item_3 = types.KeyboardButton('Головоломки')
    item_4 = types.KeyboardButton('Шутер')
    item_5 = types.KeyboardButton('Картярські')
    item_6 = types.KeyboardButton('Музика')
    item_7 = types.KeyboardButton('Перегони')
    item_8 = types.KeyboardButton('Пригодницкі')
    item_9 = types.KeyboardButton('Рольові')
    item_10 = types.KeyboardButton('Симулятори')
    item_11 = types.KeyboardButton('Складання слів')
    item_12 = types.KeyboardButton('Спортивні')
    item_13 = types.KeyboardButton('Стратегії')
    item_14 = types.KeyboardButton('Хоррор')
    markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11,
               item_12, item_13, item_14)
    bot.send_message(message.chat.id, text="Вибери категорію:", reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

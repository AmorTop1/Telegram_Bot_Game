from simulator import bot
from Bot_game.Silka.skladana_slov_silka import lirti, lirti1, lirti2, lirti3, lirti4, lirti5, lirti6, lirti7, lirti8, lirti9, lirti10, lirti11, lirti12, lirti13, lirti14, lirti15, lirti16, lirti17, lirti18, lirti19, lirti20, lirti21, lirti22, lirti23, lirti24, lirti25, lirti26, lirti27, lirti28, lirti29, lirti30, lirti31, lirti32, lirti33, lirti34, lirti35, lirti36, lirti37, lirti38, lirti39
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Складання слів'))
def skladanaslov(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.fugo.wow')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.zynga.words3')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.peoplefun.wordcross')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=in.playsimple.wordtrip')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=in.playsimple.tripcross')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.bitmango.go.wordcookies')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.scopely.wheeloffortune')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.wordgame.words.connect')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.nytimes.crossword')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=com.pieyel.scrabble')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: ' + str(lirti) +
                     '\nРейтинг: ' + str(lirti1) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti2) +
                     '\nОбмеження: ' + str(lirti3) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: ' + str(lirti4) +
                     '\nРейтинг: ' + str(lirti5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti6) +
                     '\nОбмеження: ' + str(lirti7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(lirti8) +
                     '\nРейтинг: ' + str(lirti9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti10) +
                     '\nОбмеження: ' + str(lirti11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(lirti12) +
                     '\nРейтинг: ' + str(lirti13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti14) +
                     '\nОбмеження: ' + str(lirti15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(lirti16) +
                     '\nРейтинг: ' + str(lirti17) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti18) +
                     '\nОбмеження: ' + str(lirti19) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(lirti20) +
                     '\nРейтинг: ' + str(lirti21) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti22) +
                     '\nОбмеження: ' + str(lirti23) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(lirti24) +
                     '\nРейтинг: ' + str(lirti25) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti26) +
                     '\nОбмеження: ' + str(lirti27) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(lirti28) +
                     '\nРейтинг: ' + str(lirti29) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti30) +
                     '\nОбмеження: ' + str(lirti31) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: ' + str(lirti32) +
                     '\nРейтинг: ' + str(lirti33) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti34) +
                     '\nОбмеження: ' + str(lirti35) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(lirti36) +
                     '\nРейтинг: ' + str(lirti37) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lirti38) +
                     '\nОбмеження: ' + str(lirti39) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()
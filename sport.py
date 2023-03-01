from skladanaslov import bot
from Bot_game.Silka.sport_silka import sport1, sport2, sport3, sport4, sport5, sport6, sport7, sport8, sport9, sport10, sport11, sport12, sport13, sport14, sport15, sport16, sport17, sport18, sport19, sport20, sport21, sport22, sport23, sport24, sport25, sport26, sport27, sport28, sport29, sport30, sport31, sport32, sport33, sport34, sport35, sport36, sport37, sport38, sport39
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Спортивні'))
def sport(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.ea.gp.fifamobile')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=jp.konami.pesam')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=eu.nordeus.topeleven.android')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=com.miniclip.eightballpool')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.greenhorsegames.footballrivals')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.ea.gp.fifaultimate')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.tfgco.games.sports.free.tennis.clash')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.miniclip.footballstrike')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=com.masomo.headball2')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: FIFA Футбол' +
                     '\nРейтинг: ' + str(sport1) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport2) +
                     '\nОбмеження: ' + str(sport3) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: ' + str(sport4) +
                     '\nРейтинг: ' + str(sport5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport6) +
                     '\nОбмеження: ' + str(sport7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(sport8) +
                     '\nРейтинг: ' + str(sport9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport10) +
                     '\nОбмеження: ' + str(sport11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(sport12) +
                     '\nРейтинг: ' + str(sport13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport14) +
                     '\nОбмеження: ' + str(sport15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(sport16) +
                     '\nРейтинг: ' + str(sport17) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport18) +
                     '\nОбмеження: ' + str(sport19) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(sport20) +
                     '\nРейтинг: ' + str(sport21) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport22) +
                     '\nОбмеження: ' + str(sport23) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(sport24) +
                     '\nРейтинг: ' + str(sport25) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport26) +
                     '\nОбмеження: ' + str(sport27) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(sport28) +
                     '\nРейтинг: ' + str(sport29) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport30) +
                     '\nОбмеження: ' + str(sport31) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: ' + str(sport32) +
                     '\nРейтинг: ' + str(sport33) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport34) +
                     '\nОбмеження: ' + str(sport35) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(sport36) +
                     '\nРейтинг: ' + str(sport37) +
                     '\nНа скількох пристроях скачана ігра: ' + str(sport38) +
                     '\nОбмеження: ' + str(sport39) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

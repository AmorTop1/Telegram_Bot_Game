from peregonu import bot
from Bot_game.Silka.prugoda_silka import lifi1, lifi2, lifi3, lifi4, lifi5, lifi6, lifi7, lifi8, lifi9, lifi10, lifi11, lifi12, lifi13, lifi14, lifi15, lifi16, lifi17, lifi18, lifi19, lifi20, lifi21, lifi22, lifi23, lifi24, lifi25, lifi26, lifi27, lifi28, lifi29, lifi30, lifi31, lifi32, lifi33, lifi34, lifi35, lifi36, lifi37, lifi38
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Пригодницкі'))
def prugoda(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.roblox.client')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.miHoYo.GenshinImpact')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.xdg.and.eu.lifeafter')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=net.wooga.junes_journey_hidden_object_mystery_game')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.dxx.firenow')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.playrix.manormatters')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftDOHM')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=net.wapsmskey.mrush')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.fivebn.ll8.f2p')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=com.heliogames.westland')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: ' + str(lifi1) +
                     '\nРейтинг: ' + str(lifi2) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi3) +
                     '\nОбмеження: ' + str(lifi4) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: Genshin Impact' +
                     '\nРейтинг: ' + str(lifi5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi6) +
                     '\nОбмеження: ' + str(lifi7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(lifi8) +
                     '\nРейтинг: ' + str(lifi9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi10) +
                     '\nОбмеження: ' + str(lifi11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(lifi12) +
                     '\nРейтинг: ' + str(lifi13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi14) +
                     '\nОбмеження: ' + str(lifi15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(lifi16) +
                     '\nРейтинг: ' + str(lifi17) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi18) +
                     '\nОбмеження: ' + str(lifi19) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(lifi20) +
                     '\nРейтинг: ' + str(lifi21) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi22) +
                     '\nОбмеження: ' + str(lifi23) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(lifi24) +
                     '\nРейтинг: ' + str(lifi25) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi26) +
                     '\nОбмеження: ' + str(lifi27) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(lifi28) +
                     '\nРейтинг: ' + str(lifi29) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi30) +
                     '\nОбмеження: ' + str(lifi31) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: Загублені землі 8' +
                     '\nРейтинг: ' + str(lifi32) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi33) +
                     '\nОбмеження: ' + str(lifi34) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(lifi35) +
                     '\nРейтинг: ' + str(lifi36) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifi37) +
                     '\nОбмеження: ' + str(lifi38) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

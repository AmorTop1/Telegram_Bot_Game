from golovolomki import bot
from telebot import types
from Bot_game.Silka.horror_silka import horror1, horror2, horror3, horror4, horror5, horror6, horror7, horror8, horror9, horror10, horror11, horror12, horror13, horror14, horror15, horror16, horror17, horror18, horror19, horror20, horror21, horror22, horror23, horror24, horror25, horror26, horror27, horror28, horror29, horror30, horror31, horror32, horror33, horror35, horror34, horror36, horror37


@bot.message_handler(func=lambda x: x.text.startswith('Хоррор'))
def horror(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.skytecgames.survival')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.eyesthegame.eyes')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.eg.deathpark')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=com.bhvr.deadbydaylight')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.aleson.casefiveanimatronicsfnaf')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.freerange.goosebumps')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.RaycasterGames.KadabraSurvivalHorror')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.horrogames.pipehead.scp.survival')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.escapehorrorgames.houseoffear3d2')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=io.horror.show')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: Horrorfield – Хорор Виживання' +
                     '\nРейтинг: ' + str(horror1) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror2) +
                     '\nОбмеження: ' + str(horror3) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: ' + str(horror4) +
                     '\nРейтинг: ' + str(horror5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror6) +
                     '\nОбмеження: ' + str(horror7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(horror8) +
                     '\nРейтинг: ' + str(horror9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror10) +
                     '\nОбмеження: ' + str(horror11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(horror12) +
                     '\nРейтинг: ' + str(horror13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror14) +
                     '\nОбмеження: ' + str(horror15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(horror16) +
                     '\nРейтинг: ' + str(horror17) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror18) +
                     '\nОбмеження: ' + str(horror19) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(horror20) +
                     '\nРейтинг: ' + str(horror21) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror22) +
                     '\nОбмеження: ' + str(horror23) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: Хорор Хейз: Страшні Ігри' +
                     '\nРейтинг: ' + str(horror24) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror25) +
                     '\nОбмеження: ' + str(horror26) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Весьма ігра
                     '\n\nНазва: ' + str(horror27) +
                     '\nРейтинг: ' + str(horror28) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror29) +
                     '\nОбмеження: ' + str(horror30) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: Хорор Хейз: Страшні Ігри' +
                     '\nРейтинг: ' + str(horror31) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror32) +
                     '\nОбмеження: ' + str(horror33) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(horror34) +
                     '\nРейтинг: ' + str(horror35) +
                     '\nНа скількох пристроях скачана ігра: ' + str(horror36) +
                     '\nОбмеження: ' + str(horror37) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

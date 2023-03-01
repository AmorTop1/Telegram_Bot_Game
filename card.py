from horror import bot
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Картярські'))
def sleep(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=net.supertreat.solitaire')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.playtika.wsop.gp')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.gsn.android.tripeaks')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=com.mattel163.phase10')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.zynga.livepoker')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=net.peakgames.mobile.spades.android')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.wizards.mtga')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.bbumgames.spadesroyale')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.island.card')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=jp.konami.duellinks')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: ' + str(lifti) +
                     '\nРейтинг: ' + str(lifti1) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti2) +
                     '\nОбмеження: ' + str(lifti3) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: ' + str(lifti4) +
                     '\nРейтинг: ' + str(lifti5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti6) +
                     '\nОбмеження: ' + str(lifti7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(lifti8) +
                     '\nРейтинг: ' + str(lifti9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti10) +
                     '\nОбмеження: ' + str(lifti11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: Phase 10' +
                     '\nРейтинг: ' + str(lifti12) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti13) +
                     '\nОбмеження: ' + str(lifti14) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(lifti15) +
                     '\nРейтинг: ' + str(lifti16) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti17) +
                     '\nОбмеження: ' + str(lifti18) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(lifti19) +
                     '\nРейтинг: ' + str(lifti20) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti21) +
                     '\nОбмеження: ' + str(lifti22) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(lifti23) +
                     '\nРейтинг: ' + str(lifti24) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti25) +
                     '\nОбмеження: ' + str(lifti26) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(lifti27) +
                     '\nРейтинг: ' + str(lifti28) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti29) +
                     '\nОбмеження: ' + str(lifti30) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: ' + str(lifti31) +
                     '\nРейтинг: ' + str(lifti32) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti33) +
                     '\nОбмеження: ' + str(lifti34) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(lifti35) +
                     '\nРейтинг: ' + str(lifti36) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lifti37) +
                     '\nОбмеження: ' + str(lifti38) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

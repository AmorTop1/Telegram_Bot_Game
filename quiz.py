from suter import bot
from Bot_game.Silka.viktoruna_silka import lins, lins1, lins2, lins3, lins4, lins5, lins6, lins7, lins8, lins9, lins10, lins11, lins12, lins13, lins14, lins15, lins16, lins17, lins18, lins19, lins20, lins21, lins22, lins23, lins24, lins25, lins26, lins27, lins28, lins29, lins30, lins31, lins32, lins33, lins34, lins35, lins36
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Вікторини'))
def suter(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.xmonetize.quizzland')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.unicostudio.braintest')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.asmolgam.flags')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=fun.arts.studio.rotate.baraban')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.nuomondo.millionaire.quiz')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.whotir.uquiz')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.submarineapps.mill')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.RedTower.AFourRoulette')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=by.panko.wherelogic')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=com.openmygame.games.android.pics')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: ' + str(lins) +
                     '\nРейтинг: ' + str(lins1) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins2) +
                     '\nОбмеження: ' + str(lins3) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: ' + str(lins4) +
                     '\nРейтинг: ' + str(lins5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins6) +
                     '\nОбмеження: ' + str(lins7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(lins8) +
                     '\nРейтинг: ' + str(lins9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins10) +
                     '\nОбмеження: ' + str(lins11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(lins12) +
                     '\nРейтинг: ' + str(lins13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins14) +
                     '\nОбмеження: ' + str(lins15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: Мільйонер: Вікторина' +
                     '\nРейтинг: ' + str(lins16) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins17) +
                     '\nОбмеження: ' + str(lins18) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(lins19) +
                     '\nРейтинг: ' + str(lins20) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins21) +
                     '\nОбмеження: ' + str(lins22) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(lins23) +
                     '\nРейтинг: ' + str(lins24) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins25) +
                     '\nОбмеження: ' + str(lins26) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(lins27) +
                     '\nРейтинг: ' + str(lins28) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins29) +
                     '\nОбмеження: ' + str(lins30) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: Де логіка? - Гра' +
                     '\nРейтинг: ' + str(lins31) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins32) +
                     '\nОбмеження: ' + str(lins33) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: 101 Картинка : Фото Вікторина' +
                     '\nРейтинг: ' + str(lins34) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lins35) +
                     '\nОбмеження: ' + str(lins36) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

from musika import bot
from Bot_game.Silka.peregonu_silka import lafa1, lafa2, lafa3, lafa4, lafa5, lafa6, lafa7, lafa8, lafa9, lafa10, lafa11, lafa12, lafa13, lafa14, lafa15, lafa16, lafa17, lafa18, lafa19, lafa20, lafa21, lafa22, lafa23, lafa24, lafa25, lafa26, lafa27, lafa28, lafa29, lafa30, lafa31, lafa32, lafa33, lafa34, lafa35, lafa36, lafa37, lafa38, lafa39
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Перегони'))
def peregonu(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.naturalmotion.customstreetracer2')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.ea.game.nfs14_row')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftA9HM')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=com.fingersoft.hcr2')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.hutchgames.cccg')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.battlecreek.offroadoutlaws')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.ea.games.r3_na')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.hutchgames.formularacing')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=com.creativemobile.nno')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: ' + str(lafa1) +
                     '\nРейтинг: ' + str(lafa2) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa3) +
                     '\nОбмеження: ' + str(lafa4) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: Need for Speed: NL Гонки' +
                     '\nРейтинг: ' + str(lafa5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa6) +
                     '\nОбмеження: ' + str(lafa7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(lafa8) +
                     '\nРейтинг: ' + str(lafa9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa10) +
                     '\nОбмеження: ' + str(lafa11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(lafa12) +
                     '\nРейтинг: ' + str(lafa13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa14) +
                     '\nОбмеження: ' + str(lafa15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(lafa16) +
                     '\nРейтинг: ' + str(lafa17) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa18) +
                     '\nОбмеження: ' + str(lafa19) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(lafa20) +
                     '\nРейтинг: ' + str(lafa21) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa22) +
                     '\nОбмеження: ' + str(lafa23) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(lafa24) +
                     '\nРейтинг: ' + str(lafa25) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa26) +
                     '\nОбмеження: ' + str(lafa27) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(lafa28) +
                     '\nРейтинг: ' + str(lafa29) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa30) +
                     '\nОбмеження: ' + str(lafa31) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: ' + str(lafa32) +
                     '\nРейтинг: ' + str(lafa33) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa34) +
                     '\nОбмеження: ' + str(lafa35) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(lafa36) +
                     '\nРейтинг: ' + str(lafa37) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lafa38) +
                     '\nОбмеження: ' + str(lafa39) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

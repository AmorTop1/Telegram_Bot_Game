from strateg import bot
from Bot_game.Silka.suter_silka import link, link1, link2, link3, link4, link5, link6, link7, link8, link9, link10, link11, link12, link13, link14, link15, link16, link17, link18, link19, link20, link21, link22, link23, link24, link25, link26, link27, link28, link29, link30, link31, link32, link33, link35, link34, link36, link37
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Шутер'))
def suter(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.axlebolt.standoff2')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.tencent.ig')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.mobile.legends')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=com.activision.callofduty.shooter')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.supercell.brawlstars')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.dts.freefireth')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.pixonic.wwr')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.fungames.battletanksbeta')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.dts.freefiremax')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=zombie.survival.craft.z')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: ' + str(link) +
                     '\nРейтинг: ' + str(link1) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link2) +
                     '\nОбмеження: ' + str(link3) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: ' + str(link4) +
                     '\nРейтинг: ' + str(link5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link6) +
                     '\nОбмеження: ' + str(link7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(link8) +
                     '\nРейтинг: ' + str(link9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link10) +
                     '\nОбмеження: ' + str(link11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(link12) +
                     '\nРейтинг: ' + str(link13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link14) +
                     '\nОбмеження: ' + str(link15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(link16) +
                     '\nРейтинг: ' + str(link17) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link18) +
                     '\nОбмеження: ' + str(link19) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: Garena Free Fire' +
                     '\nРейтинг: ' + str(link20) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link21) +
                     '\nОбмеження: ' + str(link22) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(link23) +
                     '\nРейтинг: ' + str(link24) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link25) +
                     '\nОбмеження: ' + str(link26) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Весьма ігра
                     '\n\nНазва: ' + str(link27) +
                     '\nРейтинг: ' + str(link28) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link29) +
                     '\nОбмеження: ' + str(link30) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: Garena Free Fire MAX' +
                     '\nРейтинг: ' + str(link31) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link32) +
                     '\nОбмеження: ' + str(link33) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(link34) +
                     '\nРейтинг: ' + str(link35) +
                     '\nНа скількох пристроях скачана ігра: ' + str(link36) +
                     '\nОбмеження: ' + str(link37) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

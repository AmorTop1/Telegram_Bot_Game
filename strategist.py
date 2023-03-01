from sport import bot
from Bot_game.Silka.strateg_silka import strateg1, strateg2, strateg3, strateg4, strateg5, strateg6, strateg7,strateg8, strateg9, strateg10, strateg11, strateg12, strateg13, strateg14, strateg15, strateg16, strateg17, strateg18, strateg19, strateg20, strateg21, strateg22, strateg23, strateg24, strateg25, strateg26, strateg27, strateg28, strateg29, strateg30, strateg31, strateg32, strateg33, strateg34, strateg35, strateg36, strateg37, strateg38, strateg39
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Стратегії'))
def strateg(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=net.wargaming.wot.blitz')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.igg.android.lordsmobile')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.hcg.cok.gp')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.kingsgroup.sos')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.plarium.vikings')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.im30.ROE.gp')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.supercell.clashofclans')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.star.union.planetant')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=com.yottagames.mafiawar')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: World of Tanks Blitz PVP битви' +
                     '\nРейтинг: ' + str(strateg1) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg2) +
                     '\nОбмеження: ' + str(strateg3) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: ' + str(strateg4) +
                     '\nРейтинг: ' + str(strateg5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg6) +
                     '\nОбмеження: ' + str(strateg7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(strateg8) +
                     '\nРейтинг: ' + str(strateg9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg10) +
                     '\nОбмеження: ' + str(strateg11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(strateg12) +
                     '\nРейтинг: ' + str(strateg13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg14) +
                     '\nОбмеження: ' + str(strateg15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(strateg16) +
                     '\nРейтинг: ' + str(strateg17) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg18) +
                     '\nОбмеження: ' + str(strateg19) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(strateg20) +
                     '\nРейтинг: ' + str(strateg21) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg22) +
                     '\nОбмеження: ' + str(strateg23) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(strateg24) +
                     '\nРейтинг: ' + str(strateg25) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg26) +
                     '\nОбмеження: ' + str(strateg27) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(strateg28) +
                     '\nРейтинг: ' + str(strateg29) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg30) +
                     '\nОбмеження: ' + str(strateg31) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: ' + str(strateg32) +
                     '\nРейтинг: ' + str(strateg33) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg34) +
                     '\nОбмеження: ' + str(strateg35) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(strateg36) +
                     '\nРейтинг: ' + str(strateg37) +
                     '\nНа скількох пристроях скачана ігра: ' + str(strateg38) +
                     '\nОбмеження: ' + str(strateg39) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

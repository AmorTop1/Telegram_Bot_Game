from rolovi import bot
from Bot_game.Silka.simulator_silka import limi, limi1, limi2, limi3, limi4, limi5, limi6, limi7, limi8, limi9, limi10, limi11, limi12, limi13, limi14, limi15, limi16, limi17, limi18, limi19, limi20, limi21, limi22, limi23, limi24, limi25, limi26, limi27, limi28, limi29, limi30, limi31, limi32, limi33, limi34, limi35, limi36
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Симулятори'))
def simulator(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.vizorapps.klondike')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.tensquaregames.letsfish2')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=progameslab.com.magic.seasons2023.farm.build')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=com.yourstoryinteractive.sails.pirate.adventure')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.farmadventure.global')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.mytona.cookingdiary.android')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.redcell.goldandgoblins')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.phoenix.game.and.ddj')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.xp101.ava_rus')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=com.olzhas.carparking.multyplayer')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: Клондайк' +
                     '\nРейтинг: ' + str(limi) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi1) +
                     '\nОбмеження: ' + str(limi2) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: Fishing Clash: Рибалка ігра 3D' +
                     '\nРейтинг: ' + str(limi3) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi4) +
                     '\nОбмеження: ' + str(limi5) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: Ялинка 2023 року: нова ферма' +
                     '\nРейтинг: ' + str(limi6) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi7) +
                     '\nОбмеження: ' + str(limi8) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(limi9) +
                     '\nРейтинг: ' + str(limi10) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi11) +
                     '\nОбмеження: ' + str(limi12) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(limi13) +
                     '\nРейтинг: ' + str(limi14) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi15) +
                     '\nОбмеження: ' + str(limi16) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(limi17) +
                     '\nРейтинг: ' + str(limi18) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi19) +
                     '\nОбмеження: ' + str(limi20) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(limi21) +
                     '\nРейтинг: ' + str(limi22) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi23) +
                     '\nОбмеження: ' + str(limi24) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(limi25) +
                     '\nРейтинг: ' + str(limi26) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi27) +
                     '\nОбмеження: ' + str(limi28) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: ' + str(limi29) +
                     '\nРейтинг: ' + str(limi30) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi31) +
                     '\nОбмеження: ' + str(limi32) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(limi33) +
                     '\nРейтинг: ' + str(limi34) +
                     '\nНа скількох пристроях скачана ігра: ' + str(limi35) +
                     '\nОбмеження: ' + str(limi36) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

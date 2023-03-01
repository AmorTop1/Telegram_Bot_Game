from prugoda import bot
from Bot_game.Silka.rolovi_silka import liri, liri1, liri2, liri3, liri4, liri5, liri6, liri7, liri8, liri9, liri10, liri11, liri12, liri13, liri14, liri15, liri16, liri17, liri18, liri19, liri20, liri21, liri22, liri23, liri24, liri25, liri26, liri27, liri28, liri29, liri30, liri31, liri32, liri33, liri34, liri35, liri36, liri37, liri38, liri39
from telebot import types


@bot.message_handler(func=lambda x: x.text.startswith('Рольові'))
def rolovi(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.blizzard.diablo.immortal')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.plarium.raidlegends')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.nexters.herowars')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=com.ncsoft.lineage2mru')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.whaleapp.blitz.rise.heroes.idle.rpg.battle')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=com.karma.mythwarspuzzles')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.dena.a12026418')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=valhalla.survival.craft.z')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.lilithgame.hgame.gp')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=com.pwrd.pwmru')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: ' + str(liri) +
                     '\nРейтинг: ' + str(liri1) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri2) +
                     '\nОбмеження: ' + str(liri3) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: ' + str(liri4) +
                     '\nРейтинг: ' + str(liri5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri6) +
                     '\nОбмеження: ' + str(liri7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(liri8) +
                     '\nРейтинг: ' + str(liri9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri10) +
                     '\nОбмеження: ' + str(liri11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(liri12) +
                     '\nРейтинг: ' + str(liri13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri14) +
                     '\nОбмеження: ' + str(liri15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(liri16) +
                     '\nРейтинг: ' + str(liri17) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri18) +
                     '\nОбмеження: ' + str(liri19) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(liri20) +
                     '\nРейтинг: ' + str(liri21) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri22) +
                     '\nОбмеження: ' + str(liri23) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(liri24) +
                     '\nРейтинг: ' + str(liri25) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri26) +
                     '\nОбмеження: ' + str(liri27) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(liri28) +
                     '\nРейтинг: ' + str(liri29) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri30) +
                     '\nОбмеження: ' + str(liri31) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: ' + str(liri32) +
                     '\nРейтинг: ' + str(liri33) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri34) +
                     '\nОбмеження: ' + str(liri35) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(liri36) +
                     '\nРейтинг: ' + str(liri37) +
                     '\nНа скількох пристроях скачана ігра: ' + str(liri38) +
                     '\nОбмеження: ' + str(liri39) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

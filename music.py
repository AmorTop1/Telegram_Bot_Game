from karta import bot
from telebot import types
from Bot_game.Silka.musika_silka import lift, lift1, lift2, lift3, lift4, lift5, lift6, lift7, lift8, lift9, lift10, lift11, lift12, lift13, lift14, lift15, lift16, lift17, lift18, lift19, lift20, lift21, lift22, lift23, lift24, lift25, lift26, lift27, lift28, lift29, lift30, lift31, lift32, lift33, lift34, lift35, lift36, lift37, lift38, lift39


@bot.message_handler(func=lambda x: x.text.startswith('Музика'))
def musika(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton("1",
                                         url='https://play.google.com/store/apps/details?id=com.piano.tiles.music.game.circles.dancing.beat.magictiles')

    button2 = types.InlineKeyboardButton("2",
                                         url='https://play.google.com/store/apps/details?id=com.amanotes.beathopper')

    button3 = types.InlineKeyboardButton("3",
                                         url='https://play.google.com/store/apps/details?id=com.joyjourney.PianoWhiteGo')

    button4 = types.InlineKeyboardButton("4",
                                         url='https://play.google.com/store/apps/details?id=com.music.game.dancing.hair.beat.race')

    button5 = types.InlineKeyboardButton("5",
                                         url='https://play.google.com/store/apps/details?id=com.orange.kidspiano.music.songs')

    button6 = types.InlineKeyboardButton("6",
                                         url='https://play.google.com/store/apps/details?id=beatmaker.edm.musicgames.PianoGames')

    button7 = types.InlineKeyboardButton("7",
                                         url='https://play.google.com/store/apps/details?id=com.youmusic.magictiles')

    button8 = types.InlineKeyboardButton("8",
                                         url='https://play.google.com/store/apps/details?id=com.bilkon.easypiano')

    button9 = types.InlineKeyboardButton("9",
                                         url='https://play.google.com/store/apps/details?id=com.rhythmdance.taptile.rt')

    button10 = types.InlineKeyboardButton("10",
                                          url='https://play.google.com/store/apps/details?id=com.rhythm.games.pink.tiles')

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id,
                     # Перша ігра
                     'Назва: ' + str(lift) +
                     '\nРейтинг: ' + str(lift1) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift2) +
                     '\nОбмеження: ' + str(lift3) +
                     '\nЩоб скачати ігру нажми на кнопку 1' +
                     # Друга ігра
                     '\n\nНазва: ' + str(lift4) +
                     '\nРейтинг: ' + str(lift5) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift6) +
                     '\nОбмеження: ' + str(lift7) +
                     '\nЩоб скачати ігру нажми на кнопку 2' +
                     # Третя ігра
                     '\n\nНазва: ' + str(lift8) +
                     '\nРейтинг: ' + str(lift9) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift10) +
                     '\nОбмеження: ' + str(lift11) +
                     '\nЩоб скачати ігру нажми на кнопку 3' +
                     # Четверта ігра
                     '\n\nНазва: ' + str(lift12) +
                     '\nРейтинг: ' + str(lift13) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift14) +
                     '\nОбмеження: ' + str(lift15) +
                     '\nЩоб скачати ігру нажми на кнопку 4' +
                     # П'ята ігра
                     '\n\nНазва: ' + str(lift16) +
                     '\nРейтинг: ' + str(lift17) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift18) +
                     '\nОбмеження: ' + str(lift19) +
                     '\nЩоб скачати ігру нажми на кнопку 5' +
                     # Шоста ігра
                     '\n\nНазва: ' + str(lift20) +
                     '\nРейтинг: ' + str(lift21) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift22) +
                     '\nОбмеження: ' + str(lift23) +
                     '\nЩоб скачати ігру нажми на кнопку 6' +
                     # Сьома ігра
                     '\n\nНазва: ' + str(lift24) +
                     '\nРейтинг: ' + str(lift25) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift26) +
                     '\nОбмеження: ' + str(lift27) +
                     '\nЩоб скачати ігру нажми на кнопку 7' +
                     # Восьма ігра
                     '\n\nНазва: ' + str(lift28) +
                     '\nРейтинг: ' + str(lift29) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift30) +
                     '\nОбмеження: ' + str(lift31) +
                     '\nЩоб скачати ігру нажми на кнопку 8' +
                     # Дев'ята ігра
                     '\n\nНазва: ' + str(lift32) +
                     '\nРейтинг: ' + str(lift33) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift34) +
                     '\nОбмеження: ' + str(lift35) +
                     '\nЩоб скачати ігру нажми на кнопку 9' +
                     # Десята ігра
                     '\n\nНазва: ' + str(lift36) +
                     '\nРейтинг: ' + str(lift37) +
                     '\nНа скількох пристроях скачана ігра: ' + str(lift38) +
                     '\nОбмеження: ' + str(lift39) +
                     '\nЩоб скачати ігру нажми на кнопку 10',
                     reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()

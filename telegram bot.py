import telebot
from googletrans import Translator

TOKEN = "5377628254:AAGluU_Ht4vbDoGk4vZxidYTbzV1lhTw1Zo"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['boshlash'])
def send_welcome(message):
    username = message.from_user.username
    xabar = f'Assalom alaykum, {username} Uz-Rus-Uz botiga xush kelibsiz!'
    xabar += '\nMatningizni yuboring.'
    bot.reply_to(message, xabar)


@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    tarjimon = Translator()
    msg = message.text
    if msg.isascii():
        tarjima = tarjimon.translate(matn, src="uz", dest="rus")
        xabar = tarjima.text
    else:
        tarjima = tarjimon.translate(matn, src="rus", dest="uz")
        xabar = tarjima.text
    bot.reply_to(message, xabar)


bot.polling()


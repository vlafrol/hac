"""
Телеграм бот - GET GIF NOW
Бот обрабатывает сообщения пользователей и возвращает гифку 
"""
import sys
import requests
import telebot
from gif_generator import GifGetter

TELEGRAM_TOKEN = '322265468:AAFStMAbn1rTJaR4kAov7Q9oWh9gPYssPCo'
YANDEX_API_KEY = "trnsl.1.1.20170502T123550Z.39074518419bf48e.b2ba2aba05c21568173b3593b8db4f94a06dde60"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
gif_gen = GifGetter(YANDEX_API_KEY)


@bot.message_handler(content_types=["text"])
def send_gif(message):
    """
    Функция отправляет пользователю ссылку на гифку найденую по его сообщению 
    :param message: 
    :return None: 
    """
    print("Message: " + message.text)
    gif_url = gif_gen.get_gif_by_tag(message.text)
    print("Return gif: " + gif_url)
    bot.send_message(message.chat.id, gif_url)


if __name__ == '__main__':
    print("Start bot!")
    while True:
        try:
            bot.polling(none_stop=True)
        except requests.exceptions.ReadTimeout:
            print('Timeout')
            continue
        except requests.exceptions.ConnectionError:
            print('Connection error! Try to check internet connection')
            sys.exit(1)

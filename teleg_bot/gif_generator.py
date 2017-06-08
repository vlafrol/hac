import re
import requests
from random import randint, seed
from time import time


class GifGetter:
    """
    GiffGetter реалтизует функцию возврата случайной гифки по тегу.
    В качестве БД с гифками импользуется сервис GIPHY.
    Сервис ориентирован на англоязычную аудиторию, поэтому искать гифку по тегам 
    написанных на русском языке может ничего не выдать.
    Для решения данной пороблемы было решено переводить все теги написанные на русском с помощью
    API Яндекс.Переводчик.
    """
    def __init__(self, ya_key):
        """
        :param ya_key (String) - ключ для API Яндекс.Переводчик.
        """
        self.yandex_api_key = ya_key

    def get_gif_by_tag(self, tag):
        """
        Возвращает ссылку на случайную гифку найденную по тегу.
        :argument - tag (String)
        :return - url (String)
        """
        # С помощью регулрных выражений проверяем тег на то написан ли он на русском или нет.
        if re.findall('[а-яА-Я]', tag):
            # Если да, то переводим его.
            tag = self.__translate(tag)

        # Задаем сид для генератора случайных чисел.
        # В качестве параметра берется текущее время, так сид будет всегда разным.
        seed(time())
        # Формируем строку запроса. Добавляем в нее принимаемый функцие тег.
        search_url = "http://api.giphy.com/v1/gifs/search?q={}&api_key=dc6zaTOxFJmzC".format(tag)
        # Делаем запрос.
        request = requests.get(url=search_url)
        # Полученный json с помощью соответсвующей функции преобразуем в словарь
        json = request.json()['data']
        size = len(json)
        # Если ничего вернулось, то функция вернет сообщение о том, что ничего не найдено
        if size < 1:
            return "{} not found =(".format(tag)
        else:
            # Иначе функция вернет случайную ссылку
            return json[randint(0, size - 1)]['images']['original']['url']

    def __translate(self, word):
        """
        Возвращает слово переведеное на русский язык
        :param word: 
        :return string: 
        """
        # Формируем аргументы GET запроса
        data = dict(text=word,
                    lang='en',
                    key=self.yandex_api_key)
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        # Делаем запрос Яндекс.Переводчик-у
        response = requests.post(url, data=data)
        # Возвращаем полученый результат
        return response.json()['text'][0]






import requests
import random
from basic_word import BasicWord


def load_random_word(link):
    """
    Принимает ссылку на json читает из него и возвращает в случайном порядке.
    """
    response = requests.get(link)
    list_words = response.json()
    random.shuffle(list_words)

    for i in list_words:
        random_word = BasicWord(i['word'], i['subwords'])
        return random_word


def main_game(user, random_word):
    """
    Функция принимает экземпляр класса Player и BasicWord
    и запускает цикл игры
    """
    while len(user.user_words) < len(random_word.set_words):
        user_word = (input()).lower()
        if user_word != 'stop':
            if len(user_word) >= 3:
                if user_word in random_word.set_words:
                    if user.chek_user_words(user_word):
                        print('верно')
                        user.add_word_in_list(user_word)
                    else:
                        print('уже использовано')
                else:
                    print('неверно')
            else:
                print('слишком короткое слово')
        else:
            break

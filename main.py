from utils import load_random_word, main_game
from player import Player


def main():
    # Передаем список слов для игры из ссылки в функцию
    random_word = load_random_word('https://jsonkeeper.com/b/LCIJ')
    user_name = input('Ввведите имя игрока ')
    # создаем экземпляр класса Player
    user = Player(user_name)
    # выводим репр из класса Player и BasicWord
    print(user)
    print(random_word)
    # передаем в функцию созданные экземпляры для запуска цикла игры
    main_game(user, random_word)
    print(f'Игра завершена, вы угадали {len(user.user_words)} слов!')


if __name__ == "__main__":
    main()

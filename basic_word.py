class BasicWord:
    def __init__(self, main_word, set_words):
        self.main_word = main_word
        self.set_words = set_words
        self.input_word = None

    def check_word(self):
        """
        проверкf введенного слова в списке допустимых подслов (вернет bool)
        """
        if self.input_word in self.set_words:
            return True
        else:
            return False

    def count_set_words(self):
        """
        подсчет количества подслов (вернет int)
        """
        return len(self.set_words)

    def __repr__(self):
        return f'Составьте 8 слов из слова {self.main_word}\n' \
               f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n' \
               f'Поехали, ваше первое слово?'

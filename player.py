class Player:
    def __init__(self, name, user_words=[]):
        self.name = name
        self.user_words = user_words

    def get_coun_words(self):
        """
        получение количества использованных слов (возвращает int)
        """
        return len(self.user_words)

    def add_word_in_list(self, user_answer):
        """
        добавление слова в использованные слова (ничего не возвращает)
        """
        if self.chek_user_words(user_answer):
            self.user_words.append(user_answer)

    def chek_user_words(self, user_answer):
        """
        проверка использования данного слова до этого (возвращает bool)
        """
        if user_answer not in self.user_words:
            return True
        return False

    def __repr__(self):
        return f'Привет, {self.name}!'

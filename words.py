import random

class WordGenerator:
    def __init__(self):
        from nltk.corpus import words
        self.score = 0
        self.words = words.words()
        self.correct_words = []
        self.current_word = None

    def generate_word(self):
        self.current_word = random.choice(self.words)
        return f'{self.current_word}'

    def check(self, word):
        typed_word = word
        if self.current_word.lower() == typed_word:
            self.correct_words.append(self.current_word)
            self.score += 1
            return True
        return False

    def final_score(self):
        final_score = len(self.correct_words)
        return f'Final Score: {final_score}'


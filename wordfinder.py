"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    >>> wf = WordFinder("/Users/eduardopedroza/downloads/python-oo-practice/./words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    
    def __init__ (self, path):
        self.path = path
        self.words = []
        self.read_words()

    def read_words(self):
        try: 
            with open(self.path, 'r') as file:
                self.words = file.read().splitlines()
            print(f"{len(self.words)} words were read")
        except FileNotFoundError:
            print("File not found")

    def random(self):
        random_int = random.randint(0, len(self.words))
        return self.words[random_int]
    


class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)

    def has_comment_or_blank(self, word):
        return "#" in word or " " in word
    
    def random(self):
        while True:
            random_word = super().random()
            if not self.has_comment_or_blank(random_word):
                return random_word
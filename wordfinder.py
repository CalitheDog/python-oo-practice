"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    '''Finds random words in the dictionary.'''

    def __init__(self, path):
        """Reads dictionary and prints # of items read"""
        path = open('words.txt')
        dict = open(path)
        self.words = self.parse(dict)
        print(f'{len(self.words)} words read')

    def parse(self, dict):
        '''Parses the dict into a list of words.'''
        return [w.strip() for w in dict]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments."""

    def parse(self, dict):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [word.strip() for word in dict
                if word.strip() and not word.startswith("#")]

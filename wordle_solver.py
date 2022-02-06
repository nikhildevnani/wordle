import random
from collections import defaultdict


def get_words_without_letters(letters, words):
    result = []
    for word in words:
        skip_word = False
        for letter in letters:
            if letter in word:
                skip_word = True
                continue
        if not skip_word:
            result.append(word)
    return result


def get_words_with_letter(letters_in_word, word_list):
    result = []
    for word in word_list:
        add_word = True
        for letter in letters_in_word:
            if letter not in word:
                add_word = False
                continue
        if add_word:
            result.append(word)
    return result


def get_words_with_correct_positions(correct_positions, word_list):
    result = []
    for word in word_list:
        add_word = True
        for letter, positions in correct_positions.items():
            if letter not in word:
                add_word = False
                continue
            for position in positions:
                if word[position] != letter:
                    add_word = False
                    continue
        if add_word:
            result.append(word)
    return result


def ignore_wrong_positions(words, wrong_positions):
    result = []
    for word in words:
        add_word = True
        for letter, positions in wrong_positions.items():
            if letter not in word:
                add_word = False
                continue
            for position in positions:
                if word[position] == letter:
                    add_word = False
                    continue
        if add_word:
            result.append(word)

    return result


def count_vowels(word):
    num_vowels = 0
    for char in word:
        if char in "aeiou":
            num_vowels = num_vowels + 1
    return num_vowels


class WordleSolver:

    def __init__(self):

        with open('sgb-words.txt') as f:
            lines = f.read().splitlines()
        self.word_list = lines

    def get_words_with_most_vowels(self):
        vowel_count = defaultdict(list)
        words = self.word_list
        for word in words:
            vowel_count[count_vowels(word)].append(word)
        max_vowels = max(vowel_count.keys())
        return vowel_count[max_vowels]

    """
    correct_positions (dic): containing letter and their right positions
    letters_in_word: list of letter that could be anywhere in the word
    letter_not_in_word: list of letters that are not in the word
    cold_start: True, False
    """

    def solve(self, correct_positions, wrong_positions, letter_not_in_word, cold_start):

        word_list = self.word_list
        if cold_start:
            best_words = self.get_words_with_most_vowels()
            return random.choice(best_words)

        word_list = ignore_wrong_positions(word_list, wrong_positions)
        word_list = get_words_with_correct_positions(correct_positions, word_list)
        word_list = get_words_without_letters(letter_not_in_word, word_list)

        return word_list


wordle = WordleSolver()
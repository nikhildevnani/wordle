import random


class WordleSolver:

    def __init__(self):
        with open('word_list.txt') as f:
            lines = f.read().splitlines()
        self.word_list = lines
        self.get_user_input()

    def update_word_list(self, word, feedback):
        """
        Trim the word list based on the feedback got for current word
        :param word: current word being used to trim the word list
        :param feedback: feedback given for the current word
        :return: nothing, just trim the word list
        """

        dont_skip_letters = self.handle_counts(word, feedback)

        for position, (character, ch_result) in enumerate(zip(word, feedback)):
            # character is not present at all
            if ch_result == '_':
                if character in dont_skip_letters:
                    continue
                self.word_list = [x for x in self.word_list if character not in x]
            # correct position
            if ch_result == '+':
                self.word_list = [x for x in self.word_list if x[position] == character]
            # present but in a different position
            if ch_result == '?':
                self.word_list = [x for x in self.word_list if character in x and x[position] != character]

    def handle_counts(self, word, feedback):
        """
        Deletes word from word list if we can figure out exact count
        :param word: current word being evaluated
        :param feedback: feedback received for the current word
        :return: letters that should not be skipped
        """
        dont_skip_this_letter = set()
        for letter in set(word):
            if word.count(letter) < 2:
                continue
            results = [feedback[position] for position in range(5) if word[position] == letter]
            if results.count('_') != len(results):
                actual_present = len(results) - results.count('_')
                self.word_list = [x for x in self.word_list if x.count(letter) == actual_present]
                dont_skip_this_letter.add(letter)
        return dont_skip_this_letter

    def get_user_input(self):
        """
        Function that interacts with the user
        :return:
        """
        print("############ WELCOME ############")
        print(
            "For every guess, please enter a 5 letter response where you'd enter:\n '_' if the letter at the position "
            "does not exist in the word,\n '+' if both the letter and the position were guessed correctly,\n '?' if "
            "the letter exists in the word but not in the same position")

        user_feedback = input('Select mode, auto or manual:')


        if user_feedback == 'auto':
            guess = 'audio'
            print("My guess is:", guess, end="\n")
            user_feedback = input('Enter your feedback:\n')
            while user_feedback != "stop":
                self.update_word_list(guess, user_feedback)
                if self.word_list:
                    print("Remaining words:", len(self.word_list), end="\n")
                else:
                    print('No words match your criteria!\n')
                    break
                guess = random.choice(self.word_list)
                print("My guess is:", guess, end="\n")
                user_feedback = input('Enter your feedback: ')
                self.word_list = [x for x in self.word_list if x != guess]

            print("Remaining words:", self.word_list)
        else:
            while user_feedback != "stop":
                guess = input("Enter your word:\n")
                feedback = input('Enter your feedback:\n')
                self.update_word_list(guess, feedback)
                print("Remaining words:", self.word_list)




if __name__ == "__main__":
    wordle = WordleSolver()

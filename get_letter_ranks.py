from collections import defaultdict

with open('word_list.txt') as f:
    lines = f.read().splitlines()

letter_count = defaultdict(int)
for letter in 'abcdefghijklmnopqrstuvwxyz':
    for word in lines:
        if letter in word:
            letter_count[letter] += 1

letters = [letter for letter, count in sorted(letter_count.items(), key=lambda x: x[1], reverse=True)]
letter_ranks = dict()

for index, letter in enumerate(letters):
    letter_ranks[letter] = 25 - index

print(letter_ranks)

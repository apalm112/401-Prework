"""Codecademy Unit 3: Pyglatin Part 10."""

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original
    word = word.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print(new_word)
else:
    print 'empty'

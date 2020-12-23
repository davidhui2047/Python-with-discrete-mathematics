'''
KIT103/KMA155 Programming Assignment 5: Permutations and Combinations
Submission script

Name: chiu fan hui
ID: 497790

Enter your answers to each question below either by replacing the
value None with a short piece of Python code that will calculate or
generate the answer or, in the case of Question 4, replacing the
body of the two functions with your implementation. After answering
a question run this script and test your implementation in the
IPython console.
'''

from itertools import combinations, permutations, product
from scipy.special import comb, factorial
def fact(n):
    '''Returns the exact, integer value of n!'''
    return factorial(n, exact=True)

# Answers that can be calculated by single lines of code will be stored in
# this dictionary. Question 4's answers will be in the form of functions.
value_ans = {}

# Question 1: Permutations (1 mark)

value_ans['q1 a'] = 4**3
value_ans['q1 b'] = { ''.join(p) for p in product('AUGC', repeat = 3) }
value_ans['q1 c'] = fact(6) / fact(6-3)
value_ans['q1 d'] = { p for p in permutations(['hop', 'pot', 'top', 'cop', 'lop', 'mop'], 3) }


# Question 2: Combinations (1 mark)

letters, numbers = {'R', 'D'}, {2, 4}
droids = [ '{}{}{}{}'.format(*c) for c in product(letters, numbers, letters, numbers) ]
# If you use this list then your answers will be in the same order as the test program
star_trek_species = [ 'Andoran', 'Bajoran', 'Cardassian', 'Ferenghi',
                      'Human', 'Klingon', 'Romulan', 'Vulcan' ]

value_ans['q2 a'] = comb(16, 4, True)
value_ans['q2 b'] = { c for c in combinations(droids, 4) }
value_ans['q2 c'] = comb(len(star_trek_species), 2, True)
value_ans['q2 d'] = { c for c in combinations(star_trek_species, 2) }


# Question 3: You choose which (2 marks)

from string import ascii_uppercase
dvds = set( ascii_uppercase[:17] ) #'A' through 'Q'

value_ans['q3 a'] = fact(len(dvds))/fact(len(dvds)-len(dvds))
value_ans['q3 b'] = { c for c in combinations(dvds, 4) }
value_ans['q3 c'] = { p for p in product(dvds, repeat=3) }
value_ans['q3 d'] = 17**3


# Question 4: Do words sow rows or swords? (1 mark)

def string_permutations(word, length):
    '''Returns the set of all `length`-permutations of the letters in `word`.'''
    #Question 4a: Replace none with an expression to generate all strings that are length-permutations of the letters in word
    return { ''.join(c) for c in permutations(word, length) }

def subanagrams(word, length):
    '''Returns the set of all `length` sub-anagrams of `word` (provided
    it is between 2 and 10 characters long). Behaviour is unspecified
    if the word is shorter or longer than that, or if `length` is longer
    than `len(word)`.
    '''
    #Question 4b: Replace None with an expression to generate all length-permutations of word and filter that to contain only valid words
    return string_permutations(word, length) & word_sets[length]

# Needed for Question 4

from os.path import isfile

def load_words():
    name = 'dictionary2-10.txt'
    if isfile(name):
        all_words = [ l.rstrip() for l in open(name, 'r') ]
        as_lists = { size : [ word for word in all_words if len(word) == size ] for size in range(2, 11) }
        as_sets = { size : (set(words) if words else None) for size, words in as_lists.items() }
        return as_lists, as_sets
    return None, None

word_lists, word_sets = load_words()
# Usage examples (note that you do not necessarily need to use both word_lists and word_sets):
# word_lists[2] is a list of the two-letter words
# word_sets[9] is a set of the nine-letter words

# End of things needed for Question 4

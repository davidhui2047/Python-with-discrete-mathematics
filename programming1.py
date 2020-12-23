'''
KIT103/KMA155 Programming Assignment 1: Sets
Submission script

Name: Replace with your name
ID: Replace with your student ID

Enter your answers to each question below, replacing None with the
code requested. Question 1 part a should be stored in ans['Q1 a'] and
so on. You can use the display_answers() function from inside the
IPython console to show the result of your answers when you run this
script to evaluate all your answers.
A suggestion: Run the script first, then work out the answers in
the IPython interactive console before pasting them back here.
'''

ans = {} #an empty dictionary of answers
def display_answers(show_all=True):
    '''Prints the calculated answers to all questions.
    This function is included because it may be useful to you in
    checking your answers, but you are not required to use it.
    '''
    for a in sorted(ans):
        if show_all or ans[a] is not None:
            print('{}: {}'.format(a, 'unanswered' if ans[a] is None else ans[a]))


# Question 1: Set literals

ans['Q1 a'] = {2, 4, 6, 8, 10}
ans['Q1 b'] = {'Ada', 'Alan', 'Claude', 'George'}
ans['Q1 c'] = {'a', 'e', 'i', 'o', 'u'}

# Question 2: Set comprehensions

ans['Q2 a'] = {6*x for x in range(1, 8)}
ans['Q2 b'] = {x**3 for x in range(1, 7)}
ans['Q2 c'] = {x for x in list('woolloomooloo')}

# Question 3: Relationships

# Given these definitions provide code to answer the questions from the assignment sheet.
animals = {'cow', 'gorilla', 'hermit crab', 'human', 'iguana', 'mola mola', 'parrot', 'spider', 'tunicate'}
tetrapods = {'cow', 'gorilla', 'human', 'iguana', 'mola mola', 'parrot'}
chordates = {'cow', 'gorilla', 'human', 'iguana', 'mola mola', 'parrot', 'tunicate'}
mammals = {'cow', 'gorilla', 'human'}
pets = {'cow', 'hermit crab', 'iguana', 'parrot', 'rock', 'spider'}
can_swim = {'cow', 'human', 'iguana', 'mola mola'}

ans['Q3 a'] = pets < animals
ans['Q3 b'] = pets <= can_swim 
ans['Q3 c'] = mammals <= tetrapods

# Question 4: Set membership

ans['Q4 a'] = chordates - tetrapods
ans['Q4 b'] = can_swim | pets 
ans['Q4 c'] = pets & can_swim - mammals

# Question 5: Combinations

# Given these definitions, generate the combinations requested in the assignment sheet.
suspects = { 'Miss Scarlett', 'Colonel Mustard', 'Professor Plum' }
weapons = { 'candlestick', 'lead pipe', 'revolver' }
rooms = { 'kitchen', 'conservatory', 'library', 'dining room' }

ans['Q5 a'] = {(s, r) for s in suspects for r in rooms}
ans['Q5 b'] = {(w1, w2) for w1 in weapons for w2 in weapons} 
ans['Q5 c'] = {(s, w, r) for s in suspects for w in weapons for r in rooms}

# Question 6: Bags & Bitsets
# When checking these, note that parts (b)-(e) will look like normal decimal numbers,
# even though you will have entered binary literals in your answers to (b)-(d).
# A binary literal is just another way of expressing an integer value.

ans['Q6 a'] = bag = { 'house': 2, 'car': 3, 'key': 1}
ans['Q6 b'] = 0b00110
ans['Q6 c'] = 0b11010
ans['Q6 d'] = 0b11100
ans['Q6 e'] = ans['Q6 b'] & ans['Q6 c']

#End of answers

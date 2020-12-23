'''
KIT103/KMA155 Programming Assignment 2: Logic
Submission script

Name: Chiu Fan Hui
ID: 497790

Enter your answers to each question below by completing each function
or, in the case of Question 4a, filling in the Karnaugh map.
After answering a question run this script and test your implementation.
'''


# Question 1: Riding the Logic Circuit

REJECT, FIND_ADULT, ACCEPT = 'Sorry, you cannot ride', 'Find an adult', 'You can ride'

def q1_coaster_check(height, age, has_adult):
    '''Returns one of three string messages depending on whether a
    person can ride the Logic Circuit or not.
    Parameters:
    height - integer height in cm
    age - integer age in years
    has_adult - True iff the person is accompanied by an adult
    '''
    if height < 120 or height > 200 or age < 7:
        return REJECT
    elif age >= 7 and age <= 9 and has_adult == False:
        return FIND_ADULT
    else:
        return ACCEPT


# Question 2: Implementing predicates as functions

def q2_a(a, b):
    return not (a and b) and (a or b)

def q2_b(a, b, c, d):
    return a and (not b or not c or not d)

def q2_c(a):
    return not a and a

def q2_d(a, b, c):
    return (a or b) and (b or c)


# Question 3: Simplifying predicates

def q3_a(a, b):
    return (a ^ b)

def q3_b(a, b, c, d):
    return a and not (b and c and d)

def q3_c(a):
    return False

def q3_d(a, b, c):
    return b or (a and c)


# Question 4: Simplifying a predicate using a Karnaugh map

#Part a: Letter Detector Karnaugh Map --- replace the appropriate 0 entries with 1 (representing True)
q4_kmap = [
#cd\ab
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 1]
]

#Part b: The detector function
def q4_acme_letter_detector(a, b, c, d):
    '''Returns True iff the curves present resemble a letter, False otherwise.'''
    #Your task is to replace this with an equivalent but simpler expression.
    # If you wish to split your expression over multiple lines then use a
    # slash \ at the end of each line, as below.
    return (a and not b and d) or \
           (not b and c and not d) or \
           (c and d)

#End of answers

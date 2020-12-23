'''
KIT103/KMA155 Programming Assignment 3: Number Theory part 1
Submission script

Name: Chiu Fan Hui
ID: 497790

Enter your answers to each question below by completing each
function. After answering a question run this script and test
your implementation in the IPython console.
'''


# Question 1: Divisibility of really, really big integers (2 marks)

def divisible_by_2(s):
    '''Returns True if the number represented by the string s is
    divisible by 2, False otherwise.'''
    return s[-1] in '02468'

def divisible_by_3(s):
    '''Returns True if the number represented by the string s is
    divisible by 3, False otherwise.'''
    total = 0
    for a in s:
        total += int(a)
    return total % 3 == 0

def divisible_by_4(s):
    '''Returns True if the number represented by the string s is
    divisible by 4, False otherwise.'''
    return int(s[-2:]) % 4 == 0

def divisible_by_11(s):
    '''Returns True if the number represented by the string s is
    divisible by 11, False otherwise.'''
    totalA = 0
    totalB = 0
    for a in s[0::2]:
        totalA += int(a)
    for b in s[1::2]:
        totalB += int(b)
    return (totalA - totalB) % 11 == 0


# Question 2: GCD from a prime factorisations (2 marks)

from collections import Counter

def q2_prime_factor_gcd(a, b):
    '''Returns gcd(a, b), calculated from their prime factorisations.'''
    listA = factor_list(a)
    listB = factor_list(b)
    aBag = Counter(listA)
    bBag = Counter(listB)
    exps = aBag & bBag
    gcd = 1
    for p in exps:
        gcd = gcd * p**exps[p]
    return gcd


# Question 3: Are a and b coprime (i.e., relatively prime)? (1 mark)

# Implement your additional helper function here

def q3_coprime(a, b):
    '''Returns True if a and b are coprime, False otherwise.'''
    return gcd(a, b) == 1

def gcd(a, b):
    while a > 0:
        b, a = a, b % a
    return b

# End of answers


# Provided functions

from math import floor, sqrt

def primes(n):
    '''Returns the set of primes between 2 and n, inclusive.'''
    primes = set(range(2, n+1))
    for k in range(2, floor(sqrt(n))+1):
        if k in primes:
            primes.difference_update( range(k**2, n+1, k) )
    return primes

def primes_list(n):
    '''Returns a sorted list of primes between 2 and n, inclusive.'''
    return sorted(primes(n))

def factor_list(n):
    '''Returns the list of prime factors of n.'''
    factors = []
    iprimes = iter( primes_list(n) )
    while n > 1:
        p = next(iprimes)
        while n % p == 0:
            n = n // p
            factors.append(p)
    return factors

# End of provided functions

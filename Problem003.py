# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:53:11 2016
Functions to compute largest prime factor of a given number
@author: michael
"""

import math
import time

def isPrime(x):
    for y in range(2,int(math.sqrt(x))+1):
        if x % y == 0:
            return False
    return True
    
    
def factors(x):
    factors = []
    for y in range (2,int(math.sqrt(x))+1):
        if y in factors:
            return factors
        if x % y == 0:
            factors.append(y)
    return factors
    
def primefactors(x):
    facts = factors(x)
    pfact = []
    for fact in facts:
        if isPrime(fact):
            pfact.append(fact)
    return pfact

def maxprime(x):    
    a = time.time()
    maxprim = max(primefactors(x))
    print(time.time() - a)
    return maxprim

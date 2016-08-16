# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 19:11:23 2016

@author: michael
"""

def isPalindrome(x):
    num = str(x)
    return num == num[::-1]

pprods = []
    
for x in range(999,99,-1):
    for y in range(999,99,-1):
        if isPalindrome(x*y):
            pprods.append(x*y)
        
max(pprods)

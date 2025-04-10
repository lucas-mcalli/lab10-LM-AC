# https://github.com/lucas-mcalli/lab10-LM-AC.git
# Partner 1: Lucas McAllister
# Partner 2: Aidan Chiodo

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a*b
def div(a, b):
    if b == 0:
        raise ValueError
    return a/b
def logarithm(a, b):
    if b <=0 or b == 1 or a <=0:
        raise ValueError
    return math.log(a,b)
def exp(a, b):
    return a**b

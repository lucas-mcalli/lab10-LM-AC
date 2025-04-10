import math

def add(a, b):
    return a+b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    try:
        return b/a
    except ZeroDivisionError as e:
        return e

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError as e:
        return e

def exp(a, b):
    return a**b

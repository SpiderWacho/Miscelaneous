#!Python 3

import re

def passwordDetection(password):
    security = 0
    passRegexLenght = re.compile(r'(\w){8,}')
    passRegexMinus = re.compile(r'([a-z])')
    passRegexMayus = re.compile(r'([A-Z])')
    passRegexDigit = re.compile(r'(\d)+')
    if passRegexLenght.search(password) != None:
       security = security + 1
    else:
       security = security - 1
       print('Password must be at least 8 characters long')
    if passRegexMinus.search(password) and passRegexMayus.search(password) != None:
       security = security + 1
    else:
       security = security - 1
       print('Password must contain mayus and minus')
    if passRegexDigit.search(password) != None:
       security = security + 1
    else:
       security = security - 1
       print('Password must contain a numeric digit')
    
    if security == 3:
        print('Your password is strong')
    else:
        print('weak password')

passwordDetection('u222312312D312')
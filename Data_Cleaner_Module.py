# Data Cleaner Module
# all float
# data validation for categories
# capitalize (hackerrank practice)
# false dates (7/11 is not a date its a store)

import pandas as pd
from pandas import DataFrame

def convert_float(val) -> float:
    '''Converts value to float'''
    return float(val)

def convert_str(val) -> str:
    '''Converts value to string'''
    return str(val)

def capitalize(s:str) -> str:
    '''Capitalizes the first letter of each word in string s'''
    result = []
    next_is_start = True
    for c in s:
        if next_is_start and c.isalpha():
            new_c = c.upper()
        else:
            new_c = c.lower()

        result.append(new_c)

        if c == ' ':
            next_is_start = True
        else:
            next_is_start = False
    return ''.join(result)


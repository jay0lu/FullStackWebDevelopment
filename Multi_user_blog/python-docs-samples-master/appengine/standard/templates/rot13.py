"""
ROT13 function
Coding on Python2.7
"""

import string

def rot13Trans(text):
    rot13 = string.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return string.translate(text, rot13)

# print(rot13Trans(',<>abc'))

'''
# For python3.5 
def rot13Trans(text):
    rot13 = str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return text.translate(rot13)
'''

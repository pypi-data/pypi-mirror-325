#!/usr/bin/python
"""This is a four-function calculator for use by Roman accountants.

It will accept input in Roman or Arabic digits.
You can use + - * / functions.
Do not expect algabric results. (Al-Jabara was Arabic. That came later.)
but you can type "II+II" and get "IV".

Type "quit" when you want to exit.
"""
import sys, os
parent = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, parent)  # to find the local module
from romanclass import Roman, InvalidRomanNumeralError, OutOfRangeError

def cvt(s):
    try:
        r = Roman(s.strip())
    except InvalidRomanNumeralError: # say: "I do not understand"
        print('Ego operor non agnosco "%s"' % s.strip())
        r = Roman(0)
    return r

print('\n\n',__doc__)

while True:    
    # prompt "put number here:"
    line = input('procer numerus hic:').strip()
    if line[:4].lower() == 'quit' or line[:4].lower() == 'exit':
        break
    if len(line) == 0:
        print('Type "exit" to exit, or type a simple expression')
    try:
        addends = line.split('+')  # try brute force parsing for addition
        if len(addends) == 2:
            print(cvt(addends[0]) + cvt(addends[1]))
        else:
            subtrahends = line.split('-') # how about subtraction?
            if len(subtrahends) == 2:
                print(cvt(subtrahends[0]) - cvt(subtrahends[1]))
            else:
                multiplicands = line.split('*') # maybe it is multiplication?
                if len(multiplicands) == 2:
                    print(cvt(multiplicands[0]) * cvt(multiplicands[1]))
                else:
                    dividends = line.split('/') # or perhaps division?
                    if len(dividends) == 2:
                        print(cvt(dividends[0]) // cvt(dividends[1]))
                    else:    #  just convert/normalize
                        print(cvt(line))
    except OutOfRangeError: # say: "Number is too large."
        print('Numerus est magnus.')
print()  # make a clean exit

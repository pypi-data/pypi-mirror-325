""" A class defining a subset of integers as Roman Numerals
defining their input and output in Roman notation
(rather than arabic decimal notation as is usual for integers)
the internal value is in binary. """ 
# Roman Number Converter & Class 
#   original version by James T. Dennis (c)2001 <jimd at starshine.org>
#
# refactored 2009-02-03 by Vernon Cole
#  (added class definition and made into a module.
#  (added support for unicode, extending the range to 0 <= n < 700000.
#  (added ZERO, which may be encoded as 0, '', 'N', 'nvlla' or 'NULLA' -- will print out as 'Nulla'
#  (will accept 'J' as a last digit which is = 'I'
#
# update 2009-11-23 borrowing code from roman.py by Mark Pilgrim
# updote 2025-01-29 Python3.12 installable, drop Python2
#
#  some parts copyright 2001 (Mark Pilgrim) using Python License
#  This module is (almost) a superset Mark's, with a very similar API --
#    the fromRoman() and toRoman() methods use the same arguments.
#  For most users expecting Mark's module, this will operate as expected.
#
# This module should feel much like the built-in decimal module.
#  
# Idiosycrasy warning:  the order of arguments to binary math functions
#  IS significant -- the result will be the type of the LEFT argument.
#>>> two = roman.Roman(2)
#>>> two + 2
#Roman(4)
#>>> 2 + two
#4
#  (note: the Roman(100000), 50000, 10000 and Roman(5000) characters are Unicode
#  (code points, so you must have a correct font such as "Code2000"
#  (to display values > 3999. Some consoles, such as Windows cmd, cannot
#  (print them. 
#
#  (refactored fromRoman function -
#  (will silently accept almost any jumble of IVXLCDM
#  (or will accept any Unicode code point which is a numeric letter
#  (  -- i.e. where unicodedata.numeric() is defined
#  (No attempt is made to demand modern normalization of input strings.
#  (see http://en.wikipedia.org/wiki/Roman_numerals

#  This code is released and licensed under the terms of the MIT license
#  or, at the user's option, the BSD license as specified at the
#  following URL:
#   http://www.freebsd.org/copyright/freebsd-license.html
#
#   In any event it is provided free of charge, "as-is" and wholly
#   without any warranty.   Use it, mangle it, incorporate it into
#   any software that will have it.

 #works on python 3.4 and up

__author__ = "Vernon Cole <vernondcole at gmail.com>"
__version__ = "1.2.3"

try:
    import unicodedata
except ImportError:
    unicodedata = NotImplemented  # some older Python versions

#Define exceptions
class RomanError(ValueError): pass
class OutOfRangeError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

class Roman(int):     #define "Roman" as a subset of int
    """Class Roman is a subset of "int"
    define by: Roman(123) or Roman('123') or Roman('CXXIII')"""    
    def __new__(cls,N=0):
        if isinstance(N,str): #if arg is a string
            try:
                n = int(N)              # may be a decimal string
            except ValueError:
                try:
                    n = fromRoman(N)    # or may be a Roman number
                except InvalidRomanNumeralError:
                        raise InvalidRomanNumeralError('Not a valid Roman or Arabic number:"%s"'%N)
        else:
            n = int(N)                     # or a numeric value
        if n < 0 or n > 699999:
            raise OutOfRangeError('Cannot store "%s" as Roman' % repr(N))
        return int.__new__(cls,n)           # store as an int

    def __str__(self):
        return toRoman(self.__int__())      # print out as Roman number

    def __repr__(self):
        return 'Roman(%d)' % self.__int__() # reveal what's inside

    def __len__(self):
        return len(toRoman(self.__int__()))
    def __add__(self,other):                # so that II + II = IV
        return Roman(self.__int__() + other)
    def __sub__(self,other):
        return Roman(self.__int__() - other)
    def __mul__(self,other):
        return Roman(self.__int__() * other)
    def __floordiv__(self,other):
        return Roman(self.__int__() // other)
    def __getattr__(self,name):   # in case someone tries roman.value
        if name == 'value':
            return self.__int__()
        raise AttributeError('Type Roman does not define "%s"'%name)
    
# Convert natural numbers to their Roman numeral representations 
# and vice versa.

# First we associate a dictionary of numeric values with
# their Roman numeral (string token) equivalents as follows:
_Rom={ # Unicode code points for large Roman Numerals
 "\u2188":100000, #looks like a letter I overprinted with three coincentric circles -- http://commons.wikimedia.org/wiki/File:U%2B2188.svg
 "\u2182\u2188":90000,
 "\u2187":50000,  #looks like half of u2188 or 3 D's -- http://commons.wikimedia.org/wiki/File:U%2B2187.svg
 "\u2182\u2187":40000,
 "\u2182":10000,  #looks like two coincentric circles on a vertical bar -- http://www.fileformat.info/info/unicode/char/2182/index.htm
 "M\u2182":9000,
 "\u2181":5000, #looks like two overprinted D's -- http://www.fileformat.info/info/unicode/char/2181/index.htm
 "M\u2181":4000,
 "M":1000,   # regular ASCII letters for regular size Roman Numerals
 "CM":900,
 "D": 500,
 "CD":400, 
 "C": 100,
 "XC": 90,
 "L":  50,
 "XL": 40,
 "X":  10,
 "IX":  9,
 "V":   5,
 "IV":  4,
 "I":   1,
 "J":1 #used as the final 'I' in some ancient texts
 }
# We also create a sequence tuple in descending order.
# It's for iterating over the value list in a convenient order.

# We include the two-letter tokens (IV, CM, CD, XC, etc) because
# it makes our main conversion loop simpler (as we'll see).
# Basically it means we can loop straight through without having
# to encode a bunch of parsing conditionals (the sequence, including
# the two-letter tokens already incorporates most of the parsing
# rules for roman numeral strings).  

_RomSeq = ( "\u2188","\u2182\u2188","\u2187","\u2182\u2187","\u2182","M\u2182", "\u2181", "M\u2181",
           "M", "CM", "D", "CD", "C", "XC", "L", "XL", 
       "X", "IX", "V", "IV", "I", "J" )
# This allows us to convert from binary to Roman in about 7 lines 
# of code; and from Roman back to binary less than 20

def toRoman(N):
    "format a binary number as a Roman Unicode string."
    if N == 0: return 'Nulla' # printable value for Zero is "Nulla"
    n = int(N)  # make a copy of the value, because we are going to modify it.
    if n < 0 or n > 699999:
        raise OutOfRangeError('Cannot convert "%s" to Roman' % repr(N))
    result=""
    #   Our result starts as an empty string.
    # We interate over the sequence of Roman numeral component strings
    # if the corresponding value (the value associated with "M" or "CM", etc)
    # is greater than our number, we append that string to
    # our result and subtract its corresponding value from our copy of n
    for s in _RomSeq:  # try each possible component string
        while n >= _Rom[s]: # until its value is larger than the remaining value
            result = result + s # string concatenation (not addition)
            n -= _Rom[s]        # mathmatical subtraction
    return result

def fromRoman(S):
    "Convert a Roman numeral string to binary"
    if type(S) is Roman: return int(S) #in case it already IS Roman
    result=0
    # Start by converting to upper case for convenience
    us = S.strip().upper()
    try:
        s = str(us)
    except UnicodeEncodeError: # IronPython bug
        s = us
    #test for zero
    if s == '' or s == 'N' or s[:5] == 'NULLA':  # Latin for "nothing"
        return 0
# This simplified algorithm (V.Cole) will correctly convert any correctly formed
# Roman number. It will also convert lots of incorrectly formed numbers, and will
# accept any combination of ASCII 'MCDLXVI' and Unicode numeric code points.
    held = 0    # this is the memory for the previous Roman digit value
    for c in s:    #this will get the value of a sequence of Unicode numeric points
        try:        # may be a normal alphabetic character
            val = _Rom[c]  #pick the value out of the dict
        except KeyError: # may be a Unicode character with a value
            try: 
                val = int(unicodedata.numeric(c))  # retrieve the value from the Unicode chart
            except Exception:
                raise InvalidRomanNumeralError('incorrectly formatted Roman Numeral '+repr(S)) 

        if val > held:    # if there was a smaller value to the left, subtract it
            result -= held
        else:             # otherwise add it
            result += held 
        held = val        # try this loop's letter value on the next loop
    result += held  #the last letter value is always added
    return result

def toUnicodeRoman(N):
    """format a binary number into a true Unicode Roman string.
    so you get \\u2160 rather than "I" etc."""
    n = int(N)
    ##if n == 0: return u'\u0bbf' # ideographic number Zero
    if 0 < n <= 12:
        return chr(0x215f + n) # I to XII as a single code point
    s = toRoman(N)
    # put in the true Unicode points rather than the ASCII look alikes
    s = s.replace('I','\u2160').replace('V','\u2164').replace('X','\u2169')
    s = s.replace('L','\u216c').replace('C','\u216d').replace('D','\u216e').replace('M','\u216f')
    return s

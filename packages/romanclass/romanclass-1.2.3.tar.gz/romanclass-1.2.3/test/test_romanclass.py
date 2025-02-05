#!/usr/bin/env python3

import unittest
import unicodedata
import sys, os
mommy = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, mommy)  # use the local copy, not some system version

from romanclass import Roman, fromRoman, toRoman, toUnicodeRoman, InvalidRomanNumeralError, OutOfRangeError

# ----------------------------------------- Test program follows ---------------------------------
# The following simply creates a list by converting to a roman number *and back*.
class TheBigTest(unittest.TestCase):
    def test_it(self):
        longest = ""
        mini = Roman()
        bigList = []
        i = Roman(0)
        while i < 4007:
            rs = Roman(i)
            j = fromRoman(rs)
            assert i == j, '%d -> %s -> %s' % (i, repr(rs), j)

            if len(rs) > len(longest):  # Roman has a len() method
                longest = rs
            mini = min(mini, i)  # integer functions should work
            bigList.append(rs)
            i += 1
        maxi = max(bigList)
        print('The longest number between %s and ' % mini, end=' ')
        try:
            print(maxi)
        except UnicodeEncodeError:
            print(repr(maxi))
        print('was "%s" which is "%d" in Arabic' % (longest, longest))
        assert fromRoman(longest) == 3888

        ## -- now test some sample convertions ---------------------------------------------
        assert fromRoman('IIIJ') == 4  # test that the archaic construction works
        try:
            s = toRoman(-1)
            assert False, "toRoman(-1) should fail"
        except OutOfRangeError:
            pass
        try:
            s = Roman(1000000)
            assert False, "roman.Roman(10000000) should fail"
        except OutOfRangeError:
            pass
        try:
            i = fromRoman('XXY')
            assert False, "fromRoman('XXY') should fail"
        except InvalidRomanNumeralError:
            pass
        assert toRoman(0) == 'Nulla'  # zero really needs to be printable
        assert toRoman('3') == 'III'  # Arabic string literals work
        assert toRoman(12.1) == 'XII'  # float numbers are truncated
        assert Roman('DCLXVI') == 666  # class instances work as integers
        r = Roman('MDCCCCX')  # malformed input - as 1910 on Admiralty Arch in London.
        if str(r) != r.__str__():
            print('Error in type object use of str(). [IronPython?]')
        assert r.__str__() == 'MCMX'  # output is normalized Roman form
        two = Roman(2)
        four = two + two  # addition works
        assert four.__str__() == 'IV'  # result prints as a Roman numeral
        eight = two * four  # multiplication works
        assert eight.__str__() == 'VIII'
        sixteen = Roman('XVI')
        assert sixteen.value == 16  # if a programmer tries, we can get the .value
        assert sixteen // Roman('V') == Roman('III')  # floor division works
        assert (sixteen - four).__str__() == 'XII'  # subtraction works
        assert Roman('\u217b') == 12  # unicode Roman number 'xii' as a single charactor
        assert Roman('\u2167') == 8  # unicode Roman number 'VIII'
        assert Roman('\u2160\u216f') == 999  # unicode 'IM' which is a badly formed number
        assert fromRoman('\u2182\u2182\u2182\u2182\u2181MMMCCLXIJ') == 48262
        assert fromRoman('\u2188\u2182\u2187\u2181v') == 145005

        assert toUnicodeRoman(166447) == \
               '\u2188\u2187\u2182\u2181\u216f\u216d\u216e\u2169\u216c\u2164\u2160\u2160'
        assert toUnicodeRoman(12) == '\u216b'

        nl = [5000, 10000, 50000, 100000]
        for nb in nl:
            n = toRoman(nb)
            try:
                nn = unicodedata.numeric(n)
                name = unicodedata.name(n)
            except ValueError:
                nn = '<<ValueError -- Python issue 6383 still exists>>'
                name = ''
            except NameError:
                name = 'unicodedata not implemented.'
                nn = '[Iron Python?]'
            print(n, name, nn)
            try:
                print('unicode=', n.encode('unicode_escape'))
            except Exception:
                print('  (cannot be printed here)')

if __name__ == "__main__":
    unittest.main()

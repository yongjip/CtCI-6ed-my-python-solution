# O(NlogN)
# Given two strings, write a method to decide if one is a permutation of the other.
import unittest
from collections import defaultdict, Counter


def check_permutation(string):
    # function checks if a string is permutation of another
    if len(string) != 2 or len(string[0]) != len(string[1]):
        return False
    checker = {0: Counter(), 1: Counter()}
    for i, string_i in enumerate(string):
        for letter in string_i:
            checker[i][letter] += 1
    if checker[0] == checker[1]:
        return True
    return False



class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]

    def test_cp(self):
        # true check
        for test_string in self.dataT:
            actual = check_permutation(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = check_permutation(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()

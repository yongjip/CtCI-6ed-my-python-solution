# O(N)
import unittest
from collections import Counter


'''Check if a string can converted to another string with a single edit'''

def one_away(s1, s2):
    checker = {0: Counter(), 1: Counter()}
    for i, string in enumerate([s1, s2]):
        for letter in string:
            checker[i][letter] += 1
    for key, value in checker[0].items():
        checker[1][key] -= value
    abs_difference = sum([abs(val) for val in checker[1].values()])
    if abs_difference == 1:
        return True
    if sum(checker[1].values()) == 0:
        return True
    return False



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('palesss', 'plesss', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'ble', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

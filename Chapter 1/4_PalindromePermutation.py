# O(N)
import unittest
from collections import defaultdict

def pal_perm(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    letters = defaultdict(int)
    phrase = phrase.replace(' ','').lower()
    for letter in phrase:
        letters[letter] += 1
    remainder = 0
    for value in letters.values():
        remainder += value % 2
    if len(phrase) % 2 == 1 and remainder == 1:
        return True
    elif remainder == 0:
        return True
    return False




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

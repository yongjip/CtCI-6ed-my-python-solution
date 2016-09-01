# O(N)
'''
Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring("waterbottle" if a rotation of "erbottlewat")
'''

import unittest

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        start_part = s1[:i]
        end_part = s1[i:]
        if isSubstring(s2, start_part) and isSubstring(s2, end_part):
            return True
    return False

def isSubstring(string, sub):
    if string.find(sub) == -1:
        return False
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('water','', False)
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

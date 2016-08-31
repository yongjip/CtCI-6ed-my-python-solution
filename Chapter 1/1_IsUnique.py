# O(N)
#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
import unittest


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 127:
        return False

    char_set = [False for _ in range(128)]
    for letter in string:
        val = ord(letter) - 1
        if char_set[val]:
            return False
        char_set[val] = True
    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()

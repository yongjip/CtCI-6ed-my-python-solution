# O(N)
import unittest


def string_compression(string):
    last_letter = ''
    count = 1
    out = ''
    if len(set(list(string))) == len(list(string)):
        return string
    for letter in string:
        if last_letter == letter:
            count += 1
        else:
            out += last_letter + str(count)
            last_letter = letter
            count = 1
    if last_letter == letter:
        out += letter + str(count)
    return out[1:]




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

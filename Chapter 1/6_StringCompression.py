# O(N)
'''
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. if the "compressed" string would not become smaller than the origical string, yourmethold should return the original string. You can assume the string has only uppercase and lowercase letters.
'''
import unittest


def string_compression(string):
    if len(set(string)) == len(string):
        return False
    last_letter = string[0]
    count = 1
    out = ''
    for letter in string[1:]:
        if last_letter == letter:
            count += 1
        else:
            out += last_letter + str(count)
            last_letter = letter
            count = 1
    out += letter + str(count)
    if len(out) < len(string):
        return out
    return string




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef'),
        ('aassssc','a2s4c1')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

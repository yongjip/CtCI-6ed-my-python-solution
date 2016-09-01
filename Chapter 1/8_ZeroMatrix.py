# O(MxN)
'''
Write an algorithm such that if an element in an MxN matrics is 0, it's entire row and column are set to 0.
'''
import unittest
import copy

def zero_matrix(matrix):
    output = copy.deepcopy(matrix)
    row_len = len(matrix[0])
    zero_vector = [0 for _ in range(row_len)]
    for ii, row_ii in enumerate(matrix):
        for jj, value_jj in enumerate(row_ii):
            if value_jj == 0:
                output[ii] = copy.copy(zero_vector)
                for row in output:
                    row[jj] = 0
    return output


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

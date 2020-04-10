# O(NxN)
import unittest


def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    x_len = len(matrix)
    y_len = len(matrix[0])
    result = [[0 for x in range(x_len)] for x in range(y_len)] 
    for i in range(y_len):
        for j in range(x_len):
            #result[4][0...5] = matrix[0...5][0]
            result[j][i] = matrix[y_len-1-i][j]
    return result

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

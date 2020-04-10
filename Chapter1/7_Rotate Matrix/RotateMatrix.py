# O(NxN)
import unittest

# Example turn in place:
    # [0][0]-> [0][4] -> [4][4] ->[4][0] -> [0][0]
    # [0][1]-> [1][4] -> [4][3] ->[3][0] -> [0][1]
    # [0][2]-> [2][4] -> [4][2] ->[2][0] -> [0][2]
    # [0][3]-> [3][4] -> [4][1] ->[1][0] -> [0][3]
    # [0][4]-> [4][4] -> [4][0] ->[0][0] -> [0][4]

    # [1][1]-> [1][3] -> [3][3] ->[3][1] -> [1][1]
    # [1][2]-> [2][3] -> [3][2] ->[2][1] -> [1][2]
    # [1][2]-> [2][3] -> [3][2] ->[2][1] -> [1][2]

def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    x_len = len(matrix)-1
    y_len = len(matrix[0])-1

    i_range = int(len(matrix)/2)
    j_range = int(len(matrix[0])/2) + len(matrix[0])%2

    for i in range(i_range):
        for j in range(j_range):
            temp = matrix[j][y_len-i]
            matrix[j][y_len-i] = matrix[i][j]

            temp2 = matrix[y_len-i][x_len-j]
            matrix[y_len-i][x_len-j]=temp

            temp3 =matrix[x_len-j][i]
            matrix[x_len-j][i] = temp2

            matrix[i][j] = temp3
    return matrix

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

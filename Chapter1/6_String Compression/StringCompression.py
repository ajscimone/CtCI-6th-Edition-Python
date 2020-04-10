# O(N)
import unittest


def string_compression(string):
    prev = string[0]
    count = 1
    result = ""
    for i in range(1, len(string)):
        if string[i] == prev:
            count +=1
        else:
            result = result + prev + str(count)
            prev = string[i]
            count = 1
    result = result + prev + str(count)
    if len(string) <= len(result):
        return string
    return result


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

# O(N)
import unittest

def string_rotation(s1, s2):
    for i in range(len(s1)):
        top = s1[0:1]
        s1 = s1[1:]
        s1 += top
        if s1 == s2:
            return True
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

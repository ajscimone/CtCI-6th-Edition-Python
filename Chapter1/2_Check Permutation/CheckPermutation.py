# O(N)
import unittest
from collections import Counter


def check_permutation(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    return str1==str2

def check_permutation_faster(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        stack = list(str1)
        for letter in str2:
            if letter in stack:
                stack.remove(letter)
    if len(stack)==0:
        return True
    return False

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation_faster(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation_faster(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

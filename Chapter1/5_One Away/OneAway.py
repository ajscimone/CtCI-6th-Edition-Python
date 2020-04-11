# O(N)
import unittest
import string

def one_away(s1, s2):
    '''Check if a string can converted to another string with a single edit'''
    if not s1 and len(s2)==1:
        return True
    elif len(s1) == 1 and len(s2) == 1:
        return True
    elif s1[:-1] == s2 or s1 == s2[:-1]:
        return True
    elif s1 == s2:
        return True

    alphabet = list(string.ascii_lowercase)
    for i in range(len(s1)):
        if i < len(s2) and s1[i] != s2[i]:
            for letter in alphabet:
                #inert
                if s1[:i] + letter + s1[i:] == s2:
                    return True
                #replace
                if s1[:i] + letter + s1[i+1:] == s2:
                    return True
            #remove
            if s1[:i-1] + s1[i:] == s2:
                return True
    return False
    

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

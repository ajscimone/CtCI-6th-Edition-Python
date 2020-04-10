# O(N)
import unittest


def pal_perm(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    phrase=sorted(phrase.lower())
    while phrase[0] == ' ':
        phrase.pop(0)
    stack = []
    for l in phrase:
        if not stack:
            stack.append(l)
        elif stack[len(stack)-1] == l:
            stack.pop()
        else:
            stack.append(l)
    if len(stack) > 1:
        return False
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

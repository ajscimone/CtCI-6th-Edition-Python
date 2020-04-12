# O(N)
import unittest

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    while string[-1] == ' ':
        string.pop()
    string = "".join(string)
    string = string.replace(' ', "%20")
    return list(string)

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

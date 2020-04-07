# O(N)
import unittest


def unique(string):
    if not string:
        return True
    strlist = []
    for l in string:
        strlist.append(l)
    strset = set(strlist)
    for item in strset:
        if item in strlist:
            strlist.pop(strlist.index(item))
    if strlist:
        return False
    return True

def unique_nodatastructure(string):
    if not string:
        return True
    string = sorted(list(string))
    prev = string[0]
    for i in range(1, len(string)):
        if string[i] == prev:
            return False
        prev = string[i]
    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)
    
    def test_unique_nods(self):
        # true check
        for test_string in self.dataT:
            actual = unique_nodatastructure(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique_nodatastructure(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()

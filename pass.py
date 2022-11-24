#!/opt/homebrew/bin/python3

import unittest
from isPerfsqr import isSqr


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(isSqr(625), 1)

    def testCase2(self):
        self.assertEqual(isSqr(441), 1)

    def testCase3(self):
        self.assertEqual(isSqr(196), 1)

    def testcase4(self):
        self.assertEqual(isSqr(961), 1)

    def testcase5(self):
        self.assertEqual(isSqr(1), 1)

    def testcase5(self):
        self.assertEqual(isSqr(100), 1)


if __name__ == '__main__':
    unittest.main()

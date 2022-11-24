#!/usr/bin/python3
import unittest
from isPerfsqr import isSqr


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(isSqr(624), 1)

    def testCase2(self):
        self.assertEqual(isSqr(442), 1)

    def testCase3(self):
        self.assertEqual(isSqr(197), 1)

    def testcase4(self):
        self.assertEqual(isSqr(906), 1)

    def testcase5(self):
        self.assertEqual(isSqr(12), 1)

    def testcase6(self):
        self.assertEqual(isSqr(10), 1)


if __name__ == '__main__':
    unittest.main()

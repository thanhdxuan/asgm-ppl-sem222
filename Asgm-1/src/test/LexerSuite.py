import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("12_124_123", "12124123,<EOF>", 101))
    def test2(self):
        self.assertTrue(TestLexer.test("12_124_123.473", "12124123.473,<EOF>", 102))
    def test3(self):
        self.assertTrue(TestLexer.test("12E10", "12E10,<EOF>", 103))
    def test4(self):
        self.assertTrue(TestLexer.test("12E-10", "12E-10,<EOF>", 104))
    def test5(self):
        self.assertTrue(TestLexer.test("12_124_123", "12124123,<EOF>", 105))
    def test6(self):
        self.assertTrue(TestLexer.test("125.e10", "125.e10,<EOF>", 106))

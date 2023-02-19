import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"heheha\"", "heheha,<EOF>", 101))
        #test escape sequences
        self.assertTrue(TestLexer.test("\"heh\teha\"", "heh\teha,<EOF>", 102))
        self.assertTrue(TestLexer.test("\"heh\\eha\"", "heh\eha,<EOF>", 103))
        self.assertTrue(TestLexer.test("\"heh\\\"eha\"", "heh\\\"eha,<EOF>", 104))

import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("{1, 2, 3, 4, 5, 6}", "{1, 2, 3, 4, 5, 6},<EOF>", 101))
        self.assertTrue(TestLexer.test("{\"Kangxi\", \"Yongz\\lheng\", \"Qianlong\"}", "{\"Kangxi\", \"Yongzheng\", \"Qianlong\"},<EOF>", 102))


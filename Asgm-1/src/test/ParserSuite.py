import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """test declare var"""
        input = """a,b,c: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_simple_program_1(self):
        """test funct decla"""
        input = """fact: function integer (n : integer) {body}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_simple_program_2(self):
        """test funct decla"""
        input = """fact: function integer () {body}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_simple_program_3(self):
        """test funct decla"""
        input = """fact: function integer (out n: hehe) {body}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_simple_program_4(self):
        """test funct decla"""
        input = """fact: function integer (out n: float) {body}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

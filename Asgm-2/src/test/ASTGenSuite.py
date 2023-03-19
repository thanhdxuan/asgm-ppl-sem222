import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    #NOTE -  TEST VAR DECLARE SHORT FORM
    def test_short_vardecl_1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 101))
    def test_short_vardecl_2(self):
        input = """x: string;"""
        expect = str(Program([VarDecl("x", StringType())]))
        self.assertTrue(TestAST.test(input, expect, 102))
    def test_short_vardecl_3(self):
        input = """x, y, z: float;"""
        expect = str(Program([
            VarDecl("x", FloatType()),
            VarDecl("y", FloatType()),
            VarDecl("z", FloatType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 103))
    
    def test_short_vardecl_4(self):
        input = """x, y, z: boolean;"""
        expect = str(Program([
            VarDecl("x", BooleanType()),
            VarDecl("y", BooleanType()),
            VarDecl("z", BooleanType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 104))
    def test_short_vardecl_5(self):
        input = """x, y, z: array[1, 2] of integer;"""
        expect = str(Program([
            VarDecl('x', ArrayType([1, 2], IntegerType())),
            VarDecl('y', ArrayType([1, 2], IntegerType())),
            VarDecl('z', ArrayType([1, 2], IntegerType())),
        ]))
        self.assertTrue(TestAST.test(input, expect, 105))
    def test_short_vardecl_6(self):
        input = """x, y: array[1] of string;"""
        expect = str(Program([
            VarDecl('x', ArrayType([1], StringType())),
            VarDecl('y', ArrayType([1], StringType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 106))
    def test_short_vardecl_7(self):
        input = """x: array[1] of boolean;"""
        expect = str(Program([
            VarDecl('x', ArrayType([1], BooleanType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 107))
    def test_short_vardecl_8(self):
        input = """x: auto;"""
        expect = str(Program([
            VarDecl('x', AutoType())
        ]))
        self.assertTrue(TestAST.test(input, expect, 108))
    def test_short_vardecl_9(self):
        input = """x: array[1] of integer;"""
        expect = str(Program([
            VarDecl('x', ArrayType([1], IntegerType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 109))


#NOTE -  TEST VAR DECLARE FULL FORM
    def test_full_vardecl_1(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 201))
    def test_full_vardecl_2(self):
        input = """x, y, z: integer = 1, 2 * 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, BinExpr(*, IntegerLit(2), IntegerLit(2)))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 202))
    def test_full_vardecl_3(self):
        input = """x: integer = 1 * 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 203))
    def test_full_vardecl_4(self):
        input = """x: integer = 1 + 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, IntegerLit(1), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 204))
    def test_full_vardecl_5(self):
        input = """x, y: integer = 12, foo(x, y);"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	VarDecl(y, IntegerType, FuncCall(foo, [Id(x), Id(y)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 205))
    def test_full_vardecl_6(self):
        input = """x: integer = -12;"""
        expect = """Program([
	VarDecl(x, IntegerType, UnExpr(-, IntegerLit(12)))
])"""
        self.assertTrue(TestAST.test(input, expect, 206))
    def test_full_vardecl_7(self):
        input = """x, y: integer = -12, 2 / 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, UnExpr(-, IntegerLit(12)))
	VarDecl(y, IntegerType, BinExpr(/, IntegerLit(2), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 207))
    def test_full_vardecl_8(self):
        input = """x: integer = y;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(y))
])"""
        self.assertTrue(TestAST.test(input, expect, 208))
    def test_full_vardecl_9(self):
        input = """x, y, z: float = 1.5e10, 100e-10, .1e12;"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(15000000000.0))
	VarDecl(y, FloatType, FloatLit(1e-08))
	VarDecl(z, FloatType, FloatLit(100000000000.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 209))


#NOTE - TEST EXPRESSIONS
    def test_full_vardecl_expr_1(self):
        input = """x, y: integer = 12 * 2 + 1, foo(x, y);"""
        expect = str(Program([
            VarDecl('x', IntegerType(), BinExpr('+', BinExpr('*', IntegerLit(12), IntegerLit(2)), IntegerLit(1))),
            VarDecl('y', IntegerType(), FuncCall('foo', [Id('x'), Id('y')]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 211))
    def test_full_vardecl_expr_2(self):
        input = """x: string = "asfsd23" :: "a1231212";"""
        expect = str(Program([
            VarDecl('x', StringType(), BinExpr('::', StringLit('asfsd23'), StringLit('a1231212'))),
        ]))
        self.assertTrue(TestAST.test(input, expect, 212))
    def test_full_vardecl_expr_3(self):
        input = """x: boolean = (foo(x) / 2 * 3 - 2 == 6) % 3 * 2 && (1 + 2 == 3);"""
        # foo(x)
        expect = str(Program([
	VarDecl('x', BooleanType(), BinExpr('&&', BinExpr('*', BinExpr('%', BinExpr('==', 
            BinExpr('-', BinExpr('*', BinExpr('/', FuncCall('foo', [Id('x')]), IntegerLit(2)), 
            IntegerLit(3)), IntegerLit(2)), IntegerLit(6)), IntegerLit(3)), 
            IntegerLit(2)), BinExpr('==', BinExpr('+', IntegerLit(1), IntegerLit(2)), IntegerLit(3))))
]))
        self.assertTrue(TestAST.test(input, expect, 213))
    def test_full_vardecl_expr_4(self):
        input = """x: string = ("thanh" :: "vip") :: "max";"""
        expect = str(Program([
            VarDecl('x', StringType(), BinExpr('::', BinExpr('::', StringLit('thanh'), StringLit('vip')), StringLit('max')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 214))
    def test_full_vardecl_expr_5(self):
        input = """x: integer = arr[1, 2];"""
        expect = str(Program([
            VarDecl('x', IntegerType(), ArrayCell('arr', [IntegerLit(1), IntegerLit(2)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 215))

    def test_full_vardecl_expr_6(self):
        input = """x: array [1, 3] of integer = {1, 2, 3};"""
        expect = """Program([
	VarDecl(x, ArrayType([1, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 216))
    def test_full_vardecl_expr_7(self):
        input = """arr: array[1, 3] of integer = {1, 2, 3};
        x, y: array [1, 3] of integer = {1, 2, 3}, {foo(x), 5 * 2, arr[0, 2]};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([1, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(x, ArrayType([1, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(y, ArrayType([1, 3], IntegerType), ArrayLit([FuncCall(foo, [Id(x)]), BinExpr(*, IntegerLit(5), IntegerLit(2)), ArrayCell(arr, [IntegerLit(0), IntegerLit(2)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 217))
    def test_full_vardecl_expr_8(self): #NOTE - Test mang hai chieu
        input = """arr: array[2, 3] of integer = {{1, 2}, {1, 3}, {3, 4}};
        x, y: array [1, 3] of integer = {1, 2, 3}, {foo(x), 5 * 2, arr[0, 2]};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]))
	VarDecl(x, ArrayType([1, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(y, ArrayType([1, 3], IntegerType), ArrayLit([FuncCall(foo, [Id(x)]), BinExpr(*, IntegerLit(5), IntegerLit(2)), ArrayCell(arr, [IntegerLit(0), IntegerLit(2)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 218))
    def test_full_vardecl_expr_9(self): #NOTE - Test mang da chieu
        input = """arr: array[2, 3, 4] of integer = { 
                     { {3, 4, 2, 3}, {0, -3, 9, 11}, {23, 12, 23, 2} },
                     { {13, 4, 56, 3}, {5, 9, 3, 5}, {3, 1, 4, 9} }
                 };
        """
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3, 4], IntegerType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(0), UnExpr(-, IntegerLit(3)), IntegerLit(9), IntegerLit(11)]), ArrayLit([IntegerLit(23), IntegerLit(12), IntegerLit(23), IntegerLit(2)])]), ArrayLit([ArrayLit([IntegerLit(13), IntegerLit(4), IntegerLit(56), IntegerLit(3)]), ArrayLit([IntegerLit(5), IntegerLit(9), IntegerLit(3), IntegerLit(5)]), ArrayLit([IntegerLit(3), IntegerLit(1), IntegerLit(4), IntegerLit(9)])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 219))
    def test_full_vardecl_expr_10(self): #NOTE - Test mang da chieu
        input = """
        x : array[3] of integer = {1, 2, 3};
        arr: array[2, 3, 4] of integer = { 
                     { {3, abc * xyz, 2, 3}, {0, -3, 9, 11}, {foo(x, y), 12, 23, 2} },
                     { {13, 4, x[2], 3}, {5, -(15 / 2 % 4) * 9, 3, 5}, {x[0], 1, 4, 9} }
                 };
        """
        expect = """Program([
	VarDecl(x, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(arr, ArrayType([2, 3, 4], IntegerType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(3), BinExpr(*, Id(abc), Id(xyz)), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(0), UnExpr(-, IntegerLit(3)), IntegerLit(9), IntegerLit(11)]), ArrayLit([FuncCall(foo, [Id(x), Id(y)]), IntegerLit(12), IntegerLit(23), IntegerLit(2)])]), ArrayLit([ArrayLit([IntegerLit(13), IntegerLit(4), ArrayCell(x, [IntegerLit(2)]), IntegerLit(3)]), ArrayLit([IntegerLit(5), BinExpr(*, UnExpr(-, BinExpr(%, BinExpr(/, IntegerLit(15), IntegerLit(2)), IntegerLit(4))), IntegerLit(9)), IntegerLit(3), IntegerLit(5)]), ArrayLit([ArrayCell(x, [IntegerLit(0)]), IntegerLit(1), IntegerLit(4), IntegerLit(9)])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 220))


#NOTE - TEST DECLARE FUNCITON
    def test_declare_func_1(self):
        #test: declare function - test assign_stmt
        input = """x: integer = 12;
        fact: function void(x: integer) inherit abc {
            x[2,3] = 122;
            
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(2), IntegerLit(3)]), IntegerLit(122))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 301))
    def test_declare_func_2(self):
        #test: declare function - test param
        input = """x: integer = 12;
        fact: function void(x: integer) inherit abc {
            x[2,3] = 122;
            
        }
        foo: function integer(){}
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(2), IntegerLit(3)]), IntegerLit(122))]))
	FuncDecl(foo, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect, 302))

    def test_declare_func_3(self):
        #test: declare function - test param
        input = """x: integer = 12;
        fact: function boolean (out x: boolean, inherit delta: integer, inherit out delta: integer) {}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, BooleanType, [OutParam(x, BooleanType), InheritParam(delta, IntegerType), InheritOutParam(delta, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect, 303))
    def test_declare_func_4(self):
        #test: declare function - test param
        input = """x: integer = 12;
        fact: function boolean (out x: string, inherit delta: array [2, 3] of boolean, inherit out delta: integer) {}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, BooleanType, [OutParam(x, StringType), InheritParam(delta, ArrayType([2, 3], BooleanType)), InheritOutParam(delta, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect, 304))
    def test_declare_func_5(self):
        #test: declare function - test param
        input="""
        foo: function string () {
            a = arr[c];
            arr[1] = 9;
        }
        fact: function void (out x: boolean) {}
        fact1: function array [1, 2] of integer () inherit fact {}
        """
        expect = """Program([
	FuncDecl(foo, StringType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(arr, [Id(c)])), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), IntegerLit(9))]))
	FuncDecl(fact, VoidType, [OutParam(x, BooleanType)], None, BlockStmt([]))
	FuncDecl(fact1, ArrayType([1, 2], IntegerType), [], fact, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect, 305))


#NOTE - TEST STATEMENTS
    
    #NOTE - TEST VAR DECLARE STATEMENTS
    def test_statements_1(self):
        input = """x: integer = 12;
        fact: function void(x: integer) inherit abc {
            x = 122 % (2 + 2 * (2 / 18_23 - 2));
            y = "234" :: "23423";
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(Id(x), BinExpr(%, IntegerLit(122), BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(2), BinExpr(-, BinExpr(/, IntegerLit(2), IntegerLit(1823)), IntegerLit(2)))))), AssignStmt(Id(y), BinExpr(::, StringLit(234), StringLit(23423)))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 311))
    def test_statements_2(self):
        input = """x: integer = 12;
        fact: function void(x: integer) inherit abc {
            z = - ( 12 * 12 + 2 / 3 ) + (-2);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(Id(z), BinExpr(+, UnExpr(-, BinExpr(+, BinExpr(*, IntegerLit(12), IntegerLit(12)), BinExpr(/, IntegerLit(2), IntegerLit(3)))), UnExpr(-, IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 312))
    def test_statements_3(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            temp: integer;
            temp = true;
            temp = !(12 == 3 % 4);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(temp, IntegerType), AssignStmt(Id(temp), BooleanLit(True)), AssignStmt(Id(temp), UnExpr(!, BinExpr(==, IntegerLit(12), BinExpr(%, IntegerLit(3), IntegerLit(4)))))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 313))
    def test_statements_4(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            temp: boolean;
            temp1: integer;
            temp2: integer = 1_458_000;
            x, y: integer = 12, foo(x, y);
            temp = !(12 == 3 % 4);
            f1, f0, f2: float = 1.5e10, 100e-10, .1e12;
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(temp, BooleanType), VarDecl(temp1, IntegerType), VarDecl(temp2, IntegerType, IntegerLit(1458000)), VarDecl(x, IntegerType, IntegerLit(12)), VarDecl(y, IntegerType, FuncCall(foo, [Id(x), Id(y)])), AssignStmt(Id(temp), UnExpr(!, BinExpr(==, IntegerLit(12), BinExpr(%, IntegerLit(3), IntegerLit(4))))), VarDecl(f1, FloatType, FloatLit(15000000000.0)), VarDecl(f0, FloatType, FloatLit(1e-08)), VarDecl(f2, FloatType, FloatLit(100000000000.0))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 314))
    def test_statements_5(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            temp: boolean;
            temp2: string = "1_458_000";
            arr: array [4, 5] of integer;
            arr: array [1, 2] of integer = {1 * 2, 2 % 2};
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(temp, BooleanType), VarDecl(temp2, StringType, StringLit(1_458_000)), VarDecl(arr, ArrayType([4, 5], IntegerType)), VarDecl(arr, ArrayType([1, 2], IntegerType), ArrayLit([BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(%, IntegerLit(2), IntegerLit(2))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 315))
    def test_statements_6(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            temp: boolean;
            temp: boolean = !!!63;
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(temp, BooleanType), VarDecl(temp, BooleanType, UnExpr(!, UnExpr(!, UnExpr(!, IntegerLit(63)))))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 316))
        
    #NOTE - TEST IF STATEMENTS

    def test_statements_6(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            foo: integer;
            if (foo % 2 == 0) {
                foo = foo - 1;
                foo1: integer = foo;
            }
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(foo, IntegerType), IfStmt(BinExpr(==, BinExpr(%, Id(foo), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(foo), BinExpr(-, Id(foo), IntegerLit(1))), VarDecl(foo1, IntegerType, Id(foo))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 321))
    def test_statements_7(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            foo: integer;
            if (foo % 2 == 0) {
                foo = foo - 1;
                foo1: integer = foo;
            }
            else {
                foo = foo / 2 + 1;
                temp: boolean = !foo;
            }
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(foo, IntegerType), IfStmt(BinExpr(==, BinExpr(%, Id(foo), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(foo), BinExpr(-, Id(foo), IntegerLit(1))), VarDecl(foo1, IntegerType, Id(foo))]), BlockStmt([AssignStmt(Id(foo), BinExpr(+, BinExpr(/, Id(foo), IntegerLit(2)), IntegerLit(1))), VarDecl(temp, BooleanType, UnExpr(!, Id(foo)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 322))
    def test_statements_8(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            foo: integer;
            if (foo % 2 == 0) {
                foo = foo - 1;
                foo1: integer = foo;
            }
            t = !(arr[2] < 10);
        }
        temp: integer;
        temp1: string = "121";
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(foo, IntegerType), IfStmt(BinExpr(==, BinExpr(%, Id(foo), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(foo), BinExpr(-, Id(foo), IntegerLit(1))), VarDecl(foo1, IntegerType, Id(foo))])), AssignStmt(Id(t), UnExpr(!, BinExpr(<, ArrayCell(arr, [IntegerLit(2)]), IntegerLit(10))))]))
	VarDecl(temp, IntegerType)
	VarDecl(temp1, StringType, StringLit(121))
])"""
        self.assertTrue(TestAST.test(input,expect, 323))

    ##NOTE - TEST FOR STATEMENTS
    def test_statements_9(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            y = 0;
            for (y = 1, y < 3, y + 1) {
                if (y % 2 == 0) printInteger(4_51_2);
                else printFloat(4e-2);
            }
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(Id(y), IntegerLit(0)), ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(<, Id(y), IntegerLit(3)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(y), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, IntegerLit(4512)), CallStmt(printFloat, FloatLit(0.04)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 324))
    def test_statements_10(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            for (y = 1, y < 3, y + 1) printFloat(124.122);
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(<, Id(y), IntegerLit(3)), BinExpr(+, Id(y), IntegerLit(1)), CallStmt(printFloat, FloatLit(124.122)))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 325))
    def test_statements_11(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            for (y = 1, !foo(y) == true, y + 1) printFloat(124.122);
            y: integer;
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(==, UnExpr(!, FuncCall(foo, [Id(y)])), BooleanLit(True)), BinExpr(+, Id(y), IntegerLit(1)), CallStmt(printFloat, FloatLit(124.122))), VarDecl(y, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input,expect, 326))
    def test_statements_11_1(self):
        input = """main: function void () {
            for(arr[0, 1] = 1 + 3, arr[0, 1] > 0, arr[0, 1] * 2){
                printString("Hello World");
                for(i = 0, i < n, i - 1) printInteger(1);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), BinExpr(+, IntegerLit(1), IntegerLit(3))), BinExpr(>, ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), IntegerLit(0)), BinExpr(*, ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), IntegerLit(2)), BlockStmt([CallStmt(printString, StringLit(Hello World)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(-, Id(i), IntegerLit(1)), CallStmt(printInteger, IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    #NOTE - TEST WHILE STATEMENTS
    def test_statements_12(self):
        input = """y: integer;
        fact: function void(x: integer) inherit abc {
            y = 0;
            while (y < 4) {
                if (y % 2 == 0) printInteger(4_51_2);
                else printFloat(4e-2);
                y = y - 1;
            }
        }
        """
        expect = """Program([
	VarDecl(y, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(Id(y), IntegerLit(0)), WhileStmt(BinExpr(<, Id(y), IntegerLit(4)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(y), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, IntegerLit(4512)), CallStmt(printFloat, FloatLit(0.04))), AssignStmt(Id(y), BinExpr(-, Id(y), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 331))
    def test_statements_13(self):
        input = """y: integer;
        fact: function void(x: integer) inherit abc {
            y = 0;
            while (y < 4) {
                if (y % 2 == 0) printInteger(4_51_2);
                else printFloat(4e-2);
                y = y - 1;
            }
        }
        """
        expect = """Program([
	VarDecl(y, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(Id(y), IntegerLit(0)), WhileStmt(BinExpr(<, Id(y), IntegerLit(4)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(y), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, IntegerLit(4512)), CallStmt(printFloat, FloatLit(0.04))), AssignStmt(Id(y), BinExpr(-, Id(y), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 332))
    def test_statements_14(self):
        input="""test: function void () {
            do {
            } while (a == b);
        }"""
        expect = """Program([
	FuncDecl(test, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
    def test_statements_15(self):
        input="""test: function void () {
            do {
                while (y < 4) {
                if (y % 2 == 0) printInteger(4_51_2);
                else printFloat(4e-2);
                y = y - 1;
            }
            } while (a == b);
        }"""
        expect = """Program([
	FuncDecl(test, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([WhileStmt(BinExpr(<, Id(y), IntegerLit(4)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(y), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, IntegerLit(4512)), CallStmt(printFloat, FloatLit(0.04))), AssignStmt(Id(y), BinExpr(-, Id(y), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
    #NOTE -  BREAK STATEMENTS
    def test_statements_16(self):
        input="""test: function void () {
            do {
                if (a == 0) break;
            }
            while (a == b);
        }"""
        expect = """Program([
	FuncDecl(test, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    def test_statements_17(self):
        input="""test: function void () {
            do {
                if (a == 0) break;
                else continue;
            }
            while (a == b);
        }"""
        expect = """Program([
	FuncDecl(test, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BreakStmt(), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
    def test_statements_18(self):
        input="""test: function void () {
            do {
                A();
                B(12, 48);
            }
            while (a == b);
        }"""
        expect = """Program([
	FuncDecl(test, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([CallStmt(A, ), CallStmt(B, IntegerLit(12), IntegerLit(48))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
    def test_statements_19(self):
        input="""
        test: function integer () {
            for (y = 1, y < 12, y + 3) {
                if (y == 4) return y;
            }
            return 4 % 3;
        }"""
        expect = """Program([
	FuncDecl(test, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(<, Id(y), IntegerLit(12)), BinExpr(+, Id(y), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(==, Id(y), IntegerLit(4)), ReturnStmt(Id(y)))])), ReturnStmt(BinExpr(%, IntegerLit(4), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_statements_20(self):
        input="""
        test: function integer () {
            for (y = 1, y < 12, y + 3) {
                if (y == 4) return y;
            }
            return foo(12);
        }"""
        expect = """Program([
	FuncDecl(test, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(<, Id(y), IntegerLit(12)), BinExpr(+, Id(y), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(==, Id(y), IntegerLit(4)), ReturnStmt(Id(y)))])), ReturnStmt(FuncCall(foo, [IntegerLit(12)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
    ##NOTE - TEST SPECIAL FUNCTION
    def test_special_func_1(self):
        input="""test: function void () {
            readInteger();
            printInteger(2);
            readFloat();
            printFloat(3223.001);
            readBoolean();
            printBoolean(true);
            readString();
            super(12 % 23, 3 * 3);
            preventDefault();
        }"""
        expect = """Program([
	FuncDecl(test, VoidType, [], None, BlockStmt([CallStmt(readInteger, ), CallStmt(printInteger, IntegerLit(2)), CallStmt(readFloat, ), CallStmt(printFloat, FloatLit(3223.001)), CallStmt(readBoolean, ), CallStmt(printBoolean, BooleanLit(True)), CallStmt(readString, ), CallStmt(super, BinExpr(%, IntegerLit(12), IntegerLit(23)), BinExpr(*, IntegerLit(3), IntegerLit(3))), CallStmt(preventDefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))
    def test_special_func_2(self):
        input="""test: function void () {
            x = readInteger();
            y = printInteger(2);
            z = readFloat();
            h = printFloat(3223.001);
            k = readBoolean();
            a = printBoolean(true);
            o = readString();
            d = super(12 % 23, 3 * 3);
            a = preventDefault();
        }"""
        expect = """Program([
	FuncDecl(test, VoidType, [], None, BlockStmt([AssignStmt(Id(x), FuncCall(readInteger, [])), AssignStmt(Id(y), FuncCall(printInteger, [IntegerLit(2)])), AssignStmt(Id(z), FuncCall(readFloat, [])), AssignStmt(Id(h), FuncCall(printFloat, [FloatLit(3223.001)])), AssignStmt(Id(k), FuncCall(readBoolean, [])), AssignStmt(Id(a), FuncCall(printBoolean, [BooleanLit(True)])), AssignStmt(Id(o), FuncCall(readString, [])), AssignStmt(Id(d), FuncCall(super, [BinExpr(%, IntegerLit(12), IntegerLit(23)), BinExpr(*, IntegerLit(3), IntegerLit(3))])), AssignStmt(Id(a), FuncCall(preventDefault, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 402))
    ##NOTE - END TEST
    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 403))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 404))



#FIXME - COPY
#NOTE -  TEST VAR DECLARE SHORT FORM
    def test_short_vardecl_1_1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 1))
    def test_short_vardecl_2_1(self):
        input = """x: string;"""
        expect = str(Program([VarDecl("x", StringType())]))
        self.assertTrue(TestAST.test(input, expect, 2))
    def test_short_vardecl_3_1(self):
        input = """x, y, z: float;"""
        expect = str(Program([
            VarDecl("x", FloatType()),
            VarDecl("y", FloatType()),
            VarDecl("z", FloatType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 3))
    
    def test_short_vardecl_4_1(self):
        input = """x, y, z: boolean;"""
        expect = str(Program([
            VarDecl("x", BooleanType()),
            VarDecl("y", BooleanType()),
            VarDecl("z", BooleanType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 4))
    def test_short_vardecl_5_1(self):
        input = """x, y, z: array[1, 2] of integer;"""
        expect = str(Program([
            VarDecl('x', ArrayType([1, 2], IntegerType())),
            VarDecl('y', ArrayType([1, 2], IntegerType())),
            VarDecl('z', ArrayType([1, 2], IntegerType())),
        ]))
        self.assertTrue(TestAST.test(input, expect, 5))
    def test_short_vardecl_6_1(self):
        input = """x, y: array[1] of string;"""
        expect = str(Program([
            VarDecl('x', ArrayType([1], StringType())),
            VarDecl('y', ArrayType([1], StringType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 6))
    def test_short_vardecl_7_1(self):
        input = """x: array[1] of boolean;"""
        expect = str(Program([
            VarDecl('x', ArrayType([1], BooleanType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 7))
    def test_short_vardecl_8_1(self):
        input = """x: auto;"""
        expect = str(Program([
            VarDecl('x', AutoType())
        ]))
        self.assertTrue(TestAST.test(input, expect, 8))
    def test_short_vardecl_9_1(self):
        input = """x: array[1] of integer;"""
        expect = str(Program([
            VarDecl('x', ArrayType([1], IntegerType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 9))


#NOTE -  TEST VAR DECLARE FULL FORM
    def test_full_vardecl_1_1(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 11))
    def test_full_vardecl_2_1(self):
        input = """x, y, z: integer = 1, 2 * 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, BinExpr(*, IntegerLit(2), IntegerLit(2)))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 12))
    def test_full_vardecl_3_1(self):
        input = """x: integer = 1 * 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 13))
    def test_full_vardecl_4_1(self):
        input = """x: integer = 1 + 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, IntegerLit(1), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 14))
    def test_full_vardecl_5_1(self):
        input = """x, y: integer = 12, foo(x, y);"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	VarDecl(y, IntegerType, FuncCall(foo, [Id(x), Id(y)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 15))
    def test_full_vardecl_6_1(self):
        input = """x: integer = -12;"""
        expect = """Program([
	VarDecl(x, IntegerType, UnExpr(-, IntegerLit(12)))
])"""
        self.assertTrue(TestAST.test(input, expect, 16))
    def test_full_vardecl_7_1(self):
        input = """x, y: integer = -12, 2 / 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, UnExpr(-, IntegerLit(12)))
	VarDecl(y, IntegerType, BinExpr(/, IntegerLit(2), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 17))
    def test_full_vardecl_8_1(self):
        input = """x: integer = y;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(y))
])"""
        self.assertTrue(TestAST.test(input, expect, 18))
    def test_full_vardecl_9_1(self):
        input = """x, y, z: float = 1.5e10, 100e-10, .1e12;"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(15000000000.0))
	VarDecl(y, FloatType, FloatLit(1e-08))
	VarDecl(z, FloatType, FloatLit(100000000000.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 19))


#NOTE - TEST EXPRESSIONS
    def test_full_vardecl_expr_1_1(self):
        input = """x, y: integer = 12 * 2 + 1, foo(x, y);"""
        expect = str(Program([
            VarDecl('x', IntegerType(), BinExpr('+', BinExpr('*', IntegerLit(12), IntegerLit(2)), IntegerLit(1))),
            VarDecl('y', IntegerType(), FuncCall('foo', [Id('x'), Id('y')]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 21))
    def test_full_vardecl_expr_2_1(self):
        input = """x: string = "asfsd23" :: "a1231212";"""
        expect = str(Program([
            VarDecl('x', StringType(), BinExpr('::', StringLit('asfsd23'), StringLit('a1231212'))),
        ]))
        self.assertTrue(TestAST.test(input, expect, 22))
    def test_full_vardecl_expr_3_1(self):
        input = """x: boolean = (foo(x) / 2 * 3 - 2 == 6) % 3 * 2 && (1 + 2 == 3);"""
        # foo(x)
        expect = str(Program([
	VarDecl('x', BooleanType(), BinExpr('&&', BinExpr('*', BinExpr('%', BinExpr('==', 
            BinExpr('-', BinExpr('*', BinExpr('/', FuncCall('foo', [Id('x')]), IntegerLit(2)), 
            IntegerLit(3)), IntegerLit(2)), IntegerLit(6)), IntegerLit(3)), 
            IntegerLit(2)), BinExpr('==', BinExpr('+', IntegerLit(1), IntegerLit(2)), IntegerLit(3))))
]))
        self.assertTrue(TestAST.test(input, expect, 23))
    def test_full_vardecl_expr_4_1(self):
        input = """x: string = ("thanh" :: "vip") :: "max";"""
        expect = str(Program([
            VarDecl('x', StringType(), BinExpr('::', BinExpr('::', StringLit('thanh'), StringLit('vip')), StringLit('max')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 24))
    def test_full_vardecl_expr_5_1(self):
        input = """x: integer = arr[1, 2];"""
        expect = str(Program([
            VarDecl('x', IntegerType(), ArrayCell('arr', [IntegerLit(1), IntegerLit(2)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 25))

    def test_full_vardecl_expr_6_1(self):
        input = """x: array [1, 3] of integer = {1, 2, 3};"""
        expect = """Program([
	VarDecl(x, ArrayType([1, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 26))
    def test_full_vardecl_expr_7_1(self):
        input = """arr: array[1, 3] of integer = {1, 2, 3};
        x, y: array [1, 3] of integer = {1, 2, 3}, {foo(x), 5 * 2, arr[0, 2]};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([1, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(x, ArrayType([1, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(y, ArrayType([1, 3], IntegerType), ArrayLit([FuncCall(foo, [Id(x)]), BinExpr(*, IntegerLit(5), IntegerLit(2)), ArrayCell(arr, [IntegerLit(0), IntegerLit(2)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 27))
    def test_full_vardecl_expr_8_1(self): #NOTE - Test mang hai chieu
        input = """arr: array[2, 3] of integer = {{1, 2}, {1, 3}, {3, 4}};
        x, y: array [1, 3] of integer = {1, 2, 3}, {foo(x), 5 * 2, arr[0, 2]};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]))
	VarDecl(x, ArrayType([1, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(y, ArrayType([1, 3], IntegerType), ArrayLit([FuncCall(foo, [Id(x)]), BinExpr(*, IntegerLit(5), IntegerLit(2)), ArrayCell(arr, [IntegerLit(0), IntegerLit(2)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 28))
    def test_full_vardecl_expr_9_1(self): #NOTE - Test mang da chieu
        input = """arr: array[2, 3, 4] of integer = { 
                     { {3, 4, 2, 3}, {0, -3, 9, 11}, {23, 12, 23, 2} },
                     { {13, 4, 56, 3}, {5, 9, 3, 5}, {3, 1, 4, 9} }
                 };
        """
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3, 4], IntegerType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(0), UnExpr(-, IntegerLit(3)), IntegerLit(9), IntegerLit(11)]), ArrayLit([IntegerLit(23), IntegerLit(12), IntegerLit(23), IntegerLit(2)])]), ArrayLit([ArrayLit([IntegerLit(13), IntegerLit(4), IntegerLit(56), IntegerLit(3)]), ArrayLit([IntegerLit(5), IntegerLit(9), IntegerLit(3), IntegerLit(5)]), ArrayLit([IntegerLit(3), IntegerLit(1), IntegerLit(4), IntegerLit(9)])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 29))
    def test_full_vardecl_expr_10_1(self): #NOTE - Test mang da chieu
        input = """
        x : array[3] of integer = {1, 2, 3};
        arr: array[2, 3, 4] of integer = { 
                     { {3, abc * xyz, 2, 3}, {0, -3, 9, 11}, {foo(x, y), 12, 23, 2} },
                     { {13, 4, x[2], 3}, {5, -(15 / 2 % 4) * 9, 3, 5}, {x[0], 1, 4, 9} }
                 };
        """
        expect = """Program([
	VarDecl(x, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(arr, ArrayType([2, 3, 4], IntegerType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(3), BinExpr(*, Id(abc), Id(xyz)), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(0), UnExpr(-, IntegerLit(3)), IntegerLit(9), IntegerLit(11)]), ArrayLit([FuncCall(foo, [Id(x), Id(y)]), IntegerLit(12), IntegerLit(23), IntegerLit(2)])]), ArrayLit([ArrayLit([IntegerLit(13), IntegerLit(4), ArrayCell(x, [IntegerLit(2)]), IntegerLit(3)]), ArrayLit([IntegerLit(5), BinExpr(*, UnExpr(-, BinExpr(%, BinExpr(/, IntegerLit(15), IntegerLit(2)), IntegerLit(4))), IntegerLit(9)), IntegerLit(3), IntegerLit(5)]), ArrayLit([ArrayCell(x, [IntegerLit(0)]), IntegerLit(1), IntegerLit(4), IntegerLit(9)])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 30))


#NOTE - TEST DECLARE FUNCITON
    def test_declare_func_1_1(self):
        #test: declare function - test assign_stmt
        input = """x: integer = 12;
        fact: function void(x: integer) inherit abc {
            x[2,3] = 122;
            
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(2), IntegerLit(3)]), IntegerLit(122))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 31))
    def test_declare_func_2_1(self):
        #test: declare function - test param
        input = """x: integer = 12;
        fact: function void(x: integer) inherit abc {
            x[2,3] = 122;
            
        }
        foo: function integer(){}
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(2), IntegerLit(3)]), IntegerLit(122))]))
	FuncDecl(foo, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect, 32))

    def test_declare_func_3_1(self):
        #test: declare function - test param
        input = """x: integer = 12;
        fact: function boolean (out x: boolean, inherit delta: integer, inherit out delta: integer) {}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, BooleanType, [OutParam(x, BooleanType), InheritParam(delta, IntegerType), InheritOutParam(delta, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect, 33))
    def test_declare_func_4_1(self):
        #test: declare function - test param
        input = """x: integer = 12;
        fact: function boolean (out x: string, inherit delta: array [2, 3] of boolean, inherit out delta: integer) {}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, BooleanType, [OutParam(x, StringType), InheritParam(delta, ArrayType([2, 3], BooleanType)), InheritOutParam(delta, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect, 34))
    def test_declare_func_5_1(self):
        #test: declare function - test param
        input="""
        foo: function string () {
            a = arr[c];
            arr[1] = 9;
        }
        fact: function void (out x: boolean) {}
        fact1: function array [1, 2] of integer () inherit fact {}
        """
        expect = """Program([
	FuncDecl(foo, StringType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(arr, [Id(c)])), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), IntegerLit(9))]))
	FuncDecl(fact, VoidType, [OutParam(x, BooleanType)], None, BlockStmt([]))
	FuncDecl(fact1, ArrayType([1, 2], IntegerType), [], fact, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect, 35))


#NOTE - TEST STATEMENTS
    
    #NOTE - TEST VAR DECLARE STATEMENTS
    def test_statements_1_1(self):
        input = """x: integer = 12;
        fact: function void(x: integer) inherit abc {
            x = 122 % (2 + 2 * (2 / 18_23 - 2));
            y = "234" :: "23423";
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(Id(x), BinExpr(%, IntegerLit(122), BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(2), BinExpr(-, BinExpr(/, IntegerLit(2), IntegerLit(1823)), IntegerLit(2)))))), AssignStmt(Id(y), BinExpr(::, StringLit(234), StringLit(23423)))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 41))
    def test_statements_2_1(self):
        input = """x: integer = 12;
        fact: function void(x: integer) inherit abc {
            z = - ( 12 * 12 + 2 / 3 ) + (-2);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(12))
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(Id(z), BinExpr(+, UnExpr(-, BinExpr(+, BinExpr(*, IntegerLit(12), IntegerLit(12)), BinExpr(/, IntegerLit(2), IntegerLit(3)))), UnExpr(-, IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 42))
    def test_statements_3_1(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            temp: integer;
            temp = true;
            temp = !(12 == 3 % 4);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(temp, IntegerType), AssignStmt(Id(temp), BooleanLit(True)), AssignStmt(Id(temp), UnExpr(!, BinExpr(==, IntegerLit(12), BinExpr(%, IntegerLit(3), IntegerLit(4)))))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 43))
    def test_statements_4_1(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            temp: boolean;
            temp1: integer;
            temp2: integer = 1_458_000;
            x, y: integer = 12, foo(x, y);
            temp = !(12 == 3 % 4);
            f1, f0, f2: float = 1.5e10, 100e-10, .1e12;
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(temp, BooleanType), VarDecl(temp1, IntegerType), VarDecl(temp2, IntegerType, IntegerLit(1458000)), VarDecl(x, IntegerType, IntegerLit(12)), VarDecl(y, IntegerType, FuncCall(foo, [Id(x), Id(y)])), AssignStmt(Id(temp), UnExpr(!, BinExpr(==, IntegerLit(12), BinExpr(%, IntegerLit(3), IntegerLit(4))))), VarDecl(f1, FloatType, FloatLit(15000000000.0)), VarDecl(f0, FloatType, FloatLit(1e-08)), VarDecl(f2, FloatType, FloatLit(100000000000.0))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 44))
    def test_statements_5_1(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            temp: boolean;
            temp2: string = "1_458_000";
            arr: array [4, 5] of integer;
            arr: array [1, 2] of integer = {1 * 2, 2 % 2};
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(temp, BooleanType), VarDecl(temp2, StringType, StringLit(1_458_000)), VarDecl(arr, ArrayType([4, 5], IntegerType)), VarDecl(arr, ArrayType([1, 2], IntegerType), ArrayLit([BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(%, IntegerLit(2), IntegerLit(2))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 45))
    def test_statements_6_1(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            temp: boolean;
            temp: boolean = !!!63;
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(temp, BooleanType), VarDecl(temp, BooleanType, UnExpr(!, UnExpr(!, UnExpr(!, IntegerLit(63)))))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 46))
        
    #NOTE - TEST IF STATEMENTS

    def test_statements_6_12(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            foo: integer;
            if (foo % 2 == 0) {
                foo = foo - 1;
                foo1: integer = foo;
            }
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(foo, IntegerType), IfStmt(BinExpr(==, BinExpr(%, Id(foo), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(foo), BinExpr(-, Id(foo), IntegerLit(1))), VarDecl(foo1, IntegerType, Id(foo))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 51))
    def test_statements_7_1(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            foo: integer;
            if (foo % 2 == 0) {
                foo = foo - 1;
                foo1: integer = foo;
            }
            else {
                foo = foo / 2 + 1;
                temp: boolean = !foo;
            }
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(foo, IntegerType), IfStmt(BinExpr(==, BinExpr(%, Id(foo), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(foo), BinExpr(-, Id(foo), IntegerLit(1))), VarDecl(foo1, IntegerType, Id(foo))]), BlockStmt([AssignStmt(Id(foo), BinExpr(+, BinExpr(/, Id(foo), IntegerLit(2)), IntegerLit(1))), VarDecl(temp, BooleanType, UnExpr(!, Id(foo)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 52))
    def test_statements_8_1(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            foo: integer;
            if (foo % 2 == 0) {
                foo = foo - 1;
                foo1: integer = foo;
            }
            t = !(arr[2] < 10);
        }
        temp: integer;
        temp1: string = "121";
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([VarDecl(foo, IntegerType), IfStmt(BinExpr(==, BinExpr(%, Id(foo), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(foo), BinExpr(-, Id(foo), IntegerLit(1))), VarDecl(foo1, IntegerType, Id(foo))])), AssignStmt(Id(t), UnExpr(!, BinExpr(<, ArrayCell(arr, [IntegerLit(2)]), IntegerLit(10))))]))
	VarDecl(temp, IntegerType)
	VarDecl(temp1, StringType, StringLit(121))
])"""
        self.assertTrue(TestAST.test(input,expect, 53))

    ##NOTE - TEST FOR STATEMENTS
    def test_statements_9_1(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            y = 0;
            for (y = 1, y < 3, y + 1) {
                if (y % 2 == 0) printInteger(4_51_2);
                else printFloat(4e-2);
            }
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([AssignStmt(Id(y), IntegerLit(0)), ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(<, Id(y), IntegerLit(3)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(y), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, IntegerLit(4512)), CallStmt(printFloat, FloatLit(0.04)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 54))
    def test_statements_10_1(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            for (y = 1, y < 3, y + 1) printFloat(124.122);
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(<, Id(y), IntegerLit(3)), BinExpr(+, Id(y), IntegerLit(1)), CallStmt(printFloat, FloatLit(124.122)))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 55))
    def test_statements_11_1(self):
        input = """x: integer;
        fact: function void(x: integer) inherit abc {
            for (y = 1, !foo(y) == true, y + 1) printFloat(124.122);
            y: integer;
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(fact, VoidType, [Param(x, IntegerType)], abc, BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(==, UnExpr(!, FuncCall(foo, [Id(y)])), BooleanLit(True)), BinExpr(+, Id(y), IntegerLit(1)), CallStmt(printFloat, FloatLit(124.122))), VarDecl(y, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input,expect, 56))
    def test_statements_11_12(self):
        input = """main: function void () {
            for(arr[0, 1] = 1 + 3, arr[0, 1] > 0, arr[0, 1] * 2){
                printString("Hello World");
                for(i = 0, i < n, i - 1) printInteger(1);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), BinExpr(+, IntegerLit(1), IntegerLit(3))), BinExpr(>, ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), IntegerLit(0)), BinExpr(*, ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), IntegerLit(2)), BlockStmt([CallStmt(printString, StringLit(Hello World)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(-, Id(i), IntegerLit(1)), CallStmt(printInteger, IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 57))


    def test_full_vardecl_expr_8_734(self): #NOTE - Test mang hai chieu
            input = """arr: array[2, 3] of integer = {{1}, {1}, {3}};
            x, y: array [1, 3] of integer = {1, 2, 3}, {foo(x), 5 * 2, arr[0, 2]};
            """
            expect = """Program([
        VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]))
        VarDecl(x, ArrayType([1, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
        VarDecl(y, ArrayType([1, 3], IntegerType), ArrayLit([FuncCall(foo, [Id(x)]), BinExpr(*, IntegerLit(5), IntegerLit(2)), ArrayCell(arr, [IntegerLit(0), IntegerLit(2)])]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 58))

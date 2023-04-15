from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC
"""
class StaticError(Exception):
    pass


class Kind(ABC):
    def __str__(self):
        return self.__class__.__name__


class Variable(Kind):
    pass


class Parameter(Kind):
    pass


class Function(Kind):
    pass


class Identifier(Kind):
    pass


class Redeclared(StaticError):
    def __init__(self, kind: Kind, identifier: str):
        self.kind = kind
        self.identifier = identifier

    def __str__(self):
        return f"Redeclared {str(self.kind)}: {self.identifier}"


class Undeclared(StaticError):
    def __init__(self, kind: Kind, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Undeclared {str(self.kind)}: {self.name}"


class Invalid(StaticError):
    def __init__(self, kind: Kind, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Invalid {str(self.kind)}: {self.name}"

class TypeMismatchInVarDecl(StaticError):
        def __init__(self, decl):
            self.decl = decl

        def __str__(self):
            return f"Type mismatch in Variable Declaration: {str(self.decl)}"
    
class TypeMismatchInExpression(StaticError):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return f"Type mismatch in expression: {str(self.expr)}"


class TypeMismatchInStatement(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return f"Type mismatch in statement: {str(self.stmt)}"


class MustInLoop(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return f"Must in loop: {str(self.stmt)}"


class IllegalArrayLiteral(StaticError):
    def __init__(self, literal):
        self.literal = literal

    def __str__(self):
        return f"Illegal array literal: {str(self.literal)}"


class InvalidStatementInFunction(StaticError):
    def __init__(self, function_name: str):
        self.function_name = function_name

    def __str__(self):
        return f"Invalid statement in function: {str(self.function_name)}"


class NoEntryPoint(StaticError):
    def __str__(self):
        return "No entry point"
"""
class GetEnv(Visitor):

    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast, o):
        self.visit(ast.left, o)
        self.visit(ast.right, o)
    # op: str, val: Expr
    def visitUnExpr(self, ast, o):
        self.visit(ast.val, o)
    # name: str
    def visitId(self, ast, o):
        for env in o:
            for decl in env:
                if ast.name == decl.name:
                    return
        raise Undeclared(Identifier(), ast.name)
    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast, o):
        for env in o:
            for decl in env:
                if ast.name == decl.name:
                    for exp in ast.cell:
                        self.visit(exp, o)
                    return
        raise Undeclared(Identifier(), ast.name)

    def visitIntegerLit(self, ast, param): #val: int
        return param
    def visitFloatLit(self, ast, param): #val: float
        return param
    def visitStringLit(self, ast, param): #val: str
        return param
    def visitBooleanLit(self, ast, param): #val: bool
        return param
    # explist: List[Expr]
    def visitArrayLit(self, ast, o): 
        for exp in ast.explist:
            self.visit(exp, o)
    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, o):
        for env in o:
            for decl in env:
                if ast.name == decl.name: return
        raise Undeclared(Function(), ast.name)
    # lhs: LHS, rhs: Expr //LHS is Id or ArrayCell
    def visitAssignStmt(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, o):
        env = o
        for sq in ast.body:
            if type(sq) is Stmt:
                self.visit(sq, env)
            else:
                env = self.visit(sq, env)

    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast, o):
        self.visit(ast.cond, o)

    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast, o):
        self.visit(ast.init, o)
        self.visit(ast.cond, o)
        self.visit(ast.upd, o)
        self.visit(ast.stmt, o)

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast, o):
        self.visit(ast.cond, o)
        self.visit(ast.stmt, o)


    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast, o):
        self.visit(ast.cond, o)
        self.visit(ast.stmt, o)



    def visitBreakStmt(self, ast, param): pass
    def visitContinueStmt(self, ast, param): pass


    # expr: Expr or None = None
    def visitReturnStmt(self, ast, o):
        if ast.expr:
            self.visit(ast.expr, o)

    # name: str, args: List[Expr]
    def visitCallStmt(self, ast, o):
        for env in o:
            for decl in env:
                if decl.name == ast.name:
                    for exp in ast.args:
                        self.visit(exp, o)
                    return
        raise Undeclared(Function(), ast.name)

    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast, o):
        for decl in o[0]:
            if ast.name == decl.name:
                kind  = Variable()
                name = ast.name
                raise Redeclared(kind, name)
        o[0] += [ast]
        return o

    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        for decl in o[0]:
            if ast.name == decl.name:
                kind = Parameter()
                name = ast.name
                raise Redeclared(kind, name)
        o[0] += [ast]
        return o

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, o):
        for decl in o[0]:
            if ast.name == decl.name:
                kind = Function()
                name = ast.name
                raise Redeclared(kind, name)
        o[0] += [ast]
        env = [[]] + o
        for param in ast.params:
            env = self.visit(param, env)
        env = self.visit(ast.body, env)
        # for decl in env:
        #     s = [ele.name for ele in decl]
        #     print(decl)
        return o
    # decls: List[Decl]
    def visitProgram(self, ast, o):
        o = [[]]
        for decl in ast.decls:
            o = self.visit(decl, o)
        return o[0]
    
class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        return self.visitProgram(self.ast, [])
    
    def visitIntegerType(self, ast, param):
        return IntegerType()
    def visitFloatType(self, ast, param):
        return FloatType()
    def visitBooleanType(self, ast, param):
        return BooleanType()
    def visitStringType(self, ast, param):
        return StringType()
    def visitArrayType(self, ast, param):
        return ArrayType()
    def visitAutoType(self, ast, param):
        return AutoType()
    def visitVoidType(self, ast, param):
        return VoidType()

    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast, param): pass
    # op: str, val: Expr
    def visitUnExpr(self, ast, param): pass
    # name: str
    def visitId(self, ast, param): pass
    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast, param): pass


    def visitIntegerLit(self, ast, param): #val: int
        return IntegerType()
    def visitFloatLit(self, ast, param): #val: float
        return FloatType()
    def visitStringLit(self, ast, param): #val: str
        return StringType()
    def visitBooleanLit(self, ast, param): #val: bool
        return BooleanType()

    # explist: List[Expr]
    def visitArrayLit(self, ast, param): 
        return ArrayType()
    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, param): pass
    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast, param): pass
    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, param): pass
    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast, param): pass
    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast, param): pass
    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast, param): pass
    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast, param): pass
    def visitBreakStmt(self, ast, param): pass
    def visitContinueStmt(self, ast, param): pass
    # expr: Expr or None = None
    def visitReturnStmt(self, ast, param): pass
    # name: str, args: List[Expr]
    def visitCallStmt(self, ast, param): pass
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast, param): pass
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, param): pass
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, param): pass
    # decls: List[Decl]
    def visitProgram(self, ast, o):
        env = GetEnv().visit(ast, o)
        # for decl in env:
        #     if type(decl) is VarDecl:
        #         print("VarDecl: ", decl.name)
        #     elif type(decl) is FuncDecl:
        #         print("FuncDecl: ", decl.name)

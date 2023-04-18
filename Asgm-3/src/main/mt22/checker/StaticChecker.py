from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class NoType(Type): pass

class Ultils:
    def infer(self, name, typ): pass
class Symbol:
    def __init__(self, name, typ, inherit):
        self.name = name
        self.typ = typ
        self.inherit = inherit
class GetEnv(Visitor):
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast, o): return o

    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        o += [Symbol()]

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, o):
        paramdecl = []
        for param in ast.params:
            paramdecl = self.visit(param, paramdecl)
        return o + [ast]
    # decls: List[Decl]
    def visitProgram(self, ast, o):
        o = []
        for decl in ast.decls:
            o = self.visit(decl, o)
        return o
    
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
    def visitBlockStmt(self, ast, o):
        # o[0]: function name
        # o[1]: function return type
        # o[2]: parent_info
        # o[3]: param_decl
        # o[4]: local env
        # o[5]: global env
        # o[6]: True if....
        if len(o) == 5 and o[4] is True: #From function inherited
            env = [[]] + o[1]
            env[0] += o[0] + o[1]
            if len(o[2]) == 0:
                if type(ast.body[0]) is not CallStmt:
                    self.visit(o[2], o) #visit its super class
                else:
                    if ast.body[0].name == "super" and len(ast.body[0].args) != 0:
                        raise InvalidStatementInFunction(o[0])
                    elif ast.body[0].name == "super" and len(ast.body[0].args) == 0:
                        self.visit(o[2], o) #visit its super class
                    # else: ignore
            else:
                if ast.body[0].name == "super" or ast.body[0].name == "preventDefault":
                    if ast.body[0].name == "super":
                        if len(ast.body[0].args) != len(o[2].params):
                            raise InvalidStatementInFunction(o[0])
                        self.visit(o[2], o) #visit its super class
                else:
                    raise InvalidStatementInFunction(o[0])
            for stmt in ast.body:
                if type(stmt) is Stmt:
                env = self.visit(stmt, env)
                if type(stmt) is VarDecl:


        if len(o) == 5 and o[4] is False:



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
    def visitParamDecl(self, ast, o):
        # o[0]: parent's param declares
        # o[1]: its function param declares
        # o[2]: True if this function have a parent

        for param_decl in o[0]:
            if param_decl.name == ast.name:
                raise Invalid(Parameter(), ast.name)

        for param_decl in o[1]:
            if param_decl.name == ast.name:
                raise Redeclared(Parameter(), ast.name)

        o[1] += [ast]
        return o[1]

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, o):
        #check Redeclared
        for decl in o[0][0]:
            if decl.name == ast.name:
                raise Redeclared(Function(), ast.name)
        param_decl = []
        parent_param = []
        parent_info = None
        if ast.inherit is None:
            for param in params:
                param_decl = self.visit(ast, ([], param_decl, False)) #False if this function have no parent
            # self.visit(ast.body, ([], param_decl, o[0], o[1], False)) #o[0]: local env, o[1]: global env, False: is not inherit
            self.visit(ast.body, (ast.name, ast.return_type, parent_info, param_decl, o[0], o[1], False)) #o[0]: local env, o[1]: global env, True: inherit
        else:
            parent_found = False
            parent_info = None
            for decl in o[1]:
                if decl.name == ast.inherit:
                    parent_found = True
                    parent_info = decl
            if not parent_found:
                raise Undeclared(Function(), ast.inherit)
            # if its parent is found

            # Get inherit parameter from its parent
            for param in parent_info.params:
                if param.inherit is True:
                    param_param += [param]

            for param in ast.params:
                param_decl = self.visit(param, (parent_param, param_decl, True)) #True if this func have a parent
            
            self.visit(ast.body, (ast.name, ast.return_type, parent_info, param_decl, o[0], o[1], True)) #o[0]: local env, o[1]: global env, True: inherit

            
            
    # decls: List[Decl]
    def visitProgram(self, ast, o):
        global_env = GetEnv().visit(ast, [])
        o = [[]]
        for decl in ast.decls:
            o = self.visit(decl, (o, global_env))

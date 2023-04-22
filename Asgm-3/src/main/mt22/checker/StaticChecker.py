from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class NoType(Type): pass

class Ultils:
    def infer(self, name, typ, o):
        for symbol_lst in o:
            for symbol in symbol_lst:
                if symbol.name == name:
                    symbol.typ = typ
class FSymbol:
    def __init__(self, name, typ, inherit):
        self.name = name
        self.typ = typ
        self.inherit = inherit
class VSymbol:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
class ParamSymbol:
    def __init__(self, name, typ, inherit):
        self.name = name
        self.typ = typ
        self.inherit = inherit
class GetEnv(Visitor):
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast, o): return o

    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o): return o

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

    def getFunctionInf(self, name, env):
        for decl in env:
            if decl.name == name:
                return decl
        raise Undeclared(Function(), name)

    # name: str, args: List[Expr] -> Expr
    def visitFuncCall(self, ast, o):
        # o[0]: local env
        # o[1]: global env
        
        fInfor = getFunctionInf(ast.name, o[1])
        if len(ast.args) != len(fInfor.params):
            raise TypeMismatchInExpression(ast)
        for i in range(len(ast.args)):
            at = self.visit(ast.args[i], o) # arguments type
            pt = fInfor.params[i] # parameter type
            
            if type(at) is not type(pt): raise TypeMismatchInExpression(ast)

            

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

        if len(o) == 7 and o[6] is True: #From function inherited
            env = [[]] + o[4]
            env[0] += o[3]
            env = (env, o[5])
            # print(ast.body[0].name)
            if len(o[2].params) == 0: # super(args): len(args) == 0
                if len(ast.body) != 0 and ast.body[0].name == "super" and len(ast.body[0].args) != 0:
                    raise InvalidStatementInFunction(o[0])
            else: # super(args): len(args) != 0
                if len(ast.body) == 0:
                    raise InvalidStatementInFunction(o[0])
                elif ast.body[0].name == "super" or ast.body[0].name == "preventDefault":
                    if ast.body[0].name == "super":
                        if len(ast.body[0].args) < len(o[2].params):
                            raise TypeMismatchInExpression()
                        elif len(ast.body[0].args) > len(o[2].params):
                            mismatch_idx = len(o[2].params)
                            raise TypeMismatchInExpression(ast.body[0].args[mismatch_idx])
                        else:
                            # check suitable type in super()
                            for i in range(len(o[2].params)):
                                args_type = self.visit(ast.body[0].args[i], env)
                                param_type = o[2].params[i].typ
                                if type(args_type) is not type(param_type):
                                    raise TypeMismatchInExpression(ast.body[0].args[i])
                else:
                    raise InvalidStatementInFunction(o[0])
            for stmt in ast.body:
                if type(stmt) is Stmt:
                    self.visit(stmt, env)
                if type(stmt) is VarDecl:
                    env = self.visit(stmt, env)
            return o
        elif len(o) == 7 and o[6] is False: #from normal function (no inherit)
            env = [[]] + o[4]
            env[0] += o[3]
            env = (env, o[5])
            for stmt in ast.body:
                if type(stmt) is Stmt:
                    self.visit(stmt, env)
                if type(stmt) is VarDecl:
                    env = self.visit(stmt, env)
            return o

        # from normal block
        env = [[]] + o
        for stmt in ast.body:
            if type(stmt) is Stmt:
                self.visit(stmt, env)
            else:
                env = self.visit(stmt, env)



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
    def visitVarDecl(self, ast, o):
        # o[0]: [[Symbol]]
        # o[1]: global_env
        for symbol in o[0][0]:
            if symbol.name == ast.name:
                raise Redeclared(Variable(), ast.name)

        if type(ast.typ) is AutoType and ast.init is None:
            raise Invalid(Variable(), ast.name)

        init_type = NoType()
        if ast.init is not None:
            init_type = self.visit(ast.init, o)
        
        # integer and float
        if type(init_type) is IntegerType and type(ast.typ) is FloatType:
            init_type = FloatType()

        if ast.init and type(init_type) is not type(ast.typ) and type(ast.typ) is not AutoType:
            raise TypeMismatchInVarDecl(ast)
        
        o[0][0] += [VSymbol(ast.name, init_type if ast.init else ast.typ)]
        # for symbol_lst in o[0]:
        #     for symbol in symbol_lst:
        #         print((symbol.name, str(symbol.typ)))
        # print('--------')

        return o
        
        
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        # o[0]: parent's param declares
        # o[1]: its function param declares
        # o[2]: True if this function have a parent
        for param_decl in o:
            if param_decl.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
        o += [ParamSymbol(ast.name, ast.typ, ast.inherit)]
        return o

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, o):
        #check Redeclared
        for decl in o[0][0]:
            if decl.name == ast.name:
                raise Redeclared(Function(), ast.name)
        param_decl = []
        parent_param = []
        parent_info = None

        for param in ast.params:
            param_decl = self.visit(param, param_decl)

        if ast.inherit is None:
            self.visit(ast.body, (ast.name, ast.return_type, parent_info, param_decl, o[0], o[1], False)) 
            #o[0]: local env, o[1]: global env, True: inherit
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
                    parent_param = self.visit(param, parent_param)

            for param in parent_param:
                for symbol in param_decl:
                    if param.name == symbol.name:
                        raise Invalid(Parameter(), symbol.name)
                param_decl += [param]


            self.visit(ast.body, (ast.name, ast.return_type, parent_info, param_decl, o[0], o[1], True)) 
            #o[0]: local env, o[1]: global env, True: inherit

        o[0][0] += [FSymbol(ast.name, ast.return_type, ast.inherit is None)]
        return o
            
            
    # decls: List[Decl]
    def visitProgram(self, ast, o):
        global_env = GetEnv().visit(ast, [])
        o = ([[]], global_env)
        for decl in ast.decls:
            o = self.visit(decl, o)


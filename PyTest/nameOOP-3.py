class Type(ABC): pass
class IntType(Type): pass
class BoolType(Type): pass
class FloatType(Type): pass
class StaticCheck(Visitor):
    #decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self,ctx:Program,o):
        o = {}
        for decl in ctx.decl:
            o = self.visit(decl, o)
        for stmt in ctx.stmts:
            self.visit(stmt, o)
    #name:str
    def visitVarDecl(self,ctx:VarDecl,o):
        o[ctx.name] = None
        return o
    #lhs:Id,rhs:Exp
    def visitAssign(self,ctx:Assign,o):
        rhs_type = self.visit(ctx.rhs, o)
        lhs_type = self.visit(ctx.lhs, o)
        if lhs_type is None:
            if rhs_type is None:
                raise TypeCannotBeInferred(ctx)
            o[ctx.lhs.name] = rhs_type
            return
        if type(lhs_type) is not type(rhs_type):
            raise TypeMismatchInStatement(ctx)
    #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o):
        op = ctx.op
        e1t = self.visit(ctx.e1, o)
        e2t = self.visit(ctx.e2, o)

        if op in ['+', '-', '*', '/']:
            if e1t is None:
                o[ctx.e1.name] = IntType()
                e1t = IntType()
            if e2t is None:
                o[ctx.e2.name] = IntType()
                e2t = IntType()
            if type(e1t) is not IntType or type(e2t) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
        elif op in ['+.', '-.', '*.', '/.']:
            if e1t is None:
                o[ctx.e1.name] = FloatType()
                e1t = FloatType()
            if e2t is None:
                o[ctx.e2.name] = FloatType()
                e2t = FloatType()
            if type(e1t) is not FloatType or type(e2t) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        elif op in ['>', '=']:
            if e1t is None:
                o[ctx.e1.name] = IntType()
                e1t = IntType()
            if e2t is None:
                o[ctx.e2.name] = IntType()
                e2t = IntType()
            if type(e1t) is not IntType or type(e2t) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif op in ['>.', '=.']:
            if e1t is None:
                o[ctx.e1.name] = FloatType()
                e1t = FloatType()
            if e2t is None:
                o[ctx.e2.name] = FloatType()
                e2t = FloatType()
            if type(e1t) is not FloatType or type(e2t) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif op in ['&&', '||', '>b', '=b']:
            if e1t is None:
                o[ctx.e1.name] = BoolType()
                e1t = BoolType()
            if e2t is None:
                o[ctx.e2.name] = BoolType()
                e2t = BoolType()
            if type(e1t) is not BoolType or type(e2t) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
    #op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        et = self.visit(ctx.e, o)
        if op == '-':
            if et is None:
                o[ctx.e.name] = IntType()
                return IntType()
            if type(et) is not IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()
        if op == '-.':
            if et is None:
                o[ctx.e.name] = FloatType()
                return FloatType()
            if type(et) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if op == '!':
            if et is None:
                o[ctx.e.name] = BoolType()
                return BoolType()
            if type(et) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if op == 'i2f':
            if et is None:
                o[ctx.e.name] = IntType()
                return FloatType()
            if et is not IntType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if op == 'floor':
            if et is None:
                o[ctx.e.name] = FloatType()
                return IntType()
            if type(et) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return IntType()

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()
    #name:str
    def visitId(self,ctx,o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o[ctx.name]

"""
var x, y, z;
x = (x && y) >b (False || (z) > 3)
z = x
"""

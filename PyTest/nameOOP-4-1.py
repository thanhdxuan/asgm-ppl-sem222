from functools import reduce
class Type(ABC): pass
class Unknown(Type): pass
class IntType(Type): pass
class BoolType(Type): pass
class FloatType(Type): pass

def infer(id, type, o):
    for env in o:
        if id.name in env:
            env[id.name] = type
            return type

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = [{}]
        reduce(lambda _, ele: self.visit(ele, o), ctx.decl, [])
        reduce(lambda _, ele: self.visit(ele, o), ctx.stmts, [])

    def visitVarDecl(self,ctx:VarDecl,o): 
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = Unknown()

    def visitBlock(self,ctx:Block,o): 
        env = [{}] + o
        reduce(lambda _, ele: self.visit(ele, env), ctx.decl, [])
        reduce(lambda _, ele: self.visit(ele, env), ctx.stmts, [])

    def visitAssign(self,ctx:Assign,o): 
        lType = self.visit(ctx.lhs, o)
        rType = self.visit(ctx.rhs, o)
        
        if type(lType) is Unknown and type(rType) is Unknown:
            raise TypeCannotBeInferred(ctx)
            
        if type(lType) is Unknown:
            infer(ctx.lhs, rType, o)
            return
        
        if type(rType) is Unknown and type(ctx.rhs) is Id:
            infer(ctx.rhs, lType, o)
            return
        
        if type(lType) is not type(rType):
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self,ctx:BinOp,o): 
        op = ctx.op
        
        lType = self.visit(ctx.e1, o)
        rType = self.visit(ctx.e2, o)
        
        if op in ['+', '-', '*', '/']:
            if intersection([type(lType), type(rType)], [BoolType, FloatType]):
                raise TypeMismatchInExpression(ctx)
            
            if type(lType) is Unknown:
                infer(ctx.e1, IntType(), o)
            
            if type(rType) is Unknown:
                infer(ctx.e2, IntType(), o)
                
            return IntType()
        
        elif op in ['+.', '-.', '*.', '/.']:
            if intersection([type(lType), type(rType)], [BoolType, IntType]):
                raise TypeMismatchInExpression(ctx)
            
            if type(lType) is Unknown:
                infer(ctx.e1, FloatType(), o)
            
            if type(rType) is Unknown:
                infer(ctx.e2, FloatType(), o)
                
            return FloatType()
            
        elif op in ['>', '=']:
            if intersection([type(lType), type(rType)], [BoolType, FloatType]):
                raise TypeMismatchInExpression(ctx)
            
            if type(lType) is Unknown:
                infer(ctx.e1, IntType(), o)
            
            if type(rType) is Unknown:
                infer(ctx.e2, IntType(), o)
                
            return BoolType()
        
        elif op in ['>.', '=.']:
            if intersection([type(lType), type(rType)], [BoolType, IntType]):
                raise TypeMismatchInExpression(ctx)
            
            if type(lType) is Unknown:
                infer(ctx.e1, FloatType(), o)
            
            if type(rType) is Unknown:
                infer(ctx.e2, FloatType(), o)
                
            return BoolType()
            
        elif op in ['&&', '||', '>b', '=b']:
            if intersection([type(lType), type(rType)], [FloatType, IntType]):
                raise TypeMismatchInExpression(ctx)
            
            if type(lType) is Unknown:
                infer(ctx.e1, BoolType(), o)
            
            if type(rType) is Unknown:
                infer(ctx.e2, BoolType(), o)
                
            return BoolType()

    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        
        eType = self.visit(ctx.e, o)
        
        if op in ['-']:
            if type(eType) in [BoolType, FloatType]:
                raise TypeMismatchInExpression(ctx)
            
            if type(eType) is Unknown:
                infer(ctx.e, IntType(), o)
                
            return IntType()
            
        elif op in ['-.']:
            if type(eType) in [BoolType, IntType]:
                raise TypeMismatchInExpression(ctx)
            
            if type(eType) is Unknown:
                infer(ctx.e, FloatType(), o)
                
            return FloatType()
        
        elif op in ['!']:
            if type(eType) in [FloatType, IntType]:
                raise TypeMismatchInExpression(ctx)
            
            if type(eType) is Unknown:
                infer(ctx.e, BoolType(), o)
                
            return BoolType()
            
        elif op in ['i2f']:
            if type(eType) in [FloatType, BoolType]:
                raise TypeMismatchInExpression(ctx)
            
            if type(eType) is Unknown:
                infer(ctx.e, IntType(), o)
                
            return FloatType()
            
        elif op in ['floor']:
            if type(eType) in [IntType, BoolType]:
                raise TypeMismatchInExpression(ctx)
            
            if type(eType) is Unknown:
                infer(ctx.e, FloatType(), o)
                
            return IntType()

    def visitIntLit(self,ctx:IntLit,o): 
        return IntType()

    def visitFloatLit(self,ctx,o): 
        return FloatType()

    def visitBoolLit(self,ctx,o): 
        return BoolType()

    def visitId(self,ctx,o): 
        for env in o:
            if ctx.name in env:
                return env[ctx.name]
        raise UndeclaredIdentifier(ctx.name)

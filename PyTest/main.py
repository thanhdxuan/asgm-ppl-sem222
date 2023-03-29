from functools import reduce
def lstSquare(n):
   # if n == 1: return [n]
   # return lstSquare(n - 1) + [n * n]
   # return [i * i for i in range(1, n + 1)] 
   return list(map(lambda x: x * x, range(1, n + 1)))

def dist(lst, n):
   # if len(lst) == 0: return []
   # if len(lst) == 1: return [(lst[0], n)]
   # return [(lst[0], n)] + dist(lst[1:], n)
   # return [(i, n) for i in lst]
   return list(map(lambda x: (x, n), lst))

def lessThan(lst, n):
   # if len(lst) == 0: return []
   # if lst[0] < n: return [lst[0]] + lessThan(lst[1:], n)
   # return lessThan(lst[1:], n)
   # return [i for i in lst if i < n]
   # return list(filter(lambda x: x < n, lst))
   return reduce(lambda prev, curr: prev + [curr] if curr < n else prev, lst, [])

# prev = [], curr = [1] -> [1]
# prev = [1], curr = [2] -> [1,2]
# prev = [1, 2], curr = [3] -> [1,2,3]
# prev = [1,2,3], curr = [4] -> [1,2,3] + []

def flatten(lst):
   # if len(lst) == 0: return lst
   # return lst[0] + flatten(lst[1:])
   # result = []
   # for i in lst:
   #    for j in i:
   #       result.append(j)
   # return result
   # return [j for i in lst for j in i]
   return reduce(lambda prev, curr: prev + curr, lst, [])

# print(flatten([[1,2,3],[6,7]]))
class Exp:pass
class BinExp(Exp):
    def __init__(self,o1,op,o2):
        self.left = o1
        self.op = op
        self.right = o2
    def accept(self,v): return v.visitBinExp(self)
class UnExp(Exp): 
    def __init__(self,op,o1):
        self.op = op
        self.operand = o1
    def accept(self,v): return v.visitUnExp(self)
class IntLit(Exp):
    def __init__(self,v):
        self.value = v
    def accept(self,v): return v.visitIntLit(self)
class FloatLit(Exp):
    def __init__(self,v):
        self.value = v
    def accept(self,v): return v.visitFloatLit(self)
   
class Visitor:
    def visit(self, ctx):
        return ctx.accept(self)
   
class Eval(Visitor):
   def visitFloatLit(self, expr):
      return expr.value
   def visitIntLit(expr):
      return expr.value
   def visitBinExp(self,expr):
      left = self.visit(expr.left)
      right = self.visit(expr.right)
      return eval("{} {} {}").format(left, expr.op, right)
   def visitUnExp(self, expr):
       oprd = self.visit(expr.operand)
       return -oprd if expr.op == "-" else oprd

class PrintPrefix(Visitor):
    def visitFloatLit(self, expr):
        return str(expr.value) + ' '
    def visitIntLit(expr):
      return str(expr.value) + ' '
    def visitBinExp(self,expr):
      left = self.visit(expr.left)
      right = self.visit(expr.right)
      return str(expr.op) + ' ' + str(left) + str(right)
    def visitUnExp(self, expr):
       oprd = self.visit(expr.operand)
       return str(expr.op) + '.' + ' ' + str(oprd)
      
x1 = IntLit(4)

x2 = FloatLit(2.0)

x3 = BinExp(x1,"+",x1)

x4 = UnExp("-",x1)

x5 = BinExp(x4,"+",BinExp(IntLit(3),"*",x2))

v1 = Eval()
v2 = PrintPrefix()
print(v2.visit(x5))

class Human:
   "hshfhadsf"
   @classmethod
   def Eat(): pass
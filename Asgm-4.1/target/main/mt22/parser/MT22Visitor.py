# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#body.
    def visitBody(self, ctx:MT22Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_shortform.
    def visitVar_shortform(self, ctx:MT22Parser.Var_shortformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_fullform.
    def visitVar_fullform(self, ctx:MT22Parser.Var_fullformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#base.
    def visitBase(self, ctx:MT22Parser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#helpper.
    def visitHelpper(self, ctx:MT22Parser.HelpperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramprime.
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_typ.
    def visitParam_typ(self, ctx:MT22Parser.Param_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_return_type.
    def visitFunc_return_type(self, ctx:MT22Parser.Func_return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logic_op.
    def visitLogic_op(self, ctx:MT22Parser.Logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relation_op.
    def visitRelation_op(self, ctx:MT22Parser.Relation_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprprime.
    def visitExprprime(self, ctx:MT22Parser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#nonempty_exprlist.
    def visitNonempty_exprlist(self, ctx:MT22Parser.Nonempty_exprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#str_operands.
    def visitStr_operands(self, ctx:MT22Parser.Str_operandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_expr.
    def visitInt_expr(self, ctx:MT22Parser.Int_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term1.
    def visitInt_term1(self, ctx:MT22Parser.Int_term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term2.
    def visitInt_term2(self, ctx:MT22Parser.Int_term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term3.
    def visitInt_term3(self, ctx:MT22Parser.Int_term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term4.
    def visitInt_term4(self, ctx:MT22Parser.Int_term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term5.
    def visitInt_term5(self, ctx:MT22Parser.Int_term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term6.
    def visitInt_term6(self, ctx:MT22Parser.Int_term6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_term7.
    def visitInt_term7(self, ctx:MT22Parser.Int_term7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_func_read_expr.
    def visitSpecial_func_read_expr(self, ctx:MT22Parser.Special_func_read_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_func_print_expr.
    def visitSpecial_func_print_expr(self, ctx:MT22Parser.Special_func_print_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_func_super_expr.
    def visitSpecial_func_super_expr(self, ctx:MT22Parser.Special_func_super_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_func_callstmt.
    def visitSpecial_func_callstmt(self, ctx:MT22Parser.Special_func_callstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specialfunc_read.
    def visitSpecialfunc_read(self, ctx:MT22Parser.Specialfunc_readContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specialfunc_print.
    def visitSpecialfunc_print(self, ctx:MT22Parser.Specialfunc_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specialfunc_super.
    def visitSpecialfunc_super(self, ctx:MT22Parser.Specialfunc_superContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callexpr.
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtslist.
    def visitStmtslist(self, ctx:MT22Parser.StmtslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtprime.
    def visitStmtprime(self, ctx:MT22Parser.StmtprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmts.
    def visitStmts(self, ctx:MT22Parser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#cond_expr.
    def visitCond_expr(self, ctx:MT22Parser.Cond_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension_list.
    def visitDimension_list(self, ctx:MT22Parser.Dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_type.
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)



del MT22Parser
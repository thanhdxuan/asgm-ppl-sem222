# Generated from /home/thanhdxn/Documents/222/PPL_Doc/Asgm-1/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'false'", "'integer'", "'void'", 
                     "'array'", "'break'", "'float'", "'return'", "'out'", 
                     "'boolean'", "'for'", "'string'", "'continue'", "'do'", 
                     "'function'", "'true'", "'of'", "'else'", "'if'", "'while'", 
                     "'inherit'", "'::'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "';'", "','", "'('", "')'", "'{'", 
                     "'}'", "'.'" ]

    symbolicNames = [ "<INVALID>", "KW_AUTO", "KW_FALSE", "KW_INT", "KW_VOID", 
                      "KW_ARRAY", "KW_BREAK", "KW_FLOAT", "KW_RETURN", "KW_OUT", 
                      "KW_BOOL", "KW_FOR", "KW_STR", "KW_CONTINUE", "KW_DO", 
                      "KW_FUNCT", "KW_TRUE", "KW_OF", "KW_ELSE", "KW_IF", 
                      "KW_WHILE", "KW_INHERIT", "OP_SCOPE", "OP_ADD", "OP_MINUS", 
                      "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", "OP_AND", 
                      "OP_OR", "OP_EQ", "OP_INEQ", "OP_LESS", "OP_GREATER", 
                      "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", "SEMI", "COMMA", 
                      "LB", "RB", "LP", "RP", "DOT", "FLOATLIT", "INTLIT", 
                      "STRINGLIT", "ARRLIT", "ID", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    KW_AUTO=1
    KW_FALSE=2
    KW_INT=3
    KW_VOID=4
    KW_ARRAY=5
    KW_BREAK=6
    KW_FLOAT=7
    KW_RETURN=8
    KW_OUT=9
    KW_BOOL=10
    KW_FOR=11
    KW_STR=12
    KW_CONTINUE=13
    KW_DO=14
    KW_FUNCT=15
    KW_TRUE=16
    KW_OF=17
    KW_ELSE=18
    KW_IF=19
    KW_WHILE=20
    KW_INHERIT=21
    OP_SCOPE=22
    OP_ADD=23
    OP_MINUS=24
    OP_MUL=25
    OP_DIV=26
    OP_MOD=27
    OP_NOT=28
    OP_AND=29
    OP_OR=30
    OP_EQ=31
    OP_INEQ=32
    OP_LESS=33
    OP_GREATER=34
    OP_LESS_OR_EQ=35
    OP_GREA_OR_EQ=36
    SEMI=37
    COMMA=38
    LB=39
    RB=40
    LP=41
    RP=42
    DOT=43
    FLOATLIT=44
    INTLIT=45
    STRINGLIT=46
    ARRLIT=47
    ID=48
    WS=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51
    ERROR_CHAR=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






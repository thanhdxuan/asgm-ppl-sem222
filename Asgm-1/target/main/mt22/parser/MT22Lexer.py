# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\37\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6")
        buf.write("\2\17\n\2\r\2\16\2\20\3\3\6\3\24\n\3\r\3\16\3\25\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7")
        buf.write("\3\2\4\5\2\62;C\\c|\5\2\13\f\17\17\"\"\2 \2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\16")
        buf.write("\3\2\2\2\5\23\3\2\2\2\7\31\3\2\2\2\t\33\3\2\2\2\13\35")
        buf.write("\3\2\2\2\r\17\t\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16")
        buf.write("\3\2\2\2\20\21\3\2\2\2\21\4\3\2\2\2\22\24\t\3\2\2\23\22")
        buf.write("\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26")
        buf.write("\27\3\2\2\2\27\30\b\3\2\2\30\6\3\2\2\2\31\32\13\2\2\2")
        buf.write("\32\b\3\2\2\2\33\34\13\2\2\2\34\n\3\2\2\2\35\36\13\2\2")
        buf.write("\2\36\f\3\2\2\2\5\2\20\25\3\b\2\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



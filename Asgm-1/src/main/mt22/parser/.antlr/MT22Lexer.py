# Generated from /home/thanhdxn/Documents/222/PPL_Doc/Asgm-1/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0131\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3-\7-\u0117\n-")
        buf.write("\f-\16-\u011a\13-\5-\u011c\n-\3.\3.\7.\u0120\n.\f.\16")
        buf.write(".\u0123\13.\3/\6/\u0126\n/\r/\16/\u0127\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\2\2\63\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("\3\2\7\3\2\63;\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\n")
        buf.write("\f\17\17\"\"\2\u0134\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\3e\3\2\2\2\5j\3\2\2\2\7p\3\2\2\2\tx\3\2\2\2\13}\3\2")
        buf.write("\2\2\r\u0083\3\2\2\2\17\u0089\3\2\2\2\21\u008f\3\2\2\2")
        buf.write("\23\u0096\3\2\2\2\25\u009a\3\2\2\2\27\u00a2\3\2\2\2\31")
        buf.write("\u00a6\3\2\2\2\33\u00ad\3\2\2\2\35\u00b6\3\2\2\2\37\u00b9")
        buf.write("\3\2\2\2!\u00c2\3\2\2\2#\u00c7\3\2\2\2%\u00ca\3\2\2\2")
        buf.write("\'\u00cf\3\2\2\2)\u00d2\3\2\2\2+\u00d8\3\2\2\2-\u00e0")
        buf.write("\3\2\2\2/\u00e3\3\2\2\2\61\u00e5\3\2\2\2\63\u00e7\3\2")
        buf.write("\2\2\65\u00e9\3\2\2\2\67\u00eb\3\2\2\29\u00ed\3\2\2\2")
        buf.write(";\u00ef\3\2\2\2=\u00f2\3\2\2\2?\u00f5\3\2\2\2A\u00f8\3")
        buf.write("\2\2\2C\u00fb\3\2\2\2E\u00fd\3\2\2\2G\u00ff\3\2\2\2I\u0102")
        buf.write("\3\2\2\2K\u0105\3\2\2\2M\u0107\3\2\2\2O\u0109\3\2\2\2")
        buf.write("Q\u010b\3\2\2\2S\u010d\3\2\2\2U\u010f\3\2\2\2W\u0111\3")
        buf.write("\2\2\2Y\u011b\3\2\2\2[\u011d\3\2\2\2]\u0125\3\2\2\2_\u012b")
        buf.write("\3\2\2\2a\u012d\3\2\2\2c\u012f\3\2\2\2ef\7c\2\2fg\7w\2")
        buf.write("\2gh\7v\2\2hi\7q\2\2i\4\3\2\2\2jk\7h\2\2kl\7c\2\2lm\7")
        buf.write("n\2\2mn\7u\2\2no\7g\2\2o\6\3\2\2\2pq\7k\2\2qr\7p\2\2r")
        buf.write("s\7v\2\2st\7g\2\2tu\7i\2\2uv\7g\2\2vw\7t\2\2w\b\3\2\2")
        buf.write("\2xy\7x\2\2yz\7q\2\2z{\7k\2\2{|\7f\2\2|\n\3\2\2\2}~\7")
        buf.write("c\2\2~\177\7t\2\2\177\u0080\7t\2\2\u0080\u0081\7c\2\2")
        buf.write("\u0081\u0082\7{\2\2\u0082\f\3\2\2\2\u0083\u0084\7d\2\2")
        buf.write("\u0084\u0085\7t\2\2\u0085\u0086\7g\2\2\u0086\u0087\7c")
        buf.write("\2\2\u0087\u0088\7m\2\2\u0088\16\3\2\2\2\u0089\u008a\7")
        buf.write("h\2\2\u008a\u008b\7n\2\2\u008b\u008c\7q\2\2\u008c\u008d")
        buf.write("\7c\2\2\u008d\u008e\7v\2\2\u008e\20\3\2\2\2\u008f\u0090")
        buf.write("\7t\2\2\u0090\u0091\7g\2\2\u0091\u0092\7v\2\2\u0092\u0093")
        buf.write("\7w\2\2\u0093\u0094\7t\2\2\u0094\u0095\7p\2\2\u0095\22")
        buf.write("\3\2\2\2\u0096\u0097\7q\2\2\u0097\u0098\7w\2\2\u0098\u0099")
        buf.write("\7v\2\2\u0099\24\3\2\2\2\u009a\u009b\7d\2\2\u009b\u009c")
        buf.write("\7q\2\2\u009c\u009d\7q\2\2\u009d\u009e\7n\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7p\2\2\u00a1\26")
        buf.write("\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\30\3\2\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8")
        buf.write("\7v\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\u00ac\7i\2\2\u00ac\32\3\2\2\2\u00ad\u00ae")
        buf.write("\7e\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4")
        buf.write("\7w\2\2\u00b4\u00b5\7g\2\2\u00b5\34\3\2\2\2\u00b6\u00b7")
        buf.write("\7f\2\2\u00b7\u00b8\7q\2\2\u00b8\36\3\2\2\2\u00b9\u00ba")
        buf.write("\7h\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd")
        buf.write("\7e\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7p\2\2\u00c1 \3\2\2\2\u00c2\u00c3")
        buf.write("\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\"\3\2\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9$\3\2\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc")
        buf.write("\7n\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7g\2\2\u00ce&\3")
        buf.write("\2\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7h\2\2\u00d1(\3")
        buf.write("\2\2\2\u00d2\u00d3\7y\2\2\u00d3\u00d4\7j\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7\7g\2\2\u00d7*\3")
        buf.write("\2\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da\7p\2\2\u00da\u00db")
        buf.write("\7j\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7k\2\2\u00de\u00df\7v\2\2\u00df,\3\2\2\2\u00e0\u00e1")
        buf.write("\7<\2\2\u00e1\u00e2\7<\2\2\u00e2.\3\2\2\2\u00e3\u00e4")
        buf.write("\7-\2\2\u00e4\60\3\2\2\2\u00e5\u00e6\7/\2\2\u00e6\62\3")
        buf.write("\2\2\2\u00e7\u00e8\7,\2\2\u00e8\64\3\2\2\2\u00e9\u00ea")
        buf.write("\7\61\2\2\u00ea\66\3\2\2\2\u00eb\u00ec\7\'\2\2\u00ec8")
        buf.write("\3\2\2\2\u00ed\u00ee\7#\2\2\u00ee:\3\2\2\2\u00ef\u00f0")
        buf.write("\7(\2\2\u00f0\u00f1\7(\2\2\u00f1<\3\2\2\2\u00f2\u00f3")
        buf.write("\7~\2\2\u00f3\u00f4\7~\2\2\u00f4>\3\2\2\2\u00f5\u00f6")
        buf.write("\7?\2\2\u00f6\u00f7\7?\2\2\u00f7@\3\2\2\2\u00f8\u00f9")
        buf.write("\7#\2\2\u00f9\u00fa\7?\2\2\u00faB\3\2\2\2\u00fb\u00fc")
        buf.write("\7>\2\2\u00fcD\3\2\2\2\u00fd\u00fe\7@\2\2\u00feF\3\2\2")
        buf.write("\2\u00ff\u0100\7>\2\2\u0100\u0101\7?\2\2\u0101H\3\2\2")
        buf.write("\2\u0102\u0103\7@\2\2\u0103\u0104\7?\2\2\u0104J\3\2\2")
        buf.write("\2\u0105\u0106\7=\2\2\u0106L\3\2\2\2\u0107\u0108\7.\2")
        buf.write("\2\u0108N\3\2\2\2\u0109\u010a\7*\2\2\u010aP\3\2\2\2\u010b")
        buf.write("\u010c\7+\2\2\u010cR\3\2\2\2\u010d\u010e\7}\2\2\u010e")
        buf.write("T\3\2\2\2\u010f\u0110\7\177\2\2\u0110V\3\2\2\2\u0111\u0112")
        buf.write("\7\60\2\2\u0112X\3\2\2\2\u0113\u011c\7\62\2\2\u0114\u0118")
        buf.write("\t\2\2\2\u0115\u0117\t\3\2\2\u0116\u0115\3\2\2\2\u0117")
        buf.write("\u011a\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u0113\3")
        buf.write("\2\2\2\u011b\u0114\3\2\2\2\u011cZ\3\2\2\2\u011d\u0121")
        buf.write("\t\4\2\2\u011e\u0120\t\5\2\2\u011f\u011e\3\2\2\2\u0120")
        buf.write("\u0123\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u0122\\\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0126\t\6\2")
        buf.write("\2\u0125\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write("\u012a\b/\2\2\u012a^\3\2\2\2\u012b\u012c\13\2\2\2\u012c")
        buf.write("`\3\2\2\2\u012d\u012e\13\2\2\2\u012eb\3\2\2\2\u012f\u0130")
        buf.write("\13\2\2\2\u0130d\3\2\2\2\7\2\u0118\u011b\u0121\u0127\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    KW_AUTO = 1
    KW_FALSE = 2
    KW_INT = 3
    KW_VOID = 4
    KW_ARRAY = 5
    KW_BREAK = 6
    KW_FLOAT = 7
    KW_RETURN = 8
    KW_OUT = 9
    KW_BOOL = 10
    KW_FOR = 11
    KW_STR = 12
    KW_CONTINUE = 13
    KW_DO = 14
    KW_FUNCT = 15
    KW_TRUE = 16
    KW_OF = 17
    KW_ELSE = 18
    KW_IF = 19
    KW_WHILE = 20
    KW_INHERIT = 21
    OP_SCOPE = 22
    OP_ADD = 23
    OP_MINUS = 24
    OP_MUL = 25
    OP_DIV = 26
    OP_MOD = 27
    OP_NOT = 28
    OP_AND = 29
    OP_OR = 30
    OP_EQ = 31
    OP_INEQ = 32
    OP_LESS = 33
    OP_GREATER = 34
    OP_LESS_OR_EQ = 35
    OP_GREA_OR_EQ = 36
    SEMI = 37
    COMMA = 38
    LB = 39
    RB = 40
    LP = 41
    RP = 42
    DOT = 43
    INTLIT = 44
    ID = 45
    WS = 46
    ERROR_CHAR = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'false'", "'integer'", "'void'", "'array'", "'break'", 
            "'float'", "'return'", "'out'", "'boolean'", "'for'", "'string'", 
            "'continue'", "'do'", "'function'", "'true'", "'of'", "'else'", 
            "'if'", "'while'", "'inherit'", "'::'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "';'", "','", "'('", "')'", "'{'", "'}'", 
            "'.'" ]

    symbolicNames = [ "<INVALID>",
            "KW_AUTO", "KW_FALSE", "KW_INT", "KW_VOID", "KW_ARRAY", "KW_BREAK", 
            "KW_FLOAT", "KW_RETURN", "KW_OUT", "KW_BOOL", "KW_FOR", "KW_STR", 
            "KW_CONTINUE", "KW_DO", "KW_FUNCT", "KW_TRUE", "KW_OF", "KW_ELSE", 
            "KW_IF", "KW_WHILE", "KW_INHERIT", "OP_SCOPE", "OP_ADD", "OP_MINUS", 
            "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", "OP_AND", "OP_OR", "OP_EQ", 
            "OP_INEQ", "OP_LESS", "OP_GREATER", "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", 
            "SEMI", "COMMA", "LB", "RB", "LP", "RP", "DOT", "INTLIT", "ID", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "KW_AUTO", "KW_FALSE", "KW_INT", "KW_VOID", "KW_ARRAY", 
                  "KW_BREAK", "KW_FLOAT", "KW_RETURN", "KW_OUT", "KW_BOOL", 
                  "KW_FOR", "KW_STR", "KW_CONTINUE", "KW_DO", "KW_FUNCT", 
                  "KW_TRUE", "KW_OF", "KW_ELSE", "KW_IF", "KW_WHILE", "KW_INHERIT", 
                  "OP_SCOPE", "OP_ADD", "OP_MINUS", "OP_MUL", "OP_DIV", 
                  "OP_MOD", "OP_NOT", "OP_AND", "OP_OR", "OP_EQ", "OP_INEQ", 
                  "OP_LESS", "OP_GREATER", "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", 
                  "SEMI", "COMMA", "LB", "RB", "LP", "RP", "DOT", "INTLIT", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



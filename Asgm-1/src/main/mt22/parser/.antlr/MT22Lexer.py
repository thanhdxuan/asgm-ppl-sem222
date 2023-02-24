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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01cd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\7\7\u0094\n\7\f\7\16\7\u0097\13\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\7\b\u00a2\n\b\f\b\16\b\u00a5\13\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(")
        buf.write("\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0147")
        buf.write("\n+\3,\3,\3,\3,\3,\5,\u014e\n,\3,\3,\5,\u0152\n,\3,\3")
        buf.write(",\3-\3-\7-\u0158\n-\f-\16-\u015b\13-\3.\3.\3.\3/\3/\3")
        buf.write("/\7/\u0163\n/\f/\16/\u0166\13/\3/\3/\6/\u016a\n/\r/\16")
        buf.write("/\u016b\7/\u016e\n/\f/\16/\u0171\13/\5/\u0173\n/\3\60")
        buf.write("\3\60\6\60\u0177\n\60\r\60\16\60\u0178\3\61\3\61\5\61")
        buf.write("\u017d\n\61\3\61\6\61\u0180\n\61\r\61\16\61\u0181\3\62")
        buf.write("\3\62\3\62\3\62\7\62\u0188\n\62\f\62\16\62\u018b\13\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\7\63\u0194\n\63\f")
        buf.write("\63\16\63\u0197\13\63\3\63\3\63\3\64\3\64\3\65\3\65\3")
        buf.write("\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\7<\u01ad")
        buf.write("\n<\f<\16<\u01b0\13<\3=\6=\u01b3\n=\r=\16=\u01b4\3=\3")
        buf.write("=\3>\3>\3>\3?\3?\7?\u01be\n?\f?\16?\u01c1\13?\3?\3?\3")
        buf.write("@\3@\7@\u01c7\n@\f@\16@\u01ca\13@\3@\3@\3\u0095\2A\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\2_\2a\2c\60e\2g\61i\62k\63m\64o\65q\66s\67")
        buf.write("u8w9y:{;}<\177=\3\2\16\4\2\f\f\17\17\3\2\63;\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\4\2\f\f$$\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\5\2\n\f\17\17\"\"\t\2))^^ddhhppttvv")
        buf.write("\3\2\60\60\2\u01dd\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2c\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\3\u0081\3\2\2\2\5\u0083\3\2\2\2\7\u0085\3\2\2\2")
        buf.write("\t\u0088\3\2\2\2\13\u008a\3\2\2\2\r\u008f\3\2\2\2\17\u009d")
        buf.write("\3\2\2\2\21\u00a8\3\2\2\2\23\u00ad\3\2\2\2\25\u00b5\3")
        buf.write("\2\2\2\27\u00ba\3\2\2\2\31\u00c0\3\2\2\2\33\u00c6\3\2")
        buf.write("\2\2\35\u00cc\3\2\2\2\37\u00d3\3\2\2\2!\u00d7\3\2\2\2")
        buf.write("#\u00df\3\2\2\2%\u00e3\3\2\2\2\'\u00ea\3\2\2\2)\u00f3")
        buf.write("\3\2\2\2+\u00f6\3\2\2\2-\u00ff\3\2\2\2/\u0102\3\2\2\2")
        buf.write("\61\u0107\3\2\2\2\63\u010a\3\2\2\2\65\u0110\3\2\2\2\67")
        buf.write("\u0118\3\2\2\29\u011b\3\2\2\2;\u011d\3\2\2\2=\u011f\3")
        buf.write("\2\2\2?\u0121\3\2\2\2A\u0123\3\2\2\2C\u0125\3\2\2\2E\u0127")
        buf.write("\3\2\2\2G\u012a\3\2\2\2I\u012d\3\2\2\2K\u0130\3\2\2\2")
        buf.write("M\u0133\3\2\2\2O\u0135\3\2\2\2Q\u0137\3\2\2\2S\u013a\3")
        buf.write("\2\2\2U\u0146\3\2\2\2W\u0151\3\2\2\2Y\u0155\3\2\2\2[\u015c")
        buf.write("\3\2\2\2]\u0172\3\2\2\2_\u0174\3\2\2\2a\u017a\3\2\2\2")
        buf.write("c\u0183\3\2\2\2e\u018f\3\2\2\2g\u019a\3\2\2\2i\u019c\3")
        buf.write("\2\2\2k\u019e\3\2\2\2m\u01a0\3\2\2\2o\u01a2\3\2\2\2q\u01a4")
        buf.write("\3\2\2\2s\u01a6\3\2\2\2u\u01a8\3\2\2\2w\u01aa\3\2\2\2")
        buf.write("y\u01b2\3\2\2\2{\u01b8\3\2\2\2}\u01bb\3\2\2\2\177\u01c4")
        buf.write("\3\2\2\2\u0081\u0082\7\"\2\2\u0082\4\3\2\2\2\u0083\u0084")
        buf.write("\7?\2\2\u0084\6\3\2\2\2\u0085\u0086\7\"\2\2\u0086\u0087")
        buf.write("\7]\2\2\u0087\b\3\2\2\2\u0088\u0089\7_\2\2\u0089\n\3\2")
        buf.write("\2\2\u008a\u008b\7\"\2\2\u008b\u008c\7q\2\2\u008c\u008d")
        buf.write("\7h\2\2\u008d\u008e\7\"\2\2\u008e\f\3\2\2\2\u008f\u0090")
        buf.write("\7\61\2\2\u0090\u0091\7,\2\2\u0091\u0095\3\2\2\2\u0092")
        buf.write("\u0094\13\2\2\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2")
        buf.write("\2\u0095\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0098")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\7,\2\2\u0099")
        buf.write("\u009a\7\61\2\2\u009a\u009b\3\2\2\2\u009b\u009c\b\7\2")
        buf.write("\2\u009c\16\3\2\2\2\u009d\u009e\7\61\2\2\u009e\u009f\7")
        buf.write("\61\2\2\u009f\u00a3\3\2\2\2\u00a0\u00a2\n\2\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a6\u00a7\b\b\2\2\u00a7\20\3\2\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac")
        buf.write("\7q\2\2\u00ac\22\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2")
        buf.write("\7i\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7t\2\2\u00b4\24")
        buf.write("\3\2\2\2\u00b5\u00b6\7x\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8")
        buf.write("\7k\2\2\u00b8\u00b9\7f\2\2\u00b9\26\3\2\2\2\u00ba\u00bb")
        buf.write("\7c\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7c\2\2\u00be\u00bf\7{\2\2\u00bf\30\3\2\2\2\u00c0\u00c1")
        buf.write("\7d\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7c\2\2\u00c4\u00c5\7m\2\2\u00c5\32\3\2\2\2\u00c6\u00c7")
        buf.write("\7h\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7c\2\2\u00ca\u00cb\7v\2\2\u00cb\34\3\2\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7w\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2\7p\2\2\u00d2\36")
        buf.write("\3\2\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6 \3\2\2\2\u00d7\u00d8\7d\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7n\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de\7p\2\2\u00de\"")
        buf.write("\3\2\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2$\3\2\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7i\2\2\u00e9&\3\2\2\2\u00ea\u00eb")
        buf.write("\7e\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7w\2\2\u00f1\u00f2\7g\2\2\u00f2(\3\2\2\2\u00f3\u00f4")
        buf.write("\7f\2\2\u00f4\u00f5\7q\2\2\u00f5*\3\2\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7e\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\u00fe\7p\2\2\u00fe,\3\2\2\2\u00ff\u0100")
        buf.write("\7q\2\2\u0100\u0101\7h\2\2\u0101.\3\2\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7n\2\2\u0104\u0105\7u\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\60\3\2\2\2\u0107\u0108\7k\2\2\u0108\u0109")
        buf.write("\7h\2\2\u0109\62\3\2\2\2\u010a\u010b\7y\2\2\u010b\u010c")
        buf.write("\7j\2\2\u010c\u010d\7k\2\2\u010d\u010e\7n\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f\64\3\2\2\2\u0110\u0111\7k\2\2\u0111\u0112")
        buf.write("\7p\2\2\u0112\u0113\7j\2\2\u0113\u0114\7g\2\2\u0114\u0115")
        buf.write("\7t\2\2\u0115\u0116\7k\2\2\u0116\u0117\7v\2\2\u0117\66")
        buf.write("\3\2\2\2\u0118\u0119\7<\2\2\u0119\u011a\7<\2\2\u011a8")
        buf.write("\3\2\2\2\u011b\u011c\7-\2\2\u011c:\3\2\2\2\u011d\u011e")
        buf.write("\7/\2\2\u011e<\3\2\2\2\u011f\u0120\7,\2\2\u0120>\3\2\2")
        buf.write("\2\u0121\u0122\7\61\2\2\u0122@\3\2\2\2\u0123\u0124\7\'")
        buf.write("\2\2\u0124B\3\2\2\2\u0125\u0126\7#\2\2\u0126D\3\2\2\2")
        buf.write("\u0127\u0128\7(\2\2\u0128\u0129\7(\2\2\u0129F\3\2\2\2")
        buf.write("\u012a\u012b\7~\2\2\u012b\u012c\7~\2\2\u012cH\3\2\2\2")
        buf.write("\u012d\u012e\7?\2\2\u012e\u012f\7?\2\2\u012fJ\3\2\2\2")
        buf.write("\u0130\u0131\7#\2\2\u0131\u0132\7?\2\2\u0132L\3\2\2\2")
        buf.write("\u0133\u0134\7>\2\2\u0134N\3\2\2\2\u0135\u0136\7@\2\2")
        buf.write("\u0136P\3\2\2\2\u0137\u0138\7>\2\2\u0138\u0139\7?\2\2")
        buf.write("\u0139R\3\2\2\2\u013a\u013b\7@\2\2\u013b\u013c\7?\2\2")
        buf.write("\u013cT\3\2\2\2\u013d\u013e\7v\2\2\u013e\u013f\7t\2\2")
        buf.write("\u013f\u0140\7w\2\2\u0140\u0147\7g\2\2\u0141\u0142\7h")
        buf.write("\2\2\u0142\u0143\7c\2\2\u0143\u0144\7n\2\2\u0144\u0145")
        buf.write("\7u\2\2\u0145\u0147\7g\2\2\u0146\u013d\3\2\2\2\u0146\u0141")
        buf.write("\3\2\2\2\u0147V\3\2\2\2\u0148\u0149\5]/\2\u0149\u014a")
        buf.write("\5_\60\2\u014a\u0152\3\2\2\2\u014b\u014d\5]/\2\u014c\u014e")
        buf.write("\5_\60\2\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0150\5a\61\2\u0150\u0152\3\2\2\2")
        buf.write("\u0151\u0148\3\2\2\2\u0151\u014b\3\2\2\2\u0152\u0153\3")
        buf.write("\2\2\2\u0153\u0154\b,\3\2\u0154X\3\2\2\2\u0155\u0159\t")
        buf.write("\3\2\2\u0156\u0158\t\4\2\2\u0157\u0156\3\2\2\2\u0158\u015b")
        buf.write("\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("Z\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\5]/\2\u015d")
        buf.write("\u015e\b.\4\2\u015e\\\3\2\2\2\u015f\u0173\7\62\2\2\u0160")
        buf.write("\u0164\t\3\2\2\u0161\u0163\t\4\2\2\u0162\u0161\3\2\2\2")
        buf.write("\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u016f\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0169")
        buf.write("\7a\2\2\u0168\u016a\t\4\2\2\u0169\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016e\3\2\2\2\u016d\u0167\3\2\2\2\u016e\u0171\3")
        buf.write("\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0173")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u015f\3\2\2\2\u0172")
        buf.write("\u0160\3\2\2\2\u0173^\3\2\2\2\u0174\u0176\7\60\2\2\u0175")
        buf.write("\u0177\t\4\2\2\u0176\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179`\3\2\2")
        buf.write("\2\u017a\u017c\t\5\2\2\u017b\u017d\t\6\2\2\u017c\u017b")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f\3\2\2\2\u017e")
        buf.write("\u0180\t\4\2\2\u017f\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182b\3\2\2")
        buf.write("\2\u0183\u0189\7$\2\2\u0184\u0185\7^\2\2\u0185\u0188\t")
        buf.write("\7\2\2\u0186\u0188\n\b\2\2\u0187\u0184\3\2\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0189\3\2\2\2")
        buf.write("\u018c\u018d\7$\2\2\u018d\u018e\b\62\5\2\u018ed\3\2\2")
        buf.write("\2\u018f\u0195\7$\2\2\u0190\u0191\7^\2\2\u0191\u0194\t")
        buf.write("\7\2\2\u0192\u0194\n\b\2\2\u0193\u0190\3\2\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0198\3\2\2\2\u0197\u0195\3\2\2\2")
        buf.write("\u0198\u0199\7$\2\2\u0199f\3\2\2\2\u019a\u019b\7=\2\2")
        buf.write("\u019bh\3\2\2\2\u019c\u019d\7.\2\2\u019dj\3\2\2\2\u019e")
        buf.write("\u019f\7*\2\2\u019fl\3\2\2\2\u01a0\u01a1\7+\2\2\u01a1")
        buf.write("n\3\2\2\2\u01a2\u01a3\7}\2\2\u01a3p\3\2\2\2\u01a4\u01a5")
        buf.write("\7\177\2\2\u01a5r\3\2\2\2\u01a6\u01a7\7\60\2\2\u01a7t")
        buf.write("\3\2\2\2\u01a8\u01a9\7<\2\2\u01a9v\3\2\2\2\u01aa\u01ae")
        buf.write("\t\t\2\2\u01ab\u01ad\t\n\2\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01afx\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b3\t\13\2")
        buf.write("\2\u01b2\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b7\b=\6\2\u01b7z\3\2\2\2\u01b8\u01b9\13\2\2\2\u01b9")
        buf.write("\u01ba\b>\7\2\u01ba|\3\2\2\2\u01bb\u01bf\7^\2\2\u01bc")
        buf.write("\u01be\n\f\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1\3\2\2\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2\3")
        buf.write("\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\b?\b\2\u01c3~\3")
        buf.write("\2\2\2\u01c4\u01c8\7$\2\2\u01c5\u01c7\t\r\2\2\u01c6\u01c5")
        buf.write("\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01cb\u01cc\b@\t\2\u01cc\u0080\3\2\2\2\30\2\u0095\u00a3")
        buf.write("\u0146\u014d\u0151\u0159\u0164\u016b\u016f\u0172\u0178")
        buf.write("\u017c\u0181\u0187\u0189\u0193\u0195\u01ae\u01b4\u01bf")
        buf.write("\u01c8\n\2\3\2\3,\2\3.\3\3\62\4\b\2\2\3>\5\3?\6\3@\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    BLOCK_COMMENT = 6
    LINE_COMMENT = 7
    AUTO = 8
    INT = 9
    VOID = 10
    ARRAY = 11
    BREAK = 12
    FLOAT = 13
    RETURN = 14
    OUT = 15
    BOOL = 16
    FOR = 17
    STR = 18
    CONTINUE = 19
    DO = 20
    FUNCT = 21
    OF = 22
    ELSE = 23
    IF = 24
    WHILE = 25
    INHERIT = 26
    OP_SCOPE = 27
    OP_ADD = 28
    OP_MINUS = 29
    OP_MUL = 30
    OP_DIV = 31
    OP_MOD = 32
    OP_NOT = 33
    OP_AND = 34
    OP_OR = 35
    OP_EQ = 36
    OP_INEQ = 37
    OP_LESS = 38
    OP_GREATER = 39
    OP_LESS_OR_EQ = 40
    OP_GREA_OR_EQ = 41
    BOOLLIT = 42
    FLOATLIT = 43
    INTEGER = 44
    INTLIT = 45
    STRINGLIT = 46
    SEMI = 47
    COMMA = 48
    LB = 49
    RB = 50
    LP = 51
    RP = 52
    DOT = 53
    COLON = 54
    ID = 55
    WS = 56
    ERROR_CHAR = 57
    ILLEGAL_ESCAPE = 58
    UNCLOSE_STRING = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '", "'='", "' ['", "']'", "' of '", "'auto'", "'integer'", 
            "'void'", "'array'", "'break'", "'float'", "'return'", "'out'", 
            "'boolean'", "'for'", "'string'", "'continue'", "'do'", "'function'", 
            "'of'", "'else'", "'if'", "'while'", "'inherit'", "'::'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'<'", "'>'", "'<='", "'>='", "';'", "','", "'('", "')'", "'{'", 
            "'}'", "'.'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", "INT", "VOID", "ARRAY", 
            "BREAK", "FLOAT", "RETURN", "OUT", "BOOL", "FOR", "STR", "CONTINUE", 
            "DO", "FUNCT", "OF", "ELSE", "IF", "WHILE", "INHERIT", "OP_SCOPE", 
            "OP_ADD", "OP_MINUS", "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", 
            "OP_AND", "OP_OR", "OP_EQ", "OP_INEQ", "OP_LESS", "OP_GREATER", 
            "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", "BOOLLIT", "FLOATLIT", "INTEGER", 
            "INTLIT", "STRINGLIT", "SEMI", "COMMA", "LB", "RB", "LP", "RP", 
            "DOT", "COLON", "ID", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "AUTO", "INT", "VOID", "ARRAY", "BREAK", 
                  "FLOAT", "RETURN", "OUT", "BOOL", "FOR", "STR", "CONTINUE", 
                  "DO", "FUNCT", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                  "OP_SCOPE", "OP_ADD", "OP_MINUS", "OP_MUL", "OP_DIV", 
                  "OP_MOD", "OP_NOT", "OP_AND", "OP_OR", "OP_EQ", "OP_INEQ", 
                  "OP_LESS", "OP_GREATER", "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", 
                  "BOOLLIT", "FLOATLIT", "INTEGER", "INTLIT", "INTPART", 
                  "DECPART", "EXPPART", "STRINGLIT", "STRPART", "SEMI", 
                  "COMMA", "LB", "RB", "LP", "RP", "DOT", "COLON", "ID", 
                  "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[42] = self.FLOATLIT_action 
            actions[44] = self.INTLIT_action 
            actions[48] = self.STRINGLIT_action 
            actions[60] = self.ERROR_CHAR_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise UncloseString(self.text)
     



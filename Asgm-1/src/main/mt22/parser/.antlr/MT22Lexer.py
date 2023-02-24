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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01bf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\7\5\u008b\n\5\f\5\16\5\u008e\13")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u0099\n\6\f")
        buf.write("\6\16\6\u009c\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\5*\u0140\n*\3+\3+\7+\u0144\n+\f+\16")
        buf.write("+\u0147\13+\3,\3,\3,\3,\3,\5,\u014e\n,\3,\3,\5,\u0152")
        buf.write("\n,\3,\3,\3-\3-\3-\3.\3.\3.\7.\u015c\n.\f.\16.\u015f\13")
        buf.write(".\3.\3.\6.\u0163\n.\r.\16.\u0164\7.\u0167\n.\f.\16.\u016a")
        buf.write("\13.\5.\u016c\n.\3/\3/\6/\u0170\n/\r/\16/\u0171\3\60\3")
        buf.write("\60\5\60\u0176\n\60\3\60\6\60\u0179\n\60\r\60\16\60\u017a")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u0181\n\61\f\61\16\61\u0184")
        buf.write("\13\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u018d\n")
        buf.write("\62\f\62\16\62\u0190\13\62\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3")
        buf.write(";\6;\u01a5\n;\r;\16;\u01a6\3;\3;\3<\3<\3<\3=\3=\7=\u01b0")
        buf.write("\n=\f=\16=\u01b3\13=\3=\3=\3>\3>\7>\u01b9\n>\f>\16>\u01bc")
        buf.write("\13>\3>\3>\3\u008c\2?\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_\2a/c\2e\60g\61")
        buf.write("i\62k\63m\64o\65q\66s\67u8w9y:{;\3\2\16\4\2\f\f\17\17")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\n\2$$))^^ddhhppttvv\4\2\f\f$$\5\2\n\f\17\17\"\"\t")
        buf.write("\2))^^ddhhppttvv\3\2\60\60\2\u01ce\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2a\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\3}\3\2\2\2\5\u0082\3\2\2\2\7\u0084\3\2\2\2\t\u0086\3")
        buf.write("\2\2\2\13\u0094\3\2\2\2\r\u009f\3\2\2\2\17\u00a4\3\2\2")
        buf.write("\2\21\u00ac\3\2\2\2\23\u00b1\3\2\2\2\25\u00b7\3\2\2\2")
        buf.write("\27\u00bd\3\2\2\2\31\u00c3\3\2\2\2\33\u00ca\3\2\2\2\35")
        buf.write("\u00ce\3\2\2\2\37\u00d6\3\2\2\2!\u00da\3\2\2\2#\u00e1")
        buf.write("\3\2\2\2%\u00ea\3\2\2\2\'\u00ed\3\2\2\2)\u00f6\3\2\2\2")
        buf.write("+\u00f9\3\2\2\2-\u00fe\3\2\2\2/\u0101\3\2\2\2\61\u0107")
        buf.write("\3\2\2\2\63\u010f\3\2\2\2\65\u0112\3\2\2\2\67\u0114\3")
        buf.write("\2\2\29\u0116\3\2\2\2;\u0118\3\2\2\2=\u011a\3\2\2\2?\u011c")
        buf.write("\3\2\2\2A\u011e\3\2\2\2C\u0121\3\2\2\2E\u0124\3\2\2\2")
        buf.write("G\u0127\3\2\2\2I\u0129\3\2\2\2K\u012c\3\2\2\2M\u012e\3")
        buf.write("\2\2\2O\u0130\3\2\2\2Q\u0133\3\2\2\2S\u013f\3\2\2\2U\u0141")
        buf.write("\3\2\2\2W\u0151\3\2\2\2Y\u0155\3\2\2\2[\u016b\3\2\2\2")
        buf.write("]\u016d\3\2\2\2_\u0173\3\2\2\2a\u017c\3\2\2\2c\u0188\3")
        buf.write("\2\2\2e\u0193\3\2\2\2g\u0195\3\2\2\2i\u0197\3\2\2\2k\u0199")
        buf.write("\3\2\2\2m\u019b\3\2\2\2o\u019d\3\2\2\2q\u019f\3\2\2\2")
        buf.write("s\u01a1\3\2\2\2u\u01a4\3\2\2\2w\u01aa\3\2\2\2y\u01ad\3")
        buf.write("\2\2\2{\u01b6\3\2\2\2}~\7d\2\2~\177\7q\2\2\177\u0080\7")
        buf.write("f\2\2\u0080\u0081\7{\2\2\u0081\4\3\2\2\2\u0082\u0083\7")
        buf.write("]\2\2\u0083\6\3\2\2\2\u0084\u0085\7_\2\2\u0085\b\3\2\2")
        buf.write("\2\u0086\u0087\7\61\2\2\u0087\u0088\7,\2\2\u0088\u008c")
        buf.write("\3\2\2\2\u0089\u008b\13\2\2\2\u008a\u0089\3\2\2\2\u008b")
        buf.write("\u008e\3\2\2\2\u008c\u008d\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008d\u008f\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0090\7")
        buf.write(",\2\2\u0090\u0091\7\61\2\2\u0091\u0092\3\2\2\2\u0092\u0093")
        buf.write("\b\5\2\2\u0093\n\3\2\2\2\u0094\u0095\7\61\2\2\u0095\u0096")
        buf.write("\7\61\2\2\u0096\u009a\3\2\2\2\u0097\u0099\n\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009a\3")
        buf.write("\2\2\2\u009d\u009e\b\6\2\2\u009e\f\3\2\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3")
        buf.write("\7q\2\2\u00a3\16\3\2\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6")
        buf.write("\7p\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7i\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7t\2\2\u00ab\20")
        buf.write("\3\2\2\2\u00ac\u00ad\7x\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af")
        buf.write("\7k\2\2\u00af\u00b0\7f\2\2\u00b0\22\3\2\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5")
        buf.write("\7c\2\2\u00b5\u00b6\7{\2\2\u00b6\24\3\2\2\2\u00b7\u00b8")
        buf.write("\7d\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7c\2\2\u00bb\u00bc\7m\2\2\u00bc\26\3\2\2\2\u00bd\u00be")
        buf.write("\7h\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7c\2\2\u00c1\u00c2\7v\2\2\u00c2\30\3\2\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7")
        buf.write("\7w\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7p\2\2\u00c9\32")
        buf.write("\3\2\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\34\3\2\2\2\u00ce\u00cf\7d\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7p\2\2\u00d5\36")
        buf.write("\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9 \3\2\2\2\u00da\u00db\7u\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de\7k\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7i\2\2\u00e0\"\3\2\2\2\u00e1\u00e2")
        buf.write("\7e\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7w\2\2\u00e8\u00e9\7g\2\2\u00e9$\3\2\2\2\u00ea\u00eb")
        buf.write("\7f\2\2\u00eb\u00ec\7q\2\2\u00ec&\3\2\2\2\u00ed\u00ee")
        buf.write("\7h\2\2\u00ee\u00ef\7w\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7e\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4")
        buf.write("\7q\2\2\u00f4\u00f5\7p\2\2\u00f5(\3\2\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7h\2\2\u00f8*\3\2\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7u\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd,\3\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7h\2\2\u0100.\3\2\2\2\u0101\u0102\7y\2\2\u0102\u0103")
        buf.write("\7j\2\2\u0103\u0104\7k\2\2\u0104\u0105\7n\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\60\3\2\2\2\u0107\u0108\7k\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\u010a\7j\2\2\u010a\u010b\7g\2\2\u010b\u010c")
        buf.write("\7t\2\2\u010c\u010d\7k\2\2\u010d\u010e\7v\2\2\u010e\62")
        buf.write("\3\2\2\2\u010f\u0110\7<\2\2\u0110\u0111\7<\2\2\u0111\64")
        buf.write("\3\2\2\2\u0112\u0113\7-\2\2\u0113\66\3\2\2\2\u0114\u0115")
        buf.write("\7/\2\2\u01158\3\2\2\2\u0116\u0117\7,\2\2\u0117:\3\2\2")
        buf.write("\2\u0118\u0119\7\61\2\2\u0119<\3\2\2\2\u011a\u011b\7\'")
        buf.write("\2\2\u011b>\3\2\2\2\u011c\u011d\7#\2\2\u011d@\3\2\2\2")
        buf.write("\u011e\u011f\7(\2\2\u011f\u0120\7(\2\2\u0120B\3\2\2\2")
        buf.write("\u0121\u0122\7~\2\2\u0122\u0123\7~\2\2\u0123D\3\2\2\2")
        buf.write("\u0124\u0125\7?\2\2\u0125\u0126\7?\2\2\u0126F\3\2\2\2")
        buf.write("\u0127\u0128\7?\2\2\u0128H\3\2\2\2\u0129\u012a\7#\2\2")
        buf.write("\u012a\u012b\7?\2\2\u012bJ\3\2\2\2\u012c\u012d\7>\2\2")
        buf.write("\u012dL\3\2\2\2\u012e\u012f\7@\2\2\u012fN\3\2\2\2\u0130")
        buf.write("\u0131\7>\2\2\u0131\u0132\7?\2\2\u0132P\3\2\2\2\u0133")
        buf.write("\u0134\7@\2\2\u0134\u0135\7?\2\2\u0135R\3\2\2\2\u0136")
        buf.write("\u0137\7v\2\2\u0137\u0138\7t\2\2\u0138\u0139\7w\2\2\u0139")
        buf.write("\u0140\7g\2\2\u013a\u013b\7h\2\2\u013b\u013c\7c\2\2\u013c")
        buf.write("\u013d\7n\2\2\u013d\u013e\7u\2\2\u013e\u0140\7g\2\2\u013f")
        buf.write("\u0136\3\2\2\2\u013f\u013a\3\2\2\2\u0140T\3\2\2\2\u0141")
        buf.write("\u0145\t\3\2\2\u0142\u0144\t\4\2\2\u0143\u0142\3\2\2\2")
        buf.write("\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146\3")
        buf.write("\2\2\2\u0146V\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149")
        buf.write("\5[.\2\u0149\u014a\5]/\2\u014a\u0152\3\2\2\2\u014b\u014d")
        buf.write("\5[.\2\u014c\u014e\5]/\2\u014d\u014c\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\5_\60\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u0148\3\2\2\2\u0151\u014b\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153\u0154\b,\3\2\u0154X\3\2\2\2")
        buf.write("\u0155\u0156\5[.\2\u0156\u0157\b-\4\2\u0157Z\3\2\2\2\u0158")
        buf.write("\u016c\7\62\2\2\u0159\u015d\t\5\2\2\u015a\u015c\t\6\2")
        buf.write("\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0168\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u0160\u0162\7a\2\2\u0161\u0163\t\6\2\2")
        buf.write("\u0162\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0160")
        buf.write("\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016b\u0158\3\2\2\2\u016b\u0159\3\2\2\2\u016c\\\3\2\2")
        buf.write("\2\u016d\u016f\7\60\2\2\u016e\u0170\t\6\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172^\3\2\2\2\u0173\u0175\t\7\2\2\u0174")
        buf.write("\u0176\t\b\2\2\u0175\u0174\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0178\3\2\2\2\u0177\u0179\t\6\2\2\u0178\u0177\3")
        buf.write("\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b")
        buf.write("\3\2\2\2\u017b`\3\2\2\2\u017c\u0182\7$\2\2\u017d\u017e")
        buf.write("\7^\2\2\u017e\u0181\t\t\2\2\u017f\u0181\n\n\2\2\u0180")
        buf.write("\u017d\3\2\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\7$\2\2\u0186\u0187")
        buf.write("\b\61\5\2\u0187b\3\2\2\2\u0188\u018e\7$\2\2\u0189\u018a")
        buf.write("\7^\2\2\u018a\u018d\t\t\2\2\u018b\u018d\n\n\2\2\u018c")
        buf.write("\u0189\3\2\2\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191\3")
        buf.write("\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\7$\2\2\u0192d\3")
        buf.write("\2\2\2\u0193\u0194\7=\2\2\u0194f\3\2\2\2\u0195\u0196\7")
        buf.write(".\2\2\u0196h\3\2\2\2\u0197\u0198\7*\2\2\u0198j\3\2\2\2")
        buf.write("\u0199\u019a\7+\2\2\u019al\3\2\2\2\u019b\u019c\7}\2\2")
        buf.write("\u019cn\3\2\2\2\u019d\u019e\7\177\2\2\u019ep\3\2\2\2\u019f")
        buf.write("\u01a0\7\60\2\2\u01a0r\3\2\2\2\u01a1\u01a2\7<\2\2\u01a2")
        buf.write("t\3\2\2\2\u01a3\u01a5\t\13\2\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8\u01a9\b;\6\2\u01a9v\3\2\2\2")
        buf.write("\u01aa\u01ab\13\2\2\2\u01ab\u01ac\b<\7\2\u01acx\3\2\2")
        buf.write("\2\u01ad\u01b1\7^\2\2\u01ae\u01b0\n\f\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b4\u01b5\b=\b\2\u01b5z\3\2\2\2\u01b6\u01ba\7$\2\2")
        buf.write("\u01b7\u01b9\t\r\2\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc\3")
        buf.write("\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be\b>\t\2\u01be")
        buf.write("|\3\2\2\2\27\2\u008c\u009a\u013f\u0145\u014d\u0151\u015d")
        buf.write("\u0164\u0168\u016b\u0171\u0175\u017a\u0180\u0182\u018c")
        buf.write("\u018e\u01a6\u01b1\u01ba\n\2\3\2\3,\2\3-\3\3\61\4\b\2")
        buf.write("\2\3<\5\3=\6\3>\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    BLOCK_COMMENT = 4
    LINE_COMMENT = 5
    AUTO = 6
    INT = 7
    VOID = 8
    ARRAY = 9
    BREAK = 10
    FLOAT = 11
    RETURN = 12
    OUT = 13
    BOOL = 14
    FOR = 15
    STR = 16
    CONTINUE = 17
    DO = 18
    FUNCT = 19
    OF = 20
    ELSE = 21
    IF = 22
    WHILE = 23
    INHERIT = 24
    OP_STR_CONCAT = 25
    OP_ADD = 26
    OP_MINUS = 27
    OP_MUL = 28
    OP_DIV = 29
    OP_MOD = 30
    OP_NOT = 31
    OP_AND = 32
    OP_OR = 33
    OP_EQ_EQ = 34
    OP_EQ = 35
    OP_INEQ = 36
    OP_LESS = 37
    OP_GREATER = 38
    OP_LESS_OR_EQ = 39
    OP_GREA_OR_EQ = 40
    BOOLLIT = 41
    ID = 42
    FLOATLIT = 43
    INTLIT = 44
    STRINGLIT = 45
    SEMI = 46
    COMMA = 47
    LB = 48
    RB = 49
    LP = 50
    RP = 51
    DOT = 52
    COLON = 53
    WS = 54
    ERROR_CHAR = 55
    ILLEGAL_ESCAPE = 56
    UNCLOSE_STRING = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'body'", "'['", "']'", "'auto'", "'integer'", "'void'", "'array'", 
            "'break'", "'float'", "'return'", "'out'", "'boolean'", "'for'", 
            "'string'", "'continue'", "'do'", "'function'", "'of'", "'else'", 
            "'if'", "'while'", "'inherit'", "'::'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'<'", "'>'", "'<='", "'>='", "';'", "','", "'('", "')'", "'{'", 
            "'}'", "'.'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", "INT", "VOID", "ARRAY", 
            "BREAK", "FLOAT", "RETURN", "OUT", "BOOL", "FOR", "STR", "CONTINUE", 
            "DO", "FUNCT", "OF", "ELSE", "IF", "WHILE", "INHERIT", "OP_STR_CONCAT", 
            "OP_ADD", "OP_MINUS", "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", 
            "OP_AND", "OP_OR", "OP_EQ_EQ", "OP_EQ", "OP_INEQ", "OP_LESS", 
            "OP_GREATER", "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", "BOOLLIT", "ID", 
            "FLOATLIT", "INTLIT", "STRINGLIT", "SEMI", "COMMA", "LB", "RB", 
            "LP", "RP", "DOT", "COLON", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BLOCK_COMMENT", "LINE_COMMENT", 
                  "AUTO", "INT", "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", 
                  "OUT", "BOOL", "FOR", "STR", "CONTINUE", "DO", "FUNCT", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "OP_STR_CONCAT", 
                  "OP_ADD", "OP_MINUS", "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", 
                  "OP_AND", "OP_OR", "OP_EQ_EQ", "OP_EQ", "OP_INEQ", "OP_LESS", 
                  "OP_GREATER", "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", "BOOLLIT", 
                  "ID", "FLOATLIT", "INTLIT", "INTPART", "DECPART", "EXPPART", 
                  "STRINGLIT", "STRPART", "SEMI", "COMMA", "LB", "RB", "LP", 
                  "RP", "DOT", "COLON", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

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
            actions[43] = self.INTLIT_action 
            actions[47] = self.STRINGLIT_action 
            actions[58] = self.ERROR_CHAR_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.UNCLOSE_STRING_action 
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
     



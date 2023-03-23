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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0241\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\7\2\u0094\n")
        buf.write("\2\f\2\16\2\u0097\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\7\3\u00a2\n\3\f\3\16\3\u00a5\13\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.")
        buf.write("\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\5\61\u01bc\n\61\3\62\3\62\7\62\u01c0")
        buf.write("\n\62\f\62\16\62\u01c3\13\62\3\63\5\63\u01c6\n\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\5\63\u01cd\n\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u01d4\n\63\5\63\u01d6\n\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\7\65\u01e0\n\65\f\65\16\65\u01e3")
        buf.write("\13\65\3\65\3\65\6\65\u01e7\n\65\r\65\16\65\u01e8\7\65")
        buf.write("\u01eb\n\65\f\65\16\65\u01ee\13\65\5\65\u01f0\n\65\3\66")
        buf.write("\3\66\7\66\u01f4\n\66\f\66\16\66\u01f7\13\66\3\67\3\67")
        buf.write("\5\67\u01fb\n\67\3\67\6\67\u01fe\n\67\r\67\16\67\u01ff")
        buf.write("\38\38\38\38\78\u0206\n8\f8\168\u0209\138\38\38\38\39")
        buf.write("\39\39\39\79\u0212\n9\f9\169\u0215\139\39\39\3:\3:\3;")
        buf.write("\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("D\6D\u022e\nD\rD\16D\u022f\3D\3D\3E\3E\3E\3F\3F\7F\u0239")
        buf.write("\nF\fF\16F\u023c\13F\3F\3F\3G\3G\3\u0095\2H\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\2o\66q\2s\67u8w9y")
        buf.write(":{;}<\177=\u0081>\u0083?\u0085@\u0087A\u0089B\u008bC\u008d")
        buf.write("D\3\2\r\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63")
        buf.write(";\3\2\62;\4\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\4\2\f\f")
        buf.write("$$\5\2\n\f\17\17\"\"\t\2))^^ddhhppttvv\2\u0252\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("o\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2")
        buf.write("\2\5\u009d\3\2\2\2\7\u00a8\3\2\2\2\t\u00ad\3\2\2\2\13")
        buf.write("\u00b5\3\2\2\2\r\u00ba\3\2\2\2\17\u00c0\3\2\2\2\21\u00c6")
        buf.write("\3\2\2\2\23\u00cc\3\2\2\2\25\u00d3\3\2\2\2\27\u00d7\3")
        buf.write("\2\2\2\31\u00df\3\2\2\2\33\u00e3\3\2\2\2\35\u00ea\3\2")
        buf.write("\2\2\37\u00f3\3\2\2\2!\u00f6\3\2\2\2#\u00ff\3\2\2\2%\u0102")
        buf.write("\3\2\2\2\'\u0107\3\2\2\2)\u010a\3\2\2\2+\u0110\3\2\2\2")
        buf.write("-\u0118\3\2\2\2/\u0124\3\2\2\2\61\u0131\3\2\2\2\63\u013b")
        buf.write("\3\2\2\2\65\u0146\3\2\2\2\67\u0152\3\2\2\29\u015f\3\2")
        buf.write("\2\2;\u016a\3\2\2\2=\u0176\3\2\2\2?\u017c\3\2\2\2A\u018b")
        buf.write("\3\2\2\2C\u018e\3\2\2\2E\u0190\3\2\2\2G\u0192\3\2\2\2")
        buf.write("I\u0194\3\2\2\2K\u0196\3\2\2\2M\u0198\3\2\2\2O\u019a\3")
        buf.write("\2\2\2Q\u019d\3\2\2\2S\u01a0\3\2\2\2U\u01a3\3\2\2\2W\u01a5")
        buf.write("\3\2\2\2Y\u01a8\3\2\2\2[\u01aa\3\2\2\2]\u01ac\3\2\2\2")
        buf.write("_\u01af\3\2\2\2a\u01bb\3\2\2\2c\u01bd\3\2\2\2e\u01d5\3")
        buf.write("\2\2\2g\u01d9\3\2\2\2i\u01ef\3\2\2\2k\u01f1\3\2\2\2m\u01f8")
        buf.write("\3\2\2\2o\u0201\3\2\2\2q\u020d\3\2\2\2s\u0218\3\2\2\2")
        buf.write("u\u021a\3\2\2\2w\u021c\3\2\2\2y\u021e\3\2\2\2{\u0220\3")
        buf.write("\2\2\2}\u0222\3\2\2\2\177\u0224\3\2\2\2\u0081\u0226\3")
        buf.write("\2\2\2\u0083\u0228\3\2\2\2\u0085\u022a\3\2\2\2\u0087\u022d")
        buf.write("\3\2\2\2\u0089\u0233\3\2\2\2\u008b\u0236\3\2\2\2\u008d")
        buf.write("\u023f\3\2\2\2\u008f\u0090\7\61\2\2\u0090\u0091\7,\2\2")
        buf.write("\u0091\u0095\3\2\2\2\u0092\u0094\13\2\2\2\u0093\u0092")
        buf.write("\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0096\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0098\u0099\7,\2\2\u0099\u009a\7\61\2\2\u009a\u009b\3")
        buf.write("\2\2\2\u009b\u009c\b\2\2\2\u009c\4\3\2\2\2\u009d\u009e")
        buf.write("\7\61\2\2\u009e\u009f\7\61\2\2\u009f\u00a3\3\2\2\2\u00a0")
        buf.write("\u00a2\n\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6\3")
        buf.write("\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\b\3\2\2\u00a7\6")
        buf.write("\3\2\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7q\2\2\u00ac\b\3\2\2\2\u00ad\u00ae")
        buf.write("\7k\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\u00b2\7i\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4")
        buf.write("\7t\2\2\u00b4\n\3\2\2\2\u00b5\u00b6\7x\2\2\u00b6\u00b7")
        buf.write("\7q\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7f\2\2\u00b9\f")
        buf.write("\3\2\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7{\2\2\u00bf\16")
        buf.write("\3\2\2\2\u00c0\u00c1\7d\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7m\2\2\u00c5\20")
        buf.write("\3\2\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9")
        buf.write("\7q\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7v\2\2\u00cb\22")
        buf.write("\3\2\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\u00d0\7w\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\24\3\2\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7w\2\2\u00d5\u00d6\7v\2\2\u00d6\26\3\2\2\2\u00d7\u00d8")
        buf.write("\7d\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\30\3\2\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\u00e2\7t\2\2\u00e2\32\3\2\2\2\u00e3\u00e4")
        buf.write("\7u\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7i\2\2\u00e9\34")
        buf.write("\3\2\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7g\2\2\u00f2\36")
        buf.write("\3\2\2\2\u00f3\u00f4\7f\2\2\u00f4\u00f5\7q\2\2\u00f5 ")
        buf.write("\3\2\2\2\u00f6\u00f7\7h\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9")
        buf.write("\7p\2\2\u00f9\u00fa\7e\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7p\2\2\u00fe\"")
        buf.write("\3\2\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7h\2\2\u0101$")
        buf.write("\3\2\2\2\u0102\u0103\7g\2\2\u0103\u0104\7n\2\2\u0104\u0105")
        buf.write("\7u\2\2\u0105\u0106\7g\2\2\u0106&\3\2\2\2\u0107\u0108")
        buf.write("\7k\2\2\u0108\u0109\7h\2\2\u0109(\3\2\2\2\u010a\u010b")
        buf.write("\7y\2\2\u010b\u010c\7j\2\2\u010c\u010d\7k\2\2\u010d\u010e")
        buf.write("\7n\2\2\u010e\u010f\7g\2\2\u010f*\3\2\2\2\u0110\u0111")
        buf.write("\7k\2\2\u0111\u0112\7p\2\2\u0112\u0113\7j\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114\u0115\7t\2\2\u0115\u0116\7k\2\2\u0116\u0117")
        buf.write("\7v\2\2\u0117,\3\2\2\2\u0118\u0119\7t\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a\u011b\7c\2\2\u011b\u011c\7f\2\2\u011c\u011d")
        buf.write("\7K\2\2\u011d\u011e\7p\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7i\2\2\u0121\u0122\7g\2\2\u0122\u0123")
        buf.write("\7t\2\2\u0123.\3\2\2\2\u0124\u0125\7r\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128\u0129")
        buf.write("\7v\2\2\u0129\u012a\7K\2\2\u012a\u012b\7p\2\2\u012b\u012c")
        buf.write("\7v\2\2\u012c\u012d\7g\2\2\u012d\u012e\7i\2\2\u012e\u012f")
        buf.write("\7g\2\2\u012f\u0130\7t\2\2\u0130\60\3\2\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134\7c\2\2\u0134\u0135")
        buf.write("\7f\2\2\u0135\u0136\7H\2\2\u0136\u0137\7n\2\2\u0137\u0138")
        buf.write("\7q\2\2\u0138\u0139\7c\2\2\u0139\u013a\7v\2\2\u013a\62")
        buf.write("\3\2\2\2\u013b\u013c\7r\2\2\u013c\u013d\7t\2\2\u013d\u013e")
        buf.write("\7k\2\2\u013e\u013f\7p\2\2\u013f\u0140\7v\2\2\u0140\u0141")
        buf.write("\7H\2\2\u0141\u0142\7n\2\2\u0142\u0143\7q\2\2\u0143\u0144")
        buf.write("\7c\2\2\u0144\u0145\7v\2\2\u0145\64\3\2\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\u0148\7g\2\2\u0148\u0149\7c\2\2\u0149\u014a")
        buf.write("\7f\2\2\u014a\u014b\7D\2\2\u014b\u014c\7q\2\2\u014c\u014d")
        buf.write("\7q\2\2\u014d\u014e\7n\2\2\u014e\u014f\7g\2\2\u014f\u0150")
        buf.write("\7c\2\2\u0150\u0151\7p\2\2\u0151\66\3\2\2\2\u0152\u0153")
        buf.write("\7r\2\2\u0153\u0154\7t\2\2\u0154\u0155\7k\2\2\u0155\u0156")
        buf.write("\7p\2\2\u0156\u0157\7v\2\2\u0157\u0158\7D\2\2\u0158\u0159")
        buf.write("\7q\2\2\u0159\u015a\7q\2\2\u015a\u015b\7n\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c\u015d\7c\2\2\u015d\u015e\7p\2\2\u015e8\3")
        buf.write("\2\2\2\u015f\u0160\7t\2\2\u0160\u0161\7g\2\2\u0161\u0162")
        buf.write("\7c\2\2\u0162\u0163\7f\2\2\u0163\u0164\7U\2\2\u0164\u0165")
        buf.write("\7v\2\2\u0165\u0166\7t\2\2\u0166\u0167\7k\2\2\u0167\u0168")
        buf.write("\7p\2\2\u0168\u0169\7i\2\2\u0169:\3\2\2\2\u016a\u016b")
        buf.write("\7r\2\2\u016b\u016c\7t\2\2\u016c\u016d\7k\2\2\u016d\u016e")
        buf.write("\7p\2\2\u016e\u016f\7v\2\2\u016f\u0170\7U\2\2\u0170\u0171")
        buf.write("\7v\2\2\u0171\u0172\7t\2\2\u0172\u0173\7k\2\2\u0173\u0174")
        buf.write("\7p\2\2\u0174\u0175\7i\2\2\u0175<\3\2\2\2\u0176\u0177")
        buf.write("\7u\2\2\u0177\u0178\7w\2\2\u0178\u0179\7r\2\2\u0179\u017a")
        buf.write("\7g\2\2\u017a\u017b\7t\2\2\u017b>\3\2\2\2\u017c\u017d")
        buf.write("\7r\2\2\u017d\u017e\7t\2\2\u017e\u017f\7g\2\2\u017f\u0180")
        buf.write("\7x\2\2\u0180\u0181\7g\2\2\u0181\u0182\7p\2\2\u0182\u0183")
        buf.write("\7v\2\2\u0183\u0184\7F\2\2\u0184\u0185\7g\2\2\u0185\u0186")
        buf.write("\7h\2\2\u0186\u0187\7c\2\2\u0187\u0188\7w\2\2\u0188\u0189")
        buf.write("\7n\2\2\u0189\u018a\7v\2\2\u018a@\3\2\2\2\u018b\u018c")
        buf.write("\7<\2\2\u018c\u018d\7<\2\2\u018dB\3\2\2\2\u018e\u018f")
        buf.write("\7-\2\2\u018fD\3\2\2\2\u0190\u0191\7/\2\2\u0191F\3\2\2")
        buf.write("\2\u0192\u0193\7,\2\2\u0193H\3\2\2\2\u0194\u0195\7\61")
        buf.write("\2\2\u0195J\3\2\2\2\u0196\u0197\7\'\2\2\u0197L\3\2\2\2")
        buf.write("\u0198\u0199\7#\2\2\u0199N\3\2\2\2\u019a\u019b\7(\2\2")
        buf.write("\u019b\u019c\7(\2\2\u019cP\3\2\2\2\u019d\u019e\7~\2\2")
        buf.write("\u019e\u019f\7~\2\2\u019fR\3\2\2\2\u01a0\u01a1\7?\2\2")
        buf.write("\u01a1\u01a2\7?\2\2\u01a2T\3\2\2\2\u01a3\u01a4\7?\2\2")
        buf.write("\u01a4V\3\2\2\2\u01a5\u01a6\7#\2\2\u01a6\u01a7\7?\2\2")
        buf.write("\u01a7X\3\2\2\2\u01a8\u01a9\7>\2\2\u01a9Z\3\2\2\2\u01aa")
        buf.write("\u01ab\7@\2\2\u01ab\\\3\2\2\2\u01ac\u01ad\7>\2\2\u01ad")
        buf.write("\u01ae\7?\2\2\u01ae^\3\2\2\2\u01af\u01b0\7@\2\2\u01b0")
        buf.write("\u01b1\7?\2\2\u01b1`\3\2\2\2\u01b2\u01b3\7v\2\2\u01b3")
        buf.write("\u01b4\7t\2\2\u01b4\u01b5\7w\2\2\u01b5\u01bc\7g\2\2\u01b6")
        buf.write("\u01b7\7h\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9\7n\2\2\u01b9")
        buf.write("\u01ba\7u\2\2\u01ba\u01bc\7g\2\2\u01bb\u01b2\3\2\2\2\u01bb")
        buf.write("\u01b6\3\2\2\2\u01bcb\3\2\2\2\u01bd\u01c1\t\3\2\2\u01be")
        buf.write("\u01c0\t\4\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c3\3\2\2\2")
        buf.write("\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2d\3\2\2")
        buf.write("\2\u01c3\u01c1\3\2\2\2\u01c4\u01c6\5i\65\2\u01c5\u01c4")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7")
        buf.write("\u01c8\5k\66\2\u01c8\u01c9\5m\67\2\u01c9\u01d6\3\2\2\2")
        buf.write("\u01ca\u01cc\5i\65\2\u01cb\u01cd\5k\66\2\u01cc\u01cb\3")
        buf.write("\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf")
        buf.write("\5m\67\2\u01cf\u01d6\3\2\2\2\u01d0\u01d1\5i\65\2\u01d1")
        buf.write("\u01d3\5k\66\2\u01d2\u01d4\5m\67\2\u01d3\u01d2\3\2\2\2")
        buf.write("\u01d3\u01d4\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01c5\3")
        buf.write("\2\2\2\u01d5\u01ca\3\2\2\2\u01d5\u01d0\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d8\b\63\3\2\u01d8f\3\2\2\2\u01d9\u01da")
        buf.write("\5i\65\2\u01da\u01db\b\64\4\2\u01dbh\3\2\2\2\u01dc\u01f0")
        buf.write("\7\62\2\2\u01dd\u01e1\t\5\2\2\u01de\u01e0\t\6\2\2\u01df")
        buf.write("\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e1\u01e2\3\2\2\2\u01e2\u01ec\3\2\2\2\u01e3\u01e1\3")
        buf.write("\2\2\2\u01e4\u01e6\7a\2\2\u01e5\u01e7\t\6\2\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e9\u01eb\3\2\2\2\u01ea\u01e4\3\2\2\2")
        buf.write("\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3")
        buf.write("\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01dc")
        buf.write("\3\2\2\2\u01ef\u01dd\3\2\2\2\u01f0j\3\2\2\2\u01f1\u01f5")
        buf.write("\7\60\2\2\u01f2\u01f4\t\6\2\2\u01f3\u01f2\3\2\2\2\u01f4")
        buf.write("\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f6l\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01fa\t\7\2")
        buf.write("\2\u01f9\u01fb\t\b\2\2\u01fa\u01f9\3\2\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fb\u01fd\3\2\2\2\u01fc\u01fe\t\6\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u01fd\3\2\2\2")
        buf.write("\u01ff\u0200\3\2\2\2\u0200n\3\2\2\2\u0201\u0207\7$\2\2")
        buf.write("\u0202\u0203\7^\2\2\u0203\u0206\t\t\2\2\u0204\u0206\n")
        buf.write("\n\2\2\u0205\u0202\3\2\2\2\u0205\u0204\3\2\2\2\u0206\u0209")
        buf.write("\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208")
        buf.write("\u020a\3\2\2\2\u0209\u0207\3\2\2\2\u020a\u020b\7$\2\2")
        buf.write("\u020b\u020c\b8\5\2\u020cp\3\2\2\2\u020d\u0213\7$\2\2")
        buf.write("\u020e\u020f\7^\2\2\u020f\u0212\t\t\2\2\u0210\u0212\n")
        buf.write("\n\2\2\u0211\u020e\3\2\2\2\u0211\u0210\3\2\2\2\u0212\u0215")
        buf.write("\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("\u0216\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0217\7$\2\2")
        buf.write("\u0217r\3\2\2\2\u0218\u0219\7=\2\2\u0219t\3\2\2\2\u021a")
        buf.write("\u021b\7.\2\2\u021bv\3\2\2\2\u021c\u021d\7]\2\2\u021d")
        buf.write("x\3\2\2\2\u021e\u021f\7_\2\2\u021fz\3\2\2\2\u0220\u0221")
        buf.write("\7*\2\2\u0221|\3\2\2\2\u0222\u0223\7+\2\2\u0223~\3\2\2")
        buf.write("\2\u0224\u0225\7}\2\2\u0225\u0080\3\2\2\2\u0226\u0227")
        buf.write("\7\177\2\2\u0227\u0082\3\2\2\2\u0228\u0229\7\60\2\2\u0229")
        buf.write("\u0084\3\2\2\2\u022a\u022b\7<\2\2\u022b\u0086\3\2\2\2")
        buf.write("\u022c\u022e\t\13\2\2\u022d\u022c\3\2\2\2\u022e\u022f")
        buf.write("\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230")
        buf.write("\u0231\3\2\2\2\u0231\u0232\bD\2\2\u0232\u0088\3\2\2\2")
        buf.write("\u0233\u0234\13\2\2\2\u0234\u0235\bE\6\2\u0235\u008a\3")
        buf.write("\2\2\2\u0236\u023a\7^\2\2\u0237\u0239\n\f\2\2\u0238\u0237")
        buf.write("\3\2\2\2\u0239\u023c\3\2\2\2\u023a\u0238\3\2\2\2\u023a")
        buf.write("\u023b\3\2\2\2\u023b\u023d\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023d\u023e\bF\7\2\u023e\u008c\3\2\2\2\u023f\u0240\13")
        buf.write("\2\2\2\u0240\u008e\3\2\2\2\30\2\u0095\u00a3\u01bb\u01c1")
        buf.write("\u01c5\u01cc\u01d3\u01d5\u01e1\u01e8\u01ec\u01ef\u01f5")
        buf.write("\u01fa\u01ff\u0205\u0207\u0211\u0213\u022f\u023a\b\b\2")
        buf.write("\2\3\63\2\3\64\3\38\4\3E\5\3F\6")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCK_COMMENT = 1
    LINE_COMMENT = 2
    AUTO = 3
    INT = 4
    VOID = 5
    ARRAY = 6
    BREAK = 7
    FLOAT = 8
    RETURN = 9
    OUT = 10
    BOOL = 11
    FOR = 12
    STR = 13
    CONTINUE = 14
    DO = 15
    FUNCT = 16
    OF = 17
    ELSE = 18
    IF = 19
    WHILE = 20
    INHERIT = 21
    READ_INT = 22
    PRINT_INT = 23
    READ_FLOAT = 24
    PRINT_FLOAT = 25
    READ_BOOL = 26
    PRINT_BOOL = 27
    READ_STR = 28
    PRINT_STR = 29
    SUPER_FUNC = 30
    PREVENT_DEFAUT = 31
    OP_STR_CONCAT = 32
    OP_ADD = 33
    OP_MINUS = 34
    OP_MUL = 35
    OP_DIV = 36
    OP_MOD = 37
    OP_NOT = 38
    OP_AND = 39
    OP_OR = 40
    OP_EQ_EQ = 41
    OP_EQ = 42
    OP_INEQ = 43
    OP_LESS = 44
    OP_GREATER = 45
    OP_LESS_OR_EQ = 46
    OP_GREA_OR_EQ = 47
    BOOLLIT = 48
    ID = 49
    FLOATLIT = 50
    INTLIT = 51
    STRINGLIT = 52
    SEMI = 53
    COMMA = 54
    LC = 55
    RC = 56
    LB = 57
    RB = 58
    LP = 59
    RP = 60
    DOT = 61
    COLON = 62
    WS = 63
    ERROR_CHAR = 64
    ILLEGAL_ESCAPE = 65
    ULLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'integer'", "'void'", "'array'", "'break'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
            "'readInteger'", "'printInteger'", "'readFloat'", "'printFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'::'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'<'", "'>'", "'<='", "'>='", "';'", "','", "'['", "']'", "'('", 
            "')'", "'{'", "'}'", "'.'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", "INT", "VOID", "ARRAY", 
            "BREAK", "FLOAT", "RETURN", "OUT", "BOOL", "FOR", "STR", "CONTINUE", 
            "DO", "FUNCT", "OF", "ELSE", "IF", "WHILE", "INHERIT", "READ_INT", 
            "PRINT_INT", "READ_FLOAT", "PRINT_FLOAT", "READ_BOOL", "PRINT_BOOL", 
            "READ_STR", "PRINT_STR", "SUPER_FUNC", "PREVENT_DEFAUT", "OP_STR_CONCAT", 
            "OP_ADD", "OP_MINUS", "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", 
            "OP_AND", "OP_OR", "OP_EQ_EQ", "OP_EQ", "OP_INEQ", "OP_LESS", 
            "OP_GREATER", "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", "BOOLLIT", "ID", 
            "FLOATLIT", "INTLIT", "STRINGLIT", "SEMI", "COMMA", "LC", "RC", 
            "LB", "RB", "LP", "RP", "DOT", "COLON", "WS", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "ULLEGAL_ESCAPE" ]

    ruleNames = [ "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", "INT", "VOID", 
                  "ARRAY", "BREAK", "FLOAT", "RETURN", "OUT", "BOOL", "FOR", 
                  "STR", "CONTINUE", "DO", "FUNCT", "OF", "ELSE", "IF", 
                  "WHILE", "INHERIT", "READ_INT", "PRINT_INT", "READ_FLOAT", 
                  "PRINT_FLOAT", "READ_BOOL", "PRINT_BOOL", "READ_STR", 
                  "PRINT_STR", "SUPER_FUNC", "PREVENT_DEFAUT", "OP_STR_CONCAT", 
                  "OP_ADD", "OP_MINUS", "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", 
                  "OP_AND", "OP_OR", "OP_EQ_EQ", "OP_EQ", "OP_INEQ", "OP_LESS", 
                  "OP_GREATER", "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", "BOOLLIT", 
                  "ID", "FLOATLIT", "INTLIT", "INTPART", "DECPART", "EXPPART", 
                  "STRINGLIT", "STRPART", "SEMI", "COMMA", "LC", "RC", "LB", 
                  "RB", "LP", "RP", "DOT", "COLON", "WS", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "ULLEGAL_ESCAPE" ]

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
            actions[49] = self.FLOATLIT_action 
            actions[50] = self.INTLIT_action 
            actions[54] = self.STRINGLIT_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
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
     



# Generated from /home/thanhdxn/Documents/222/PPL_Doc/Asgm-2/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0258\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\5\2\u0096")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u009e\n\3\3\4\3\4\3\4")
        buf.write("\3\4\7\4\u00a4\n\4\f\4\16\4\u00a7\13\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\7\5\u00b2\n\5\f\5\16\5\u00b5\13\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!")
        buf.write("\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(")
        buf.write("\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01cc\n\63\3\64")
        buf.write("\3\64\7\64\u01d0\n\64\f\64\16\64\u01d3\13\64\3\65\5\65")
        buf.write("\u01d6\n\65\3\65\3\65\3\65\3\65\3\65\5\65\u01dd\n\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\5\65\u01e4\n\65\5\65\u01e6\n\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\7\67\u01f0\n")
        buf.write("\67\f\67\16\67\u01f3\13\67\3\67\3\67\6\67\u01f7\n\67\r")
        buf.write("\67\16\67\u01f8\7\67\u01fb\n\67\f\67\16\67\u01fe\13\67")
        buf.write("\5\67\u0200\n\67\38\38\78\u0204\n8\f8\168\u0207\138\3")
        buf.write("9\39\59\u020b\n9\39\69\u020e\n9\r9\169\u020f\3:\3:\3:")
        buf.write("\3:\7:\u0216\n:\f:\16:\u0219\13:\3:\3:\3:\3;\3;\3;\3;")
        buf.write("\7;\u0222\n;\f;\16;\u0225\13;\3;\3;\3<\3<\3=\3=\3>\3>")
        buf.write("\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\6F\u023e")
        buf.write("\nF\rF\16F\u023f\3F\3F\3G\3G\3G\3H\3H\7H\u0249\nH\fH\16")
        buf.write("H\u024c\13H\3H\3H\3I\3I\7I\u0252\nI\fI\16I\u0255\13I\3")
        buf.write("I\3I\3\u00a5\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m\2o\2q\2s8u\2w9y:{;}<\177=\u0081>\u0083?\u0085")
        buf.write("@\u0087A\u0089B\u008bC\u008dD\u008fE\u0091F\3\2\16\4\2")
        buf.write("\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\4\2\f\f$$\5\2\n\f\17")
        buf.write("\17\"\"\t\2))^^ddhhppttvv\3\2\60\60\2\u0270\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2s\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\3\u0095\3\2\2\2\5\u009d\3\2\2\2\7\u009f\3\2\2")
        buf.write("\2\t\u00ad\3\2\2\2\13\u00b8\3\2\2\2\r\u00bd\3\2\2\2\17")
        buf.write("\u00c5\3\2\2\2\21\u00ca\3\2\2\2\23\u00d0\3\2\2\2\25\u00d6")
        buf.write("\3\2\2\2\27\u00dc\3\2\2\2\31\u00e3\3\2\2\2\33\u00e7\3")
        buf.write("\2\2\2\35\u00ef\3\2\2\2\37\u00f3\3\2\2\2!\u00fa\3\2\2")
        buf.write("\2#\u0103\3\2\2\2%\u0106\3\2\2\2\'\u010f\3\2\2\2)\u0112")
        buf.write("\3\2\2\2+\u0117\3\2\2\2-\u011a\3\2\2\2/\u0120\3\2\2\2")
        buf.write("\61\u0128\3\2\2\2\63\u0134\3\2\2\2\65\u0141\3\2\2\2\67")
        buf.write("\u014b\3\2\2\29\u0156\3\2\2\2;\u0162\3\2\2\2=\u016f\3")
        buf.write("\2\2\2?\u017a\3\2\2\2A\u0186\3\2\2\2C\u018c\3\2\2\2E\u019b")
        buf.write("\3\2\2\2G\u019e\3\2\2\2I\u01a0\3\2\2\2K\u01a2\3\2\2\2")
        buf.write("M\u01a4\3\2\2\2O\u01a6\3\2\2\2Q\u01a8\3\2\2\2S\u01aa\3")
        buf.write("\2\2\2U\u01ad\3\2\2\2W\u01b0\3\2\2\2Y\u01b3\3\2\2\2[\u01b5")
        buf.write("\3\2\2\2]\u01b8\3\2\2\2_\u01ba\3\2\2\2a\u01bc\3\2\2\2")
        buf.write("c\u01bf\3\2\2\2e\u01cb\3\2\2\2g\u01cd\3\2\2\2i\u01e5\3")
        buf.write("\2\2\2k\u01e9\3\2\2\2m\u01ff\3\2\2\2o\u0201\3\2\2\2q\u0208")
        buf.write("\3\2\2\2s\u0211\3\2\2\2u\u021d\3\2\2\2w\u0228\3\2\2\2")
        buf.write("y\u022a\3\2\2\2{\u022c\3\2\2\2}\u022e\3\2\2\2\177\u0230")
        buf.write("\3\2\2\2\u0081\u0232\3\2\2\2\u0083\u0234\3\2\2\2\u0085")
        buf.write("\u0236\3\2\2\2\u0087\u0238\3\2\2\2\u0089\u023a\3\2\2\2")
        buf.write("\u008b\u023d\3\2\2\2\u008d\u0243\3\2\2\2\u008f\u0246\3")
        buf.write("\2\2\2\u0091\u024f\3\2\2\2\u0093\u0096\5S*\2\u0094\u0096")
        buf.write("\5U+\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\4")
        buf.write("\3\2\2\2\u0097\u009e\5W,\2\u0098\u009e\5[.\2\u0099\u009e")
        buf.write("\5]/\2\u009a\u009e\5a\61\2\u009b\u009e\5_\60\2\u009c\u009e")
        buf.write("\5c\62\2\u009d\u0097\3\2\2\2\u009d\u0098\3\2\2\2\u009d")
        buf.write("\u0099\3\2\2\2\u009d\u009a\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009c\3\2\2\2\u009e\6\3\2\2\2\u009f\u00a0\7\61")
        buf.write("\2\2\u00a0\u00a1\7,\2\2\u00a1\u00a5\3\2\2\2\u00a2\u00a4")
        buf.write("\13\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7,\2\2\u00a9\u00aa\7")
        buf.write("\61\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\b\4\2\2\u00ac")
        buf.write("\b\3\2\2\2\u00ad\u00ae\7\61\2\2\u00ae\u00af\7\61\2\2\u00af")
        buf.write("\u00b3\3\2\2\2\u00b0\u00b2\n\2\2\2\u00b1\u00b0\3\2\2\2")
        buf.write("\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7")
        buf.write("\b\5\2\2\u00b7\n\3\2\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba")
        buf.write("\7w\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7q\2\2\u00bc\f")
        buf.write("\3\2\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7i\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\u00c4\7t\2\2\u00c4\16\3\2\2\2\u00c5\u00c6")
        buf.write("\7x\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7f\2\2\u00c9\20\3\2\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc")
        buf.write("\7t\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf")
        buf.write("\7{\2\2\u00cf\22\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7m\2\2\u00d5\24\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7v\2\2\u00db\26\3\2\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7p\2\2\u00e2\30\3\2\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6\7v\2\2\u00e6\32")
        buf.write("\3\2\2\2\u00e7\u00e8\7d\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7c\2\2\u00ed\u00ee\7p\2\2\u00ee\34\3\2\2\2\u00ef\u00f0")
        buf.write("\7h\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7t\2\2\u00f2\36")
        buf.write("\3\2\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6")
        buf.write("\7t\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7i\2\2\u00f9 \3\2\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc")
        buf.write("\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7w\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\"\3\2\2\2\u0103\u0104\7f\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105$\3\2\2\2\u0106\u0107\7h\2\2\u0107\u0108")
        buf.write("\7w\2\2\u0108\u0109\7p\2\2\u0109\u010a\7e\2\2\u010a\u010b")
        buf.write("\7v\2\2\u010b\u010c\7k\2\2\u010c\u010d\7q\2\2\u010d\u010e")
        buf.write("\7p\2\2\u010e&\3\2\2\2\u010f\u0110\7q\2\2\u0110\u0111")
        buf.write("\7h\2\2\u0111(\3\2\2\2\u0112\u0113\7g\2\2\u0113\u0114")
        buf.write("\7n\2\2\u0114\u0115\7u\2\2\u0115\u0116\7g\2\2\u0116*\3")
        buf.write("\2\2\2\u0117\u0118\7k\2\2\u0118\u0119\7h\2\2\u0119,\3")
        buf.write("\2\2\2\u011a\u011b\7y\2\2\u011b\u011c\7j\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7n\2\2\u011e\u011f\7g\2\2\u011f.\3")
        buf.write("\2\2\2\u0120\u0121\7k\2\2\u0121\u0122\7p\2\2\u0122\u0123")
        buf.write("\7j\2\2\u0123\u0124\7g\2\2\u0124\u0125\7t\2\2\u0125\u0126")
        buf.write("\7k\2\2\u0126\u0127\7v\2\2\u0127\60\3\2\2\2\u0128\u0129")
        buf.write("\7t\2\2\u0129\u012a\7g\2\2\u012a\u012b\7c\2\2\u012b\u012c")
        buf.write("\7f\2\2\u012c\u012d\7K\2\2\u012d\u012e\7p\2\2\u012e\u012f")
        buf.write("\7v\2\2\u012f\u0130\7g\2\2\u0130\u0131\7i\2\2\u0131\u0132")
        buf.write("\7g\2\2\u0132\u0133\7t\2\2\u0133\62\3\2\2\2\u0134\u0135")
        buf.write("\7r\2\2\u0135\u0136\7t\2\2\u0136\u0137\7k\2\2\u0137\u0138")
        buf.write("\7p\2\2\u0138\u0139\7v\2\2\u0139\u013a\7K\2\2\u013a\u013b")
        buf.write("\7p\2\2\u013b\u013c\7v\2\2\u013c\u013d\7g\2\2\u013d\u013e")
        buf.write("\7i\2\2\u013e\u013f\7g\2\2\u013f\u0140\7t\2\2\u0140\64")
        buf.write("\3\2\2\2\u0141\u0142\7t\2\2\u0142\u0143\7g\2\2\u0143\u0144")
        buf.write("\7c\2\2\u0144\u0145\7f\2\2\u0145\u0146\7H\2\2\u0146\u0147")
        buf.write("\7n\2\2\u0147\u0148\7q\2\2\u0148\u0149\7c\2\2\u0149\u014a")
        buf.write("\7v\2\2\u014a\66\3\2\2\2\u014b\u014c\7y\2\2\u014c\u014d")
        buf.write("\7t\2\2\u014d\u014e\7k\2\2\u014e\u014f\7v\2\2\u014f\u0150")
        buf.write("\7g\2\2\u0150\u0151\7H\2\2\u0151\u0152\7n\2\2\u0152\u0153")
        buf.write("\7q\2\2\u0153\u0154\7c\2\2\u0154\u0155\7v\2\2\u01558\3")
        buf.write("\2\2\2\u0156\u0157\7t\2\2\u0157\u0158\7g\2\2\u0158\u0159")
        buf.write("\7c\2\2\u0159\u015a\7f\2\2\u015a\u015b\7D\2\2\u015b\u015c")
        buf.write("\7q\2\2\u015c\u015d\7q\2\2\u015d\u015e\7n\2\2\u015e\u015f")
        buf.write("\7g\2\2\u015f\u0160\7c\2\2\u0160\u0161\7p\2\2\u0161:\3")
        buf.write("\2\2\2\u0162\u0163\7r\2\2\u0163\u0164\7t\2\2\u0164\u0165")
        buf.write("\7k\2\2\u0165\u0166\7p\2\2\u0166\u0167\7v\2\2\u0167\u0168")
        buf.write("\7D\2\2\u0168\u0169\7q\2\2\u0169\u016a\7q\2\2\u016a\u016b")
        buf.write("\7n\2\2\u016b\u016c\7g\2\2\u016c\u016d\7c\2\2\u016d\u016e")
        buf.write("\7p\2\2\u016e<\3\2\2\2\u016f\u0170\7t\2\2\u0170\u0171")
        buf.write("\7g\2\2\u0171\u0172\7c\2\2\u0172\u0173\7f\2\2\u0173\u0174")
        buf.write("\7U\2\2\u0174\u0175\7v\2\2\u0175\u0176\7t\2\2\u0176\u0177")
        buf.write("\7k\2\2\u0177\u0178\7p\2\2\u0178\u0179\7i\2\2\u0179>\3")
        buf.write("\2\2\2\u017a\u017b\7r\2\2\u017b\u017c\7t\2\2\u017c\u017d")
        buf.write("\7k\2\2\u017d\u017e\7p\2\2\u017e\u017f\7v\2\2\u017f\u0180")
        buf.write("\7U\2\2\u0180\u0181\7v\2\2\u0181\u0182\7t\2\2\u0182\u0183")
        buf.write("\7k\2\2\u0183\u0184\7p\2\2\u0184\u0185\7i\2\2\u0185@\3")
        buf.write("\2\2\2\u0186\u0187\7u\2\2\u0187\u0188\7w\2\2\u0188\u0189")
        buf.write("\7r\2\2\u0189\u018a\7g\2\2\u018a\u018b\7t\2\2\u018bB\3")
        buf.write("\2\2\2\u018c\u018d\7r\2\2\u018d\u018e\7t\2\2\u018e\u018f")
        buf.write("\7g\2\2\u018f\u0190\7x\2\2\u0190\u0191\7g\2\2\u0191\u0192")
        buf.write("\7p\2\2\u0192\u0193\7v\2\2\u0193\u0194\7F\2\2\u0194\u0195")
        buf.write("\7g\2\2\u0195\u0196\7h\2\2\u0196\u0197\7c\2\2\u0197\u0198")
        buf.write("\7w\2\2\u0198\u0199\7n\2\2\u0199\u019a\7v\2\2\u019aD\3")
        buf.write("\2\2\2\u019b\u019c\7<\2\2\u019c\u019d\7<\2\2\u019dF\3")
        buf.write("\2\2\2\u019e\u019f\7-\2\2\u019fH\3\2\2\2\u01a0\u01a1\7")
        buf.write("/\2\2\u01a1J\3\2\2\2\u01a2\u01a3\7,\2\2\u01a3L\3\2\2\2")
        buf.write("\u01a4\u01a5\7\61\2\2\u01a5N\3\2\2\2\u01a6\u01a7\7\'\2")
        buf.write("\2\u01a7P\3\2\2\2\u01a8\u01a9\7#\2\2\u01a9R\3\2\2\2\u01aa")
        buf.write("\u01ab\7(\2\2\u01ab\u01ac\7(\2\2\u01acT\3\2\2\2\u01ad")
        buf.write("\u01ae\7~\2\2\u01ae\u01af\7~\2\2\u01afV\3\2\2\2\u01b0")
        buf.write("\u01b1\7?\2\2\u01b1\u01b2\7?\2\2\u01b2X\3\2\2\2\u01b3")
        buf.write("\u01b4\7?\2\2\u01b4Z\3\2\2\2\u01b5\u01b6\7#\2\2\u01b6")
        buf.write("\u01b7\7?\2\2\u01b7\\\3\2\2\2\u01b8\u01b9\7>\2\2\u01b9")
        buf.write("^\3\2\2\2\u01ba\u01bb\7@\2\2\u01bb`\3\2\2\2\u01bc\u01bd")
        buf.write("\7>\2\2\u01bd\u01be\7?\2\2\u01beb\3\2\2\2\u01bf\u01c0")
        buf.write("\7@\2\2\u01c0\u01c1\7?\2\2\u01c1d\3\2\2\2\u01c2\u01c3")
        buf.write("\7v\2\2\u01c3\u01c4\7t\2\2\u01c4\u01c5\7w\2\2\u01c5\u01cc")
        buf.write("\7g\2\2\u01c6\u01c7\7h\2\2\u01c7\u01c8\7c\2\2\u01c8\u01c9")
        buf.write("\7n\2\2\u01c9\u01ca\7u\2\2\u01ca\u01cc\7g\2\2\u01cb\u01c2")
        buf.write("\3\2\2\2\u01cb\u01c6\3\2\2\2\u01ccf\3\2\2\2\u01cd\u01d1")
        buf.write("\t\3\2\2\u01ce\u01d0\t\4\2\2\u01cf\u01ce\3\2\2\2\u01d0")
        buf.write("\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2")
        buf.write("\u01d2h\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d6\5m\67")
        buf.write("\2\u01d5\u01d4\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d8\5o8\2\u01d8\u01d9\5q9\2\u01d9\u01e6")
        buf.write("\3\2\2\2\u01da\u01dc\5m\67\2\u01db\u01dd\5o8\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write("\u01df\5q9\2\u01df\u01e6\3\2\2\2\u01e0\u01e1\5m\67\2\u01e1")
        buf.write("\u01e3\5o8\2\u01e2\u01e4\5q9\2\u01e3\u01e2\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4\u01e6\3\2\2\2\u01e5\u01d5\3\2\2\2")
        buf.write("\u01e5\u01da\3\2\2\2\u01e5\u01e0\3\2\2\2\u01e6\u01e7\3")
        buf.write("\2\2\2\u01e7\u01e8\b\65\3\2\u01e8j\3\2\2\2\u01e9\u01ea")
        buf.write("\5m\67\2\u01ea\u01eb\b\66\4\2\u01ebl\3\2\2\2\u01ec\u0200")
        buf.write("\7\62\2\2\u01ed\u01f1\t\5\2\2\u01ee\u01f0\t\6\2\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2")
        buf.write("\u01f1\u01f2\3\2\2\2\u01f2\u01fc\3\2\2\2\u01f3\u01f1\3")
        buf.write("\2\2\2\u01f4\u01f6\7a\2\2\u01f5\u01f7\t\6\2\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01f4\3\2\2\2")
        buf.write("\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd\3")
        buf.write("\2\2\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01ff\u01ec")
        buf.write("\3\2\2\2\u01ff\u01ed\3\2\2\2\u0200n\3\2\2\2\u0201\u0205")
        buf.write("\7\60\2\2\u0202\u0204\t\6\2\2\u0203\u0202\3\2\2\2\u0204")
        buf.write("\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206p\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u020a\t\7\2")
        buf.write("\2\u0209\u020b\t\b\2\2\u020a\u0209\3\2\2\2\u020a\u020b")
        buf.write("\3\2\2\2\u020b\u020d\3\2\2\2\u020c\u020e\t\6\2\2\u020d")
        buf.write("\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u020d\3\2\2\2")
        buf.write("\u020f\u0210\3\2\2\2\u0210r\3\2\2\2\u0211\u0217\7$\2\2")
        buf.write("\u0212\u0213\7^\2\2\u0213\u0216\t\t\2\2\u0214\u0216\n")
        buf.write("\n\2\2\u0215\u0212\3\2\2\2\u0215\u0214\3\2\2\2\u0216\u0219")
        buf.write("\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218")
        buf.write("\u021a\3\2\2\2\u0219\u0217\3\2\2\2\u021a\u021b\7$\2\2")
        buf.write("\u021b\u021c\b:\5\2\u021ct\3\2\2\2\u021d\u0223\7$\2\2")
        buf.write("\u021e\u021f\7^\2\2\u021f\u0222\t\t\2\2\u0220\u0222\n")
        buf.write("\n\2\2\u0221\u021e\3\2\2\2\u0221\u0220\3\2\2\2\u0222\u0225")
        buf.write("\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u0226\3\2\2\2\u0225\u0223\3\2\2\2\u0226\u0227\7$\2\2")
        buf.write("\u0227v\3\2\2\2\u0228\u0229\7=\2\2\u0229x\3\2\2\2\u022a")
        buf.write("\u022b\7.\2\2\u022bz\3\2\2\2\u022c\u022d\7]\2\2\u022d")
        buf.write("|\3\2\2\2\u022e\u022f\7_\2\2\u022f~\3\2\2\2\u0230\u0231")
        buf.write("\7*\2\2\u0231\u0080\3\2\2\2\u0232\u0233\7+\2\2\u0233\u0082")
        buf.write("\3\2\2\2\u0234\u0235\7}\2\2\u0235\u0084\3\2\2\2\u0236")
        buf.write("\u0237\7\177\2\2\u0237\u0086\3\2\2\2\u0238\u0239\7\60")
        buf.write("\2\2\u0239\u0088\3\2\2\2\u023a\u023b\7<\2\2\u023b\u008a")
        buf.write("\3\2\2\2\u023c\u023e\t\13\2\2\u023d\u023c\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240\3\2\2\2")
        buf.write("\u0240\u0241\3\2\2\2\u0241\u0242\bF\2\2\u0242\u008c\3")
        buf.write("\2\2\2\u0243\u0244\13\2\2\2\u0244\u0245\bG\6\2\u0245\u008e")
        buf.write("\3\2\2\2\u0246\u024a\7^\2\2\u0247\u0249\n\f\2\2\u0248")
        buf.write("\u0247\3\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024a\u024b\3\2\2\2\u024b\u024d\3\2\2\2\u024c\u024a\3")
        buf.write("\2\2\2\u024d\u024e\bH\7\2\u024e\u0090\3\2\2\2\u024f\u0253")
        buf.write("\7$\2\2\u0250\u0252\t\r\2\2\u0251\u0250\3\2\2\2\u0252")
        buf.write("\u0255\3\2\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2")
        buf.write("\u0254\u0256\3\2\2\2\u0255\u0253\3\2\2\2\u0256\u0257\b")
        buf.write("I\b\2\u0257\u0092\3\2\2\2\33\2\u0095\u009d\u00a5\u00b3")
        buf.write("\u01cb\u01d1\u01d5\u01dc\u01e3\u01e5\u01f1\u01f8\u01fc")
        buf.write("\u01ff\u0205\u020a\u020f\u0215\u0217\u0221\u0223\u023f")
        buf.write("\u024a\u0253\t\b\2\2\3\65\2\3\66\3\3:\4\3G\5\3H\6\3I\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LOGIC_OP = 1
    RELATION_OP = 2
    BLOCK_COMMENT = 3
    LINE_COMMENT = 4
    AUTO = 5
    INT = 6
    VOID = 7
    ARRAY = 8
    BREAK = 9
    FLOAT = 10
    RETURN = 11
    OUT = 12
    BOOL = 13
    FOR = 14
    STR = 15
    CONTINUE = 16
    DO = 17
    FUNCT = 18
    OF = 19
    ELSE = 20
    IF = 21
    WHILE = 22
    INHERIT = 23
    READ_INT = 24
    PRINT_INT = 25
    READ_FLOAT = 26
    PRINT_FLOAT = 27
    READ_BOOL = 28
    PRINT_BOOL = 29
    READ_STR = 30
    PRINT_STR = 31
    SUPER_FUNC = 32
    PREVENT_DEFAUT = 33
    OP_STR_CONCAT = 34
    OP_ADD = 35
    OP_MINUS = 36
    OP_MUL = 37
    OP_DIV = 38
    OP_MOD = 39
    OP_NOT = 40
    OP_AND = 41
    OP_OR = 42
    OP_EQ_EQ = 43
    OP_EQ = 44
    OP_INEQ = 45
    OP_LESS = 46
    OP_GREATER = 47
    OP_LESS_OR_EQ = 48
    OP_GREA_OR_EQ = 49
    BOOLLIT = 50
    ID = 51
    FLOATLIT = 52
    INTLIT = 53
    STRINGLIT = 54
    SEMI = 55
    COMMA = 56
    LC = 57
    RC = 58
    LB = 59
    RB = 60
    LP = 61
    RP = 62
    DOT = 63
    COLON = 64
    WS = 65
    ERROR_CHAR = 66
    ILLEGAL_ESCAPE = 67
    UNCLOSE_STRING = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'integer'", "'void'", "'array'", "'break'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'::'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'<'", "'>'", "'<='", "'>='", "';'", "','", "'['", "']'", "'('", 
            "')'", "'{'", "'}'", "'.'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "LOGIC_OP", "RELATION_OP", "BLOCK_COMMENT", "LINE_COMMENT", 
            "AUTO", "INT", "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", 
            "OUT", "BOOL", "FOR", "STR", "CONTINUE", "DO", "FUNCT", "OF", 
            "ELSE", "IF", "WHILE", "INHERIT", "READ_INT", "PRINT_INT", "READ_FLOAT", 
            "PRINT_FLOAT", "READ_BOOL", "PRINT_BOOL", "READ_STR", "PRINT_STR", 
            "SUPER_FUNC", "PREVENT_DEFAUT", "OP_STR_CONCAT", "OP_ADD", "OP_MINUS", 
            "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", "OP_AND", "OP_OR", "OP_EQ_EQ", 
            "OP_EQ", "OP_INEQ", "OP_LESS", "OP_GREATER", "OP_LESS_OR_EQ", 
            "OP_GREA_OR_EQ", "BOOLLIT", "ID", "FLOATLIT", "INTLIT", "STRINGLIT", 
            "SEMI", "COMMA", "LC", "RC", "LB", "RB", "LP", "RP", "DOT", 
            "COLON", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "LOGIC_OP", "RELATION_OP", "BLOCK_COMMENT", "LINE_COMMENT", 
                  "AUTO", "INT", "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", 
                  "OUT", "BOOL", "FOR", "STR", "CONTINUE", "DO", "FUNCT", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "READ_INT", "PRINT_INT", 
                  "READ_FLOAT", "PRINT_FLOAT", "READ_BOOL", "PRINT_BOOL", 
                  "READ_STR", "PRINT_STR", "SUPER_FUNC", "PREVENT_DEFAUT", 
                  "OP_STR_CONCAT", "OP_ADD", "OP_MINUS", "OP_MUL", "OP_DIV", 
                  "OP_MOD", "OP_NOT", "OP_AND", "OP_OR", "OP_EQ_EQ", "OP_EQ", 
                  "OP_INEQ", "OP_LESS", "OP_GREATER", "OP_LESS_OR_EQ", "OP_GREA_OR_EQ", 
                  "BOOLLIT", "ID", "FLOATLIT", "INTLIT", "INTPART", "DECPART", 
                  "EXPPART", "STRINGLIT", "STRPART", "SEMI", "COMMA", "LC", 
                  "RC", "LB", "RB", "LP", "RP", "DOT", "COLON", "WS", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
            actions[51] = self.FLOATLIT_action 
            actions[52] = self.INTLIT_action 
            actions[56] = self.STRINGLIT_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[71] = self.UNCLOSE_STRING_action 
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
     



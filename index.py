import jametLang_interpreter
import jametLang_lexer
import jametLang_parser

from sys import *

#DENGAN MASUKAN BERUPA FILE DENGAN EKSTENSION .jmt
lexer = jametLang_lexer.leksikal()
parser = jametLang_parser.sintaksis()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    jametLang_interpreter.BasicExecute(tree, env)
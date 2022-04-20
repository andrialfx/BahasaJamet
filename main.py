import jametLang_interpreter
import jametLang_lexer
import jametLang_parser

from sys import *

#MASUKAN LANGSUNG DENGAN TERMINAL PADA PROGRAM
if __name__ == '__main__':
    lexer = jametLang_lexer.leksikal()
    parser = jametLang_parser.sintaksis()
    env = {}
    while True:
        try:
            text = input('j4m3t > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            jametLang_interpreter.BasicExecute(tree, env)
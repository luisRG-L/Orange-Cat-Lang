from lexer import *

def parse_code(code):
    parser = Parser(iterateTokens(code))

class Parser:
    op_toks = []

    def __init__(self, op_toks):
        self.op_tok = op_toks
        if VERBOSE_ACTIONS:
            print("Parsing operation tokens")
# type: ignore
from lexer import *

def parse_code(op_tok):
    parser = Parser(op_tok)

class Parser:
    op_tok = None

    def __init__(self, op_tok)
        self.op_tok = op_tok
        if VERBOSE_ACTIONS:
            print("Parsing operation tokens")
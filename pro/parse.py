from lexer import *

def parse_code(code):
    parser = Parser(iterateTokens(code), code)

class Parser:
    op_toks = []
    code = []
    token_pos = 0

    variables = []

    def __init__(self, op_toks, code):
        self.op_toks = op_toks
        self.code = code
        if VERBOSE_ACTIONS:
            print("Parsing operation tokens")

    def error(self):
        raise("Syntax error")

    def verify(self, tokenType):
        if self.op_toks[self.token_pos] == tokenType:
            self.token_pos += 1
        else:
            self.error()

    def doFunctionally(self):
        if self.op_toks[self.token_pos] == tokens[VARTYPE_TOKEN]:
            self.token_pos += 1
            self.verify(tokens[VARNAME_TOKEN])
            self.variables.append([self.code[self.token_pos - 1], self.code[self.token_pos + 1]])
            self.verify(tokens[ASSIGN_TOKEN])
            self.verify(tokens[VALUE_TOKEN])
        elif self.op_toks[self.token_pos] == tokens[VARNAME_TOKEN]:
            verified = False
            for x in range(len(self.variables)):
                if self.variables[x][0] == self.code[self.token_pos]:
                    verified = True
            if not verified:
                self.error()
        self.verify(tokens[END_TOKEN])

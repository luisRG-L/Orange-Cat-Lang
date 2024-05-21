from lexer import *

def parse_code(code):
    tokens = iterateTokens(code)
    parser = Parser(tokens, code)
    parser.doFunctionally()
    parser.iterate()

class Parser:
    def __init__(self, op_toks, code):
        self.op_toks = op_toks
        self.code = code
        self.token_pos = 0
        self.variables = []
        if VERBOSE_ACTIONS:
            print("Parsing operation tokens")

    def error(self):
        raise Exception("Syntax error")

    def verify(self, tokenType):
        if self.op_toks[self.token_pos] == tokenType:
            self.token_pos += 1
        else:
            self.error()

    def doFunctionally(self):
        while self.token_pos < len(self.op_toks):
            if self.op_toks[self.token_pos] == VARTYPE_TOKEN:
                self.token_pos += 1
                self.verify(VARNAME_TOKEN)
                var_name = self.code[self.token_pos - 1]
                self.verify(ASSIGN_TOKEN)
                self.verify(VALUE_TOKEN)
                var_value = self.code[self.token_pos - 1]
                self.variables.append([var_name, var_value])
            elif self.op_toks[self.token_pos] == VARNAME_TOKEN:
                var_name = self.code[self.token_pos]
                if not any(var[0] == var_name for var in self.variables):
                    self.error()
                self.token_pos += 1
            elif self.op_toks[self.token_pos] == COMMAND_TOKEN and self.code[self.token_pos] == "print":
                self.token_pos += 1
                self.verify(KEYWORD_TOKEN)
                self.verify(VALUE_TOKEN)
                printMessage =  self.code[self.token_pos - 1]
                printMessage = printMessage.strip('\"')
                printMessage = printMessage.replace('%', ' ')
                print(printMessage)
                self.verify(KEYWORD_TOKEN)
            else:
                self.error()

    def iterate(self):
        for var in self.variables:
            print(f"Variable {var[0]} with value {var[1]}")

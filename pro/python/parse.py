from lexer import *
from errors import *
from config import *

def parse_code(code):
    tokens = iterateTokens(code)
    parser = Parser(tokens, code)
    parser.doFunctionally()
    if VERBOSE_MEMORY:
        parser.iterate()

class Parser:
    def __init__(self, op_toks, code):
        self.op_toks = op_toks
        self.code = code.split('\n')
        self.token_pos = 0
        self.variables = {}
        self.local_variables = {}
        self.methods = {}
        self.isRunning = True
        if VERBOSE_ACTIONS:
            print("Parsing operation tokens")

    def error(self, text):
        printSyntaxError(text)
        self.isRunning = False

    def verify(self, tokenType, token2=None):
        if self.token_pos < len(self.op_toks):
            if self.op_toks[self.token_pos] == tokenType or (token2 is not None and self.op_toks[self.token_pos] == token2):
                self.token_pos += 1
            else:
                self.error(f"Unexpected token '{self.code[self.token_pos]}'")

    def doFunctionally(self):
        while self.token_pos < len(self.op_toks) and self.isRunning:
            if self.op_toks[self.token_pos] == VARTYPE_TOKEN:
                self.parseVariableDeclaration()
            elif self.op_toks[self.token_pos] == VARNAME_TOKEN:
                if self.code[self.token_pos] in self.methods:
                    self.parseFunctionCall()
                else:
                    self.parseVariableAssignment()
            elif self.op_toks[self.token_pos] == COMMAND_TOKEN:
                if self.code[self.token_pos] == "print":
                    self.parsePrintStatement()
            elif self.op_toks[self.token_pos] == COMMENT_TOKEN:
                print("Comment")
            elif self.op_toks[self.token_pos] == LOCAL_TOKEN:
                self.parseLocalVariableDeclaration()
            else:
                self.error("Unexpected token")
            if self.isRunning and self.token_pos < len(self.op_toks) and self.op_toks[self.token_pos] != END_TOKEN:
                self.error("Expected end of statement")
            else:
                self.token_pos += 1

    def parseVariableDeclaration(self):
        var_type = self.code[self.token_pos]
        self.token_pos += 1
        self.verify(VARNAME_TOKEN)
        var_name = self.code[self.token_pos - 1]
        
        # Check if the variable name is already in use
        if var_name in self.variables:
            self.error(f"Variable {var_name} is already declared")
            return
        
        if var_type == "int" or var_type == "decimal":
            self.verify(ASSIGN_TOKEN)
            var_value = self.parseExpression()  # Parse expression for variable value
            self.variables[var_name] = var_value
        elif var_type == "string":
            self.verify(ASSIGN_TOKEN)
            self.verify(VALUE_TOKEN)  # Check if next token is a value
            var_value = self.code[self.token_pos - 1]
            self.variables[var_name] = var_value
        elif var_type == "bool":
            self.verify(ASSIGN_TOKEN)
            self.verify(VALUE_TOKEN)  # Check if next token is a value
            var_value = True if self.code[self.token_pos - 1] == "true" else False
            self.variables[var_name] = var_value
        elif var_type == "func":
            self.verify(KEYWORD_TOKEN)  # Verifying '('
            params = []
            while self.op_toks[self.token_pos] != KEYWORD_TOKEN or self.code[self.token_pos] != ")":
                param_type = self.code[self.token_pos]
                self.verify(VARTYPE_TOKEN)
                param_name = self.code[self.token_pos]
                self.verify(VARNAME_TOKEN)
                params.append((param_type, param_name))
                if self.op_toks[self.token_pos] == KEYWORD_TOKEN and self.code[self.token_pos] == ",":
                    self.token_pos += 1  # Skip ',

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
        self.code = code
        self.token_pos = 0
        self.variables = {}
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
                elif self.code[self.token_pos] == "question":
                    self.parseAnswerStatement()
            elif self.op_toks[self.token_pos] == COMMENT_TOKEN:
                print("Comment")
            else:
                self.error("Unexpected token")
            if self.isRunning and self.token_pos < len(self.op_toks) and self.op_toks[self.token_pos] != END_TOKEN:
                self.error("Expected end of statement")
            else:
                self.token_pos += 1

    def parseVariableUsage(self):
        var_name = self.code[self.token_pos]
        if var_name in self.variables:
            value = int(self.variables[var_name])
            self.token_pos += 1
            return value
        else:
            self.error(f"Variable {var_name} does not exist")

    def parseVariableDeclaration(self):
        var_type = self.code[self.token_pos]
        self.token_pos += 1
        self.verify(VARNAME_TOKEN)
        var_name = self.code[self.token_pos - 1]
        if var_type == "func":
            self.verify(KEYWORD_TOKEN)  # Verifying '('
            self.verify(KEYWORD_TOKEN)  # Verifying ')'
            self.verify(KEYWORD_TOKEN)  # Verifying '{'
            self.methods[var_name] = []
            while self.op_toks[self.token_pos] != KEYWORD_TOKEN or self.code[self.token_pos] != "}":
                self.methods[var_name].append(self.code[self.token_pos])
                self.token_pos += 1
            self.verify(KEYWORD_TOKEN)  # Verifying '}'
        else:
            self.verify(ASSIGN_TOKEN)
            var_value = self.parseExpression()  # Parse expression for variable value
            self.variables[var_name] = var_value

    def parseVariableAssignment(self):
        var_name = self.code[self.token_pos]
        if var_name not in self.variables:
            self.error(f"{var_name} does not exist")
        self.token_pos += 1
        self.verify(ASSIGN_TOKEN)
        var_value = self.parseExpression()  # Parse expression for variable value
        self.variables[var_name] = var_value

    def parseFunctionCall(self):
        func_name = self.code[self.token_pos]
        self.token_pos += 1
        self.verify(KEYWORD_TOKEN)  # Verifying '('
        self.verify(KEYWORD_TOKEN)  # Verifying ')'
        if func_name not in self.methods:
            self.error(f"Function {func_name} does not exist")
        else:
            self.execute_function(func_name)

    def execute_function(self, func_name):
        if VERBOSE_ACTIONS:
            print(f"Executing function {func_name}")
        func_body = self.methods[func_name]
        token_backup = self.op_toks
        code_backup = self.code
        token_pos_backup = self.token_pos
        
        self.op_toks = iterateTokens(func_body)
        self.code = func_body
        self.token_pos = 0
        
        while self.token_pos < len(self.op_toks) and self.isRunning:
            if self.op_toks[self.token_pos] == COMMAND_TOKEN:
                if  self.code[self.token_pos] == "print":
                    self.parsePrintStatement()
                elif self.code[self.token_pos] == "question":
                    self.parseAnswerStatement()
            elif self.op_toks[self.token_pos] == VARNAME_TOKEN:
                if self.code[self.token_pos] in self.variables:
                    self.parseVariableUsage()
            elif self.op_toks[self.token_pos] == VARNAME_TOKEN:
                if self.code[self.token_pos] in self.methods:
                    self.parseFunctionCall()
            elif self.op_toks[self.token_pos] == VARTYPE_TOKEN:
                self.parseVariableDeclaration()
            self.verify(END_TOKEN)
        
        self.op_toks = token_backup
        self.code = code_backup
        self.token_pos = token_pos_backup

    def parsePrintStatement(self):
        self.token_pos += 1  # Skip 'print'
        self.verify(KEYWORD_TOKEN)  # Verifying '('
        message_tokens = []
        while self.op_toks[self.token_pos] != KEYWORD_TOKEN or self.code[self.token_pos] != ")":
            message_tokens.append(self.code[self.token_pos])
            self.token_pos += 1
        self.verify(KEYWORD_TOKEN)  # Verifying ')'
        
        message = " ".join(message_tokens)
        # Replace ${var} with the variable's value
        for var in self.variables:
            message = message.replace(f"${{{var}}}", str(self.variables[var]))
        
        print(message.strip('"').replace('%', ' '))
    
    def parseAnswerStatement(self):
        self.token_pos += 1  # Skip 'print'
        self.verify(KEYWORD_TOKEN)  # Verifying '('
        message_tokens = []
        while self.op_toks[self.token_pos] != KEYWORD_TOKEN or self.code[self.token_pos] != ")":
            message_tokens.append(self.code[self.token_pos])
            self.token_pos += 1
        self.verify(KEYWORD_TOKEN)  # Verifying ')'
        
        message = " ".join(message_tokens)
        # Replace ${var} with the variable's value
        for var in self.variables:
            message = message.replace(f"${{{var}}}", str(self.variables[var]))
        
        question = message.strip('"').replace('%', ' ')
        print(f"Answer: {input(question)}")

    def iterate(self):
        for var in self.variables:
            print(f"Variable {var} with value {self.variables[var]}")
        for method in self.methods:
            print(f"Method {method} with code: {self.methods[method]}")

    def parseExpression(self):
        result = self.parseTerm()
        while self.token_pos < len(self.op_toks) and (self.code[self.token_pos] == '+' or self.code[self.token_pos] == '-'):
            if self.code[self.token_pos] == '+':
                self.token_pos += 1
                result += self.parseTerm()
            elif self.code[self.token_pos] == '-':
                self.token_pos += 1
                result -= self.parseTerm()
        return result

    def parseTerm(self):
        result = self.parseFactor()
        while self.token_pos < len(self.op_toks) and (self.code[self.token_pos] == '*' or self.code[self.token_pos] == '/'):
            if self.code[self.token_pos] == '*':
                self.token_pos += 1
                result *= self.parseFactor()
            elif self.code[self.token_pos] == '/':
                self.token_pos += 1
                result /= self.parseFactor()
        return result

    def parseFactor(self):
        if self.op_toks[self.token_pos] == VALUE_TOKEN:
            value = int(self.code[self.token_pos])
            self.token_pos += 1
            return value
        elif self.op_toks[self.token_pos] == VARNAME_TOKEN:
            var_name = self.code[self.token_pos]
            if var_name in self.variables:
                value = int(self.variables[var_name])
               

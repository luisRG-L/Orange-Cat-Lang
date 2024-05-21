# lexer.py
from config import *

VARTYPE = [
    "int",
    "decimal",
    "bool",
    "func",
    "char",
    "string",
    "class",
    "enum"
]

VARNAME = []

ASSIGN = [
    "=",
    "*=",
    "&="
]

VALUE = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "'",
    "\"",
    "true",
    "false",
    "none",
    "null",
    "void"
]

OPERATOR = [
    "==",
    "**",
    "&&",
    ">",
    "*>",
    "&>",
    "<",
    "*<",
    "&<",
    ">=",
    "*>=",
    "&>=",
    "<=",
    "*<=",
    "&<="
]

COMMAND = [
    "if",
    "else",
    "elif",
    "forever",
    "for",
    "break",
    "return",
    "import",
    "export",
    "then",
    "print"
]

COMMENT = [
    "//",
    "//<",
    "///<",
    "/#",
    "/*",
    "/+"
]

END = [";"]

KEYWORD = [
    "(", ")",
    "{", "}",
    "[", "]",
    "/", "/"
]

tokens = [
    VARTYPE,
    VARNAME,
    OPERATOR,
    VALUE,
    ASSIGN,
    COMMAND,
    COMMENT,
    END,
    KEYWORD
]

VARTYPE_TOKEN = 0
VARNAME_TOKEN = 1
OPERATOR_TOKEN = 2
VALUE_TOKEN = 3
ASSIGN_TOKEN = 4
COMMAND_TOKEN = 5
COMMENT_TOKEN = 6
END_TOKEN = 7
KEYWORD_TOKEN = 8

tokenName = [
    "Var type",
    "Var name",
    "Operator",
    "Value",
    "Assign",
    "Command",
    "Comment",
    "End",
    "Keyword"
]

def lexer_code(line: str):
    lexer = Lexer(line)
    return lexer.lexer_code()

def specify_code(line: str):
    return tokenName[lexer_code(line)]

class Lexer:
    def __init__(self, line: str):
        self.line = line
    
    def lexer_code(self):
        if VERBOSE_ACTIONS:
            print("Lexing")
        if self.line is None:
            raise NotImplementedError("Lexer error: Not implemented line")
        if self.line == "":
            return VARNAME_TOKEN
        for i in range(len(tokens)):
            for n in range(len(tokens[i])):
                if self.line.startswith(tokens[i][n]):
                    return i
        return VARNAME_TOKEN
    
def iterateTokens(code):
    tokenList = []
    for line in code:
        result = lexer_code(line)
        tokenList.append(result)
    return tokenList

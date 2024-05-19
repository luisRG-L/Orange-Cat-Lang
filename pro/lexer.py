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
    "void",
    "{",
    "}"
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
    "then"
]

COMMENT = [
    "//",
    "//<",
    "///<",
    "/#",
    "/*",
    "/+"
]

tokens = [
    VARTYPE,
    VARNAME,
    OPERATOR,
    VALUE,
    ASSIGN,
    COMMAND,
    COMMENT
]

VARTYPE_TOKEN = 0
VARNAME_TOKEN = 1
OPERATOR_TOKEN = 2
VALUE_TOKEN = 3
ASSIGN_TOKEN = 4
COMMAND_TOKEN = 5
COMMENT_TOKEN = 6

tokenName = [
    "Var type",
    "Var name",
    "Operator",
    "Value",
    "Assign",
    "Command",
    "Comment"
]

def lexer_code(line: str):
    if VERBOSE_ACTIONS:
        print("Lexing")
    if line is None:
        raise NotImplementedError("Lexer error: Not implemented line")
    if line == "":
        return VARNAME_TOKEN
    for i in range(len(tokens)):
        for n in range(len(tokens[i])):
            if line.startswith(tokens[i][n]):
                try:
                    return i
                except:
                    return VARNAME_TOKEN
    return VARNAME_TOKEN

def specify_code(line: str):
    if VERBOSE_ACTIONS:
        print("Lexing")
    if line is None:
        raise NotImplementedError("Lexer error: Not implemented line")
    if line == "":
        return VARNAME_TOKEN
    for i in range(len(tokens)):
        for n in range(len(tokens[i])):
            if line.startswith(tokens[i][n]):
                try:
                    return tokens[i][n]
                except:
                    return "Unknown"
    return tokenName[VARNAME_TOKEN]

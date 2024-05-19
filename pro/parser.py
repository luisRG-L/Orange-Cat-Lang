# parser.py
tokens = []
pos = 0

def next_token():
    global pos
    if pos < len(tokens):
        pos += 1
    return tokens[pos - 1] if pos - 1 < len(tokens) else None

def parse_program():
    functions = []
    while pos < len(tokens):
        func = parse_function()
        if func:
            functions.append(func)
    return functions

def parse_function():
    token = next_token()
    if token == "func":
        name = next_token()
        next_token()  # Skip '('
        next_token()  # Skip ')'
        next_token()  # Skip '{'
        body = parse_statements()
        next_token()  # Skip '}'
        return ('function', name, body)
    return None

def parse_statements():
    statements = []
    while pos < len(tokens):
        token = tokens[pos]
        if token == '}':
            break
        elif token == "print":
            statements.append(parse_print())
        elif token == "main":
            statements.append(parse_main_call())
        else:
            next_token()  # Skip unknown tokens for now
    return statements

def parse_print():
    next_token()  # Skip 'print'
    next_token()  # Skip '('
    string = next_token()
    next_token()  # Skip ')'
    next_token()  # Skip ';'
    return ('print', string)

def parse_main_call():
    name = next_token()  # 'main'
    next_token()  # Skip '('
    next_token()  # Skip ')'
    next_token()  # Skip ';'
    return ('call', name)

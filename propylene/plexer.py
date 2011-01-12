# -----------------------------------------------------------------------------
# plexer.py
#
# A lexical analyzer for PROFETA
# -----------------------------------------------------------------------------
import sys
import ply.lex as lex

## tokens names
tokens = [
    'LAMBDA',    ## lambda expr
    'LITERAL',   ## any string literal
    'NUMBER',    ## all numbers
    'COLON',     ## ':'
    'LCHEVRONS', ## '>>'
    'GREATER',   ## '>'
    'EQUALS',    ## '='
    'LESS',      ## '<'
    'PIPE',      ## '|'
    'TILDE',     ## '~'
    'BWAND',     ## '&'
    'PLUS',      ## '+'
    'MINUS',     ## '-'
    'MULT',      ## '*'
    'DIV',       ## '/'
    'LPAREN',    ## '('
    'RPAREN',    ## ')'
    'LSBRACKET', ## '['
    'RSBRACKET', ## ']'
    'COMMA',     ## ','
    'QUOTES',    ## '"'
    'COMMENT',   ## any string preceeded by '#'
    'ID'         ## reserved words
    ]

## tokens regexps
t_LAMBDA    = r'lambda'
t_LITERAL   = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COLON     = r':'
t_LCHEVRONS = r'>>'
t_GREATER   = r'>'
t_EQUALS    = r'='
t_LESS      = r'<'
t_PIPE      = r'\|'
t_TILDE     = r'~'
t_BWAND     = r'&'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULT      = r'\*'
t_DIV       = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LSBRACKET = r'\['
t_RSBRACKET = r']'
t_COMMA     = r','
t_QUOTES    = r'"'

## ignored chars
t_ignore  = ' \t'

## rules
def t_NUMBER(t):
    r'\d+[.\d]*'
    t.value = float(t.value)
    return t

## a rule for comments
def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

## a rule for reserved words
# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z_0-9]*'
#     t.type = reserved.get(t.value,'ID') # Check for reserved words
#     return t

## a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

## error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

if __name__ == '__main__':
    path_to_file = sys.argv[1]
    print path_to_file

    ## initialize the lexer
    lexer = lex.lex()

    ## lex the file
    f = open (path_to_file, 'r')
    lines = f.readlines ()
    f.close ()
    
    for line in lines:
        lexer.input (line)
        while True:
            tok = lexer.token()
            if not tok: break  ## no more input
            print tok

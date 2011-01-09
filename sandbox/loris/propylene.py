# -----------------------------------------------------------------------------
# propylene.py
#
# blah blah blah
# -----------------------------------------------------------------------------
import sys
import ply.lex as lex

## tokens names
tokens = (
    'NAME',      ## any string literal
    'NUMBER',    ## all numbers
    'LCHEVRONS', ## '>>'
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
    'QUOTES'     ## '"'
    )

## tokens regexps
t_NAME      = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER    = r'[0-9]+'
t_LCHEVRONS  = r'>>'
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
t_COMMA     = ','
t_QUOTES    = '"'

## ignored chars
t_ignore  = ' \t'

## rules

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

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

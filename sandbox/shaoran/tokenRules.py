# ----------------------------------------------------------
# tokenRules.py
# 
# This module contains the specification of Tokens and the
# corresponding REGEXPs to match them
# ----------------------------------------------------------

tokens = (
   'IDENTIFIER',
   'INTEGER',
   'FLOATING',
   'STRING',
   'RANGLES'   # >>
)


# Literals, matched 'as is'
literals = ['+','-','~','(',')','[',']','|','&',',','_','.']


# Raw string REGEXP for Tokens
t_IDENTIFIER= r'( [a-zA-Z][a-zA-Z_0-9]* | _[a-zA-z_0-9]+ )'
t_RANGLES   = r'>>'   



# Function REGEXP for Tokens
def t_FLOATING(t):
    r'-? [0-9]+ (\.[0-9]+){1,1} ([eE][+-]?[0-9]+)?'
    t.value = float(t.value)
    # The token should be returned; otherwise, it is discarded.
    print "Floating Point literal is: " + str(t.value)
    return t


def t_INTEGER(t):
    r'-? [0-9]+'
    t.value = int(t.value)
    print "Integer literal is: " + str(t.value)
    return t


def t_STRING(t):
    r' " (\. | [^\\"])* " '
#    print 'Got a string: ' + t.value
    return t

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Discard comments
def t_comments(t):
    r'\#.*'
#    print 'Comment is:' + t.value

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)



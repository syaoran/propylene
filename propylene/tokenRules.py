# ----------------------------------------------------------
# tokenRules.py
# 
# This module contains the specification of Tokens and the
# corresponding REGEXPs to match them
# ----------------------------------------------------------

reserved = {
    'lambda': 'LAMBDA',
    'or'    : 'ORLITERAL',
    'and'   : 'ANDLITERAL',
    '_'     : 'USCORE'
}


tokens = [
   'NAME',
   'NUMBER',
   'STRING',
   'EQUALS',
   'NOTEQ',
   'GREATEQ',
   'LESSEQ',
#   'COMPOP',     # Comparison operators 
   'RANGLES'    # >>
] + list(reserved.values())


# Literals, matched 'as is'
literals = ['+','-','~','(',')','[',']','|','&',',',":",'>','<']


# Raw string REGEXP for Tokens
t_RANGLES   = r'>>'
t_EQUALS    = r'=='
t_NOTEQ     = r'!='
t_GREATEQ   = r'>='
t_LESSEQ    = r'<='


# Function REGEXP for Tokens

def t_NAME(t):
    r'( [a-zA-Z_][a-zA-Z_0-9]* )'
    t.type = reserved.get(t.value,'NAME')
    #print t.type
    return t


# Note: the '-' sign is explicitly considered in this regexp
def t_NUMBER(t):
    r'-? [0-9]+ (\.[0-9]+)? ([eE][+-]?[0-9]+)?'
    t.value = float(t.value)
    # The token should be returned; otherwise, it is discarded.
    #print "Number is: " + str(t.value)
    return t


#def t_INTEGER(t):
#    r'-? [0-9]+'
#    t.value = int(t.value)
#    print "Integer literal is: " + str(t.value)
#    return t
#

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



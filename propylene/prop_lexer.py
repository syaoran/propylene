# ----------------------------------------------------------
# PropLexer.py
# 
# This module contains the specification of Tokens and the
# corresponding REGEXPs to match them
# ----------------------------------------------------------
import ply.lex as lex

class PropLexer:

    def __init__ (self, *args, **kwargs):
        self.states = (('variables','inclusive'),)

        self.reserved = {
            'lambda': 'LAMBDA',
            'or'    : 'ORLITERAL',
            'and'   : 'ANDLITERAL',
            'not'   : 'NOTLITERAL',
            '_'     : 'USCORE'
            }

        self.tokens = [
            'NAME',
            'NUMBER',
            'STRING',
            'VARIABLE',
            'EQUALS',
            'NOTEQ',
            'GREATEQ',
            'LESSEQ',
            #   'COMPOP',     # Comparison operators 
            'RANGLES'    # >>
            ] + list(self.reserved.values())

        # Literals, matched 'as is'
        self.literals = ['+','-','~','(',')','[',']','|','&',',',":",'>','<']

        # Raw string REGEXP for Tokens
        self.t_RANGLES   = r'>>'
        self.t_EQUALS    = r'=='
        self.t_NOTEQ     = r'!='
        self.t_GREATEQ   = r'>='
        self.t_LESSEQ    = r'<='

        # A string containing ignored characters (spaces and tabs)
        self.t_ignore  = ' \t'

        ## ok, build the lexer
        self.lexer = lex.lex (module=self, **kwargs)

    def get_tokens(self):
        return self.tokens

    # Function REGEXP for Tokens
    def t_NAME(self, t):
        r'( [a-zA-Z_][a-zA-Z_0-9]* )'
        t.type = self.reserved.get(t.value,'NAME')
        ##if type of token is USCORE
        if t.type == 'USCORE':
            t.lexer.push_state ('variables')
        return t


    # Note: the '-' sign is explicitly considered in this regexp
    def t_NUMBER(self, t):
        r'-? [0-9]+ (\.[0-9]+)? ([eE][+-]?[0-9]+)?'
        t.value = float(t.value)
        # The token should be returned; otherwise, it is discarded.
        #print "Number is: " + str(t.value)
        return t


#def t_INTEGER(self, t):
#    r'-? [0-9]+'
#    t.value = int(t.value)
#    print "Integer literal is: " + str(t.value)
#    return t
#

    def t_variables_VARIABLE(self, t):
        r' " (\. | [^\\"])* " '
        #print 'Got a variable: ' + t.value
        t.lexer.pop_state ()    
        return t

    def t_STRING(self, t):
        r' " (\. | [^\\"])* " '
        #print 'Got a string: ' + t.value
        return t

    # Track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

        # Discard comments
    def t_comments(self, t):
        r'\#.*'
        #print 'Comment is:' + t.value

    # Error handling rule
    def t_error(self, t):
        print "PropLexer: Illegal character '%s'" % t.value[0], ": skipped."
        t.lexer.skip(1)

    ## Testing function
    def test (self, data):
        self.lexer.input (data)
        while True:
            tok = self.lexer.token ()
            if not tok: break
            print tok


if __name__ == "__main__":
    ## run a test
    p = PropLexer ()
    f = open ("test/lamb-test", 'r')
    text = f.readlines ()
    for line in text:
        p.test (line)
    f.close ()



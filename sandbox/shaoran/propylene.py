# ----------------------------------------------------------
# propylene.py
# 
# This file contains the Grammar rules and the corresponding
# semantic actions
# ----------------------------------------------------------

import sys
import ply.lex as lex
import ply.yacc as yacc
import tokenRules

from tokenRules import tokens


# Start symbol: strategy
def p_strategy(p):
    ''' Strategy : Plan
                 | Strategy Plan
    '''

# Plan
def p_plan(p):
    ''' Plan    : '(' Head ')' RANGLES Body 
    '''
    print 'Successfully parsed a valid plan'

# Head
def p_head(p):
    ''' Head    : Event
                | Event '|' '(' Condition ')'  
    '''

# Tiggering Event
def p_event(p):
    ''' Event   : GoalEvent
                | BeliefEvent
    '''

# Goal Event
def p_goalevent(p):
    ''' GoalEvent   : '+' '~' Belief
                    | '-' '~' Belief
    '''
    p[0] = p[3]
    outputString = ""
    outputString += "\nclass " + p[0] + "(Goal):\n\tpass"
    print outputString

# Belief Event
def p_beliefevent(p):
    ''' BeliefEvent : '+' Belief
                    | '-' Belief
    '''
    p[0] = p[2]
    outputString = ""
    outputString += "\nclass " + p[0] + "(Belief):\n\tpass"
    print outputString


# Condition of Plan
# lambda yet to be considered
def p_condition(p):
    ''' Condition   : Belief
                    | Condition '&' Belief
    '''

# Body of Plan
def p_body(p):
    ''' Body    : '[' ']'
                | '[' IntentionList ']'
    '''

# Items in the Body of a Plan
def p_intentionlist(p):
    ''' IntentionList   : Intention
                        | IntentionList ',' Intention
    '''

# Single item in the body of a Plan
def p_intention(p):
    ''' Intention   : Event
                    | AtomicAction
    '''

# Belief
def p_belief(p):
    ''' Belief          : IDENTIFIER '(' ')'
                        | IDENTIFIER '(' ArgumentList ')'
    '''
    p[0] = p[1]

# Action
def p_atomicaction(p):
    ''' AtomicAction    : IDENTIFIER '(' ')'
                        | IDENTIFIER '(' ArgumentList ')'
    '''
    p[0] = p[1]
    actionString = ""
    actionString += "\nclass " + p[0] + "(Action):\n\tdef execute(self):\n\t\t## ..."
    print actionString

# List of arguments
def p_argumentlist(p):
    ''' ArgumentList    : Argument
                        | ArgumentList ',' Argument
    '''

# Single argument
def p_argument(p):
    ''' Argument    : STRING
                    | '_' '(' STRING ')'
                    | Numeral
    '''                 

def p_numeral(p):
    ''' Numeral : NUMBER
                | '-' NUMBER
    '''

def p_error(p):
    print 'Syntax error in input!'



# Build the parser
lexer = lex.lex(module=tokenRules)
parser = yacc.yacc()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputFilePath = sys.argv[1]
        inputFile = open(inputFilePath, 'r')
        inputFileLines = inputFile.readlines()
        inputFile.close()
        totalString = "" 
        for line in inputFileLines:
            totalString += line

        result = parser.parse(totalString)
#        print result
    else:
        print 'Usage: python propylene filePath'

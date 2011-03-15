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
    ''' Plan : '(' Head ')' RANGLES Body 
    '''
    print 'Got a valid plan'

# Head of plan
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

# Belief Event
def p_beliefevent(p):
    ''' BeliefEvent : '+' Belief
                    | '-' Belief
    '''

# Condition of Plan
# lambda yet to be considered
def p_condition(p):
    ''' Condition   : Belief
                    | Condition '&' Belief
    '''

# Body of Plan
def p_body(p):
    ''' Body    : '[' ']'
                | '[' ActionList ']'
    '''

# Items in the Body of the Plan
def p_actionlist(p):
    ''' ActionList  : Event
                    | AtomicAction
                    | ActionList ',' Event
                    | ActionList ',' AtomicAction
    '''

def p_atomicaction(p):
    ''' AtomicAction    : IDENTIFIER '(' ')'
                        | IDENTIFIER '(' arguments ')'
    '''


def p_belief(p):
    ''' Belief  : IDENTIFIER '(' ')'
                | IDENTIFIER '(' arguments ')'
    '''

def p_arguments(p):
    ''' arguments   : argument
                    | arguments ',' argument
    '''

def p_argument(p):
    ''' argument    : STRING
                    | numeral
                    | '_' '(' STRING ')'
    '''                 

def p_numeral(p):
    ''' numeral : NUMBER
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
        print result
    else:
        print 'Usage: python propylene filePath'

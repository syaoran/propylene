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
from p_ast import *

plan_count = -1


def p_start(p):
    ''' Start : Strategy 
    '''
    print "End of Strategy!"
    p[0] = p[1]
    v = Visitor('')
    p[0].Visit(v)


# Start symbol: strategy
def p_strategy(p):
    ''' Strategy : Plan
                 | Plan Strategy
    '''
    if len(p)==2:
        p[0] = Strategy('',[ p[1] ] )
    else:
        p[0] = Strategy('', [  p[1], p[2] ])

# Plan
def p_plan(p):
    ''' Plan    : '(' Head ')' RANGLES '[' IntentionList ']' 
    '''
    global plan_count
    plan_count+=1
    print 'Successfully parsed Plan n. ' + str(plan_count)
    p[0] = Plan('', [ p[2], p[6]  ] )
# Head
def p_head(p):
    ''' Head    : Event
                | Event '|' '(' Condition ')'  
    '''
    #print p.lineno(0)
    p[1] = Trigger('',[p[1]])
    if len(p)==6:
        p[0] = Head('',[ p[1], p[4] ] )
    else:
        p[0] = Head('',[p[1]])
        
# Tiggering Event
def p_event(p):
    ''' Event   : GoalEvent
                | BeliefEvent
    '''
    p[0] = p[1]
# Goal Event

def p_goal_event(p):
    ''' GoalEvent   : '+' Goal
                    | '-' Goal
    '''
    p[0] = p[2]
    #outputString = ""
    #outputString += "\nclass " + p[0] + "(Goal):\n\tpass"
    #print outputString
#    print "Goal: " + p[0]

# Belief Event
def p_belief_event(p):
    ''' BeliefEvent : '+' Belief
                    | '-' Belief
    '''
    p[0] = p[2]
    #outputString = ""
    #outputString += "\nclass " + p[0] + "(Belief):\n\tpass"
    #print outputString
#    print "Belief: " + p[0]


# Condition of Plan
def p_condition(p):
    ''' Condition   : Belief
                    | Belief '&' Condition
                    | '(' LambdaExpr ')'
    '''
    if len(p)==2:
        p[0] = Condition('', [ p[1] ])
    elif p[2]=='&':
        p[0] = Condition('', [p[1], p[3] ])
    else:
        p[0] = Condition('', [ p[2] ] )
#eErrors
# ----------------------------------------------------------
def p_error_condition_with_event(p):
    ''' Condition   : Event
                    | Event '&' Condition
    '''
    mex = "Condition cannot contain Event"
    print_error(mex, p.lineno(1))

def p_error_condition_with_goal(p):
    ''' Condition   : Goal
                    | Goal '&' Condition
    '''
    mex = "Condition cannot contain Goal"
    print_error(mex, p.lineno(1))

def p_error_condition_lambda_not_enclosed(p):
    ''' Condition   : LambdaExpr
    '''
    mex = "lambda is not enclosed in '(' ')'"
    print_error(mex, p.lineno(1))
# ----------------------------------------------------------



# Items in the Body of a Plan
def p_intention_list(p):
    ''' IntentionList   : Intention ',' IntentionList
                        | Intention
                        | empty 
    '''
    if len(p) == 4:
        p[0] = Body('', [ p[1], p[3] ] )
    elif p[1] != "empty":
        p[0] = Body('', [ p[1]] )
    else:
        p[0] = Body('')



# Single item in the body of a Plan
def p_intention(p):
    ''' Intention   : Event
                    | AtomicAction
    '''
    p[0] = p[1]
# Lambda expression
# es.1  lambda : Z>2
def p_lambda_expr(p):
    ''' LambdaExpr  : LAMBDA ':' LambdaTest
    '''
#    print "Lambda Parsed"
    p[0] = Lambda('')

# Condition to be tested in the lambda expression. 
# es.2 lambda : (X!=2) and (Y<3) or (Z>=W) 
def p_lambda_test(p):
    ''' LambdaTest  : Comparison                    
                    | CompoundTest
    '''
                   # | '(' LambdaTest ')'

def p_compound_test(p):
    ''' CompoundTest    : UnaryTest ORLITERAL CompoundTest
                        | UnaryTest ANDLITERAL CompoundTest
                        | UnaryTest
    '''

def p_unary_test(p):
    ''' UnaryTest   :   NOTLITERAL '(' Comparison ')'
                    |   '(' Comparison ')'
    '''

def p_comparison(p):
    ''' Comparison  :  CompTerm CompOp CompTerm '''
 


# Comparison term
def p_comp_term(p):
    ''' CompTerm    : NAME
                    | NUMBER
                    | STRING
    '''

# Comparison operator
def p_comp_op(p):
    ''' CompOp  : '>'  
                | '<'
                | EQUALS
                | GREATEQ
                | LESSEQ
                | NOTEQ

    '''

# Belief
def p_belief(p):
    ''' Belief  : NAME '(' ArgumentList ')'
    '''
    p[0] = Belief(p[1])
    #print "Belief: " + p[0]


# Goal
def p_goal(p):
    ''' Goal  : '~' NAME '(' ArgumentList ')'
    '''
    p[0] = Goal(p[1])
    #print "Belief: " + p[0]


# Action
def p_atomicaction(p):
    ''' AtomicAction    : NAME '(' ArgumentList ')'
    '''
    p[0] = Action(p[1])
    #print "Belief: " + p[0]
#    actionString = ""
#    actionString += "\nclass " + p[0] + "(Action):\n\tdef execute(self):\n\t\t## ..."
    #print actionString
    #print "Action : " + p[0]

# List of arguments
def p_argumentlist(p):
    ''' ArgumentList    : Argument ',' ArgumentList
                        | Argument
                        | empty
    '''

# Single argument
def p_argument(p):
    ''' Argument    : STRING
                    | USCORE '(' VARIABLE ')'
                    | NUMBER
                    | NAME
                    | '[' ArgumentList ']'
                    | '(' ArgumentList ')'
    '''                 


# Empty production
def p_empty(p):
    ''' empty :
    '''
    p[0] = "empty"

def p_error(p):
    print 'Syntax error in input!'


def print_error(message, lineno):
    print "Error (line " + str(lineno) + "): " + message


# Build the parser
lexer = lex.lex(module=tokenRules)
parser = yacc.yacc(tabmodule='parse_table',outputdir='parser_out')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputFilePath = sys.argv[1]
        inputFile = open(inputFilePath, 'r')
        inputFileLines = inputFile.readlines()
        inputFile.close()
        totalString = "" 
        for line in inputFileLines:
            totalString += line

        result = parser.parse(totalString, tracking=True)
#        print result
    else:
        print 'Usage: python propylene filePath'

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


plan_count = -1

# Start symbol: strategy
def p_strategy(p):
    ''' Strategy : Plan
                 | Strategy Plan
    '''

# Plan
def p_plan(p):
    ''' Plan    : '(' Head ')' RANGLES '[' IntentionList ']' 
    '''
    global plan_count
    plan_count+=1
    print 'Successfully parsed Plan n. ' + str(plan_count)

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
def p_goal_event(p):
    ''' GoalEvent   : '+' Goal
                    | '-' Goal
    '''
    p[0] = p[2]
    outputString = ""
    outputString += "\nclass " + p[0] + "(Goal):\n\tpass"
    #print outputString
#    print "Goal: " + p[0]

# Belief Event
def p_belief_event(p):
    ''' BeliefEvent : '+' Belief
                    | '-' Belief
    '''
    p[0] = p[2]
    outputString = ""
    outputString += "\nclass " + p[0] + "(Belief):\n\tpass"
    #print outputString
#    print "Belief: " + p[0]


# Condition of Plan
def p_condition(p):
    ''' Condition   : Belief
                    | Belief '&' Condition
                    | '(' LambdaExpr ')'
    '''


# Items in the Body of a Plan
def p_intention_list(p):
    ''' IntentionList   : Intention ',' IntentionList
                        | Intention
                        | empty 
    '''

# Single item in the body of a Plan
def p_intention(p):
    ''' Intention   : Event
                    | AtomicAction
    '''

# Lambda expression
# es.1  lambda : Z>2
def p_lambda_expr(p):
    ''' LambdaExpr  : LAMBDA ':' LambdaTest
    '''
    print "Lambda Parsed"


# Condition to be tested in the lambda expression. 
# es.2 lambda : (X!=2) and (Y<3) or (Z>=W) 
def p_lambda_test(p):
    ''' LambdaTest  : CompTerm CompOp CompTerm
                    | '(' LambdaTest ')'
                    | '(' LambdaTest ')' ORLITERAL  LambdaTest 
                    | '(' LambdaTest ')' ANDLITERAL  LambdaTest 
    '''

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
    p[0] = p[1]
    #print "Belief: " + p[0]


# Goal
def p_goal(p):
    ''' Goal  : '~' NAME '(' ArgumentList ')'
    '''
    p[0] = p[2]
    #print "Belief: " + p[0]


# Action
def p_atomicaction(p):
    ''' AtomicAction    : NAME '(' ArgumentList ')'
    '''
    p[0] = p[1]
    actionString = ""
    actionString += "\nclass " + p[0] + "(Action):\n\tdef execute(self):\n\t\t## ..."
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
                    | USCORE '(' STRING ')'
                    | NUMBER
                    | NAME
                    | '[' ArgumentList ']'
                    | '(' ArgumentList ')'
    '''                 


# Empty production
def p_empty(p):
    ''' empty :
    '''
    pass

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

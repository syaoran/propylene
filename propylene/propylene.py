# ----------------------------------------------------------
# propylene.py
# 
# This file contains the Grammar rules and the corresponding
# semantic actions
# ----------------------------------------------------------

import sys
import ply.lex as lex
import ply.yacc as yacc
from PropLexer import PropLexer as PropLexer

## from tokenRules import tokens
from p_ast import *
from exception import *

class Propylene:
    def __init__ (self, *args, **kwargs):
        self.plan_count = -1

        self.sym_table_stack = [ {}]
        self.variable_status = "declaration"

    def p_start(p):
        ''' Start : Strategy 
        '''
        print "End of Strategy!"
        p[0] = p[1]
        v = Visitor()
        p[0].Visit(v)
        v.GenerateCode ()


    # Start symbol: strategy
    def p_strategy(p):
        ''' Strategy : Plan
                     | Plan Strategy
        '''
        if len(p)==2:
            p[0] = Strategy(uChildren=[ p[1] ] )
        else:
            p[0] = Strategy(uChildren=[ p[1], p[2] ])    
        p[0]._children = flatten_strategies (p[0])
    

# Plan
    def p_plan(p):
        ''' Plan    : '(' seen_Plan Head ')' RANGLES '[' seen_IntentionList IntentionList ']' 
        '''
        self.plan_count += 1
        print 'Successfully parsed Plan n. ' + str(self.plan_count)
        p[8]._children = flatten_c(p[8]) 
        p[0] = Plan(uChildren=[ p[3], p[8] ])
        self.sym_table_stack.pop()


        def p_seen_IntentionList(p):
            ''' seen_IntentionList : '''
            self.variable_status = "usage"

        def p_seen_Plan(p):
            '''seen_Plan : '''
            self.sym_table_stack.append({})
            
        # Head
        def p_head(p):
            ''' Head    : Event
            | Event '|' '(' Condition ')'  
                '''
    #print p.lineno(0)
            p[1] = Trigger(uChildren=[p[1]])
            if len(p)==6:
                p[4]._children = flatten_c(p[4])
                p[0] = Head(uChildren=[ p[1], p[4] ])
            else:
                p[0] = Head(uChildren=[p[1]])
        
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
            | '(' seen_LambdaExpr LambdaExpr ')'
            '''
            if len(p)==2:
                p[0] = Condition(uChildren=[ p[1] ])
            elif p[2]=='&':
                p[0] = Condition(uChildren=[ p[1], p[3] ])
            else:
                p[0] = Condition(uChildren=[ p[2] ] )


        def p_seen_LambdaExpr(p):
            ''' seen_LambdaExpr : '''
            self.variable_status = "usage"




#eErrors
# ----------------------------------------------------------
# def p_error_condition_with_event(p):
#     ''' Condition   : Event
#                     | Event '&' Condition
#     '''
#     mex = "Condition cannot contain Event"
#     print_error(mex, p.lineno(1))

# def p_error_condition_with_goal(p):
#     ''' Condition   : Goal
#                     | Goal '&' Condition
#     '''
#     mex = "Condition cannot contain Goal"
#     print_error(mex, p.lineno(1))

# def p_error_condition_lambda_not_enclosed(p):
#     ''' Condition   : LambdaExpr
#     '''
#     mex = "lambda is not enclosed in '(' ')'"
#     print_error(mex, p.lineno(1))
# ----------------------------------------------------------



    # Items in the Body of a Plan
    def p_intention_list(p):
        ''' IntentionList   : Intention ',' IntentionList
        | Intention
        | empty 
        '''
        if len(p) == 4:
            p[0] = Body(uChildren=[ p[1], p[3] ] )
        elif p[1] != "empty":
            p[0] = Body(uChildren=[ p[1] ] )
        else:
            p[0] = Body()


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
        p[0] = Lambda()

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
    p[0] = Belief(uName=p[1])
    insert_symbol(p[1],'Belief')


    #print "Belief: " + p[0]


# Goal
def p_goal(p):
    ''' Goal  : '~' NAME '(' ArgumentList ')'
    '''
    p[0] = Goal(uName=p[2])
    insert_symbol(p[2],'Goal')
    #print "Belief: " + p[0]


# Action
def p_atomicaction(p):
    ''' AtomicAction    : NAME '(' ArgumentList ')'
    '''
    p[0] = Action(uName=p[1])
    insert_symbol(p[1],'Action')
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
    if len(p)==5:
        global sym_table_stack
        if variable_status == "usage":
            try:
                sym_table_stack[-1][p[3]]
            except(KeyError):
                raise UnboundedVariable()
        elif variable_status == "declaration":
            sym_table_stack[-1][p[3]] = "Variable"
        print sym_table_stack
                

# Empty production
def p_empty(p):
    ''' empty :
    '''
    p[0] = "empty"

def p_error(p):
    print 'Syntax error in input!'


def print_error(message, lineno):
    print "Error (line " + str(lineno) + "): " + message



###
# Utility Functions
###

def insert_symbol(uName,uType):
    global sym_table_stack
    print sym_table_stack
    try:
        type = sym_table_stack[0][uName]
        print type, uType
        if type != uType:
            raise AttitudeTypeMismatch()  
    except(KeyError):
        sym_table_stack[0][uName] = uType





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
        #global sym_table
        print sym_table_stack
#        print result
    else:
        print 'Usage: python propylene filePath'

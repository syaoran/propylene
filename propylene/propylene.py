##------------------------------------------------------------------------------
## propylene.py
## 
## This file contains the Grammar rules and the corresponding
## semantic actions
##------------------------------------------------------------------------------
## global imports
##------------------------------------------------------------------------------
import sys
import ply.lex as lex
import ply.yacc as yacc
##
##------------------------------------------------------------------------------
## local imports
##------------------------------------------------------------------------------
from prop_lexer import PropLexer as PropLexer
from p_ast import *
from exception import *
from state import *
##
##------------------------------------------------------------------------------
## class Propylene
##------------------------------------------------------------------------------
class Propylene:
    def __init__ (self, *args, **kwargs):
        self._plan_count = -1

        self._sym_table_stack = [{}]
        self._variable_parsing_status = VariableDeclarationState()

        self._lexer = PropLexer()
        self.tokens = self._lexer.get_tokens()
        #self._parser = yacc.yacc(module=self, tabmodule='parse_table', outputdir='parser_out')
        self._parser = yacc.yacc(module=self,)
        
        ## if the output file was specified, save it
        try: self._out = kwargs["out"]
        except: pass
        
        
    def parse(self, input):
        return self._parser.parse(input, tracking=True)

    
    def p_start(self, p):
        ''' Start : Strategy 
        '''
        print "End of Strategy!"

        ## create the visitor
        try: v = Visitor(uTarget = self._out)
        except: v = Visitor ()

        p[0] = p[1]
        
        ## visit the tree
        p[0].Visit(v)

        ## generate the target
        v.GenerateCode ()


    # Start symbol: strategy
    def p_strategy(self, p):
        ''' Strategy : Plan
                     | Plan Strategy
        '''
        if len(p)==2:
            p[0] = Strategy(uChildren=[ p[1] ] )
        else:
            p[0] = Strategy(uChildren=[ p[1], p[2] ])    

        p[0]._children = flatten_strategies (p[0])
    

    # Plan
    def p_plan(self, p):
        ''' Plan    : '(' seen_Plan Head ')' RANGLES '[' seen_IntentionList IntentionList ']' 
        '''
        self._plan_count += 1
        print 'Successfully parsed Plan n. ' + str(self._plan_count)
        p[8]._children = flatten_c(p[8]) 
        p[0] = Plan(uChildren=[ p[3], p[8] ])
        self._sym_table_stack.pop()

    # An intentions list
    def p_seen_IntentionList(self, p):
        ''' seen_IntentionList : '''
        self._variable_parsing_status = VariableUsageState()

    ## Seen Plan (embedded action)
    def p_seen_Plan(self, p):
        '''seen_Plan : '''
        self._sym_table_stack.append({})
        self._variable_parsing_status = VariableDeclarationState ()
        
        
    # Head
    def p_head(self, p):
        ''' Head    : Event
                    | Event '|' '(' Condition ')'  
            '''
        p[1] = Trigger(uChildren=[p[1]])
        if len(p)==6:
            p[4]._children = flatten_c(p[4])
            p[0] = Head(uChildren=[ p[1], p[4] ])
            
        else:
            p[0] = Head(uChildren=[p[1]])
            
    
    # Triggering Event
    def p_event(self, p):
        ''' Event   : GoalEvent
                    | BeliefEvent
        '''
        p[0] = p[1]


    # Goal Event
    def p_goal_event(self, p):
        ''' GoalEvent   : '+' Goal
                        | '-' Goal
        '''
        p[0] = p[2]


    # Belief Event
    def p_belief_event(self, p):
        ''' BeliefEvent : '+' Belief
                        | '-' Belief
        '''
        p[0] = p[2]


    # Condition of Plan
    def p_condition(self, p):
        ''' Condition   : Belief
                        | Belief '&' Condition
                        | '(' seen_LambdaExpr LambdaExpr ')'
        '''
        if len(p)==2:
            p[0] = Condition(uChildren=[ p[1] ])
        elif p[2]=='&':
            p[0] = Condition(uChildren=[ p[1], p[3] ])
        else:
            p[0] = Condition(uChildren=[ p[3] ] )
            

    # Lambda Expr Seen (embedded action)
    def p_seen_LambdaExpr(self, p):
        ''' seen_LambdaExpr : '''
        self._variable_parsing_status = VariableUsageState()
        #"usage"


#Errors
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
    def p_intention_list(self, p):
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


    # An intention, i.e. a single item in the body of a Plan
    def p_intention(self, p):
        ''' Intention   : Event
                        | AtomicAction
        '''
        p[0] = p[1]


    # Lambda expression
    # es.1  lambda : Z>2
    def p_lambda_expr(self, p):
        ''' LambdaExpr  : LAMBDA ':' LambdaTest
        '''
        p[0] = Lambda()


    # Condition to be tested in the lambda expression. 
    # e.g. 2 lambda : (X!=2) and (Y<3) or (Z>=W) 
    def p_lambda_test(self, p):
            ''' LambdaTest  : Comparison                    
                            | CompoundTest
            '''
            # | '(' LambdaTest ')'


    def p_compound_test(self, p):
        ''' CompoundTest    : UnaryTest ORLITERAL CompoundTest
                            | UnaryTest ANDLITERAL CompoundTest
                            | UnaryTest
        '''

    
    def p_unary_test(self, p):
        ''' UnaryTest   :   NOTLITERAL '(' Comparison ')'
                        |   '(' Comparison ')'
        '''

    
    def p_comparison(self, p):
        ''' Comparison  :  CompTerm CompOp CompTerm '''
     
    
    # Comparison term
    def p_comp_term(self, p):
        ''' CompTerm    : NAME
                        | NUMBER
                        | STRING
        '''
        if isinstance(p[1], str):
            if p[1][0] != "\"":
                self._variable_parsing_status.handle_symbol (self._sym_table_stack[-1], 
                                                             p[1])
                
                
    # Comparison operator
    def p_comp_op(self, p):
        ''' CompOp  : '>'  
                    | '<'
                    | EQUALS
                    | GREATEQ
                    | LESSEQ
                    | NOTEQ
    
        '''
    

    # Belief
    def p_belief(self, p):
        ''' Belief  : NAME '(' ArgumentList ')'
        '''
        p[0] = Belief(uName=p[1])
        self.insert_symbol(p[1],'Belief')
    
    
    # Goal
    def p_goal(self, p):
        ''' Goal  : '~' NAME '(' ArgumentList ')'
        '''
        p[0] = Goal(uName=p[2])
        self.insert_symbol(p[2],'Goal')
    
    
    # Action
    def p_atomicaction(self, p):
        ''' AtomicAction    : NAME '(' ArgumentList ')'
        '''
        p[0] = Action(uName=p[1])
        self.insert_symbol(p[1],'Action')
        print self._sym_table_stack
        
    
    # List of arguments
    def p_argumentlist(self, p):
        ''' ArgumentList    : Argument ',' ArgumentList
                            | Argument
                            | empty
        '''
    

    # Single argument
    def p_argument(self, p):
        ''' Argument    : STRING
                        | USCORE '(' VARIABLE ')'
                        | NUMBER
                        | NAME
                        | '[' ArgumentList ']'
                        | '(' ArgumentList ')'
        '''                 
        if len(p)==5:
            self._variable_parsing_status.handle_symbol(self._sym_table_stack[-1], 
                                                        p[3])
                    
            
    # Empty production
    def p_empty(self, p):
        ''' empty :
        '''
        p[0] = "empty"
    

    def p_error(self, p):
        print 'Syntax error in input!'
    
    
    def print_error(self, message, lineno):
        print "Error (line " + str(lineno) + "): " + message
    
        
    ###
    # Ancillary Functions
    ###
    def insert_symbol(self, uName,uType):
        print self._sym_table_stack
        try:
            type = self._sym_table_stack[0][uName]
            print type, uType
            if type != uType:
                raise AttitudeTypeMismatch()  
        except(KeyError):
            self._sym_table_stack[0][uName] = uType
##
##------------------------------------------------------------------------------
## class AugmentedPropylene ---> Propylene
##------------------------------------------------------------------------------
class AugmentedPropylene(Propylene):

    def __init__(self, *args, **kwargs):
        Propylene.__init__(self, *args, **kwargs)

# ----------------------------------------------------------
    def p_error_condition_with_event(self, p):
        ''' Condition   : Event
                        | Event '&' Condition
        '''
        mex = "Condition cannot contain Event"
        self.print_error(mex, p.lineno(1))
   
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
##
##------------------------------------------------------------------------------
##  Main
##------------------------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: python propylene.py <SOURCE> [--output [OUTPUT]]"
        sys.exit (0)

    if len (sys.argv) == 3:
        output = sys.argv[2]
        
    try:    p = AugmentedPropylene(out=output)
    except: p =  AugmentedPropylene()

    inputFilePath = sys.argv[1]
    inputFile = open(inputFilePath, 'r')
    inputFileLines = inputFile.readlines()
    inputFile.close()
    totalString = "" 
    for line in inputFileLines:
        totalString += line

    result = p.parse(totalString)

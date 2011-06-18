##------------------------------------------------------------------------------
## propylene.py
## 
## This file contains the CFG specification of PROFETA and all necessary
## semantic actions

##------------------------------------------------------------------------------
## global imports
##------------------------------------------------------------------------------
import sys
import ply.lex as lex
import ply.yacc as yacc

##------------------------------------------------------------------------------
## local imports
##------------------------------------------------------------------------------
from prop_lexer import PropLexer as PropLexer
from p_ast import *
from exception import *
from state import *

##------------------------------------------------------------------------------
## Propylene, the base class to build a PROFETA parser and class generator
##------------------------------------------------------------------------------
class Propylene:
    def __init__ (self, *args, **kwargs):
        ## DEBUG: keep track of the total number of plans
        self._plan_count = -1
        ## Total number of encountered syntax error
        self._syntax_errors_count = 0
        self._syntax_errors_info = []
        ## If the following limit is exceeded, the parser stops
        try:    self._syntax_errors_limit = kwargs["syntax_errors_limit"]
        except: self._syntax_errors_limit = 10
        ## The bottom of the stack is the global symbol table 
        self._symbol_table_stack = [ {} ]
        self._variable_parsing_status = VariableDeclarationState()
        
        ## Build the lexer
        self._lexer = PropLexer()
        ## Acquire the tokens defined and used by the lexer
        self.tokens = self._lexer.get_tokens()
        ## Build the parser
        self._parser = yacc.yacc(module=self, debug=1)
        #self._parser = yacc.yacc(module=self, tabmodule='parse_table', outputdir='parser_out')
        
        ## if the target file was specified, save it
        try: self._out = kwargs["out"]
        except: pass
        try: self._generate_graphical_ast = kwargs["generate_graphical_ast"]
        except: self._generate_graphical_ast = False
    
    ## Wrapper method for parsing
    def parse(self, input):
        ## PLY BUG! Ply can't track 'erro' special token
        #return self._parser.parse(input, tracking=True)
        return self._parser.parse(input)

##------------------------------------------------------------------------------
## CFG Grammar specification of PROFETA
##------------------------------------------------------------------------------
    # Start symbol of the grammar 
    def p_start(self, p):
        ''' Start : Strategy 
        '''        
        ## Syntax errors detected: cannot generate code
        if self._syntax_errors_count > 0:
            print "Propylene has found {0} syntax errors:" \
                .format(self._syntax_errors_count)

            self.print_syntax_error_info()
            print "Cannot generate code."
            print "Aborted."
            sys.exit (-1)

        else:
            ## create the visitors
            try: code_generator = CodeGenerator(uTarget = self._out)
            except: code_generator = CodeGenerator ()
            ast_visual_generator = ASTVisualGenerator ()
            
            p[0] = p[1]

            ## visit the tree and generate the code
            code_generator.Visit (p[0])
            code_generator.GenerateCode ()

            ## if visual support was requested:
            if self._generate_graphical_ast:
                ast_visual_generator.Visit (p[0])
                ast_visual_generator.GenerateImage ()

    ## Strategy is a set of Plans
    def p_strategy(self, p):
        ''' Strategy : Plan
                     | Plan Strategy
        '''
        if len(p)==2:
            p[0] = Strategy(uChildren=[ p[1] ] )
        else:
            p[0] = Strategy(uChildren=[ p[1], p[2] ])    

        p[0]._children = flatten_strategies (p[0])
    
    ## a Plan in PROFETA
    def p_plan(self, p): # >>
        ''' Plan : Head RANGLES Body
        '''
        self._plan_count += 1
        print "Finished parsing Plan n. {0}" .format(self._plan_count)
        # Build the 'Plan' Node
        p[0] = Plan(uChildren=[ p[1], p[3] ])
        # Pop the local symbol table
        #print self._symbol_table_stack
        self._symbol_table_stack.pop()

    # Head of a Plan, which contains the mandatory Triggering Event
    # and an optional Condition
    def p_head(self, p):
        ''' Head : '(' enter_Head Event ')'
                 | '(' enter_Head Event '|' Condition ')'
        '''
        p[3] = Trigger(uChildren=[ p[3] ])
        if len(p)==5:   # Only the Triggering Event is specified
            p[0] = Head(uChildren=[ p[3] ])
        else:           # The Condition is specified, too
            p[0] = Head(uChildren=[ p[3], p[5] ])
    
    # The Body of a plan is a sequence of intentions
    def p_body(self, p):
        ''' Body : '[' enter_Body IntentionList ']'  
        '''
        p[0] = p[3]
        # flat the body
        p[0]._children =  flatten_c(p[0])

    # We just entered the head of a Plan, thus we create the
    # local symbol table and shift to Declaration state
    def p_enter_Head(self, p):
        ''' enter_Head : '''
        self._symbol_table_stack.append({})
        self._variable_parsing_status = VariableDeclarationState ()
 
    # We just entered the body of a Plan, and thus we must switch
    # to Usage state
    def p_enter_Body(self, p):
        ''' enter_Body : '''
        self._variable_parsing_status = VariableUsageState()

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

    # The condition of a plan is a sequence of beliefs with
    # an optional lambda term
    def p_condition(self, p):
        ''' Condition : '(' ConditionTerms ')'
        '''
        p[0] = p[2]
        p[0]._children = flatten_c(p[0])

    def p_condition_terms(self, p):
        ''' ConditionTerms : Belief 
                           | Belief '&' ConditionTerms
                           | '(' enter_LambdaExpr LambdaExpr ')'
        '''
        if len(p)==2:
            p[0] = Condition(uChildren=[ p[1] ])
        elif p[2]=='&':
            p[0] = Condition(uChildren=[ p[1], p[3] ])
        else:
            p[0] = Condition(uChildren=[ p[3] ] )
            
    # We have just entered a lambda expression, which can only
    # use previously bounded variables
    def p_seen_LambdaExpr(self, p):
        ''' enter_LambdaExpr : '''
        self._variable_parsing_status = VariableUsageState()

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
                try: 
                    self._variable_parsing_status.handle_symbol (
                        self._symbol_table_stack[-1], 
                        p[1])
                except UnboundedVariable as e:
                    e.lineno = p.lineno(1)
                    raise e
                
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
        try: self.insert_symbol(p[1],'Belief')
        except AttitudeTypeMismatch as e:
            e.lineno = p.lineno(1)
            raise e
    
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
        #print self._symbol_table_stack
        
    
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
            try:
                self._variable_parsing_status.handle_symbol(
                    self._symbol_table_stack[-1], 
                    p[3])
            except UnboundedVariable as e:
                e.lineno = p.lineno(1)
                raise e
                    
            
    # Empty production
    def p_empty(self, p):
        ''' empty :
        '''
        p[0] = "empty"
    

    # PLY error function
    def p_error(self, p): 
        # Simple and generic error message
        self.add_generic_syntax_error_message(p)
        ## 
        #yacc.errok()
        self._syntax_errors_count += 1
        # Too many errors encountered: abort immediately
        if self._syntax_errors_count>=self._syntax_errors_limit:
            raise TooManySyntaxErrors()
        #self.print_syntax_error_message(p)
   
        
    ###
    # Ancillary Functions
    ###
    def insert_symbol(self, uName, uType):
        ## if the symbol was already in the table
        ## check its type
        try:
            type = self._symbol_table_stack[0][uName]
            #print type, uType
            if type != uType:
                e = AttitudeTypeMismatch()
                e.attitude_name = uName
                e.type1 = type
                e.type2 = uType
                raise e

        ## insert it in the table as a new element, otherwise
        except(KeyError):
            self._symbol_table_stack[0][uName] = uType

    def add_generic_syntax_error_message(self, uLexToken):
        mex = "Line {0} : Syntax error - unexpected token '{1}'"\
                .format(uLexToken.lineno, uLexToken.value)
        self._syntax_errors_info.append(mex)

    def print_syntax_error_info(self):
        for info in self._syntax_errors_info:
            print info

#    def print_syntax_error_message(self, uLexToken):
#        print 
        
##------------------------------------------------------------------------------
## class AugmentedPropylene ---> Propylene
##------------------------------------------------------------------------------
class AugmentedPropylene(Propylene):

    def __init__(self, *args, **kwargs):
        Propylene.__init__(self, *args, **kwargs)


    def add_custom_syntax_error_message(self, uMessage, uLexToken):
        self._syntax_errors_info.append("Line {0} : {1}." \
                                        .format(uLexToken.lineno, uMessage))
 

# ----------------------------------------------------------
# Error Productions
# ----------------------------------------------------------
    
    def p_head_error(self, p):
        ''' Head : '(' enter_Head error ')'
        '''
        mex = "Error in the Head of the plan"
        #print "Reducing..."
        self.add_custom_syntax_error_message(mex, p[3])
    
    
    # Error in Triggering Event
    def p_trigger_error(self, p):
        ''' Head : '(' enter_Head error '|' Condition ')'  
        '''
        mex = "Illegal Triggering Event"
        self.add_custom_syntax_error_message(mex, p[3])
    

    # Error in Condition
    def p_condition_error(self, p):
        ''' Condition : '(' error ')'  
        '''
        mex = "Error detected in the Condition of the plan"
        self.add_custom_syntax_error_message(mex, p[2])
 

    # Error in body
    def p_body_error(self, p):
        ''' Body : '[' enter_Body error ']'  
        '''
        mex = "Error detected in the Body of the plan"
        self.add_custom_syntax_error_message(mex, p[3])

# ----------------------------------------------------------



##------------------------------------------------------------------------------
##  Main
##------------------------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: python propylene.py <SOURCE> [--output [OUTPUT] [--graphical-ast]"
        sys.exit (0)
        
    else: ##scan arguments
        inputFilePath = sys.argv[1]
        output = None
        gen_graphical_ast = False
        for i in range(len(sys.argv)):
            if sys.argv[i] == "--output": output = sys.argv[i+1]
            elif sys.argv[i] == "--graphical-ast": gen_graphical_ast = True
            
        if output is not None:
            p = AugmentedPropylene (out = output,
                                    generate_graphical_ast = gen_graphical_ast)
        else:
            p = AugmentedPropylene (generate_graphical_ast = gen_graphical_ast)
        
    inputFile = open(inputFilePath, 'r')
    inputFileLines = inputFile.readlines()
    inputFile.close()
    totalString = "" 
    for line in inputFileLines:
        totalString += line

    try: p.parse(totalString)
    except TooManySyntaxErrors as e:
        p.print_syntax_error_info()
        print "Too many syntax errors."
        print "Aborted."
        sys.exit (-1)

    except AttitudeTypeMismatch as e:
        print "Line {0} : detected {1} \"{2}\" previously used as a {3}"\
            .format (e.lineno, e.type2, e.attitude_name, e.type1)
        print "Aborted."
        sys.exit (-1)

    except UnboundedVariable as e:
        print "Line {0} : referenced unbounded variable {1}"\
            .format (e.lineno, e.symbol)
        print "Aborted."
        sys.exit (-1)

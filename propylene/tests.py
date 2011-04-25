##------------------------------------------------------------------------------
## tests.py
## 
## Unit tests for propylene
##------------------------------------------------------------------------------
##
##------------------------------------------------------------------------------
## local imports
##------------------------------------------------------------------------------
from propylene import Propylene as Propylene
from propylene import AugmentedPropylene as AugmentedPropylene
from exception import *
##
##------------------------------------------------------------------------------
## global imports
##------------------------------------------------------------------------------
import glob
import unittest
##
TEST_DIR = "test/"
##
##------------------------------------------------------------------------------
## class PropyleneTest
##------------------------------------------------------------------------------
class PropyleneTest(unittest.TestCase):
        
    def scenarios (self):
        return { 'base'     : ("classes/base-test-out.py", "test/base-test"),
                 'cond'     : ("classes/cond-test-out.py", "test/cond-test"),
                 'args'     : ("classes/args-test-out.py", "test/args-test"),
                 'lambda'   : ("classes/lambda-test-out.py", "test/lambda-test"),
                 'type-err' : ("classes/attitude-type-mismatch-err-out.py", "test/type-err"),
                 'lex-err'  : ("classes/lexical-err-out.py", "test/lexical-err"),
                 'syn-err'  : ("classes/syntax-err-out.py", "test/syntax-err"),
                 'unb-err'  : ("classes/unbound-err-out.py", "test/unbound-err"),
                 }

    

    def test_attitude_type_mismatch (self):
        scenario = self.scenarios ()['type-err']
        print "TESTING ", scenario
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.assertRaises (AttitudeTypeMismatch, 
                           self.parse, inputfile, outputfile)

    def test_lexical_error (self):
        scenario = self.scenarios ()['lex-err']
        print "TESTING ", scenario
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile)

    def test_syntax_error0 (self):
        scenario = self.scenarios ()['syn-err']
        print "TESTING ", scenario
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.assertRaises (TooManySyntaxErrors,
                           self.parse, inputfile, outputfile)

    def test_syntax_error1 (self):
        scenario = self.scenarios ()['syn-err']
        print "TESTING ", scenario
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile, 20)

    def test_lexical_error (self):
        scenario = self.scenarios ()['unb-err']
        print "TESTING ", scenario
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.assertRaises (UnboundedVariable, 
                           self.parse, inputfile, outputfile)

    def test_lamb (self):
        scenario = self.scenarios ()['lambda']
        print "TESTING ", scenario
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile)

    def test_args (self):
        scenario = self.scenarios ()['args']
        print "TESTING ", scenario
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile)

    def test_base (self):
        scenario = self.scenarios ()['base']
        print "TESTING ", scenario
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile)

    def test_cond (self):
        scenario = self.scenarios ()['cond']
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile)

    def parse (self, uInputFile, uOutputFile, uSynErrorsLimit = 10):
        p = AugmentedPropylene (out = uOutputFile, 
                                syntax_errors_limit = uSynErrorsLimit)
        inputFile = open (uInputFile, 'r')
        inputFileLines = inputFile.readlines()
        inputFile.close()
        totalString = "" 
        for line in inputFileLines:
            totalString += line

        result = p.parse (totalString)
##
##------------------------------------------------------------------------------
##  Main
##------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()

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
        return { 'base' : ("classes/base-test-out.py", "test/base-test"),
                 'cond' : ("classes/cond-test-out.py", "test/cond-test"),
                 'args' : ("classes/args-test-out.py", "test/args-test"),
                 'lamb' : ("classes/lamb-test-out.py", "test/lamb-test")}

    def test_lamb (self):
        scenario = self.scenarios ()['lamb']
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile)

    def test_args (self):
        scenario = self.scenarios ()['args']
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile)

    def test_base (self):
        scenario = self.scenarios ()['base']
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile)

    def test_cond (self):
        scenario = self.scenarios ()['cond']
        outputfile = scenario [0]
        inputfile  = scenario [1]
        self.parse (inputfile, outputfile)

    def parse (self, uInputFile, uOutputFile):
        p = AugmentedPropylene (out = uOutputFile)
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

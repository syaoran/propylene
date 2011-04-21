# ----------------------------------------------------------
# tests.py
# 
# Unit tests for propylene
# ----------------------------------------------------------
from propylene import Propylene as Propylene
from propylene import AugmentedPropylene as AugmentedPropylene
import glob
import unittest

TEST_DIR = "test/"

class PropyleneTest(unittest.TestCase):

    def scenarios (self):
        return glob.glob (TEST_DIR + "*-test")

    def test_all (self):
        p = AugmentedPropylene ()
        scenarios = self.scenarios ()

        for scenario in scenarios:
            inputFile = open(scenario, 'r')
            inputFileLines = inputFile.readlines()
            inputFile.close()
            totalString = "" 
            for line in inputFileLines:
                totalString += line
                
            result = p.parse(totalString)

if __name__ == '__main__':
    unittest.main()

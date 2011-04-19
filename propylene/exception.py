###
# exception.py
###


class SemanticError(Exception):
    '''A semantic error has occurred'''


class AttitudeTypeMismatch(SemanticError):
    ''' The same class refers to different attitude'''

class UnboundedVariable(SemanticError):
    ''' Usage of an unbounded variable'''

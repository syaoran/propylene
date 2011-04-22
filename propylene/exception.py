###
# exception.py
###


class TooManySyntaxErrors(Exception):
    ''' The syntax errors limit has been exceeded '''

class SemanticError(Exception):
    ''' A semantic error has occurred '''

class AttitudeTypeMismatch(SemanticError):
    ''' The same class refers to different attitudes '''

class UnboundedVariable(SemanticError):
    ''' Usage of an unbounded Variable has been detected '''

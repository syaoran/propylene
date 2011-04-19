###
# exception.py
###


class SemanticError(Exception):
    '''A semantic error has occurred'''


class AttitudeTypeMismatch(Exception):
    ''' The same class refers to different attitude'''


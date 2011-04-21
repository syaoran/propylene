##------------------------------------------------------------------------------
## state.py
## 
## This file contains the classes that encapsulates the variable parsing state
## of Propylene
##------------------------------------------------------------------------------
## global imports
##------------------------------------------------------------------------------
from exception import *
##
##------------------------------------------------------------------------------
## class VariableUsageState
##
## implements the 'Borg' pattern
##------------------------------------------------------------------------------
class VariableUsageState:
    __shared_state = {}    

    def __init__(self, *args, **kwargs):
        self.__dict__ = self.__shared_state

    def handle_symbol(self, symbol_table, symbol):
        ## if there are quotes, remove them
        if symbol[0] == "\"": symbol = symbol[1:-1]
        try:
            symbol_table[symbol]
        except(KeyError):
            raise UnboundedVariable()
##
##------------------------------------------------------------------------------
## class VariableDeclarationState
##
## implements the 'Borg' pattern
##------------------------------------------------------------------------------
class VariableDeclarationState:
    __shared_state = {}    
    
    def __init__(self, *args, **kwargs):
        self.__dict__ = self.__shared_state

    def handle_symbol(self, symbol_table, symbol):
        ## if there are quotes, remove them
        if symbol[0] == "\"": symbol = symbol[1:-1]
        symbol_table[symbol] = "Variable"

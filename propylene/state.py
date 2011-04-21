from exception import *

class VariableUsageState:
    
    def __init__(self, *args, **kwargs):
        pass

    def handle_symbol(self, symbol_table, symbol):
        ## if there are quotes, remove them
        if symbol[0] == "\"": symbol = symbol[1:-1]
        try:
            symbol_table[symbol]
        except(KeyError):
            raise UnboundedVariable()



class VariableDeclarationState:
    
    def __init__(self, *args, **kwargs):
        pass

    def handle_symbol(self, symbol_table, symbol):
        ## if there are quotes, remove them
        if symbol[0] == "\"": symbol = symbol[1:-1]
        symbol_table[symbol] = "Variable"        

      


class VariableUsageState:
    
    def __init__(self, *args, **kwargs):
        pass

    def handle_symbol(self, symbol_table, symbol):
        try:
            symbol_table[symbol]
        except(KeyError):
            raise UnboundedVariable()



class VariableDeclarationState:
    
    def __init__(self, *args, **kwargs):
        pass

    def handle_symbol(self, symbol_table, symbol):
        symbol_table[symbol] = "Variable"        

      

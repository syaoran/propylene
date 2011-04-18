"""
p_ast.py
"""

class Node:
    """Represents a Node of the AST. """
    def __init__(self, uName, uChildren = []):
        self._name = uName
        self._children = uChildren
        ## self.__someOtherInfo = []
        ##self.__parent = uParent
        
    def __repr__ (self):
        return repr("Node: " + self._name)
        
    def AddChild (self, child):
        self._children.append (child)

    def Visit (self, uVisitor):
        print self.__class__
        for c in self._children:
            c.Visit (uVisitor)
            
class Strategy (Node):
    """Represents a Strategy node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

class Plan (Node):
    """Represents a Plan node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

class Head (Node):
    """Represents a Head node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

class Body (Node):
    """Represents a Body node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

class Trigger (Node):
    """Represents a Trigger node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

class Condition (Node):
    """Represents a Condition node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

class Lambda (Node):
    """Represents a Lambda Leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

    def Visit (self, uVisitor):
        pass

class Belief (Node):
    """Represents a Belief leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        
    def Visit (self, uVisitor):
        uVisitor.VisitBelief (self)

class Action (Node):
    """Represents an Action leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

    def Visit (self, uVisitor):
        uVisitor.VisitAction (self)
        
class Goal (Node):
    """Represents a Goal leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

    def Visit (self, uVisitor):
        uVisitor.VisitGoal (self)
##
##
##
class Visitor:
    def __init__ (self, uTarget):
        self._belief_buf = ''
        self._action_buf = ''
        self._goal_buf = ''
        self._filename = uTarget
    
    def VisitBelief (self, uBelief):
        self._belief_buf = self._belief_buf + '\n class ' \
            + uBelief._name \
            + '(Belief):\n\t' \
            + 'pass'
        print "Belief"

    def VisitAction (self, uAction):
        self._action_buf = self._action_buf + '\n class ' \
            + uAction._name \
            + '(Action):\n\t' \
            + 'def execute (self):\n\t\t##...'
        print "Action"
    def VisitGoal (self, uGoal):
        self._goal_buf = self._goal_buf + '\n class ' \
            + uGoal._name \
            + '(Goal):\n\t' \
            + 'pass'
        print "Goal"


def flatten_c (uNode, uDepth = -1):    
    ## if no depth has been specified:
    if uDepth == -1:
        if uNode._children == []:
            return [uNode]
        else:
            new_children = []
            for c in uNode._children:
                new_c = flatten_c (c)
                new_children.append (new_c)

            return list(flatten_l (new_children))

def flatten_l(lst):
    for elem in lst:
        if isinstance (elem, list):
            for i in flatten_l(elem):
                yield i
        else:
            yield elem
        
    
def flatten_test ():
    v = Visitor ('')
    tree = Condition('', [
            Belief(''), 
            Condition('', [
                    Belief(''),
                    Condition('', [
                            Belief('')])])])
    
    
    tree.Visit (v)
    tree._children = flatten_c (tree)
    print ""
    tree.Visit (v)
    
    
    
    
            
            
            

        
        
     
    








    
        
        
            
    



# def Visit (uAst):
#     print uAst
#     if isinstance (uAst, Node):
#         for child in uAst._children:
#             Visit (child)
        

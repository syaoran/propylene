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
        for c in self._children:
            c.Visit (uVisitor)
            
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
    








    
        
        
            
    



# def Visit (uAst):
#     print uAst
#     if isinstance (uAst, Node):
#         for child in uAst._children:
#             Visit (child)
        

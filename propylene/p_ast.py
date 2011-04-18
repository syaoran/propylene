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
        print uVisitor.get_depth()*"\t", self
        uVisitor.inc_depth()

        for c in self._children:
            c.Visit (uVisitor)
        uVisitor.dec_depth()
            
class Strategy (Node):
    """Represents a Strategy node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name = "Strategy"

class Plan (Node):
    """Represents a Plan node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Plan"

class Head (Node):
    """Represents a Head node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Head"

class Body (Node):
    """Represents a Body node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Body"

class Trigger (Node):
    """Represents a Trigger node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Trigger"

class Condition (Node):
    """Represents a Condition node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Condition"

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
        Node.Visit(self,uVisitor)
        uVisitor.VisitBelief (self)

class Action (Node):
    """Represents an Action leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

    def Visit (self, uVisitor):
        Node.Visit(self,uVisitor)
        uVisitor.VisitAction (self)
        
class Goal (Node):
    """Represents a Goal leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

    def Visit (self, uVisitor):
        Node.Visit(self,uVisitor)
        uVisitor.VisitGoal (self)
##
##
##
class Visitor:
    def __init__ (self, uTarget = 'classes.py'):
        self._belief_buf = ''
        self._action_buf = ''
        self._goal_buf = ''
        self._depth = 0
        self._filename = uTarget

    def get_depth(self):
        return self._depth

    def inc_depth(self):
        self._depth = self._depth +1

    def dec_depth(self):
        self._depth = self._depth -1
    
    def VisitBelief (self, uBelief):
        self._belief_buf = self._belief_buf + '\n class ' \
            + uBelief._name \
            + '(Belief):\n\t' \
            + 'pass'
        #print "Belief"

    def VisitAction (self, uAction):
        self._action_buf = self._action_buf + '\n class ' \
            + uAction._name \
            + '(Action):\n\t' \
            + 'def execute (self):\n\t\t##...'
        #print "Action"
        
    def VisitGoal (self, uGoal):
        self._goal_buf = self._goal_buf + '\n class ' \
            + uGoal._name \
            + '(Goal):\n\t' \
            + 'pass'
        print "Goal"

    def GenerateCode (self):
        f = open (self._filename, 'w')
        f.write (self._belief_buf)
        f.write (self._action_buf)
        f.write (self._goal_buf)
        f.close ()
##
##
##
def flatten_c (uNode, uDepth = -1):    
    ## if no depth has been specified:
    if uDepth == -1:
        if isinstance (uNode, Belief) or \
           isinstance (uNode, Action) or \
           isinstance (uNode, Goal):
            return [uNode]
        else:
            new_children = []
            for c in uNode._children:
                new_c = flatten_c (c)
                new_children.append (new_c)

            return list(flatten_l (new_children))
##
##
##
def flatten_l(lst):
    for elem in lst:
        if isinstance (elem, list):
            for i in flatten_l(elem):
                yield i
        else:
            yield elem
##
##      
##    
def flatten_test ():
    v = Visitor ('')
    tree = Condition('', [
            Belief('belief1'), 
            Condition('', [
                    Belief('belief2'),
                    Condition('', [
                            Belief('belief3')])])])    
    tree.Visit (v)
    tree._children = flatten_c (tree)
    tree.Visit (v)

    print ""

    tree = Body('', [
            Belief('belief1'), 
            Body('', [
                    Belief('belief2'),
                    Body('', [
                            Belief('belief3')])])])    

    tree.Visit (v)
    tree._children = flatten_c (tree)
    tree.Visit (v)

def flatten_test2 ():
    v = Visitor ('')
##
##
##
##
# def Visit (uAst):
#     print uAst
#     if isinstance (uAst, Node):
#         for child in uAst._children:
#             Visit (child)

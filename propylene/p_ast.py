##------------------------------------------------------------------------------
## p_ast.py
## 
## This file contains the classes needed by PROPYLENE to represent and visit
## an AST. 
## 
##------------------------------------------------------------------------------
## global imports
##------------------------------------------------------------------------------
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from networkx import graphviz_layout
##
##------------------------------------------------------------------------------
##  The Node class. Parent class for a node in the AST.
##------------------------------------------------------------------------------
class Node:
    """Represents a Node of the AST. """
    def __init__(self, uName='', uChildren = []):
        self._name = uName
        self._children = uChildren
        
    def __repr__ (self):
        ## return repr(self._name + "@" + str (id(self)))
        return self._name
    
    def Name (self):
        return self._name

    def SetName (self, uName):
        self._name = uName

    def Accept (self, uVisitor):
       uVisitor.VisitBasicNode (self)
##
##------------------------------------------------------------------------------
##  The Strategy class. Represents a Strategy in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Strategy (Node):
    """Represents a Strategy node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name = "Strategy"
##
##------------------------------------------------------------------------------
##  The Plan class. Represents a Plan in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Plan (Node):
    """Represents a Plan node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Plan"
##
##------------------------------------------------------------------------------
##  The Head class. Represents a Head in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Head (Node):
    """Represents a Head node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Head"
##
##------------------------------------------------------------------------------
##  The Body class. Represents a Body in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Body (Node):
    """Represents a Body node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Body"
##
##------------------------------------------------------------------------------
##  The Trigger class. Represents a Trigger in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Trigger (Node):
    """Represents a Trigger node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Trigger"
##
##------------------------------------------------------------------------------
##  The Condition class. Represents a Condition in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Condition (Node):
    """Represents a Condition node in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Condition"
##
##------------------------------------------------------------------------------
##  The Lambda class. Represents a Lambda in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Lambda (Node):
    """Represents a Lambda Leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        self._name="Lambda"

    def Visit (self, uVisitor):
        Node.Visit(self,uVisitor)
##
##------------------------------------------------------------------------------
##  The Belief class. Represents a Belief in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Belief (Node):
    """Represents a Belief leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)
        
    def Accept (self, uVisitor):
        uVisitor.VisitBelief (self)
##
##------------------------------------------------------------------------------
##  The Action class. Represents an Action in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Action (Node):
    """Represents an Action leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

    def Accept (self, uVisitor):
        uVisitor.VisitAction (self)
##
##------------------------------------------------------------------------------
##  The Goal class. Represents a Goal in the AST. Subclasses Node.
##------------------------------------------------------------------------------            
class Goal (Node):
    """Represents a Goal leaf in an AST. """
    def __init__ (self, *args, **kwargs):
        Node.__init__ (self, *args, **kwargs)

    def Accept (self, uVisitor):
        uVisitor.VisitGoal (self)
##
##
##
##------------------------------------------------------------------------------
##  The Visitor base class.
##------------------------------------------------------------------------------
class Visitor:
    def __init__ (self, *args, **kwargs): self._depth = 0
    def VisitBasicNode (self, uNode): pass
    def VisitBelief (self, uBelief): pass
    def VisitGoal (self, uGoal): pass
    def VisitAction (self, uAction): pass
    def get_depth(self): return self._depth
    def inc_depth(self): self._depth = self._depth +1
    def dec_depth(self): self._depth = self._depth -1
##
##------------------------------------------------------------------------------
##  The CodeGenerator class. Implements the Visitor interface.
##------------------------------------------------------------------------------
class CodeGenerator (Visitor):
    def __init__ (self, uTarget = './classes/classes.py'):
        Visitor.__init__ (self)
        self._items = {}
        self._belief_buf = '\n\n##BELIEFS\n'
        self._goal_buf = '\n\n##GOALS\n'
        self._action_buf = '\n\n##ACTIONS\n'
        self._filename = uTarget
        print uTarget
        
    def VisitBasicNode (self, uNode):
        ##print self.get_depth()*"    ", uNode
        self.inc_depth()

        for n in uNode._children:
            n.Accept (self)
        self.dec_depth()
    
    def VisitBelief (self, uBelief):
        ##print self.get_depth()*"    ", uBelief
        if uBelief.Name () in self._items: return
        else:
            self._items[uBelief.Name ()] = 'Belief'
            self._belief_buf = self._belief_buf + '\nclass ' \
                + uBelief._name \
                + '(Belief):\n    ' \
                + 'pass\n'

    def VisitGoal (self, uGoal):
        ##print self.get_depth()*"    ", uGoal
        if uGoal.Name () in self._items: return
        else:
            self._items[uGoal.Name ()] = 'Goal'
            self._goal_buf = self._goal_buf + '\nclass ' \
                + uGoal._name \
                + '(Goal):\n    ' \
                + 'pass\n'

    def VisitAction (self, uAction):
        ##print self.get_depth()*"    ", uAction
        if uAction.Name () in self._items: return
        else:
            self._items[uAction.Name ()] = 'Action'
            self._action_buf = self._action_buf + '\nclass ' \
                + uAction._name \
                + '(Action):\n    ' \
                + 'def execute (self):\n        ##...\n'
            
    def Visit (self, uTree):
        uTree.Accept (self)
        
    def GenerateCode (self):
        f = open (self._filename, 'w')
        f.write (self._belief_buf)
        f.write (self._goal_buf)
        f.write (self._action_buf)
        f.close ()
##
##------------------------------------------------------------------------------
##  Class ASTVisualGenerator.
##------------------------------------------------------------------------------
class ASTVisualGenerator (Visitor):
    def __init__ (self, *args, **kwargs):
        Visitor.__init__ (self)
        self._nodes_buf = []
        self._edges_buf = []
        self._counter = 0
        self._queue = deque ([])

    def VisitBelief (self, uBelief): self.VisitBasicNode (uBelief)
    def VisitGoal (self, uGoal):     self.VisitBasicNode (uGoal)
    def VisitAction (self, uAction): self.VisitBasicNode (uAction)

    def VisitBasicNode (self, uNode):
        uNode.SetName (str (self._counter) + " : " +uNode.Name ())
        self._counter += 1
        for node in uNode._children:
            node.Accept (self)

    ## implements a breadth-first visit of the tree
    def Visit (self, uTree):
        uTree.Accept (self)

        self._queue.append(uTree)
        while not len (self._queue) == 0:
            node = self._queue.popleft ()
            self._nodes_buf.append (node)
            self._counter += 1
            for child in node._children:
                self._edges_buf.append ((node, child))
                self._queue.append (child)
    
    def GenerateImage (self):
        G = nx.DiGraph()
        G.add_nodes_from (self._nodes_buf)
        G.add_edges_from (self._edges_buf)
        pos = nx.graphviz_layout (G, prog = 'dot', args = '')
        plt.figure (figsize = (30, 10))
        nx.draw(G , pos, node_size=0, alpha=0.1, font_size = 40)
        plt.axis('equal')
        #plt.show()
        plt.savefig('strategy-ir.pdf')
##
##------------------------------------------------------------------------------
##  Ancillary functions.
##------------------------------------------------------------------------------
##------------------------------------------------------------------------------
##  function flatten_strategies
##  flattend all plans on a single level
##------------------------------------------------------------------------------
def flatten_strategies (uNode):
    if isinstance (uNode, Strategy):
        new_children = []
        for c in uNode._children:
            new_c = flatten_strategies (c)
            new_children.append (new_c)
            
        return list(flatten_l (new_children))
    
    else:
        return [uNode]
##
##
##
##------------------------------------------------------------------------------
##  function flatten_c
##  returns a tree where Conditions and Actions have been flattened
##------------------------------------------------------------------------------
def flatten_c (uNode):
    if isinstance (uNode, Belief) or \
       isinstance (uNode, Action) or \
       isinstance (uNode, Goal)   or \
       isinstance (uNode, Lambda):
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
##------------------------------------------------------------------------------
##  function flatten_l
##  implements an iterator over nested lists
##------------------------------------------------------------------------------
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
##------------------------------------------------------------------------------
##  Test functions.
##------------------------------------------------------------------------------
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
##
##
##
def flatten_test2 ():
    v = Visitor ('')

import networkx as nx
import matplotlib.pyplot as plt

try:
    from networkx import graphviz_layout
except ImportError:
    raise ImportError("This example needs Graphviz and either PyGraphviz or Pydot")


G=nx.balanced_tree(3,5)
G = nx.Graph ()
G.add_nodes_from(['a : Belief',2,3,4,5,6])
G.add_edge('a : Belief',2)
G.add_edge('a : Belief',3)
G.add_edge(2,4)
G.add_edge(4,5)
G.add_edge(3,6)

pos=nx.graphviz_layout(G,prog='dot',args='')
plt.figure(figsize=(8,8))
#nx.draw(G,pos,node_size=20,alpha=0.5,node_color="blue", with_labels=False)
nx.draw(G,pos,node_size=0, alpha=0.2, node_color="blue")
plt.axis('equal')
#plt.savefig('circular_tree.png')
plt.show() 

import networkx as nx
import pygraphviz
import matplotlib.pyplot as plt

g=nx.DiGraph()
g.add_edges_from([(0,1),(1,2),(1,7),(2,3),(2,6),(3,4),(3,5),(4,3),(5,2),(6,7),(7,8),(7,9),(8,9)])
# pos=nx.spring_layout(g)
pos=nx.nx_agraph.graphviz_layout(g, prog='dot')
plt.figure(figsize=(12,12))
labels={}
labels[0]=r'$B_{999}$'
labels[1]=r'$B_0$'
labels[2]=r'$B_1$'
labels[3]=r'$B_2$'
labels[4]=r'$B_6$'
labels[5]=r'$B_7$'
labels[6]=r'$B_8$'
labels[7]=r'$B_3$'
labels[8]=r'$B_4$'
labels[9]=r'$B_5$'
nx.draw_networkx_edges(g,pos,
                       width=1,alpha=0.5,edge_color='black', arrows=True)
nx.draw_networkx_nodes(g,pos,
                       node_color='r',
                       node_size=1000,
                   alpha=0.8)
nx.draw_networkx_labels(g,pos,labels,font_size=16)

plt.axis('off')
# plt.figure(figsize=(8,6))
plt.savefig("graph.png") # save as png
plt.show() # display
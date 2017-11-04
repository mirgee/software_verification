import networkx as nx
import pygraphviz
import matplotlib.pyplot as plt

g=nx.DiGraph()
g.add_edges_from(ebunch = [(1,2),(2,3),(3,4),(3,5),(4,5),(5,6),(5,12),(6,7),(6,8),(7,6),(8,9),(8,10),(9,8),(10,11),(11,5)])
# pos=nx.spring_layout(g)
pos=nx.nx_agraph.graphviz_layout(g, prog='dot')
plt.figure(figsize=(12,12))
labels={}
labels[1]=r'$B_{999}$'
labels[2]=r'$B_0$'
labels[3]=r'$B_1$'
labels[4]=r'$B_9$'
labels[5]=r'$B_2$'
labels[6]=r'$B_4$'
labels[7]=r'$B_8$'
labels[8]=r'$B_5$'
labels[9]=r'$B_6$'
labels[10]=r'$B_7$'
labels[11]=r''
labels[12]=r'$B_3$'
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
import networkx as nx
import matplotlib.pyplot as plt

er=nx.erdos_renyi_graph(5000,0.05)
# ps=nx.shell_layout(er)#布置框架
# nx.draw(er,ps,with_labels=False,node_size=30)
# plt.show()
nodes = er.nodes
edges = er.edges

with open('./nodes.csv', "w+", encoding='utf-8') as nodesFile:
    for node in nodes:
        nodesFile.write(str(node))
        nodesFile.write('\n')

with open('./edges.csv', "w+", encoding='utf-8') as edgesFile:
    for edge in edges:
        line = str(edge[0])+","+str(edge[1])+'\n'
        edgesFile.write(line)


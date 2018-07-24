import matplotlib.pyplot as plt
import networkx as nx
import json

with open("data.json", "r") as data:
    graph = json.load(data)
#make node and edges 
nodes = []
edges = []#tuples including base links and every link that follows
for link in graph:
    nodes.append(link)
    for x in graph[link]:#loop through links it connect too
        edges.append((link, x))#add a tuple from base link to new node

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
nx.draw(G)
plt.show()
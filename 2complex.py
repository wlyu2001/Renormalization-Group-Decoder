#2complex

import networkx as nx

class 2complex(nx.Graph):
	def __init__(self,vertices,edges,faces):
		super(nx.Graph, self).__init__()
		self.add_nodes_from(vertices)
		self.add_edges_from(edges)
		self.faces = faces
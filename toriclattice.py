#toric lattice


import numpy
import networkx as nx


class lattice(object):
	def __init__(self,dimension):
	    self.dim = dimension
	    self.systole = dimension
	    self.graph = nx.cartesian_product(nx.generators.classic.cycle_graph(dimension), nx.generators.classic.cycle_graph(dimension))
	    #relabel nodes and edges
	    rlabels = dict(enumerate(self.graph.nodes()))
	    labels = dict(zip(rlabels.values(),rlabels.keys()))
	    self.graph = nx.relabel_nodes(self.graph,labels)
	    self.faces = [ [[labels[v,u], labels[(v+1)%dimension,u]], [labels[v,u], labels[v,(u+1)%dimension]], [labels[(v+1)%dimension,u], labels[(v+1)%dimension,(u+1)%dimension]], [labels[v,(u+1)%dimension], labels[(v+1)%dimension,(u+1)%dimension]]] for v in range(dimension) for u in range(dimension) ]

	def adjMatrix(self):
		return nx.adjacency_matrix(self.graph)

	def incMatrix(self):
		return nx.incidence_matrix(self.graph)

	def nEdges(self):
		return len(self.graph.edges())

	def edges(self):
		return self.graph.edges()

	def nVertices(self):
		return len(self.graph.nodes())

	def vertices(self):
		return self.graph.nodes()
		
# 	def faces(self):
# 		return self.faces
	
	#this method gets called a lot, maybe precompute results for each lattice
	def dist(self,x,y):
		return nx.shortest_path_length(self.graph,x,y)
		
	def shortestPath(self,x,y):
		return nx.shortest_path(self.graph,x,y)



class cluster(object):
	def __init__(self,lattice):
	    self.defects = []
	    self.lat = lattice
	    
	def diam(self):			#this is very, very, very inefficient!
		nodes = self.defects
		len = []
		while nodes:
			v = nodes.pop()
			for u in nodes:
				len.append(nx.all_pairs_dijkstra_path_length(self.lat.graph,v,u))
		return max(len)
		
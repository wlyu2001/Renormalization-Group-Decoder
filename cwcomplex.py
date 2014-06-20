#2complex

import networkx as nx



class TwoComplex(nx.Graph):
	def __init__(self,vertices,edges,faces,systolelength):
		super(TwoComplex, self).__init__()
		self.add_nodes_from(vertices)
		self.add_edges_from(edges)
		self.fac = faces
		self.systole = systolelength

	def vertices(self):
		return self.nodes()
		
	def faces(self):
		return self.fac

	def nEdges(self):
		return len(self.edges())

	def nVertices(self):
		return len(self.nodes())

	def dist(self,x,y):
		return nx.shortest_path_length(self,x,y)
		
	def shortestPath(self,x,y):
		return nx.shortest_path(self,x,y)
		
	def bound1(self):
		return nx.incidence_matrix(self)



class pointCluster(object):
	def __init__(self,complex):
	    self.defects = []
	    self.compl = complex
	    
	def diam(self):			#this is very, very, very inefficient!
		nodes = self.defects
		len = []
		while nodes:
			v = nodes.pop()
			for u in nodes:
				len.append(nx.all_pairs_dijkstra_path_length(self.compl,v,u))
		return max(len)
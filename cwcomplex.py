#cwcomplex

import networkx as nx
import numpy as np



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
		
	def nVertices(self):
		return len(self.nodes())

	def nEdges(self):
		return len(self.edges())
		
	def nFaces(self):
		return len(self.fac)

	def dist(self,x,y):
		return nx.shortest_path_length(self,x,y)
		
	def shortestPath(self,x,y):
		return nx.shortest_path(self,x,y)
		
	def bound1(self):
		return nx.incidence_matrix(self).astype(int)
		
	def bound2(self):
		mat = np.zeros((self.nEdges(), self.nFaces()),dtype = np.int)
		edgelist = [set(e) for e in self.edges()]
		for i in range(len(self.fac)):
			for j in range(len(self.fac[i])):
				mat[edgelist.index(set(self.fac[i][j]))][i] = 1
		return mat



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
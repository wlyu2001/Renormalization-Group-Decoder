#toric lattice

import networkx as nx
from cwcomplex import TwoComplex



class ToricLattice(TwoComplex):
	def __init__(self,L):
		#compute vertices, edges and faces
		torus = nx.cartesian_product(nx.generators.classic.cycle_graph(L), nx.generators.classic.cycle_graph(L))
		rlabels = dict(enumerate(torus.nodes()))
		labels = dict(zip(rlabels.values(),rlabels.keys()))
		torus = nx.relabel_nodes(torus,labels)
		faces = [ [[labels[v,u], labels[(v+1)%L,u]], [labels[v,u], labels[v,(u+1)%L]], [labels[(v+1)%L,u], labels[(v+1)%L,(u+1)%L]], [labels[v,(u+1)%L], labels[(v+1)%L,(u+1)%L]]] for v in range(L) for u in range(L) ]
		#initialize TwoComplex
		super(ToricLattice,self).__init__(torus.nodes(),torus.edges(),faces,L)
#error correction


import numpy, random, cwcomplex
from operator import add



class errorChain(object):
	def __init__(self,complex):
		self.cplx = complex
		self.Xerrors = [0 for i in range(complex.nEdges())]
		self.Xsynd = [0 for i in range(complex.nVertices())]
		
	def createRandom(self,rate):
		for e in range(self.cplx.nEdges()):
			if random.random() < rate:
				self.Xerrors[e] = (self.Xerrors[e]+1) % 2
				
	def getXSyndrome(self):
		self.Xsynd = numpy.ravel(numpy.dot(self.cplx.bound1(), self.Xerrors) % 2)
		return self.Xsynd



class errorCorrection(object):
	def __init__(self,complex,Xsyndrome):
		self.cplx = complex
		self.Xsynd = Xsyndrome

	def getDefectPositions(self):
		return [i for i, x in enumerate(self.Xsynd) if x == 1]
		
	def decomposeSparse(self,unitOfLength):
		family = []
		defects = self.getDefectPositions()
		while defects:	#non-empty sequences are true.
			newCluster = cwcomplex.pointCluster(self.cplx)
			#define new cluster with some base point from the defect list
			newCluster.defects.append(defects.pop())
			# i marks the base point from which we search for new close-by defects
			i = 0
			while True:
				for de in defects:
					if self.cplx.dist(newCluster.defects[i],de) <= unitOfLength:
						newCluster.defects.append(de)
						defects.remove(de)
				i += 1
				if i >= len(newCluster.defects):
					break
			#compute size of the cluster here
			family.append(newCluster)
		return family
		
	def pairAnyons(self,d1,d2):
		path = self.cplx.shortestPath(d1,d2)
		P = [0 for i in range(self.cplx.nEdges())]
		for i in path:
			P[i] = 1
		return P
		
	def annihilateCluster(self,cl):
		P = [0 for i in range(self.cplx.nEdges())]
		#cluster cl not neutral -> return identity operator
		if len(cl.defects)%2 != 0:
			return P
		#guarantee that decoder won't do a logical operator
# 		elif cl.diam() > self.cplx.systole/2:
# 			return P
		else:
			while cl.defects:
				d1 = cl.defects.pop()
				d2 = cl.defects.pop()
				P = map(add, P, self.pairAnyons(d1,d2))
				P = [x %2 for x in P]
			return P
			
	def annihilate(self, level):
		family = self.decomposeSparse(2^level)
		P = [0 for i in range(self.cplx.nEdges())]
		while family:
			P = map(add, P, self.annihilateCluster(family.pop()))
			P = [x %2 for x in P]
		return P
		
	def runRG(self):
		Q = [0 for i in range(self.cplx.nEdges())]
		maxlvl = int(numpy.log2(self.cplx.systole/2))
		for p in range(maxlvl):
			Q = map(add, Q, self.annihilate(p))
			Q = [x %2 for x in Q]
		return Q
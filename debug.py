#!/usr/local/bin/python

import toriclattice as tor
import errorcorrection
import networkx as nx
import matplotlib.pyplot as plt
import pdb

lat = tor.ToricLattice(6)
ec = errorcorrection.errorChain(lat)

ec.createRandom(0.1)
print(ec.Xerrors)
synd = ec.getXSyndrome()
print(synd)

corr = errorcorrection.errorCorrection(lat,synd)

print(corr.runRG())




# nx.draw(lat.graph)
# 
# plt.show()

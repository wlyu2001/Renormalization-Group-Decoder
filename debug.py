#!/usr/bin/env python

import toriclattice as tor
import errorcorrection
import networkx as nx
import matplotlib.pyplot as plt
import pdb
import numpy as np

np.set_printoptions(threshold='nan')

lat = tor.ToricLattice(4)
# ec = errorcorrection.errorChain(lat)
# 
# ec.createRandom(0.1)
# print(ec.Xerrors)
# synd = ec.getXSyndrome()
# print(synd)
# 
# corr = errorcorrection.errorCorrection(lat,synd)
# 
# print(corr.runRG())
# print(lat.edges())
# print(lat.faces())
# print(lat.bound1())
# print(lat.bound2())
#print(np.dot(lat.bound1(),lat.bound2()) % 2)
print(lat.bettiNumber())

# nx.draw(lat.graph)
# 
# plt.show()

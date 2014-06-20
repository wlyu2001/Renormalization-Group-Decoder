#Linear Algebra stuff


import numpy

#elementary operations
#all arithmetic in F2
def rowSwap(A, i, j):
	temp = numpy.copy(A[i, :])
	A[i, :] = A[j, :]
	A[j, :] = temp
 
def colSwap(A, i, j):
	temp = numpy.copy(A[:, i])
	A[:, i] = A[:, j]
	A[:, j] = temp
 
def colCombine(A, addTo, scaleCol):
	A[:, addTo] ^= A[:, scaleCol]
 
def rowCombine(A, addTo, scaleRow):
	A[addTo, :] ^= A[scaleRow, :]

#column reduction of A via E (from right) and multiplying E^-1 to B from left
def simultaneousReduce(A, B):
	if A.shape[1] != B.shape[0]:
		raise Exception("Matrices have the wrong shape.")
	numRows, numCols = A.shape # col reduce A
	i,j = 0,0
	while True:
		if i >= numRows or j >= numCols:
			break
		if A[i][j] == 0:
			nonzeroCol = j
			while nonzeroCol < numCols and A[i,nonzeroCol] == 0:
				nonzeroCol += 1
			if nonzeroCol == numCols:
				i += 1
				continue
			colSwap(A, j, nonzeroCol)
			rowSwap(B, j, nonzeroCol)
		for otherCol in range(0, numCols):
			if otherCol == j:
				continue
			if A[i, otherCol] != 0:
				colCombine(A, otherCol, j)
				rowCombine(B, j, otherCol)
		i += 1; j+= 1
	return A,B

def finishRowReducing(B):
	numRows, numCols = B.shape
	i,j = 0,0
	while True:
		if i >= numRows or j >= numCols:
			break
		if B[i, j] == 0:
			nonzeroRow = i
			while nonzeroRow < numRows and B[nonzeroRow, j] == 0:
				nonzeroRow += 1
			if nonzeroRow == numRows:
				j += 1
				continue
			rowSwap(B, i, nonzeroRow)
		for otherRow in range(0, numRows):
			if otherRow == i:
				continue
			if B[otherRow, j] != 0:
				rowCombine(B, otherRow, j)
		i += 1; j+= 1
	return B

def numPivotCols(A):
	z = numpy.zeros(A.shape[0])
	return [numpy.all(A[:, j] == z) for j in range(A.shape[1])].count(False)
 
def numPivotRows(A):
	z = numpy.zeros(A.shape[1])
	return [numpy.all(A[i, :] == z) for i in range(A.shape[0])].count(False)
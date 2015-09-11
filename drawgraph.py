import numpy

vertex = range(5)
edge = [(1,2),(1,5),(2,3),(2,4),(3,4),(1,3),(4,5)]

mat = numpy.array([[0 for i in vertex] for j in vertex])

for ele in edge:
    mat[ele[0]-1][ele[1]-1]=-1
    mat[ele[1]-1][ele[0]-1]=-1
    
#print matrix
    
for i in range(5):
    mat[i][i]=-1*(sum([mat[i][k] for k in range(5)]))

#print matrix

[eigs, vecs]=numpy.linalg.eig(mat)

print eigs

print vecs
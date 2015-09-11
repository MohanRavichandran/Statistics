import numpy
from numpy import linalg
#This simple programme uses a Monte-Carlo method to estimate the volume of a n sphere
'''
a = numpy.matrix([1,2,3])
b = numpy.transpose(a)
print numpy.dot(b,a)
'''

def gen(n):
    a = numpy.array([numpy.random.rand() for i in range(n)])
    return 2*a-1



def vol(n):
    
    instances = 10000

    incounter = 0
    for i in range(instances):
        a = gen(n)
        if numpy.linalg.norm(a) < 1:
            incounter+=1
        
    print float(incounter)/instances
        
for n in range(2,10):
    vol(n)
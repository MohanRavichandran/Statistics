#This program generates random n*n doubly stochastic maps using a Monte-Carlo approach
import numpy as np
np.set_printoptions(3, suppress= True)

def doublyStochastic(n):
    A = np.array([[1/float(n) for i in range(n)] for j in range(n)])
    iterations = n*100
    for i in range(iterations):
        a = np.random.randint(n)
        b = np.random.randint(n)
        c = np.random.randint(n)
        d = np.random.randint(n)
        if (a==b or c==d):
            continue
        
        #lthreshold = min([A[a][c],A[a][d],A[b][c],A[b][d]])
        #rthreshold = 1-max([A[a][c],A[a][d],A[b][c],A[b][d]])
        #threshold = min([lthreshold,rthreshold])
        #modifier = np.random.rand()*threshold
        
        modifier = np.random.rand()
        
        if (min([A[a][c]+modifier,A[a][d]-modifier,A[b][c]-modifier,A[b][d]+modifier]) > 0 and 
        max([A[a][c]+modifier,A[a][d]-modifier,A[b][c]-modifier,A[b][d]+modifier]) < 1):
            #print ("%0.3f" % modifier)
            A[a][c]=A[a][c]+modifier
            A[a][d]=A[a][d]-modifier
            A[b][c]=A[b][c]-modifier
            A[b][d]=A[b][d]+modifier
    
    
    
    return A


checkmat = []
for i in range(1000):
    A = doublyStochastic(3)
    #print A
    B = np.array([0,1,2])
    C =  np.dot(A,B)
    D = [c for c in C if c < 1]
    num1 = sum(D)
    num2 = 3-len(D)
    checkterm = num1 - 2 + num2

    checkmat = checkmat + [checkterm]

print min(checkmat)
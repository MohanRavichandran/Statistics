import numpy



def steps(dim):

    steparray = []
    for index in range(dim):
        temp = [0 for i in range(dim)]
        temp1 = [0 for i in range(dim)]
        temp[index] = 1
        temp1[index] = -1
        steparray+=[numpy.array(temp),numpy.array(temp1)]
    
    return steparray

def instance(dim,num_steps):
    origin = numpy.array([0 for i in range(dim)])
    steparray = steps(dim)
    return_time = -1
    position_array = [numpy.array([0 for i in range(dim)])]
    for i in range(num_steps-1):
        step_index = numpy.random.choice(2*dim)
        step = steparray[step_index]
        position_array+=[position_array[i]+step]
        if numpy.array_equal(position_array[i+1],origin) and return_time == -1:
            return_time = i+1
            return return_time
    #return [position_array,return_time]
    return return_time


num_iter = 5000
num_steps = 100
dim = 3

ret_time = []
for i in range(num_iter):
    ret_time+=[instance(dim,num_steps)]    

hist = [0 for i in range(num_steps)]
for i in range(num_iter):
    if ret_time[i]!=-1:
        #print ret_time[i]
        hist[ret_time[i]]+=1

    
for i in range(1,num_steps):
    hist[i]+=hist[i-1]

print hist[0:100:10]
     
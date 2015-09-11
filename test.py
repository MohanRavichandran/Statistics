a = raw_input('enter a string: ')
length = len(a)
b = ''
for ctr in range(length):
    b+=a[length-ctr-1]
print 'The reversed string is: ', b
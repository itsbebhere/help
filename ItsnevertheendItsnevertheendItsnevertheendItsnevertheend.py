from math import*
from numpy import*

asize = int(input('Please, enter the size of array: '))

####
A = random.randint(0, 50, size = asize)
print(A)
amax = argmax(A) 
print("Index of max element: %d" %amax)
####

if asize <5:
    print("Array is too short for task to be completed, it must be at least five or more elements")
else:
    temp = A[amax]
    A[amax] = A[4]
    A[4] = temp

print(A)

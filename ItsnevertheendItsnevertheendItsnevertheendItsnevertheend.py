from math import*
from numpy import*

A = random.randint(0, 50, size = 20)
print(A)
amax = argmax(A) 
print(amax)

temp = A[amax]
A[amax] = A[4]
A[4] = A[amax]

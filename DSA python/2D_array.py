import numpy as np
A = np.array([[1,2],[3,4]])
print(A)

print(A.dtype)    #know datatype
#print(A.dim)      #print return value
print(A.shape)    #it will returns the order of matrix
print(A.size)     #returns the number of element


#print rank of matrix
print(A.ndim)

#convert A into 1d array
e=A.flatten()  #print in a sequence
print(e)


b=np.array([[5,6],[7,8]])
c = A*b
print(c)

d=A-b
print(d)
f=A/b
print(f)
g=b+A
h=b%A
print(g)
print(h)



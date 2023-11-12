import numpy as np
A = np.array([[1,2],[3,4]])
print(A)
e=A.flatten()  #print in a sequence
print(e)

print(A.dtype)    #know datatype
#print(A.dim)      #print return value
print(A.shape)    #it will returns the order of matrix
print(A.size)     #returns the number of element
b=np.array([[5,6],[7,8]])
c = A*b
print(c)

d=A-b
print(d)
f=A/b
print(f)
g=b**A
h=b%A
print(g)
print(h)

# creating 3d array
d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d)

# creating list 
ab=[1,2,3,4,5,6,7,8,9]
print(ab[3])
for i in ab:
    if i ==3:
        print(i)
# replace the value in list
ab[3]=8
print(ab)
#insertion in list
ab.extend('9') #we can insert only string value 
#ab.insret(9)
print(ab)


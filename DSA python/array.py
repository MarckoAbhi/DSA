import array as arr

arr1 = [2, 12,11,8,9,7,15]

print(arr1)
# print element by indexing number
print(arr1[4])

# length of array
print(len(arr1))

#slicing 
y=slice(4)
print(arr1[y])
# append is use to add single element at the end of array

arr1.append(3)
print(arr1)

# extend is use to add 
B=[1,4,5,10,14,6]
arr1.extend(B)
print(arr1)
# to give a new memory location of array B
ac=B.copy()
print(ac)
# insert is use to add element anywhere
arr1.insert(2,13)
print(arr1)
# sorting the element
arr1.sort()
print(arr1)
# pop is use to delete element by indexing number
# if we not write element index number in pop than it will remove the last element of array
arr1.pop(3)
print(arr1)
# remove is use to remove element by name/value
arr1.remove(12)
print(arr1)

c=[11, 20, 22,24]
# loops in array
b=0
while b<= c[0]:
    print(b)
    b = b+1
#for loop
for x in c:
    print(x)
    x=++1
    
 #creating array and define length and element by user   
h=arr.array('i',[])
n=int(input("enter the length of array:"))
for j in range(n):
    k=int(input("enter the element"))
    h.append(k)
    print(h)
    
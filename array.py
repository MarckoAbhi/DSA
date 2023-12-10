import array as arr

arr1 = [2, 12,11]

print(arr1)

#i append is use to add single element at the end of array
arr1.append(3)
print(arr1)

# ii  add four element to array1
B=[1,4,5,10]
arr1.extend(B)
print(arr1)

# iii add element to the fourth position
arr1.insert(3, 13)
print(arr1)

# iv delete seventh element from array1
arr1.pop(6)
print(arr1)

#v Remove last element and return it
print(arr1.pop())

#create two arrays having three element each and merge all three arrray
arr2=[14, 15, 18]
arr3 = [22, 26,29]

merged_array= arr1 + arr2+ arr3

print(merged_array)

#determine the length of the new array formed
print(len(merged_array))

#print the ninth element of new array
print(merged_array[8])






def selection_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min=j
        arr[i], arr[min]=arr[min], arr[i]
 
arr=[89, 14, 10, 180,38,60,25]
selection_sort(arr)
print("sorted array is :", arr)
            
          
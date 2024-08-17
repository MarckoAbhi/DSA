def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
my_list = [1, 3, 5, 7, 9, 11, 13]
search_element = 10
result = linear_search(my_list, search_element)

if result != -1:
    print(f" Searching Element {search_element} found at index {result}.")
else:
    print(f" Search Element {search_element} not found in the list.")




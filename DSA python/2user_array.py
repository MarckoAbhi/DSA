import array as arr

def create_array():
    # Get the length of the array from the user
    length = int(input("Enter the length of the array: "))

    # Initialize an empty array
    my_array = []

    # Insert values into the array
    for i in range(length):
        value = int(input(f"Enter the value for index {i}: "))
        my_array.append(value)

    return my_array

# Example usage
user_array = create_array()
print("Your created array is :", user_array)

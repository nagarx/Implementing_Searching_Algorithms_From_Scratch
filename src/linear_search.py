def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Target is not found in the array

# Simple test to demonstrate Linear Search
test_array = [64, 34, 25, 12, 22, 11, 90]
result = linear_search(test_array, 25)
print(result)

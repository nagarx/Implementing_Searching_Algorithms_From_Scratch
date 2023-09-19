def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Compute mid index of the array
        mid_val = arr[mid]

        if mid_val == target:  # If the target is found
            return mid
        elif mid_val < target:  # If the target lies to the right of mid
            low = mid + 1
        else:  # If the target lies to the left of mid
            high = mid - 1

    return -1  # Target is not found in the array


# Simple test to demonstrate Binary Search
test_array = [11, 12, 22, 25, 34, 64, 90]
result = binary_search(test_array, 25)
print(result)

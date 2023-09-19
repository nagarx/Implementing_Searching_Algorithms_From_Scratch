def ubiquitous_binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the first occurrence of a target element.

    Parameters:
        arr (list): Sorted list of elements to search from.
        target (int or float): The element to search for.

    Returns:
        int: The index of the first occurrence of the target element in the list if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1  # Initialize search range
    result = -1  # Initialize result to -1 for "not found"

    while low <= high:
        mid = low + (high - low) // 2  # Compute the middle index

        if arr[mid] == target:  # Target value found
            result = mid  # Update result
            high = mid - 1  # Continue search in the left half to find the first occurrence
        elif arr[mid] < target:  # Target lies to the right of mid
            low = mid + 1
        else:  # Target lies to the left of mid
            high = mid - 1

    return result  # Return the first occurrence or -1 if not found


# Implementing a basic unit test to verify the algorithm's functionality.
test_cases = [
    {"arr": [1, 2, 3, 4, 5, 6, 7, 8, 9], "target": 5, "expected": 4},
    {"arr": [1, 2, 3, 4, 5, 6, 7, 8, 9], "target": 10, "expected": -1},
    {"arr": [], "target": 5, "expected": -1},
    {"arr": [5], "target": 5, "expected": 0},
    {"arr": [5], "target": 4, "expected": -1}
]

test_results = [ubiquitous_binary_search(tc["arr"], tc["target"]) == tc["expected"] for tc in
                test_cases]

print(test_results)

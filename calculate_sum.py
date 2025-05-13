def recursive_sum(arr, index=0):
    # Base case: if the array is fully traversed
    if index >= len(arr):
        return 0

    # Recursive case: current element + sum of remaining elements
    return arr[index] + recursive_sum(arr, index + 1)

# Example usage
numbers_sequence = [8, 10, 12, 90, 109, 210]
total_sum = recursive_sum(numbers_sequence)
print("Sum of array:", total_sum)

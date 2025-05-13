def reverse_array(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    # Base case: If start is greater than or equal to end, return
    if start >= end:
        return

    # Swap the elements
    arr[start], arr[end] = arr[end], arr[start]

    # Recursive call
    reverse_array(arr, start + 1, end - 1)

# Example usage
numbers_sequence = [8, 10, 12, 90, 109, 210]
reverse_array(numbers_sequence)
print(numbers_sequence)

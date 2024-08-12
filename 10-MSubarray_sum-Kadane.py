def kadane(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Example usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3, 7]
print(f"Maximum Subarray Sum: {kadane(arr)}")

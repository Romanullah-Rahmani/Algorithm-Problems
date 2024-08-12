arr = [12,52,121,93,76,43,89,47,39,84,32,34,24,53,24]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]< arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr= bubble_sort(arr)
print(arr)
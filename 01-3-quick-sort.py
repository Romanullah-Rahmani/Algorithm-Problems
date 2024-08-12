arr = [12,52,121,93]

def quick_sort(arr):
    if len(arr) <= 1 :
        return arr
    else:
        pivot = arr[len(arr) // 2]
        Left = [x for x in arr if x < pivot]
        Middle = [x for x in arr if x == pivot]
        Right = [x for x in arr if x > pivot]
    return quick_sort(Left) + Middle + quick_sort(Right)

arr = quick_sort(arr)
print(arr)

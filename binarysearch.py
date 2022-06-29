def binary_search(target, arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        median = (high + low) // 2
        if arr[median] < target:
            low = median + 1
        elif arr[median] > target:
            high = median - 1
        else:
            return median
    return -1
    
target = 36
arr = [2, 3, 5, 8, 9, 12, 23, 25, 36, 45]
print (binary_search(target, arr))




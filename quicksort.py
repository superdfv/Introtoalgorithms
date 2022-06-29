#Quick Sort


def quick_sort(nums, low, high):
    if low < high:
        nums, p = partition(nums, low, high)
        nums = quick_sort(nums, low, p -1)
        nums = quick_sort(nums, p +1, high)
    return nums
    


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i += 1    
    temp2 = nums[i]
    nums[i] = nums[high]
    nums[high] = temp2
    return nums, i

nums = [1,3,6,2,4,7,9,8]
quick_sort(nums, 0, 7)
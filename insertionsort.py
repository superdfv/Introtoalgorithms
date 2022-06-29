#Insertion Sort


def insertion_sort(nums):
    i = 0
    while i < len(nums):
        j = i 
        while j > 0 and nums[j-1] > nums[j]:
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            j -= 1
        i += 1
    print (nums)

nums = [3, 2, 1, 8, 6, 7]
insertion_sort(nums)


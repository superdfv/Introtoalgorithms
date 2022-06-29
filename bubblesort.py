#Bubble Sort

def bubble_sort(nums):
    swapping = True
    saved = 0
    print(len(nums))
    while swapping:
        swapping = False
        for i in range(1,len(nums)):
            print(i)
            if nums[i-1] > nums[i]:
                saved = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = saved
                swapping = True
    print (nums)




nums = [5, 3, 8, 10, 1, 4, 9,]
bubble_sort(nums)
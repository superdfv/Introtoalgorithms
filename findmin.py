#Set min to positive infinity: float("inf").
# For each number in the list nums, compare it to min. If num is smaller, set min to num.
# min is now set to the smallest number in the list.
def find_min(nums):
    min = float('inf')
    for num in nums:
        if num < min:
            min = num
     
nums = [7, 4, 3, 100, 2343243, 343434, 1, 2, 32]
find_min(nums)
#It should take a list of integers and return the largest value in the list.
def find_max(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    return max

nums = [7, 4, 3, 100, 2343243, 343434, 1, 2, 32]
find_max(nums)
#Merge Sort


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    a= merge_sort(nums[: len(nums) // 2])
    b= merge_sort(nums[len(nums) // 2 :])
    return merge(a, b)

def merge(first, second):

    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final

nums = [1, 8, 3, 10, 5, 6, 7, 4, 9, 2]
print(merge_sort(nums))
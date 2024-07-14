def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]   #list comprehension
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

def rearrange(nums):
    sorted_nums = quickSort(nums)
    odd_indices = sorted_nums[1::2][::-1]
    even_indices = sorted_nums[0::2]
    
    result = []
    oi, ei = 0, 0
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(even_indices[ei])
            ei += 1
        else:
            result.append(odd_indices[oi])
            oi += 1
    
    return result

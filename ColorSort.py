def sortColors(nums):
    l, h, curr = 0, len(nums) - 1, 0

    while curr <= h:
        if nums[curr] == 0:
            nums[l], nums[curr] = nums[curr], nums[l]
            l += 1
            curr += 1
        elif nums[curr] == 2:
            nums[h], nums[curr] = nums[curr], nums[h]
            h -= 1
        else:
            curr += 1

# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

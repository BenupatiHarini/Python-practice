def threeSumClosest(nums, target):
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(target - total) < abs(target - closest):
                closest = total
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total
    return closest
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print("Closest sum:", result)

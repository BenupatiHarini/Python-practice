def findDisappearedNumbers(nums):
    # Mark numbers that appear
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    
    # Collect numbers that never appeared
    result = [i + 1 for i in range(len(nums)) if nums[i] > 0]
    return result

nums = [4,3,2,7,8,2,3,1]
print("Input:", nums)
print("Missing Numbers:", findDisappearedNumbers(nums.copy()))

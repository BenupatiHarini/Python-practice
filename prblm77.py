def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        # left half sorted
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:  # right half sorted
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
nums1 = [4,5,6,7,0,1,2]
target1 = 0
print("Input: nums = [4,5,6,7,0,1,2], target = 0")
print("Output:", search(nums1, target1))  # expected 4

nums2 = [4,5,6,7,0,1,2]
target2 = 3
print("\nInput: nums = [4,5,6,7,0,1,2], target = 3")
print("Output:", search(nums2, target2))  # expected -1

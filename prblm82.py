def containsNearbyDuplicate(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False
nums = [1, 2, 3, 1]
k = 3
result = containsNearbyDuplicate(nums, k)
print("Input:", nums, "k =", k)
print("Contains nearby duplicate?", result)

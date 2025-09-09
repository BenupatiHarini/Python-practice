from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res

        start = nums[0]

        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == nums[i - 1] + 1:
                continue  # still in range
            else:
                end = nums[i - 1]
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                if i < len(nums):
                    start = nums[i]

        return res


# 🔹 Example run
nums = [0, 1, 2, 4, 5, 7]
print("Input:", nums)
print("Output:", Solution().summaryRanges(nums))

nums2 = [0, 2, 3, 4, 6, 8, 9]
print("\nInput:", nums2)
print("Output:", Solution().summaryRanges(nums2))

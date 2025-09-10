class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Example Run
nums = [3, 0, 1]
sol = Solution()
print("Missing number:", sol.missingNumber(nums))  # Output: 2

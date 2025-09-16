class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

if __name__ == "__main__":
    nums = [2, 2, 1, 1, 3, 3, 3]
    sol = Solution()
    print("Majority Element:", sol.majorityElement(nums))

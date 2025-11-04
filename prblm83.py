class Solution:
    def thirdMax(self, nums):
        distinct = sorted(list(set(nums)), reverse=True)
        if len(distinct) < 3:
            return distinct[0]
        else:
            return distinct[2]
nums = [2, 2, 3, 1]
obj = Solution()
result = obj.thirdMax(nums)
print("The third maximum number is:", result)

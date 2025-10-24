from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n
        path = []

        def backtrack():
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    sol = Solution()
    permutations = sol.permute(nums)
    print("Input:", nums)
    print("Number of permutations:", len(permutations))
    for i, p in enumerate(permutations, 1):
        print(f"Permutation {i}:", p)

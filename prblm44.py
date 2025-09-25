class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1

# Example test cases
sol = Solution()
print(sol.isUgly(6))   # ✅ Output: True (6 = 2 × 3)
print(sol.isUgly(14))  # ❌ Output: False (14 has factor 7)
print(sol.isUgly(1))   # ✅ Output: True (by definition)

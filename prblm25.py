class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1   # adjust for 1-based indexing
            result = chr((columnNumber % 26) + ord('A')) + result
            columnNumber //= 26
        return result
sol = Solution()
print(sol.convertToTitle(1))   # A
print(sol.convertToTitle(28))  # AB
print(sol.convertToTitle(701)) # ZY

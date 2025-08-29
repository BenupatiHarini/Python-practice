class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            # build the next row using previous row
            row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
        return row
sol = Solution()
print(sol.getRow(3))  # Output: [1, 3, 3, 1]
print(sol.getRow(5))  # Output: [1, 5, 10, 10, 5, 1]

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        curRow, step = 0, -1
        
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                step *= -1
            curRow += step
        
        return "".join(rows)
s = "PAYPALISHIRING"
numRows = 3
solution = Solution()
result = solution.convert(s, numRows)
print("Input:", s)
print("Number of Rows:", numRows)
print("Zigzag Conversion Output:", result)

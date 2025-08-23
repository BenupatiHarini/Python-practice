class Solution:
    def generate(self, numRows: int):
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)   # create a row of size (i+1), filled with 1s
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle

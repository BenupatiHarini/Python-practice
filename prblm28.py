class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
        return result


# 🔹 Example test
if __name__ == "__main__":
    solution = Solution()
    print(solution.titleToNumber("A"))   # Output: 1
    print(solution.titleToNumber("Z"))   # Output: 26
    print(solution.titleToNumber("AA"))  # Output: 27
    print(solution.titleToNumber("AB"))  # Output: 28
    print(solution.titleToNumber("ZY"))  # Output: 701

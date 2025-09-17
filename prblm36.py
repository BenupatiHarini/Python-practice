from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + [0] * len(digits)


# Example test run
if __name__ == "__main__":
    sol = Solution()
    digits = [8, 9, 9]   # Example input
    result = sol.plusOne(digits)
    print("Input:", [9, 9, 9])
    print("Output:", result)

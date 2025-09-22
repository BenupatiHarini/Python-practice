class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Use unsigned 32-bit representation
        num &= 0xFFFFFFFF  
        
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            digit = num & 15  # num % 16
            result.append(hex_chars[digit])
            num >>= 4  # divide by 16
        
        return "".join(reversed(result))


# Driver code with output statements
if __name__ == "__main__":
    sol = Solution()
    
    print("Input: 26  → Output:", sol.toHex(26))     # Expected "1a"
    print("Input: -1  → Output:", sol.toHex(-1))     # Expected "ffffffff"
    print("Input: 0   → Output:", sol.toHex(0))      # Expected "0"
    print("Input: 255 → Output:", sol.toHex(255))    # Expected "ff"
    print("Input: -26 → Output:", sol.toHex(-26))    # Expected "ffffffe6"

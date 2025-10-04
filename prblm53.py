class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        length = 0
        has_odd = False
        for cnt in counts.values():
            if cnt % 2 == 0:
                length += cnt
            else:
                length += cnt - 1
                has_odd = True
        return length + (1 if has_odd else 0)
if __name__ == "__main__":
    s = "abccccdd"
    print("Input:", s)
    res = Solution().longestPalindrome(s)
    print("Longest palindrome length:", res)  # Expected output: 7

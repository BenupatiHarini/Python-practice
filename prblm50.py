class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start, max_len = 0, 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)      # odd length
            expand(i, i + 1)  # even length

        return s[start:start + max_len]

s = "babad"
sol = Solution()
print("Input:", s)
print("Longest Palindromic Substring:", sol.longestPalindrome(s))

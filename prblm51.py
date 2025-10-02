class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()

    print(sol.strStr("sadbutsad", "sad"))   # Output: 0
    print(sol.strStr("leetcode", "leeto"))  # Output: -1
    print(sol.strStr("hello", "ll"))        # Output: 2
    print(sol.strStr("aaaaa", "bba"))       # Output: -1
    print(sol.strStr("abc", ""))            # Output: 0

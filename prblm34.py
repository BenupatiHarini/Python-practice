from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, freq in ransom_count.items():
            if magazine_count[char] < freq:
                return False
        return True


# Testing
sol = Solution()

print(sol.canConstruct("a", "b"))        # False
print(sol.canConstruct("aa", "ab"))      # False
print(sol.canConstruct("aa", "aab"))     # True
print(sol.canConstruct("abc", "cbaabc")) # True
print(sol.canConstruct("abcd", "abc"))   # False

def firstUniqChar(s: str) -> int:
    # Count frequency of each character
    from collections import Counter
    count = Counter(s)
    
    # Find the first character with frequency 1
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1


# Example test cases
print(firstUniqChar("leetcode"))      # Output: 0
print(firstUniqChar("loveleetcode"))  # Output: 2
print(firstUniqChar("aabb"))          # Output: -1

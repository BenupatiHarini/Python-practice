# LeetCode Problem 3: Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    start = max_len = 0

    for end, c in enumerate(s):
        if c in char_index and char_index[c] >= start:
            start = char_index[c] + 1
        char_index[c] = end
        max_len = max(max_len, end - start + 1)
    return max_len

s = "abcabcbb"
print("Input:", s)
print("Output:", lengthOfLongestSubstring(s))

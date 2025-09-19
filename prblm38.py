from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    # Start with the first word as the prefix
    prefix = strs[0]
    
    # Compare with each word
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # shrink prefix
            if not prefix:
                return ""
    return prefix


# 🔹 Test Cases
print(longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
print(longestCommonPrefix(["interspecies","interstellar","interstate"]))  # Output: "inters"
print(longestCommonPrefix(["throne","throne"]))         # Output: "throne"
print(longestCommonPrefix([""]))                        # Output: ""

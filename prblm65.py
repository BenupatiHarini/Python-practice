def isSubsequence(s: str, t: str) -> bool:
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

tests = [
    ("abc", "ahbgdc"),
    ("axc", "ahbgdc"),
]

for s, t in tests:
    print(f'Input: s = "{s}", t = "{t}"')
    print("Output:", "true" if isSubsequence(s, t) else "false")
    print()

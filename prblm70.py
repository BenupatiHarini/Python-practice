def countAndSay(n: int) -> str:
    if n <= 0:
        return ""
    s = "1"
    for _ in range(2, n + 1):
        i = 0
        next_s = []
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            count = j - i
            next_s.append(str(count))
            next_s.append(s[i])
            i = j
        s = "".join(next_s)
    return s

for n in range(1, 7):
    print(f"n = {n} -> {countAndSay(n)}")

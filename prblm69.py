def countAndSay(n: int) -> str:
    if n <= 0:
        return ""
    s = "1"
    for _ in range(n - 1):
        i = 0
        nxt = []
        while i < len(s):
            ch = s[i]
            cnt = 0
            while i < len(s) and s[i] == ch:
                cnt += 1
                i += 1
            nxt.append(str(cnt))
            nxt.append(ch)
        s = "".join(nxt)
    return s
if __name__ == "__main__":
    samples = [1, 2, 3, 4, 5, 6]
    for n in samples:
        print(f"Input: {n}")
        print("Output:", countAndSay(n))
        print()

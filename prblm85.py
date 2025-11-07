def findContentChildren(g, s):
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1
    return i

g = [1, 2, 3]
s = [1, 1]

result = findContentChildren(g, s)
print("Maximum number of content children:", result)

def reverseString(s):
    s = list(s)   # convert string to list since strings are immutable
    lp = 0
    rp = len(s) - 1
    
    while lp < rp:
        s[lp], s[rp] = s[rp], s[lp]
        lp += 1
        rp -= 1
    
    return "".join(s)   # convert back to string
print(reverseString("hello"))   # Output: "olleh"
print(reverseString("Python"))  # Output: "nohtyP"

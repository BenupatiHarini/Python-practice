def myAtoi(s: str) -> int:
    s = s.lstrip()  # Step 1: Remove leading spaces
    if not s:
        return 0

    sign = 1
    i = 0
    if s[0] in ['-', '+']:
        if s[0] == '-':
            sign = -1
        i += 1

    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    result *= sign

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result

inputs = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]
for inp in inputs:
    print(f'Input: "{inp}" → Output: {myAtoi(inp)}')

def reverse(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    rev = 0
    sign = 1 if x > 0 else -1
    x = abs(x)

    while x != 0:
        digit = x % 10
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
            return 0
        rev = rev * 10 + digit
        x //= 10

    return sign * rev
print(reverse(123))     # Output: 321
print(reverse(-456))    # Output: -654
print(reverse(1534236469))  # Output: 0 (overflow)

def checkPerfectNumber(num: int) -> bool:
    if num <= 1:
        return False  # 1 is not a perfect number

    total = 1  # 1 is always a divisor
    i = 2
    while i * i <= num:
        if num % i == 0:
            total += i
            if i != num // i:  # avoid adding sqrt twice
                total += num // i
        i += 1
    return total == num


# Example usage:
print(checkPerfectNumber(28))  # True (28 is perfect)
print(checkPerfectNumber(12))  # False

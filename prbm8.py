def number_of_steps(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        count += 1
    return count
print(number_of_steps(14))  # Output: 6
print(number_of_steps(8))   # Output: 4
print(number_of_steps(123)) # Output: 12

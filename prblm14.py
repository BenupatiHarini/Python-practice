def is_power_of_three(n):
    # 3^19 = 1162261467, largest power of 3 in 32-bit signed int
    return n > 0 and 1162261467 % n == 0

# Example usage
print(is_power_of_three(27))   # True
print(is_power_of_three(28))   # False

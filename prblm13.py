def is_power_of_four(n):
    return (n > 0) and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

# Example usage
num = int(input("Enter a number: "))
if is_power_of_four(num):
    print(f"{num} is a power of 4.")
else:
    print(f"{num} is NOT a power of 4.")

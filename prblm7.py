def climb_stairs(n: int) -> int:
    # Handle small values directly
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev1 = 1  # ways to reach stair 1
    prev2 = 2  # ways to reach stair 2

    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev1, prev2 = prev2, curr

    return prev2


def main():
    try:
        n = int(input("Enter number of stairs (n): ").strip())
    except ValueError:
        print("Please enter a valid integer.")
        return

    ways = climb_stairs(n)
    print(f"Number of distinct ways to climb {n} stairs: {ways}")


if __name__ == "__main__":
    main()

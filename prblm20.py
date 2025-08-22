def moveZeroes(nums):
    lastNonZeroFoundAt = 0  # position to place the next non-zero element

    for current in range(len(nums)):
        if nums[current] != 0:
            # Swap nums[current] and nums[lastNonZeroFoundAt]
            nums[lastNonZeroFoundAt], nums[current] = nums[current], nums[lastNonZeroFoundAt]
            lastNonZeroFoundAt += 1

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

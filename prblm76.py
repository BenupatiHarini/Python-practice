from itertools import permutations

def permuteUnique(nums):
    # Use set to remove duplicate permutations
    return list(set(permutations(nums)))

# Example input
nums = [1, 1, 2]
result = permuteUnique(nums)

# Convert tuples to lists for neat output
result = [list(p) for p in result]
print("Unique Permutations are:", result)

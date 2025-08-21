def rotate(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    
    k = k % n  # Handle k > n

    # Helper function to reverse part of the list
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the whole list
    reverse(0, n - 1)

    # Step 2: Reverse the first k elements
    reverse(0, k - 1)

    # Step 3: Reverse the remaining elements
    reverse(k, n - 1)

    return nums
print(rotate([1,2,3,4,5,6,7], 3))
# Output: [5, 6, 7, 1, 2, 3, 4]

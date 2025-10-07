def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate area
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_area = max(max_area, area)

        # Move the pointer that limits height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
print("Heights:", height)
print("Maximum water area:", maxArea(height))

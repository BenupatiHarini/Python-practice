# Run: python3 median.py

def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    total = m + n
    mid = total // 2
    i = j = count = 0
    prev = curr = 0

    while count <= mid:
        prev = curr
        if i < m and (j >= n or nums1[i] <= nums2[j]):
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1
        count += 1

    if total % 2 == 1:
        return float(curr)
    else:
        return (prev + curr) / 2.0

a1 = [1, 3]
b1 = [2]
print("Example 1 arrays:", a1, "and", b1)
print("Median:", findMedianSortedArrays(a1, b1))  # expected 2.0
print()


a2 = [1, 2]
b2 = [3, 4]
print("Example 2 arrays:", a2, "and", b2)
print("Median:", findMedianSortedArrays(a2, b2))  # expected 2.5

class Solution:
    def intersection(self, nums1, nums2):
        # Approach 1: Using sets
        return list(set(nums1) & set(nums2))
def intersection_set(nums1, nums2):
    """
    Approach 1: Using Python sets
    """
    return list(set(nums1) & set(nums2))


def intersection_hash(nums1, nums2):
    """
    Approach 2: Manual HashSet implementation
    """
    seen = set(nums1)
    result = set()
    for num in nums2:
        if num in seen:
            result.add(num)
    return list(result)


def intersection_two_pointer(nums1, nums2):
    """
    Approach 3: Two-pointer method (after sorting)
    Useful when arrays are large and memory is tight.
    """
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    result = set()
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    
    return list(result)


# --------------------------
# Test
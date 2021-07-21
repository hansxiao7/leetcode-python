class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = (len(nums1) + len(nums2) + 1) // 2

        left1 = 0
        right1 = len(nums1) - 1
        left2 = 0
        right2 = len(nums2) - 1

        if (len(nums1) + len(nums2)) % 2 == 0:
            return (helper(nums1, nums2, left1, right1, left2, right2, k) + helper(nums1, nums2, left1, right1, left2,
                                                                                   right2, k + 1)) / 2.
        else:
            return helper(nums1, nums2, left1, right1, left2, right2, k)


def helper(nums1, nums2, left1, right1, left2, right2, k):
    if left1 > right1:
        return nums2[left2 + k - 1]
    if left2 > right2:
        return nums1[left1 + k - 1]

    if k == 1:
        if nums1[left1] < nums2[left2]:
            return nums1[left1]
        else:
            return nums2[left2]

    mid1 = (left1 + right1) // 2
    mid2 = (left2 + right2) // 2

    length = mid1 - left1 + mid2 - left2
    diff = k - (length + 1)

    if nums1[mid1] > nums2[mid2]:
        if diff > 0:
            result = helper(nums1, nums2, left1, right1, mid2 + 1, right2, k - (mid2 - left2 + 1))
        else:
            result = helper(nums1, nums2, left1, mid1 - 1, left2, right2, k)
    else:
        if diff > 0:
            result = helper(nums1, nums2, mid1 + 1, right1, left2, right2, k - (mid1 - left1 + 1))
        else:
            result = helper(nums1, nums2, left1, right1, left2, mid2 - 1, k)

    return result
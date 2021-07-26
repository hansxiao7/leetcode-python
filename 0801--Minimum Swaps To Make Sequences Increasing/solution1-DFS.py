class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # 1. DFS
        # 2. DP with state machines
        return helper(nums1, nums2, 0, 0)


def helper(nums1, nums2, i, result):
    if i == len(nums1):
        return result

    if i == 0 or (nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]):  # no need to swap
        temp1 = helper(nums1, nums2, i + 1, result)
    else:
        temp1 = sys.maxint

    if i == 0 or (nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]):  # swap the ith element or the i+1 th element
        # swap the (i+1)th element
        nums1[i], nums2[i] = nums2[i], nums1[i]
        temp2 = helper(nums1, nums2, i + 1, result + 1)
        nums1[i], nums2[i] = nums2[i], nums1[i]
    else:
        temp2 = sys.maxint

    result = min(temp1, temp2)

    return result
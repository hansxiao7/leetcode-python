class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        left = 0
        result = 0
        for right in range(len(nums2)):

            while left < len(nums1) and left < right and nums2[right] < nums1[left]:
                left += 1

            if left < len(nums1) and nums2[right] >= nums1[left]:
                result = max(result, right - left)

        return result
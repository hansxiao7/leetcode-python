class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        # set 2 pointers
        i = 0
        j = 0

        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if len(result) == 0 or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1
        return result
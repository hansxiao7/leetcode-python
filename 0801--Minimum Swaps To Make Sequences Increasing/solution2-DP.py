class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # 1. DFS
        # 2. DP with state machines
        prevSwap = 1
        prevKeep = 0

        for i in range(1, len(nums1)):
            keep = sys.maxint
            swap = sys.maxint

            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                keep = prevKeep
                swap = prevSwap + 1

            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                keep = min(keep, prevSwap)
                swap = min(swap, prevKeep + 1)

            prevSwap = swap
            prevKeep = keep

        return min(keep, swap)



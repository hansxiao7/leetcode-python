class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # binary search
        left = 0
        right = len(nums1)

        def check_val(l):
            set1 = set()

            for i in range(l, len(nums1) + 1):
                set1.add(tuple(nums1[i - l:i]))

            for i in range(l, len(nums2) + 1):
                if tuple(nums2[i - l:i]) in set1:
                    # l too small
                    return True
            # l too larget
            return False

        while left < right:
            mid = (left + right) // 2
            if check_val(mid):
                left = mid + 1
            else:
                right = mid

        if check_val(left):
            return left
        return left - 1
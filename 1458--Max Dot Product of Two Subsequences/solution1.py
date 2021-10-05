class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        res = -sys.maxint

        m = len(nums1)
        n = len(nums2)

        cache = {}

        def helper(i, j, flag):
            if (i, j, flag) in cache:
                return cache[(i, j, flag)]
            if i >= m or j >= n:
                if flag == 0:
                    return -sys.maxint
                return 0

            if flag == 0:
                res = max(nums1[i] * nums2[j] + helper(i + 1, j + 1, 1), helper(i + 1, j, 0), helper(i, j + 1, 0))
            else:
                res = max(nums1[i] * nums2[j] + helper(i + 1, j + 1, 1), helper(i + 1, j, 1), helper(i, j + 1, 1))
            cache[(i, j, flag)] = res
            return res

        return helper(0, 0, 0)
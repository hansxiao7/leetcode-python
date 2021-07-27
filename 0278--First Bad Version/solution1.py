# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        return binary_search(0, n - 1, sys.maxint) + 1


def binary_search(left, right, rmin):
    if left < right:
        mid = (left + right) // 2
        mid_r = isBadVersion(mid + 1)
        if mid_r:
            rmin = min(mid, rmin)
            rmin = binary_search(left, mid - 1, rmin)
        else:
            rmin = binary_search(mid + 1, right, rmin)
    elif left == right:
        if isBadVersion(left + 1):
            rmin = min(rmin, left)
    return rmin
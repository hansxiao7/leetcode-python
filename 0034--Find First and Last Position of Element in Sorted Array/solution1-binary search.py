class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rmax, rmin = binary_search(nums, target, 0, len(nums) - 1, -sys.maxint, sys.maxint)
        if rmin == sys.maxint:
            return [-1, -1]
        else:
            return [rmin, rmax]


def binary_search(li, target, left, right, rmax, rmin):
    if left < right:
        mid = (left + right) // 2
        if li[mid] > target:
            rmax, rmin = binary_search(li, target, left, mid, rmax, rmin)
        elif li[mid] < target:
            rmax, rmin = binary_search(li, target, mid + 1, right, rmax, rmin)
        else:  # li[mid] == target
            rmin = min(rmin, mid)
            rmax = max(rmax, mid)
            rmax, rmin = binary_search(li, target, left, mid - 1, rmax, rmin)
            rmax, rmin = binary_search(li, target, mid + 1, right, rmax, rmin)
    elif left == right:
        if li[left] == target:
            rmin = min(rmin, left)
            rmax = max(rmax, left)
    return rmax, rmin
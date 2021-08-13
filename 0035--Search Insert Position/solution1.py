class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return binary_search(nums, 0, len(nums) - 1, target)


def binary_search(li, left, right, target):
    if left < right:
        mid = (left + right) // 2
        if li[mid] > target:
            return binary_search(li, left, mid, target)
        elif li[mid] < target:
            return binary_search(li, mid + 1, right, target)
        else:
            return mid
    else:
        if li[left] < target:
            return left + 1
        else:
            return left
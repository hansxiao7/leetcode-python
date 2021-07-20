class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        return helper(nums, left, right, target)


def helper(li, left, right, target):
    while left < right:
        mid = (left + right) // 2
        if li[mid] < target:
            return helper(li, mid + 1, right, target)
        elif li[mid] > target:
            return helper(li, left, mid, target)
        else:
            return mid

    if left == right:
        if li[left] == target:
            return left
        else:
            return -1


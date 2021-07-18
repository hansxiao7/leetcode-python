class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two-sum with sorted array
        li = []
        for i in range(len(nums)):
            li.append([nums[i], i])

        li.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            if li[left][0] + li[right][0] < target:
                left += 1
            elif li[left][0] + li[right][0] > target:
                right -= 1
            else:
                return [li[left][1], li[right][1]]

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}

        prev = 0
        n = 0

        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
            if counts[nums[i]] > 2:
                prev -= 1
            else:
                n += 1
            nums[prev] = nums[i]
            prev += 1

        return n
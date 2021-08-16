class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = {}

        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
            if counts[nums[i]] > 1:
                return True

        return False
class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        for i in range(1, len(prefix)):
            if prefix[-1] + nums[i - 1] == 2 * prefix[i]:
                return i - 1

        return -1
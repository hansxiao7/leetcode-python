class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prev_rob = 0
        prev_not_rob = 0

        for i in range(n):
            rob = prev_not_rob + nums[i]
            not_rob = max(prev_not_rob, prev_rob)

            prev_rob = rob
            prev_not_rob = not_rob

        return max(rob, not_rob)
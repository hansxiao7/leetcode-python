class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0

        n = len(nums)

        # rob first house
        rob_prev = 0
        not_rob_prev = 0

        for i in range(n - 1):
            rob = not_rob_prev + nums[i]
            not_rob = max(rob_prev, not_rob_prev)

            rob_prev = rob
            not_rob_prev = not_rob

        result1 = max(rob, not_rob)

        # not rob the first house
        rob_prev = 0
        not_rob_prev = 0

        for i in range(1, n):
            rob = not_rob_prev + nums[i]
            not_rob = max(rob_prev, not_rob_prev)

            rob_prev = rob
            not_rob_prev = not_rob

        result2 = max(rob, not_rob)

        return max(result1, result2)
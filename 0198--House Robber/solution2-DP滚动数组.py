class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rob or not rob, it is a question
        n = len(nums)
        rob = [0 for _ in range(n + 1)]

        rob[1] = nums[0]

        for i in range(2, n + 1):
            rob[i] = max(rob[i - 2] + nums[i - 1], rob[i - 1])

        return rob[n]
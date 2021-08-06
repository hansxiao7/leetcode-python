class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        last_pos = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i

        if last_pos == 0:
            return True
        return False
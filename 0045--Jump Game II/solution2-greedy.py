class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = 0
        currEnd = 0
        res = 0
        for i in range(len(nums) - 1):
            if i <= currMax:
                currMax = max(currMax, i + nums[i])

            if i == currEnd:
                res += 1
                currEnd = currMax

        return res
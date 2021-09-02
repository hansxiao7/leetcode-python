class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = 0
        res = 0

        for i in range(len(nums)):
            temp = 0
            while visited & (1 << i) == 0:
                visited |= 1 << i
                i = nums[i]
                temp += 1

            res = max(temp, res)

        return res
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = set()

        def helper(pos, curr):
            if pos == len(nums):
                if len(curr) >= 2:
                    self.res.add(tuple(curr))

                return

            helper(pos + 1, curr)
            if len(curr) == 0 or nums[pos] >= curr[-1]:
                helper(pos + 1, curr + [nums[pos]])

        helper(0, [])
        return self.res
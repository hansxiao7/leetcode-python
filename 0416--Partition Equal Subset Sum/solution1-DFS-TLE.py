class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # DFS
        total = sum(nums)

        def dfs(pos, li, curr):
            if curr == total / 2.:
                return True

            if curr > total / 2.:
                return False

            for i in range(pos, len(li)):
                temp = dfs(i + 1, li, curr + li[i])
                if temp:
                    return True

            return False

        return dfs(0, nums, 0)
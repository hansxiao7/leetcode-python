class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(pairs)

        def helper(curr):
            if dp[curr] != 0:
                return dp[curr]

            res = 1
            for i in range(len(pairs)):
                if pairs[curr][1] < pairs[i][0]:
                    res = max(res, 1 + helper(i))

            dp[curr] = res

            return res

        res = 1
        for i in range(len(pairs)):
            res = max(res, helper(i))

        return res



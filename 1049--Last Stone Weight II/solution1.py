class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        nums = stones
        n = len(stones)

        dp = [[0 for _ in range(3001)] for _ in range(n)]

        dp[0][nums[0] + 1500] += 1
        dp[0][-nums[0] + 1500] += 1

        for i in range(1, n):
            for total in range(-1000, 1001):
                j = total + 1500
                if dp[i - 1][j] != 0:
                    dp[i][j - nums[i]] += dp[i - 1][j]
                    dp[i][j + nums[i]] += dp[i - 1][j]

        for total in range(0, 1001):
            j = total + 1500
            if dp[n - 1][j] != 0:
                return total
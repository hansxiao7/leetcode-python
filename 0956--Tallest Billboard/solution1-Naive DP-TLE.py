class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        maxH = sum(rods) // 2

        n = len(rods)
        dp = [[[False for _ in range(maxH + 1)] for _ in range(maxH + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0][0] = True
        result = 0
        for i in range(1, n + 1):
            h = rods[i - 1]
            for l in range(maxH + 1):
                for r in range(maxH + 1):
                    dp[i][l][r] = dp[i - 1][l][r]

                    if l >= h:
                        dp[i][l][r] = dp[i][l][r] or dp[i - 1][l - h][r]
                    if r >= h:
                        dp[i][l][r] = dp[i][l][r] or dp[i - 1][l][r - h]

                    if l == r and dp[i][l][r]:
                        result = max(result, l)

        return result
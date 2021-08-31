class Solution(object):
    def cheapestJump(self, coins, maxJump):
        """
        :type coins: List[int]
        :type maxJump: int
        :rtype: List[int]
        """
        n = len(coins)
        dp = [[[], sys.maxint] for _ in range(n)]

        dp[0] = [[1], 0]  # path, pay

        for i in range(1, n):
            if coins[i] == -1:
                continue
            for j in range(i - 1, max(0, i - maxJump) - 1, -1):
                if coins[j] == -1:
                    continue
                if dp[j][1] + coins[i] < dp[i][1]:
                    dp[i][0] = dp[j][0] + [i + 1]
                    dp[i][1] = dp[j][1] + coins[i]
                elif dp[j][1] + coins[i] == dp[i][1]:
                    x = dp[j][0] + [i + 1]
                    y = dp[i][0]

                    if compare(x, y) == -1:
                        dp[i][0] = x

        return dp[n - 1][0]


def compare(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] == y[i]:
            continue
        else:
            if x[i] < y[i]:
                return -1
            else:
                return 1

    if len(x) < len(y):
        return -1
    else:
        return 1
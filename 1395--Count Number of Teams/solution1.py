class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        dp1 = [[0 for _ in range(4)] for _ in range(n + 1)]
        dp2 = [[0 for _ in range(4)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp1[i][1] = 1
            dp2[i][1] = 1

        for i in range(1, n + 1):
            for j in range(2, 4):
                for k in range(i - 1, 0, -1):
                    if rating[i - 1] > rating[k - 1]:
                        dp1[i][j] += dp1[k][j - 1]
                    if rating[i - 1] < rating[k - 1]:
                        dp2[i][j] += dp2[k][j - 1]

        res = 0

        for i in range(1, n + 1):
            res += dp1[i][3]
            res += dp2[i][3]

        return res
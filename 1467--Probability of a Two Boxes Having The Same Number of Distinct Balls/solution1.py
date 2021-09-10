class Solution(object):
    def getProbability(self, balls):
        """
        :type balls: List[int]
        :rtype: float
        """
        totalValue = sum(balls)
        factorial = [0] * (totalValue + 1)
        factorial[0] = factorial[1] = 1

        for i in range(2, totalValue + 1):
            factorial[i] = factorial[i - 1] * i

        def cnk(n, k):
            return factorial[n] / (factorial[n - k] * factorial[k])

        def helper(color1, color2, sum1, sum2, pos):
            if pos == len(balls):
                if color1 == color2 and sum1 == sum2:
                    return 1
                else:
                    return 0

            res = 0
            res += helper(color1 + 1, color2, sum1 + balls[pos], sum2, pos + 1)
            res += helper(color1, color2 + 1, sum1, sum2 + balls[pos], pos + 1)

            for i in range(1, balls[pos]):
                res += cnk(balls[pos], i) * helper(color1 + 1, color2 + 1, sum1 + i, sum2 + balls[pos] - i, pos + 1)

            return res

        temp = helper(0, 0, 0, 0, 0)

        total = cnk(totalValue, totalValue // 2)

        return temp / float(total)

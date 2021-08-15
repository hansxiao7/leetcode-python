class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = 1
        result = []
        while (1 + temp) * temp // 2 < n:
            result.append((1 + temp) * temp // 2)
            temp += 1

        if (1 + temp) * temp // 2 > n:
            for i in range(len(result)):
                if temp - result[i] < n:
                    temp -= i + 1
                    break
        return temp
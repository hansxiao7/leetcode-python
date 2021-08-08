class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        if len(stoneValue) <= 1:
            return 0

        n = len(stoneValue)
        sum_m = [0]

        for i in range(n):
            sum_m.append(stoneValue[i] + sum_m[-1])

        cache = [[0 for _ in range(n + 1)] for _ in range(n)]

        def helper(li, left, right):
            if left == right:
                return 0
            if cache[left][right] != 0:
                return cache[left][right]
            result = 0
            for i in range(left, right):  # choose a loc to divide
                # [left:i+1] [i+1:right+1]
                temp1 = sum_m[i + 1] - sum_m[left]
                temp2 = sum_m[right + 1] - sum_m[i + 1]
                if temp1 > temp2:
                    result = max(result, temp2 + helper(li, i + 1, right))
                elif temp1 < temp2:
                    result = max(result, temp1 + helper(li, left, i))
                else:
                    result = max(result, temp2 + helper(li, i + 1, right), temp1 + helper(li, left, i))
            cache[left][right] = result
            return result

        return helper(stoneValue, 0, len(stoneValue) - 1)
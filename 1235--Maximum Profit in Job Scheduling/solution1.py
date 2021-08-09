class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # dp[i] 第i个项目截止日期后的最大收益
        ends = []
        for i in range(len(endTime)):
            ends.append((endTime[i], startTime[i], profit[i]))

        ends.sort()

        n = len(ends)
        dp = [0 for _ in range(n + 1)]
        dp[1] = ends[0][2]
        dp[0] = 0

        for i in range(2, n + 1):
            temp = ends[i - 1][1]
            val = ends[i - 1][2]
            pos = binary_search(ends, temp, 0, n - 1)
            dp[i] = max(dp[i - 1], dp[pos + 1] + val)
        return dp[n]


def binary_search(ends, t, left, right):
    if left < right:
        mid = (left + right) // 2
        if ends[mid][0] > t:
            result = binary_search(ends, t, left, mid)
        elif ends[mid][0] <= t:
            result = binary_search(ends, t, mid + 1, right)
        return result
    else:
        if ends[left][0] > t:
            return left - 1
        return left


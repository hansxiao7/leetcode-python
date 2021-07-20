class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return helper(n)


def helper(n):
    if n == 1:
        return 1
    if n == 0:
        return 1

    result = 0

    for i in range(n // 2):  # use the ith as the top, the rest is n-1
        result += helper(i) * helper(n - 1 - i)

    if n % 2 != 0:
        result = result * 2 + helper(n // 2) ** 2
    else:
        result = 2 * result

    return result

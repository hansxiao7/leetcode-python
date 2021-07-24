class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        G = [[0 for _ in range(target)] for _ in range(d)]

        for i in range(0, target):
            if i < f:
                G[0][i] = 1

        for i in range(2, d + 1):  # d
            x = i - 1
            for j in range(1, target + 1):  # target
                y = j - 1
                for k in range(1, f + 1):
                    if k < j:
                        G[x][y] += G[x - 1][y - k]
                        # print(G)
        return G[d - 1][target - 1] % (10 ** 9 + 7)


def helper(d, f, target):
    if d == 1:
        if f >= target:
            return 1
        else:
            return 0

    result = 0
    for i in range(1, f + 1):
        if i < target:
            result += helper(d - 1, f, target - i)

    return result
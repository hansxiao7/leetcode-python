class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # brute force
        n = len(isConnected)
        visited = set()
        result = 0
        for i in range(n):
            if i not in visited:
                result += helper(i, isConnected, visited)

        return result


def helper(x, isConnected, visited):
    if x in visited:
        return 0
    n = len(isConnected)
    result = 1
    visited.add(x)
    for i in range(1, n):
        if isConnected[x][i] == 1 and i not in visited:
            result = helper(i, isConnected, visited)

    return result





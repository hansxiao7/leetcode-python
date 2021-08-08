class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger >= desiredTotal:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False

        visited = [0 for _ in range(maxChoosableInteger + 1)]
        cache = {}

        def helper(target):
            if tuple(visited) in cache:
                return cache[tuple(visited)]
            if target <= 0:
                return False

            for i in range(1, maxChoosableInteger + 1):
                if visited[i] == 0:
                    visited[i] = 1
                    temp = helper(target - i)
                    visited[i] = 0
                    if temp is False:
                        cache[tuple(visited)] = True
                        return True
            cache[tuple(visited)] = False
            return False

        return helper(desiredTotal)
class Solution(object):
    def canWin(self, currentState):
        """
        :type currentState: str
        :rtype: bool
        """
        n = len(currentState)
        if n < 2:
            return False

        cache = {}

        def helper(curr):
            if curr in cache:
                return cache[curr]
            for i in range(len(curr) - 1):
                if curr[i] == curr[i + 1] and curr[i] == '+':
                    temp = helper(curr[:i] + '--' + curr[i + 2:])
                    if temp is False:
                        cache[curr] = True
                        return True
            cache[curr] = False
            return False

        return helper(currentState)
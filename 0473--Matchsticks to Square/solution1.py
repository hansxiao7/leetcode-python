class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if len(matchsticks) < 4:
            return False

        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        length = total // 4

        # bitmask visited
        visited = 0
        cache = {}

        def helper(n, curr, length, visited):
            if visited in cache:
                return cache[visited]

            if n == 0:
                return True

            if curr == 0:
                return helper(n - 1, length, length, visited)

            for i in range(len(matchsticks)):
                # check whether i is visited
                temp = 1 << i
                if temp & visited == 0:
                    if curr - matchsticks[i] >= 0:
                        visited |= 1 << i
                        temp = helper(n, curr - matchsticks[i], length, visited)
                        visited -= 1 << i

                        if temp:
                            cache[visited] = True
                            return True
            cache[visited] = False
            return False

        return helper(4, length, length, 0)
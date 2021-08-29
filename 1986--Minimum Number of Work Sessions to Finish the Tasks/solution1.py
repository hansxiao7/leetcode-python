class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        # dfs
        visited = 0
        cache = {}

        def helper(currTime, visited):
            if (currTime, visited) in cache:
                return cache[(currTime, visited)]
            if visited == (1 << len(tasks)) - 1:
                if currTime > 0:
                    return 1
                return 0

            result = sys.maxint
            for i in range(len(tasks)):
                if visited & 1 << i == 0:
                    visited |= 1 << i
                    if currTime + tasks[i] <= sessionTime:
                        result = min(result, helper(currTime + tasks[i], visited))
                    else:
                        result = min(result, 1 + helper(tasks[i], visited))

                    visited -= 1 << i

            cache[(currTime, visited)] = result
            return result

        return helper(0, 0)
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        self.result = sys.maxint

        def dfs(sticks, curr_val, visited):
            if len(visited) == len(sticks) - 1:
                for j in range(len(sticks)):
                    if j not in visited:
                        self.result = min(self.result, curr_val)
            n = len(sticks)

            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    temp = sticks[i]
                    for j in range(n):
                        if j not in visited:
                            sticks[j] += temp
                            dfs(sticks, curr_val + sticks[j], visited)
                            sticks[j] -= temp
                    visited.remove(i)

        visited = set()
        dfs(sticks, 0, visited)

        return self.result
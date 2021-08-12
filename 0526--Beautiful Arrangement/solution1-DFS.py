class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dfs brute force
        visited = set()

        self.result = 0

        def helper(curr):
            if curr == n:
                self.result += 1
                return

            for i in range(1, n + 1):
                if i not in visited and (i % (curr + 1) == 0 or (curr + 1) % i == 0):
                    visited.add(i)
                    helper(curr + 1)
                    visited.remove(i)

        helper(0)
        return self.result
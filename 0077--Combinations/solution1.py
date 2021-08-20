class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        visited = set()
        result = []

        def helper(pos, curr, k, n):
            if k == 0:
                result.append(list(curr))
                return

            for i in range(pos, n + 1):
                if i not in visited:
                    visited.add(i)
                    helper(i + 1, curr + [i], k - 1, n)
                    visited.remove(i)

        helper(1, [], k, n)
        return result
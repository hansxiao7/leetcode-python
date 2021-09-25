class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """

        cache = {}

        def helper(i, j, k):
            if i > j:
                return 0

            if (i, j, k) in cache:
                return cache[(i, j, k)]

            res = helper(i, j - 1, 0) + (k + 1) ** 2

            for p in range(i, j):
                if boxes[p] == boxes[j]:
                    res = max(res, helper(p + 1, j - 1, 0) + helper(i, p, k + 1))
            cache[(i, j, k)] = res
            return res

        return helper(0, len(boxes) - 1, 0)
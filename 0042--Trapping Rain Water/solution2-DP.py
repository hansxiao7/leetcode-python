class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # brute force
        # find the max to the left
        n = len(height)
        max_l = [0 for _ in range(n)]
        for i in range(1, n - 1):
            max_l[i] = max(max_l[i - 1], height[i - 1])

        max_r = [0 for _ in range(n)]

        for i in range(n - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], height[i + 1])

        result = 0

        for i in range(1, n - 1):
            temp = min(max_l[i], max_r[i]) - height[i]
            if temp > 0:
                result += temp

        return result

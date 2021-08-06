class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        cache = [[-sys.maxint for _ in range(len(stones))] for _ in range(len(stones))]

        def minmax(stones, left, right, remain):
            if cache[left][right] != -sys.maxint:
                return cache[left][right]
            if left == right:
                cache[left][right] = 0
                return 0

            result = -sys.maxint

            result = max(remain - stones[left] - minmax(stones, left + 1, right, remain - stones[left]),
                         remain - stones[right] - minmax(stones, left, right - 1, remain - stones[right]),
                         result)
            cache[left][right] = result
            return result

        return minmax(stones, 0, len(stones) - 1, total)
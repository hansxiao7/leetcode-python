class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        cache = {}

        def minmax(pos, m, piles):
            if cache.get((pos, m)):
                return cache[(pos, m)]
            if 2 * m >= len(piles) - pos:
                temp = sum(piles[pos:])
                cache[(pos, m)] = temp
                return temp

            temp = -sys.maxint
            for x in range(0, 2 * m):
                temp = max(sum(piles[pos:pos + x + 1]) - minmax(pos + x + 1, max(m, x + 1), piles), temp)
            cache[(pos, m)] = temp
            return temp

        diff = minmax(0, 1, piles)

        return (sum(piles) + diff) // 2
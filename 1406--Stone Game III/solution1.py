class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        cache = [None for _ in range(len(stoneValue))]

        def minmax(pos, li):
            if cache[pos] is not None:
                return cache[pos]
            temp = -sys.maxint
            for i in range(1, 4):
                if pos + i >= len(li):
                    temp = max(temp, sum(li[pos:]))
                else:
                    temp = max(temp, sum(li[pos:pos + i]) - minmax(pos + i, li))
            cache[pos] = temp
            return temp

        temp = minmax(0, stoneValue)

        if temp > 0:
            return 'Alice'
        elif temp < 0:
            return 'Bob'
        else:
            return 'Tie'
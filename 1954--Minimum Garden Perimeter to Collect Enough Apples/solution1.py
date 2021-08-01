class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        # DP
        if neededApples <= 12:
            return 8
        n = 12
        outlayer = 12
        x = 2

        while n < neededApples:
            outlayer += (x + 2) * 4 + (x + 1) * 4 + 4 * x
            n += outlayer
            x += 2

        return 4 * x
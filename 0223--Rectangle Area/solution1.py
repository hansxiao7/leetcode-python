class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        low_x = max(ax1, bx1)
        high_x = min(ax2, bx2)

        if low_x < high_x:
            x = high_x - low_x
        else:
            x = 0

        low_y = max(ay1, by1)
        high_y = min(ay2, by2)

        if low_y < high_y:
            y = high_y - low_y
        else:
            y = 0

        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - x * y
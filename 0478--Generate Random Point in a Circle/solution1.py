class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            dx = random.random() * 2 * self.r - self.r
            dy = random.random() * 2 * self.r - self.r

            if dx ** 2 + dy ** 2 <= self.r ** 2:
                return [self.x_center + dx, self.y_center + dy]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
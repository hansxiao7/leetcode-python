class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        water = 0
        while left < right:
            bar = min(height[left], height[right])
            water = max(water, (right - left) * bar)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return water



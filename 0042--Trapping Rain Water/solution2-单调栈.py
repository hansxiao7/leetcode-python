class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        for i in range(len(height)):
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                temp = height[stack.pop()]
                if len(stack) == 0:
                    continue
                h = min(height[i], height[stack[-1]])
                if temp < h:
                    result += (h - temp) * (i - stack[-1] - 1)

            stack.append(i)

        return result
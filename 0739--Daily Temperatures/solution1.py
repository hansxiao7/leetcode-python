class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        pos = {}

        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) != 0 and temperatures[i] >= stack[-1]:
                stack.pop()
            if len(stack) != 0:
                result[i] = pos[stack[-1]] - i
            stack.append(temperatures[i])
            pos[temperatures[i]] = i

        return result
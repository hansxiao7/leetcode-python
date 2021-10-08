"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""


class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        x = 1
        y = 1000

        f = customfunction.f
        res = []

        while x < y:
            if f(x, y) < z:
                x += 1
            elif f(x, y) > z:
                y -= 1
            else:
                res.append([x, y])
                x += 1
                y -= 1

        temp1 = x
        if f(x, x) == z:
            res.append([x, x])

        x = 1000
        y = 1

        while x > y:
            if f(x, y) < z:
                y += 1
            elif f(x, y) > z:
                x -= 1
            else:
                res.append([x, y])
                x -= 1
                y += 1
        if x != temp1 and f(x, x) == z:
            res.append([x, x])

        return res
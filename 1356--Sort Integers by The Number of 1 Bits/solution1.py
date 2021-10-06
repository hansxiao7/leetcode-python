class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        def helper(num):
            res = 0

            while num > 0:
                res += num % 2
                num = num // 2

            return res

        arr.sort(key=lambda x: (helper(x), x))

        return arr
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []

        def helper(x, n):
            if x > n:
                return

            result.append(x)
            helper(x * 10, n)

            if x % 10 != 9:
                helper(x + 1, n)

        helper(1, n)

        return result
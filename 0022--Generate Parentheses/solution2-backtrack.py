class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []

        def helper(left, right, curr):
            if left > right:
                return

            if left == 0:
                res.append(curr + ')' * right)
                return

            if left == right and left == 0:
                res.append(curr)
                return

            helper(left - 1, right, curr + '(')
            helper(left, right - 1, curr + ')')

        helper(n, n, '')

        return res
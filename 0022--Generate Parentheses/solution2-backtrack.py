class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        backtrack(result, '', 0, 0, n)
        return result


def backtrack(result, s, n_open, n_close, n):
    if n_open == n_close == n:
        result.append(s)
        return

    if n_open < n:
        backtrack(result, s + '(', n_open + 1, n_close, n)

    if n_close < n_open:
        backtrack(result, s + ')', n_open, n_close + 1, n)
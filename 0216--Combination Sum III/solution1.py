class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        curr = []
        helper(1, n, k, result, curr)
        return result


def helper(pos, target, k, result, curr):
    if k == 0:
        if target == 0:
            result.append(list(curr))
        return

    for i in range(pos, 10):
        curr.append(i)
        helper(i + 1, target - i, k - 1, result, curr)
        curr.pop()
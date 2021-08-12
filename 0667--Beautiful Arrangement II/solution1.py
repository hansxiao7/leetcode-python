class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = [i for i in range(1, n - k)]

        pos = True
        for i in range(k + 1):
            if i % 2 == 0:
                result.append(i // 2 + n - k)
            else:
                result.append(n - i // 2)

        return result
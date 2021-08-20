class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return str(0)

        result = []

        for i in range(len(num)):
            while len(result) != 0 and num[i] < result[-1] and k > 0:
                result.pop()
                k -= 1
            result.append(num[i])

        while k > 0:
            result.pop()
            k -= 1
        result = ''.join(result)
        while len(result) != 0 and result[0] == '0':
            result = result[1:]

        if result == '':
            return '0'
        return result
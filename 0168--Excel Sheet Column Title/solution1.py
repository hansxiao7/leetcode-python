class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = ''

        while columnNumber:
            columnNumber -= 1
            ans = chr(65 + columnNumber % 26) + ans
            columnNumber //= 26
        return ans

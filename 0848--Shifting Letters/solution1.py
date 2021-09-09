class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        prefix = [0] * len(s)
        prefix[-1] = shifts[-1]

        for i in range(len(prefix) - 2, -1, -1):
            prefix[i] = prefix[i + 1] + shifts[i]
        res = ''
        for i in range(len(s)):
            res = res + chr((ord(s[i]) - ord('a') + prefix[i]) % 26 + ord('a'))

        return res
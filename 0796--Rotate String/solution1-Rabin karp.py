class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # rabin karp
        pow = 31
        mod = 10 ** 6

        temp = 0
        for i in range(len(s)):
            temp = temp * pow + ord(s[i])
            temp = temp % mod

        target = 0
        for i in range(len(goal)):
            target = target * pow + ord(goal[i])
            target = target % mod

        for i in range(len(s)):
            temp = temp - (ord(s[i]) * pow ** (len(s) - 1)) % mod
            if temp < 0:
                temp += mod

            temp = temp * pow + ord(s[i])
            temp = temp % mod

            if temp == target:
                return True

        return False
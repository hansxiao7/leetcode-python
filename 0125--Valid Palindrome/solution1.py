class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = filter(str.isalnum, str(s))
        s = s.lower()

        mid = (len(s) - 1) // 2
        for i in range(mid + 1):
            if s[i] == s[len(s) - 1 - i]:
                continue
            else:
                return False

        return True
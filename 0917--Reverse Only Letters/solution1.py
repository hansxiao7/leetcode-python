class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1
        s = list(s)

        while left < right:
            while left < right and ord(s[left]) not in range(97, 123) and ord(s[left]) not in range(65, 91):
                left += 1

            while left < right and ord(s[right]) not in range(97, 123) and ord(s[right]) not in range(65, 91):
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)
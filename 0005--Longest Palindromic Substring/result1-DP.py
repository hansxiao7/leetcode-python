class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        result = s[0]
        for i in range(2 * n - 3):
            if i % 2 == 0:  # in the middle
                temp = ''
                left = i / 2
                right = left + 1

            else:
                mid = (i + 1) / 2
                temp = s[mid]
                left = mid - 1
                right = mid + 1

            while left >= 0 and right < n:
                if s[left] == s[right]:
                    temp = s[left] + temp + s[right]
                    left -= 1
                    right += 1
                else:
                    break

            if len(temp) > len(result):
                result = temp

        return result


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # brute force
        if len(s) < 2:
            return s

        # the center location
        n = len(s)

        max_length = 1
        last_right = 1

        for i in range((2 * n - 1) // 2):
            if i % 2 == 0:
                l = 0
                left = i / 2
                right = left + 1

            else:
                l = 1
                mid = (i + 1) / 2
                left = mid - 1
                right = mid + 1

            while left >= 0:
                if s[left] == s[right]:
                    l += 2
                    left -= 1
                    right += 1
                else:
                    l = 0
                    break

            if l > max_length:
                max_length = l
                last_right = right

        result = s

        for j in range(last_right, len(s)):
            result = s[j] + result

        return result
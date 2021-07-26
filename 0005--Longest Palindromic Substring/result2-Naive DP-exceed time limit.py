class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_l = 1
        result = [0, 0]
        G = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            G[i][i] = True

        for left in range(n - 2, -1, -1):
            for right in range(left + 1, n):
                G[left][right] = G[left + 1][right - 1] and (s[right] == s[left])
                if right == left + 1:
                    G[left][right] = s[right] == s[left]

                if G[left][right] and right - left + 1 > max_l:
                    max_l = right - left + 1
                    result = [left, right]
        return s[result[0]:result[1] + 1]



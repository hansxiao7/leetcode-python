class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)

        dp = [[[], False] for _ in range(n + 1)]
        word_set = set(wordDict)
        dp[0][1] = True

        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if s[j:i] in word_set:
                    if dp[j][1] is True:
                        if len(dp[j][0]) == 0:
                            dp[i][0].append(s[j:i])
                        else:
                            for k in range(len(dp[j][0])):
                                dp[i][0].append(dp[j][0][k] + ' ' + s[j:i])
                        dp[i][1] = True

        return dp[n][0]





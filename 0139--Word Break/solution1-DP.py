class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)

        n = len(s)
        f = [False for _ in range(n + 1)]
        f[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        print(f)
        return f[n]

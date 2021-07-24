class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # build the matrix; row is for
        G = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:  # the last element is same
                    G[i][j] = G[i - 1][j - 1] + 1
                elif text1[i - 1] != text2[j - 1]:
                    G[i][j] = max(G[i - 1][j], G[i][j - 1])

        return G[len(text1)][len(text2)]







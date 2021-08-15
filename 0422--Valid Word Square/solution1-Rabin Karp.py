class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        # rabin karp
        m = len(words)

        n = 0
        for i in range(len(words)):
            n = max(len(words[i]), n)

        row = []
        col = []

        pow = 31
        mod = 10 ** 6

        for i in range(m):
            temp = 0
            for j in range(len(words[i])):
                temp = temp * pow + ord(words[i][j])
                temp = temp % mod
            row.append(temp)

        for j in range(n):
            temp = 0
            i = 0
            while i < m and len(words[i]) > j:
                temp = temp * pow + ord(words[i][j])
                temp = temp % mod
                i += 1
            col.append(temp)

        for i in range(min(m, n)):
            if col[i] != row[i]:
                return False

        return True
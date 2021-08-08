class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # rabin karp
        pow = 31
        mod = 10 ** 6

        word_set = {}
        for word in words:
            temp = 0
            for i in range(len(word)):
                temp = temp * pow + ord(word[i])
                temp = temp % mod

            word_set[temp] = word_set.get(temp, 0) + 1

        n = len(words[0])

        s_li = []
        temp = 0
        for i in range(len(s)):
            if i >= n:
                temp = temp - ord(s[i - n]) * pow ** (n - 1)
            temp = temp * pow + ord(s[i])
            temp = temp % mod
            s_li.append(temp)

        result = []

        for i in range(len(s_li)):
            if word_set.get(s_li[i]) is not None:
                visited = {}
                visited[s_li[i]] = visited.get(s_li[i], 0) + 1
                count = 1
                pos = i + n

                while count < len(words) and pos < len(s_li):
                    if word_set.get(s_li[pos], 0) > visited.get(s_li[pos], 0):
                        visited[s_li[pos]] = visited.get(s_li[pos], 0) + 1
                        pos += n
                        count += 1
                    else:
                        break

                if count == len(words):
                    result.append(i - n + 1)

        return result
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = {}

        for c in words[0]:
            res[c] = res.get(c, 0) + 1

        for i in range(1, len(words)):
            word = words[i]
            temp = {}
            for c in word:
                if c in res:
                    temp[c] = temp.get(c, 0) + 1

            tempKeys = list(temp.keys())
            for key in temp:
                temp[key] = min(res[key], temp[key])

            res = temp

        result = ''
        for key in res:
            result += key * res[key]

        return result
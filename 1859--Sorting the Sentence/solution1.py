class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict1 = {}

        i = 0

        while i < len(s):
            start = i
            while i < len(s) and s[i] != ' ':
                i += 1
            dict1[int(s[i - 1])] = s[start:i - 1]
            i += 1

        result = ''
        for i in range(1, 11):
            if i not in dict1:
                result = result[:len(result) - 1]
                return result

            result = result + dict1[i] + ' '

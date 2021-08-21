class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sets = set()
        result = set()

        for i in range(10, len(s) + 1):
            temp = s[i - 10:i]
            if temp in sets:
                if temp not in result:
                    result.add(temp)

            sets.add(temp)

        return result
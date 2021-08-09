class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return [[strs[0]]]

        dict1 = {}
        for i in range(len(strs)):
            word = strs[i]
            temp = [0 for _ in range(26)]
            for j in range(len(word)):
                temp[ord(word[j]) - ord('a')] += 1

            temp = tuple(temp)
            if temp not in dict1:
                dict1[temp] = []
            dict1[temp].append(strs[i])

        return dict1.values()
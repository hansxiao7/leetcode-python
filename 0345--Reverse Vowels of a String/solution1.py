class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = []
        vowels = set()
        vowels.update(['a', 'A', 'e', 'E', 'I', 'i', 'o', 'O', 'u', 'U'])

        for i in range(len(s)):
            if s[i] in vowels:
                temp.append(i)
        s = list(s)
        for i in range(len(temp) // 2):
            s[temp[i]], s[temp[len(temp) - 1 - i]] = s[temp[len(temp) - 1 - i]], s[temp[i]]

        return ''.join(s)


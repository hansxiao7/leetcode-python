class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        # Rabin Karp
        pow = 31
        mod = 10 ** 6

        target = 0
        for i in range(len(s)):
            target = target * pow + ord(s[i])
            target = target % mod

        word_set = set()
        temp = 0
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)):
                temp = temp * pow + ord(word[j])
                temp = temp % mod
            word_set.add(temp)

        if target in word_set:
            return True
        return False

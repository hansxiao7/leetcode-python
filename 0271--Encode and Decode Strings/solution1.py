class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for i in range(len(strs)):
            c = strs[i]
            if i != len(strs) - 1:
                res += c + unichr(257)
            else:
                res += c

        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s == '':
            return ['']
        res = []
        pos = 0
        temp = ''
        while pos < len(s):
            if s[pos] == unichr(257):
                res.append(temp)
                temp = ''
                pos += 1
                continue

            temp += s[pos]
            pos += 1

        res.append(temp)

        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
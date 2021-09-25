class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        pos = 0
        res = ''
        while pos < len(chars):
            c = chars[pos]
            count = 1
            while pos + 1 < len(chars) and chars[pos + 1] == c:
                count += 1
                pos += 1

            res += c
            if count > 1:
                res += str(count)

            pos += 1

        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)
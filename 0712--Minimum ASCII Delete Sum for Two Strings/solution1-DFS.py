class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        cache = {}

        def dfs(a, b):
            if cache.get((a, b)):
                return cache[(a, b)]
            if a == '' or b == '':
                temp = 0
                for i in range(len(a)):
                    temp += ord(a[i])
                for j in range(len(b)):
                    temp += ord(b[j])
                cache[(a, b)] = temp
                return temp

            if a[-1] == b[-1]:
                result = dfs(a[:len(a) - 1], b[:len(b) - 1])
            else:
                temp1 = ord(a[-1]) + dfs(a[:len(a) - 1], b)
                temp2 = ord(b[-1]) + dfs(a, b[:len(b) - 1])
                result = min(temp1, temp2)
            cache[(a, b)] = result
            return result

        result = dfs(s1, s2)
        return result
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cache = {}

        def helper(a, b):
            if (a, b) in cache:
                return cache[(a, b)]

            n = len(a)
            if a == b:
                return True

            for k in range(1, n):
                temp1 = helper(a[:k], b[:k]) and helper(a[k:], b[k:])
                if temp1:
                    cache[(a, b)] = True
                    return True

                temp2 = helper(a[:k], b[n - k:]) and helper(a[k:], b[:n - k])

                if temp2:
                    cache[(a, b)] = True
                    return True
            cache[(a, b)] = False
            return False

        return helper(s1, s2)
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g_p = 0
        s_p = 0

        result = 0
        g.sort()
        s.sort()

        while g_p < len(g) and s_p < len(s):
            if s[s_p] >= g[g_p]:
                result += 1
                g_p += 1
                s_p += 1
            else:
                s_p += 1

        return result

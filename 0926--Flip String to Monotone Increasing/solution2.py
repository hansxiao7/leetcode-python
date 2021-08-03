class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        f_0 = [0 for _ in range(n)]
        f_1 = [0 for _ in range(n)]

        # 把后面的都变成1，把前面的都变成0

        count = 0
        for i in range(n):
            if s[i] == '1':
                count += 1

            f_0[i] = count

        count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                count += 1
            f_1[i] = count
        result = sys.maxint
        for i in range(n - 1):
            result = min(result, f_0[i] + f_1[i + 1], f_1[0], f_0[n - 1])

        return result


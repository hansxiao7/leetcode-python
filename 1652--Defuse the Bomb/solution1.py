class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        temp = code + code + code

        total = 0
        for i in range(3 * n):
            total += temp[i]
            temp[i] = total

        if k == 0:
            for i in range(n):
                code[i] = 0
        elif k > 0:
            for i in range(n):
                code[i] = temp[i + n + k] - temp[i + n]

        elif k < 0:
            for i in range(n):
                code[i] = temp[i + n - 1] - temp[i + n - 1 + k]

        return code
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        bits = [0] * 32

        for num in nums:
            for i in range(32):
                if num & (1 << i) != 0:
                    bits[i] += 1

        res = 0

        for i in range(32):
            bits[i] = bits[i] % 3
            if bits[i] == 1:
                res = res + (1 << i)
        if res >= 2 ** 31 - 1:
            res = -(2 ** 32 - res)

        if res < - 2 ** 31:
            res = 2 ** 32 + res
        return res
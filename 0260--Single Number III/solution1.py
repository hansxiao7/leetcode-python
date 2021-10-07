class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0

        for num in nums:
            res = res ^ num

        lowbit = res & (-res)
        num1 = 0
        num2 = 0

        for num in nums:
            if num & lowbit == 0:
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num

        return [num1, num2]
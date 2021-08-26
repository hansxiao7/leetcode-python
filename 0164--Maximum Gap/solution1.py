class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        # radix sort
        maxValue = max(nums)

        exp = 1

        while maxValue >= exp:
            radix = [[] for _ in range(10)]
            temp = [0] * len(nums)

            for num in nums:
                radix[(num // exp) % 10].append(num)

            pos = 0
            for i in range(10):
                for j in range(len(radix[i])):
                    temp[pos] = radix[i][j]
                    pos += 1

            for k in range(len(nums)):
                nums[k] = temp[k]

            exp = exp * 10

        result = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > result:
                result = nums[i + 1] - nums[i]

        return result

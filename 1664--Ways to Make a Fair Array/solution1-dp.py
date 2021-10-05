class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l_odd = [0] * n
        l_even = [0] * n

        r_odd = [0] * n
        r_even = [0] * n

        for i in range(1, n):
            if (i - 1) % 2 == 0:
                l_even[i] = l_even[i - 1] + nums[i - 1]
                l_odd[i] = l_odd[i - 1]

            else:
                l_even[i] = l_even[i - 1]
                l_odd[i] = l_odd[i - 1] + nums[i - 1]

        for i in range(n - 2, -1, -1):
            if (i + 1) % 2 == 0:
                r_even[i] = r_even[i + 1] + nums[i + 1]
                r_odd[i] = r_odd[i + 1]

            else:
                r_even[i] = r_even[i + 1]
                r_odd[i] = r_odd[i + 1] + nums[i + 1]

        res = 0
        for i in range(n):
            if (l_even[i] + r_odd[i]) == (l_odd[i] + r_even[i]):
                res += 1

        return res
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict1 = {0: -1}

        total = 0
        result = 0

        for i in range(len(nums)):
            total += nums[i]

            if dict1.get(total) is None:
                dict1[total] = i

            if dict1.get(total - k) is not None:
                result = max(result, i - dict1[total - k])

        print(dict1)
        return result
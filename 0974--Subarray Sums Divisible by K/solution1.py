class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = {0: 1}

        total = 0
        res = 0

        for num in nums:
            total += num
            if total % k in counts:
                res += counts[total % k]

            counts[total % k] = counts.get(total % k, 0) + 1

        return res
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}

        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for key in counts.keys():
            buckets[counts[key]].append(key)

        count = 0
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(buckets[i]) != 0:
                res.extend(buckets[i])
                count += len(buckets[i])

            if count == k:
                return res




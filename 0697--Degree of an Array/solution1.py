class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = [1, [i, i]]
            else:
                counts[nums[i]] = [counts[nums[i]][0] + 1, [counts[nums[i]][1][0], i]]

        maxValue = 0
        candidates = []

        for key in counts.keys():
            if counts[key][0] > maxValue:
                maxValue = counts[key][0]
                candidates = [key]
            elif counts[key][0] == maxValue:
                candidates.append(key)

        res = len(nums)
        for num in candidates:
            res = min(res, counts[num][1][1] - counts[num][1][0] + 1)

        return res
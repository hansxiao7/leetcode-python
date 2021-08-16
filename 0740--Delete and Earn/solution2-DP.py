class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1

        prev = None
        keys = counts.keys()
        keys.sort()

        take = [0 for _ in range(len(keys))]
        skip = [0 for _ in range(len(keys))]

        take[0] = keys[0] * counts[keys[0]]

        for i in range(1, len(keys)):
            k = keys[i]
            if keys[i - 1] == k - 1:
                take[i] = skip[i - 1] + counts[k] * k
                skip[i] = max(skip[i - 1], take[i - 1])
            else:
                take[i] = max(skip[i - 1], take[i - 1]) + counts[k] * k
                skip[i] = max(skip[i - 1], take[i - 1])

        return max(take[len(keys) - 1], skip[len(keys) - 1])
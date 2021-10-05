class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counts = {}

        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        n = len(arr)

        keys = counts.keys()
        keys.sort(key=lambda x: -counts[x])

        res = 0
        removed = 0
        for key in keys:
            removed += counts[key]
            res += 1

            if removed >= n / 2.0:
                return res


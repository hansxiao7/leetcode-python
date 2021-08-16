class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        counts = {}

        for i in range(len(citations)):
            counts[citations[i]] = counts.get(citations[i], 0) + 1

        keys = counts.keys()

        keys.sort()
        total = 0
        result = 0
        for i in range(len(keys) - 1, -1, -1):
            total += counts[keys[i]]

            result = max(result, min(total, keys[i]))

        return result

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = {}

        for c in s:
            counts[c] = counts.get(c, 0) + 1

        result = ''

        buckets = [set() for _ in range(max(counts.values()) + 1)]

        for key in counts.keys():
            buckets[counts[key]].add(key)

        result = ''
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                result += i * c

        return result
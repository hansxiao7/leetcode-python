class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        total = 0
        pos = {}
        result = 0

        for i in range(len(hours)):
            if hours[i] > 8:
                total += 1
            else:
                total -= 1

            if total > 0:
                result = max(result, i + 1)
            else:
                if total - 1 in pos:
                    result = max(result, i - pos[total - 1])

                if total not in pos:
                    pos[total] = i

        return result

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0 for _ in range(length)]
        for i in range(len(updates)):
            start = updates[i][0]
            end = updates[i][1]
            step = updates[i][2]

            result[start] += step
            if end + 1 < length:
                result[end + 1] -= step

        for j in range(len(result) - 1):
            result[j + 1] += result[j]

        return result

class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort()
        slots2.sort()

        i = 0
        j = 0

        while i < len(slots1) and j < len(slots2):
            low = max(slots1[i][0], slots2[j][0])
            high = min(slots1[i][1], slots2[j][1])

            if low <= high:
                if high - low >= duration:
                    return [low, low + duration]

            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1

        return []
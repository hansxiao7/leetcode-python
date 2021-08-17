class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        temp = []
        for t in slots1:
            start = t[0]
            end = t[1]

            temp.append((start, 1))
            temp.append((end, -1))

        for t in slots2:
            start = t[0]
            end = t[1]

            temp.append((start, 1))
            temp.append((end, -1))

        temp.sort()

        count = 0
        start = None
        end = None

        for i in range(len(temp)):
            count += temp[i][1]

            if count == 2:
                start = temp[i][0]

            if start is not None:
                if count == 1:
                    end = temp[i][0]
                    if end - start >= duration:
                        break
                    start = None

        if start is not None:
            return [start, start + duration]
        return []
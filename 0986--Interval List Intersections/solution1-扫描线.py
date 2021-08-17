class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        temp = []
        for i in range(len(firstList)):
            start = firstList[i][0]
            end = firstList[i][1]

            temp.append((start, 1))
            temp.append((end, -1))

        for i in range(len(secondList)):
            start = secondList[i][0]
            end = secondList[i][1]

            temp.append((start, 1))
            temp.append((end, -1))

        temp.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        result = []
        start = None
        end = None

        for i in range(len(temp)):
            count += temp[i][1]

            if count == 2:
                start = temp[i][0]

            if start is not None:
                if count == 1:
                    end = temp[i][0]
                    result.append([start, end])
                    start = None

        return result

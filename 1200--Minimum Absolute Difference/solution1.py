class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()

        result = []
        diff = sys.maxint
        for i in range(len(arr) - 1):
            temp = arr[i + 1] - arr[i]

            if temp < diff:
                result = [[arr[i], arr[i + 1]]]
                diff = temp
            elif temp == diff:
                result.append([arr[i], arr[i + 1]])

        return result
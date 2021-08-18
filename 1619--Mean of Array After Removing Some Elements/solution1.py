class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        n = len(arr)
        x = int(0.05 * n)

        return sum(arr[x:n - x]) / float(n - 2 * x)
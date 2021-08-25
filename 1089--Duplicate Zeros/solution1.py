class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        count = 0
        n = len(arr)
        for num in arr:
            if num == 0:
                count += 1

        arr.extend([0] * count)

        pos = len(arr) - 1
        i = pos - count

        while i >= 0:
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos -= 1
            else:
                arr[pos] = 0
                arr[pos - 1] = 0
                pos -= 2

            i -= 1

        for i in range(count):
            arr.pop()
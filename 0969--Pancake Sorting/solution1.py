class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        # find the max
        def find(left, right):
            maxV = 0
            pos = None
            for i in range(left, right + 1):
                if arr[i] > maxV:
                    maxV = arr[i]
                    pos = i

            return pos

        def flip(left, right):
            mid = (right + left) // 2
            for i in range(left, mid + 1):
                arr[i], arr[right + left - i] = arr[right + left - i], arr[i]

        result = []
        for right in range(len(arr) - 1, 0, -1):
            pos = find(0, right)
            if pos == right:
                continue
            else:
                result.append(pos + 1)
                flip(0, pos)
                result.append(right + 1)
                flip(0, right)

        return result
class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        if len(arr) == 1:
            return 1

        cache = [0 for _ in range(len(arr))]

        def helper(pos, arr, d):
            if cache[pos] != 0:
                return cache[pos]
            result = 1
            for i in range(pos + 1, pos + d + 1):
                if i >= len(arr) or arr[i] >= arr[pos]:
                    break
                result = max(result, 1 + helper(i, arr, d))

            for i in range(pos - 1, pos - d - 1, -1):
                if i < 0 or arr[i] >= arr[pos]:
                    break
                result = max(result, 1 + helper(i, arr, d))
            cache[pos] = result
            return result

        result = 1
        for i in range(len(arr)):
            result = max(helper(i, arr, d), result)

        return result

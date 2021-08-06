class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        visited = set()
        cache = [None for _ in range(n)]

        def helper(pos, arr):
            if cache[pos] is not None:
                return cache[pos]
            n = len(arr)
            if arr[pos] == 0:
                cache[pos] = True
                return True

            if pos in visited:
                return False

            visited.add(pos)

            result = False
            if pos - arr[pos] >= 0 and (pos - arr[pos]) not in visited:
                result = result or helper(pos - arr[pos], arr)

            if pos + arr[pos] < n and (pos + arr[pos]) not in visited:
                result = result or helper(pos + arr[pos], arr)
            cache[pos] = result
            return result

        return helper(start, arr)
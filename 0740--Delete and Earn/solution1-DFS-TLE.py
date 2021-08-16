class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1

        visited = set()
        cache = {}

        def helper():
            if tuple(visited) in cache:
                return cache[tuple(visited)]
            if len(visited) == len(counts.keys()):
                return 0

            result = 0
            for key in counts.keys():
                flag1 = None
                flag2 = None
                if key not in visited:
                    if key + 1 in counts and key + 1 not in visited:
                        visited.add(key + 1)
                        flag1 = True
                    if key - 1 in counts and key - 1 not in visited:
                        visited.add(key - 1)
                        flag2 = True
                    visited.add(key)
                    result = max(result, counts[key] * key + helper())

                    if flag1:
                        visited.remove(key + 1)

                    if flag2:
                        visited.remove(key - 1)
                    visited.remove(key)
            cache[tuple(visited)] = result
            return result

        return helper()
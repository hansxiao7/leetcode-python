class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maps = {}

        for i in range(1, 5):
            maps[i] = {}

        for num in nums:
            depth = num // 100
            pos = (num - depth * 100) // 10
            val = num - depth * 100 - pos * 10

            maps[depth][pos] = val

        def helper(depth, pos):
            if depth not in maps or pos not in maps[depth]:
                return []

            l = helper(depth + 1, pos * 2 - 1)
            r = helper(depth + 1, pos * 2)

            val = maps[depth][pos]
            res = []

            if len(l) == 0 and len(r) == 0:
                res = [val]

            for i in range(len(l)):
                res.append(val + l[i])
            for j in range(len(r)):
                res.append(val + r[j])

            return res

        res = helper(1, 1)

        return sum(res)
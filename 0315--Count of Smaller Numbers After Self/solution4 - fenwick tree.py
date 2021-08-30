class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # discrete elements
        maps = {}
        temp = list(set(tuple(nums)))

        temp.sort()

        for i in range(len(temp)):
            maps[temp[i]] = i

        tree = [0] * (len(maps.keys()) + 1)

        # only need to add 1
        def lowbit(x):
            return x & (-x)

        def update(num):
            pos = maps[num]

            i = pos + 1

            while i < len(tree):
                tree[i] += 1
                i += lowbit(i)

        def query(index):
            i = index + 1
            total = 0
            while i > 0:
                total += tree[i]
                i -= lowbit(i)

            return total

        def rangeSum(left, right):
            return query(right) - query(left - 1)

        result = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            update(nums[i])
            result[i] = rangeSum(0, maps[nums[i]] - 1)

        return result









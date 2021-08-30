class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # calculate prefix
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        # discrete elements
        maps = {}

        temp = set()

        for i in range(len(prefix)):
            temp.add(lower + prefix[i])
            temp.add(prefix[i])
            temp.add(upper + prefix[i])

        temp.add(upper)
        temp.add(lower)

        temp = list(temp)
        temp.sort()

        for i in range(len(temp)):
            maps[temp[i]] = i

        # build the fenwick tree
        tree = [0] * (len(maps.keys()) + 1)

        def lowbit(x):
            return x & (-x)

        def update(val):
            index = maps[val]
            i = index + 1

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

        result = 0
        for i in range(len(prefix) - 1, -1, -1):
            left = maps[lower + prefix[i]]
            right = maps[upper + prefix[i]]
            result += rangeSum(left, right)

            update(prefix[i])

        left = maps[lower]
        right = maps[upper]
        result += rangeSum(left, right)

        return result
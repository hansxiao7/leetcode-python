class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # discrete
        maps = {}

        temp = set()
        for num in nums:
            temp.add(2 * num)
            temp.add(num)
        temp = list(temp)
        temp.sort()

        for i in range(len(temp)):
            maps[temp[i]] = i

        # build binary-index tree
        def lowbit(x):
            return x & (-x)

        tree = [0] * (len(temp) + 1)

        def update(val):
            index = maps[val]
            i = index + 1

            while i < len(tree):
                tree[i] += 1
                i += lowbit(i)

        def query(val):
            index = maps[val]
            i = index + 1

            res = 0

            while i > 0:
                res += tree[i]
                i -= lowbit(i)

            return res

        result = 0
        total = 0
        for num in nums:
            result += total - query(2 * num)
            update(num)
            total += 1

        return result
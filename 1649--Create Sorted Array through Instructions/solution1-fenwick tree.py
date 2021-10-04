class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """

        def lowbit(x):
            return x & (-x)

        sets = set()

        for num in instructions:
            sets.add(num)

        sets = list(sets)
        sets.sort()

        maps = {}

        for i in range(len(sets)):
            maps[sets[i]] = i + 1

        trees = [0] * (len(sets) + 1)

        def update(x):
            i = maps[x]

            while i < len(trees):
                trees[i] += 1
                i += lowbit(i)

        def query(i):

            res = 0
            while i > 0:
                res += trees[i]
                i -= lowbit(i)

            return res

        res = []
        for num in instructions:
            update(num)
            i = maps[num] - 1
            temp1 = query(i)

            i = len(trees) - 1
            j = maps[num]
            temp2 = query(i) - query(j)
            res.append(min(temp1, temp2))

        return sum(res) % (10 ** 9 + 7)
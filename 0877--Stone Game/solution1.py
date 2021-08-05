class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        cache = {}

        def helper(li, l, r):
            if cache.get((l, r)):
                return cache[(l, r)]
            if l == r:
                return li[l]

            temp = max(li[l] - helper(li, l + 1, r), li[r] - helper(li, l, r - 1))
            cache[(l, r)] = temp
            return temp

        temp = helper(piles, 0, len(piles) - 1)
        if temp > 0:
            return True
        return False
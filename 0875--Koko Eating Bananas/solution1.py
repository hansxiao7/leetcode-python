class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if len(piles) == 1:
            return piles[0] // h + (piles[0] % h != 0)

        def check_val(val, h):
            count = 0

            for pile in piles:
                if pile <= val:
                    count += 1
                else:
                    count += pile // val + 1

                if count > h:
                    return False

            return True

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if check_val(mid, h):
                right = mid
            else:
                left = mid + 1

        return left
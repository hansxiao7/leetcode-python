class Solution(object):
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """

        def check_val(val):
            added = 0
            for i in range(len(stations) - 1):
                diff = stations[i + 1] - stations[i]
                if diff <= val:
                    continue
                else:
                    if diff % val == 0:
                        added += diff // val - 1
                    else:
                        added += diff // val

                if added > k:
                    # the val is too small
                    return False
            # added <= k, val is too large
            return True

        right = stations[-1] - stations[0]
        left = 10 ** -6

        while right - left > 10 ** -6:
            mid = (left + right) / 2.0
            if check_val(mid):
                right = mid
            else:
                left = mid + 10 ** -6

        return left

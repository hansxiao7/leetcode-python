class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if len(bloomDay) < m * k:
            return -1
        left = min(bloomDay)
        right = max(bloomDay)

        def check_val(val, m, k):
            # check the val doable
            count = 0
            bloom = 0
            i = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= val:
                    bloom += 1
                else:
                    bloom = 0

                if bloom == k:
                    count += 1
                    bloom = 0

                # value too large
                if count >= m:
                    return True

            # vaule too small
            return False

        while left < right:
            mid = (left + right) // 2
            if check_val(mid, m, k):
                right = mid
            else:
                left = mid + 1

        return left

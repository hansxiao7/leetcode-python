class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()

        def check_val(val, m):
            prev = position[0]
            count = 1

            for i in range(1, len(position)):
                if position[i] - prev <= val:
                    continue
                else:
                    prev = position[i]
                    count += 1
                # val too small
                if count >= m:
                    return True
            # val too big
            return False

        left = 1
        right = position[-1] - position[0]

        while left < right:
            mid = (left + right) // 2
            if check_val(mid, m):
                left = mid + 1
            else:
                right = mid

        return left
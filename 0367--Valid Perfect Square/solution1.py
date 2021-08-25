class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num

        while left < right:
            mid = (left + right) // 2
            if mid ** 2 < num:
                left = mid + 1
            elif mid ** 2 > num:
                right = mid
            else:
                return True

        if left ** 2 == num:
            return True

        return False
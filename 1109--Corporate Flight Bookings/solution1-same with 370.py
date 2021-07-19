class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """

        result = [0 for _ in range(n)]

        for i in bookings:
            start = i[0] - 1
            end = i[1] - 1
            step = i[2]

            result[start] += step
            if end + 1 < n:
                result[end + 1] -= step

        for j in range(n - 1):
            result[j + 1] += result[j]

        return result

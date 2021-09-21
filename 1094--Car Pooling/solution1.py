class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        temp = []

        for n, start, end in trips:
            temp.append((start, n))
            temp.append((end, -n))

        temp.sort()

        curr = 0

        for pos, num in temp:
            curr += num
            if curr > capacity:
                return False

        return True
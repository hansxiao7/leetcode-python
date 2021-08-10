class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        temp = [1]
        id2 = 0
        id3 = 0
        id5 = 0

        while len(temp) < n:
            new_val = min(temp[id2] * 2, temp[id3] * 3, temp[id5] * 5)

            if new_val == temp[id2] * 2:
                id2 += 1

            if new_val == temp[id3] * 3:
                id3 += 1

            if new_val == temp[id5] * 5:
                id5 += 1

            temp.append(new_val)
        return temp[n - 1]

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        set_31 = set((1, 3, 5, 7, 8, 10, 12))

        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        if year % 4 == 0:
            feb = 29
        else:
            feb = 28

        result = 0
        for i in range(1, month):
            if i in set_31:
                result += 31
            elif i == 2:
                result += feb
            else:
                result += 30

        result += day

        return result
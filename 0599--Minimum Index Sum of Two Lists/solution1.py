class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {}

        for i in range(len(list1)):
            dict1[list1[i]] = i

        total = sys.maxint
        result = []
        for i in range(len(list2)):
            r = list2[i]
            if r not in dict1:
                continue

            temp = i + dict1[r]
            if temp < total:
                total = temp
                result = [r]
            elif temp == total:
                result.append(r)

        return result
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        temp_arr = list(arr)
        temp_arr.sort()

        ranks = {}
        temp = 1
        for i in range(len(arr)):
            if i != 0 and temp_arr[i] == temp_arr[i - 1]:
                continue
            ranks[temp_arr[i]] = temp
            temp += 1

        result = []
        for i in range(len(arr)):
            result.append(ranks[arr[i]])

        return result
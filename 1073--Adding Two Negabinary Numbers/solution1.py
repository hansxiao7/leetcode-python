class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        result = [0 for _ in range(len(arr1))]

        n = len(arr2)

        prev = 0
        for i in range(n - 1, -1, -1):
            temp = arr1[len(arr1) - n + i] + arr2[i] + prev
            if temp == -1:
                result[len(arr1) - n + i] = 1
                prev = 1
            else:
                result[len(arr1) - n + i] = temp % 2
                prev = - (abs(temp) // 2)

        for j in range(len(arr1) - n - 1, -1, -1):
            temp = arr1[j] + prev
            if temp == -1:
                result[j] = 1
                prev = 1
            else:
                result[j] = temp % 2
                prev = - (abs(temp) // 2)

        if prev == 0:
            while result[0] == 0 and len(result) != 1:
                result.pop(0)
        elif prev == 1:
            result = [1] + result
        elif prev == -1:
            result = [1, 1] + result

        return result

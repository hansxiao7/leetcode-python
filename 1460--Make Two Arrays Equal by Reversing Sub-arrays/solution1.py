class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) != len(target):
            return False

        count1 = {}
        count2 = {}

        for i in range(len(arr)):
            count1[arr[i]] = count1.get(arr[i], 0) + 1

        for i in range(len(target)):
            count2[target[i]] = count2.get(target[i], 0) + 1

        return count1 == count2
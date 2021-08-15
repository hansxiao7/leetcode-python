class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        flag = True

        for i in range(len(arr) - 1):
            if arr[i + 1] > arr[i] and flag:
                continue
            elif arr[i + 1] < arr[i] and not flag:
                continue
            elif arr[i + 1] < arr[i] and flag:
                if i == 0:
                    return False
                flag = not flag
                continue
            else:
                return False

        if not flag:
            return True
        return False